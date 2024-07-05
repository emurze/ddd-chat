import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from injector import Injector

from api.main import create_app


@pytest.fixture(scope="function")
def app(infra_injector: Injector) -> FastAPI:
    return create_app(infra_injector)


@pytest.fixture(scope="function")
async def client(app: FastAPI) -> AsyncClient:
    async with AsyncClient(
        app=app, base_url="http://test"
    ) as ac:  # TODO: understand
        yield ac
