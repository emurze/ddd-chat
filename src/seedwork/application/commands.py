import abc
from dataclasses import dataclass


@dataclass(frozen=True)
class Command:
    pass


@dataclass(frozen=True)
class CommandHandler(abc.ABC):
    @abc.abstractmethod
    async def handle(self, command: Command):
        ...


@dataclass(frozen=True)
class CommandResult:
    pass
