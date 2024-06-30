from dataclasses import dataclass, field
from datetime import datetime

from seedwork.domain.events import Event
from seedwork.domain.services import get_current_date


@dataclass
class Entity:
    created_at: datetime = field(
        default_factory=get_current_date,
        kw_only=True,
    )


@dataclass
class AggregateRoot(Entity):
    _events: list[Event] = field(
        default_factory=list,
        kw_only=True,
    )

    def register_event(self, event: Event) -> None:
        self._events.append(event)

    def pull_events(self) -> list[Event]:
        events = self._events
        self._events = []
        return events
