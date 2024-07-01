from functools import lru_cache, partial

from punq import Container, Scope

from config.config import AppConfig
from modules.chat.application.commands.create_chat import (
    CreateChatHandler,
    CreateChatCommand,
)
from modules.chat.application.repositories import IChatRepository
from modules.chat.infra.repositories import (
    MemoryChatRepository,
)
from seedwork.application.commands import ICommandHandler
from seedwork.application.mediator import Mediator


# @lru_cache(1)
# def init_container() -> Container:
#     return _init_container()


@lru_cache(1)
def init_container() -> Container:
    container = Container()

    # Infrastructure
    container.register(
        IChatRepository,
        MemoryChatRepository,
        scope=Scope.singleton,
    )

    # Services
    container.register(ICommandHandler, CreateChatHandler)

    def init_mediator() -> Mediator:
        # Registry
        mediator = Mediator()
        mediator.register_command(
            CreateChatCommand,
            [container.resolve(ICommandHandler)],
        )
        return mediator

    container.register(Mediator, factory=init_mediator)
    container.register(AppConfig, factory=partial(AppConfig))
    return container
