from dataclasses import dataclass

from modules.chat.application.exceptions import ChatTitleAlreadyExistsException
from modules.chat.domain.entities import Chat
from modules.chat.application.repositories import IChatRepository
from modules.chat.domain.values import Title
from seedwork.application.commands import Command, ICommandHandler


@dataclass(frozen=True)
class CreateChatCommand(Command):
    title: str


@dataclass(frozen=True)
class CreateChatHandler(ICommandHandler):
    chat_repo: IChatRepository

    async def handle(self, command: CreateChatCommand) -> Chat:
        if await self.chat_repo.check_chat_exists_by_title(command.title):
            raise ChatTitleAlreadyExistsException(command.title)

        title = Title(command.title)
        chat = Chat.create(title=title)

        await self.chat_repo.add(chat)  # TODO: pull events from entities
        return chat
