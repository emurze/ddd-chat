import asyncio
from dataclasses import dataclass

from injector import Module, Injector, Binder, singleton, inject
from repo import ChatRepository, Engine, IChatRepository
from seedwork.application.commands import Command, ICommandHandler
from seedwork.application.mediator import Mediator
from seedwork.infra.injector import singleton_provider


@dataclass(frozen=True)
class CreatePostCommand(Command):
    title: str


@dataclass(frozen=True)
class CreatePostHandler(ICommandHandler):
    chat_repo: IChatRepository

    async def handle(self, command: CreatePostCommand) -> None:
        print(f"{command.title} was created.")


class AppModule(Module):
    def configure(self, binder: Binder):
        binder.bind(Engine, to=Engine, scope=singleton)

    @singleton_provider
    def provide_chat_repo(self, engine: Engine) -> IChatRepository:
        return ChatRepository(engine=engine)

    @singleton_provider
    def provide_mediator(self, injector: Injector) -> Mediator:
        mediator = Mediator()
        mediator.register_command(
            CreatePostCommand,
            [injector.get(inject(CreatePostHandler))],
        )
        return mediator


async def main() -> None:
    injector = Injector([AppModule()])
    mediator = injector.get(Mediator)
    await mediator.handle_command(CreatePostCommand(title="A new mega post"))


if __name__ == "__main__":
    asyncio.run(main())
