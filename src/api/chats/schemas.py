from modules.chat.domain.entities import Chat
from seedwork.presentation.schemas import Schema


class CreateChatRequestSchema(Schema):
    title: str


class CreateChatResponseSchema(Schema):
    id: str

    @classmethod
    def from_entity(cls, chat: Chat):
        return cls(id=chat.id)
