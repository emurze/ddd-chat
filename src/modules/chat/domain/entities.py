from dataclasses import dataclass, field
from typing import Any

from modules.chat.domain.events import NewMessageReceived, NewChatCreated
from modules.chat.domain.values import Text, Title, MessageId, ChatId
from seedwork.domain.entities import Entity, AggregateRoot
from seedwork.domain.services import next_id


@dataclass
class Message(Entity):
    id: MessageId = field(
        default_factory=lambda: MessageId(next_id()), kw_only=True
    )
    text: Text

    def __hash__(self) -> int:
        return hash(str(self.id))

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Message):
            return self.id == other.id
        return False


@dataclass
class Chat(AggregateRoot):
    id: ChatId = field(
        default_factory=lambda: ChatId(next_id()),
        kw_only=True,
    )
    title: Title
    messages: set[Message] = field(
        default_factory=set,
        kw_only=True,
    )

    @classmethod
    def create(cls, title: Title) -> "Chat":
        chat = cls(title=title)
        chat.register_event(
            NewChatCreated(
                chat_id=chat.id,
                title=title.as_generic_type(),
            )
        )
        return chat

    def add_message(self, message: Message) -> None:
        self.messages.add(message)
        self.register_event(
            NewMessageReceived(
                message_id=message.id,
                message_text=message.text.as_generic_type(),
                chat_id=self.id,
            )
        )
