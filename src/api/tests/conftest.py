import pytest
from fastapi import FastAPI
from injector import Injector
from starlette.testclient import TestClient

from api.main import create_app


@pytest.fixture(scope="function")
def app(infra_injector: Injector) -> FastAPI:
    return create_app(infra_injector)


@pytest.fixture(scope="function")
def client(app: FastAPI) -> TestClient:
    return TestClient(app=app)
