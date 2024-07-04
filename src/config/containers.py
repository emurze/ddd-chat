from typing import TypeAlias

import motor
from injector import Module, singleton, Binder, Injector, inject
from motor.core import AgnosticClient

from config.config import AppConfig
from modules.chat.application.commands.create_chat import (
    CreateChatHandler,
    CreateChatCommand,
)
from modules.chat.application.repositories import IChatRepository
from modules.chat.infra.repositories import MongoChatRepository
from seedwork.application.mediator import Mediator
from seedwork.infra.injector import singleton_provider

MongoDBClient: TypeAlias = AgnosticClient


class AppModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(AppConfig, to=AppConfig, scope=singleton)

    @singleton_provider
    def provide_mongodb_client(self, config: AppConfig) -> MongoDBClient:
        return motor.MotorClient(
            config.mongodb_connection_dsn,
            serverSelectionTimeoutMS=5000,
        )

    @singleton_provider
    def provide_mongodb_chat_repository(
        self,
        mongodb_client: MongoDBClient,
        config: AppConfig,
    ) -> IChatRepository:
        return MongoChatRepository(
            mongo_db_client=mongodb_client,
            mongo_db_db_name=config.mongodb_chat_database,
            mongo_db_collection_name=config.mongodb_chat_collection,
        )

    @singleton_provider
    def provide_mediator(self, injector: Injector) -> Mediator:
        mediator = Mediator()
        mediator.register_command(
            CreateChatCommand,
            [injector.get(inject(CreateChatHandler))],
        )
        return mediator


def init_injector() -> Injector:
    return Injector(AppModule())
