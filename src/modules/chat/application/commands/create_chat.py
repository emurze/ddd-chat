from dataclasses import dataclass

from modules.chat.application.exceptions import ChatTitleAlreadyExistsException
from modules.chat.domain.entities import Chat
from modules.chat.domain.repositories import IChatRepository
from modules.chat.domain.values import Title
from seedwork.application.commands import Command, CommandHandler


@dataclass(frozen=True)
class CreateChatCommand(Command):
    title: str


@dataclass(frozen=True)
class CreateChatHandler(CommandHandler):
    chat_repo: IChatRepository

    async def handle(self, command: CreateChatCommand) -> Chat:
        if await self.chat_repo.check_chat_exists_by_title(command.title):
            raise ChatTitleAlreadyExistsException(command.title)

        title = Title(command.title)
        chat = Chat.create(title=title)
        # TODO: pull events from entities
        return chat
