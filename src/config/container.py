from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Singleton

from config.config import AppConfig


class AppContainer(DeclarativeContainer):
    config = Singleton(AppConfig)


container = AppContainer()
