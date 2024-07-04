from injector import Injector, singleton

from config.config import AppConfig
from config.containers import init_injector
from modules.chat.application.repositories import IChatRepository
from modules.chat.infra.repositories import MemoryChatRepository


def init_memory_injector() -> Injector:
    """Creates a new dummy memory container."""
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
