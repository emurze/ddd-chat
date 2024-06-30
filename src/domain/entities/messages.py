from dataclasses import dataclass, field
from typing import NewType, Any

from domain.entities.base import Entity
from domain.services import next_id
from domain.values.messages import Text, Title

MessageId = NewType('MessageId', str)
ChatId = NewType('ChatId', str)


@dataclass
class Message(Entity):
    id: MessageId = field(
        default_factory=lambda: MessageId(next_id()),
        kw_only=True
    )
    text: Text

    def __hash__(self) -> int:
        return hash(str(self.id))

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Message):
            return self.id == other.id
        return False


@dataclass
class Chat(Entity):
    id: ChatId = field(
        default_factory=lambda: ChatId(next_id()),
        kw_only=True
    )
    title: Title
    messages: set[Message] = field(
        default_factory=set,
        kw_only=True,
    )

    def add_message(self, message: Message) -> None:
        self.messages.add(message)
