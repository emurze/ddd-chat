import abc


class IChatRepository(abc.ABC):
    @abc.abstractmethod
    async def check_chat_exists_by_title(self, title: str) -> None:
        ...
