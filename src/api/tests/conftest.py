from functools import lru_cache

import pytest
from fastapi import FastAPI
from punq import Container
from starlette.testclient import TestClient

from api.main import create_app
from config.containers import init_container
from fixtures import init_dummy_container


def init_e2e_container():
    """Inits container with test_db"""
    container = ...


@pytest.fixture(scope="function")  # TODO: add db
def app() -> FastAPI:
    container = init_e2e_container()
    app = create_app(container)
    app.dependency_overrides[init_container] = _init_dummy_container  # noqa
    return app


@pytest.fixture(scope="function")
def client(app: FastAPI) -> TestClient:
    return TestClient(app=app)
