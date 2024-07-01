import abc

from seedwork.domain.events import Event


class IEventHandler(abc.ABC):
    @abc.abstractmethod
    async def handle(self, event: Event): ...
