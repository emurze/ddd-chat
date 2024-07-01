from modules.chat.domain.entities import Chat
from modules.chat.application.repositories import IChatRepository


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


class MongoChatRepository(IChatRepository):
    async def check_chat_exists_by_title(self, title: str) -> bool:
        raise NotImplementedError()

    async def add(self, chat: Chat) -> None:
        raise NotImplementedError()
