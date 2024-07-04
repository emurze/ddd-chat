from fastapi import FastAPI
from injector import Injector
from starlette.middleware.cors import CORSMiddleware

from api.chats.handlers import router as chats_router
from config.config import AppConfig
from config.containers import init_injector
from config.log_config import configure_logging


def create_app(injector: Injector | None = None) -> FastAPI:
    injector = injector or init_injector()
    config = injector.get(AppConfig)
    configure_logging(config.log_level, config.debug)

    app = FastAPI(
        title=config.app_title,
        docs_url=config.docs_url,
        redoc_url=config.redoc_url,
        version=config.version,
        debug=config.debug,
        injector=injector,
    )
    app.include_router(chats_router)

    # noinspection PyTypeChecker
    app.add_middleware(
        CORSMiddleware,
        allow_origins=config.allowed_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/health")
    async def health() -> dict:
        return {"status": "ok"}

    return app
