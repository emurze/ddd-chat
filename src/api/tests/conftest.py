import pytest
from fastapi import FastAPI
from starlette.testclient import TestClient

from api.main import create_app
from fixtures import init_dummy_container


@pytest.fixture(scope="function")
def app() -> FastAPI:
    return create_app(
        init_dummy_container,
        init_container=init_dummy_container,
    )


@pytest.fixture(scope="function")
def client(app: FastAPI) -> TestClient:
    return TestClient(app=app)
