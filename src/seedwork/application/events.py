import abc
from dataclasses import dataclass

from seedwork.domain.events import Event


@dataclass(frozen=True)
class EventHandler(abc.ABC):
    async def handle(self, event: Event):
        ...


@dataclass(frozen=True)
class EventResult:
    pass
