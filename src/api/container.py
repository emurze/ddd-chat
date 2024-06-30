from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Singleton

from api.config import AppConfig


class AppContainer(DeclarativeContainer):
    config = Singleton(AppConfig)
    # crypto_adapter = Singleton(
    #     CryptoAdapter,
    #     url=config.provided.crypto_api_url,
    #     api_key=config.provided.crypto_api_key,
    # )


container = AppContainer()
