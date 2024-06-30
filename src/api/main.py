from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from config.container import container


def create_app():
    # Logging
    config = container.config()
    config.configure_logging()

    app = FastAPI(
        title=config.app_title,
        docs_url=config.docs_url,
        redoc_url=config.redoc_url,
        version=config.version,
        debug=config.debug,
        secret_key=config.secret_key,
        config=config,
        container=container,
    )

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
