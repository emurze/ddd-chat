from os import getenv as env

from injector import Injector, singleton

from config.config import AppConfig
from config.containers import init_injector


def init_e2e_injector() -> Injector:
    """Inits container with test dependencies like database"""
    # TODO: make runnable in any place env

    injector = init_injector()
    injector.binder.bind(
        AppConfig,
        to=AppConfig(
            app_title="Test App",
            secret_key="Suppressed",
            mongodb_connection_dsn=env("TEST_MONGODB_CONNECTION_DSN"),
            mongodb_chat_database=env("TEST_MONGODB_CHAT_DATABASE"),
            mongodb_chat_collection=env("TEST_MONGODB_CHAT_COLLECTION"),
        ),
        scope=singleton,
    )
    return injector
