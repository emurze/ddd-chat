from dataclasses import dataclass

from seedwork.domain.events import Event


@dataclass(frozen=True)
class NewMessageReceivedEvent(Event):
    message_text: str
    message_id: str
    chat_id: str
