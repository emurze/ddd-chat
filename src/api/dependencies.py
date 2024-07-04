from injector import Injector
from starlette.requests import Request


async def get_injector(request: Request) -> Injector:
    return request.app.extra["injector"]
