import abc

from modules.chat.domain.entities import Chat


class IChatRepository(abc.ABC):
    identity_map: dict[str, Chat]

    @abc.abstractmethod
    async def check_chat_exists_by_title(self, title: str) -> None: ...

    @abc.abstractmethod
    async def add(self, chat: Chat) -> None: ...
