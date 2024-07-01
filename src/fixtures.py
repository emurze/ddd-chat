from punq import Scope, Container

from config.config import AppConfig

# noinspection PyProtectedMember
from config.containers import init_container  # TODO: resolve problem
from modules.chat.application.repositories import IChatRepository
from modules.chat.infra.repositories import MemoryChatRepository


def init_dummy_container() -> Container:
    def config_factory() -> AppConfig:
        return AppConfig(
            app_title="Test App",
            secret_key="Test Key",
        )

    container = init_container()
    container.register(AppConfig, factory=config_factory)
    container.register(
        IChatRepository,
        MemoryChatRepository,
        scope=Scope.singleton,
    )
    return container
