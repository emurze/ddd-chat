import abc
from dataclasses import dataclass


@dataclass(frozen=True)
class Command:
    pass


class ICommandHandler(abc.ABC):
    @abc.abstractmethod
    async def handle(self, command: Command): ...
