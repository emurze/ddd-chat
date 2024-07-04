from collections.abc import Callable
from functools import lru_cache, partial
from typing import Optional

import motor
from injector import Module, singleton, provider, Binder
from motor.core import AgnosticClient

from config.config import AppConfig
from modules.chat.application.commands.create_chat import (
    CreateChatHandler,
    CreateChatCommand,
)
from modules.chat.application.repositories import IChatRepository
from modules.chat.infra.repositories import MongoChatRepository
from seedwork.application.mediator import Mediator


class ApplicationModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(CreateChatHandler)  # Repository should be injected!

    @singleton_provider
    def provide_config(self) -> AppConfig:
        return AppConfig()

    @singleton_provider
    def provide_mongodb(self, config: AppConfig) -> AgnosticClient:
        return motor.MotorClient(
            config.mongodb_connection_dsn,
            serverSelectionTimeoutMS=5000,
        )

    @singleton_provider
    def provide_mongodb_chat_repository(
        self,
        mongodb: AgnosticClient,
        config: AppConfig,
    ) -> IChatRepository:
        return MongoChatRepository(
            mongo_db_client=mongodb,
            mongo_db_db_name=config.mongodb_chat_database,
            mongo_db_collection_name=config.mongodb_chat_collection,
        )

    @singleton_provider
    def provide_mediator(
        self,
        mongodb_chat_repository: IChatRepository,
    ) -> Mediator:
        mediator = Mediator()
        mediator.register_command(
            CreateChatCommand,
            [CreateChatHandler(chat_repo=mongodb_chat_repository)],
        )
        return mediator


@lru_cache(1)
def init_container() -> Container:
    return _init_container()
