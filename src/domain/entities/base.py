from dataclasses import dataclass, field
from datetime import datetime

from domain.services import get_current_date


@dataclass
class Entity:
    created_at: datetime = field(
        default_factory=get_current_date,
        kw_only=True,
    )
