from dataclasses import dataclass

from motor.motor_asyncio import AsyncIOMotorClient

from modules.chat.application.repositories import IChatRepository
from modules.chat.domain.entities import Chat


class MemoryChatRepository(IChatRepository):
    def __init__(self):
        self.identity_map: dict[str, Chat] = {}

    async def check_chat_exists_by_title(self, title: str) -> bool:
        try:
            return bool(
                next(
                    chat
                    for chat in self.identity_map.values()
                    if chat.title.as_generic_type() == title
                )
            )
        except StopIteration:
            return False

    async def add(self, chat: Chat) -> None:
        self.identity_map[chat.id] = chat


@dataclass(frozen=True)
class MongoChatRepository(IChatRepository):
    mongo_db_client: AsyncIOMotorClient
    mongo_db_db_name: str
    mongo_db_collection_name: str

    async def check_chat_exists_by_title(self, title: str) -> bool:
        print(self.mongo_db_client)
        raise NotImplementedError()

    async def add(self, chat: Chat) -> None:
        raise NotImplementedError()
