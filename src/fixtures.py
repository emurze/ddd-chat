from injector import Injector, singleton
from pydantic_settings import SettingsConfigDict, BaseSettings

from config.config import AppConfig
from config.containers import init_injector
from modules.chat.application.repositories import IChatRepository
from modules.chat.infra.repositories import MemoryChatRepository


def init_memory_injector() -> Injector:
    """Creates a new dummy memory container for unit tests."""
    injector = init_injector()
    injector.binder.bind(
        AppConfig,
        to=AppConfig(
            app_title="Test App",
            secret_key="Suppressed",
            mongodb_connection_dsn="Suppressed",
            mongodb_chat_database="Suppressed",
            mongodb_chat_collection="Suppressed",
        ),
        scope=singleton,
    )
    injector.binder.bind(
        IChatRepository,
        to=MemoryChatRepository,
        scope=singleton,
    )
    return injector


class TestInfraConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="allow",
    )

    test_mongodb_connection_dsn: str
    test_mongodb_chat_database: str
    test_mongodb_chat_collection: str


def init_infra_injector() -> Injector:
    """
    Initializes the injector with test infrastructure dependencies
    (e.g., database). for integration and e2e tests
    """
    config = TestInfraConfig()
    injector = init_injector()
    injector.binder.bind(
        AppConfig,
        to=AppConfig(
            app_title="Test App",
            secret_key="Suppressed",
            mongodb_connection_dsn=config.test_mongodb_connection_dsn,
            mongodb_chat_database=config.test_mongodb_chat_database,
            mongodb_chat_collection=config.test_mongodb_chat_collection,
        ),
        scope=singleton,
    )
    return injector
