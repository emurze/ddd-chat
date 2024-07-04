import pytest
from fastapi import FastAPI
from injector import Injector
from starlette.testclient import TestClient

from api.main import create_app
from api.tests.fixtures import init_e2e_injector


@pytest.fixture(scope="session")
def injector() -> Injector:
    return init_e2e_injector()


@pytest.fixture(scope="function")
def app(injector: Injector) -> FastAPI:
    return create_app(injector)


@pytest.fixture(scope="function")
def client(app: FastAPI) -> TestClient:
    return TestClient(app=app)
