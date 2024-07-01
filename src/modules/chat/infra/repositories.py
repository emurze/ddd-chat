from modules.chat.domain.entities import Chat
from modules.chat.domain.repositories import IChatRepository


class MemoryChatRepository(IChatRepository):
    def __init__(self):
        self._identity_map: dict[str, Chat] = {}

    async def check_chat_exists_by_title(self, title: str) -> bool:
        try:
            return bool(
                next(
                    chat for chat in self._identity_map.values()
                    if chat.title == title
                )
            )
        except StopIteration:
            return False


class MongoChatRepository(IChatRepository):
    async def check_chat_exists_by_title(self, title: str) -> bool:
        ...
