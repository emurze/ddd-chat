from dataclasses import dataclass, field

from seedwork.domain.services import next_id


@dataclass(frozen=True)
class Event:  # Domain and Integration
    event_id: str = field(default_factory=next_id, kw_only=True)
