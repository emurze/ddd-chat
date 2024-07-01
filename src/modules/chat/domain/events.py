from dataclasses import dataclass

from seedwork.domain.events import Event


@dataclass(frozen=True)
class NewMessageReceived(Event):
    message_text: str
    message_id: str
    chat_id: str


@dataclass(frozen=True)
class NewChatCreated(Event):
    chat_id: str
    title: str
