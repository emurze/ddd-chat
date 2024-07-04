import abc
from dataclasses import dataclass


class IChatRepository(abc.ABC):
    @abc.abstractmethod
    def get_message(self) -> str:
        pass


class Engine:
    def __str__(self) -> str:
        return "Mega engine"


@dataclass(frozen=True)
class ChatRepository(IChatRepository):
    engine: "Engine"

    def get_message(self) -> str:
        return f"Chat message from {self.engine}"
