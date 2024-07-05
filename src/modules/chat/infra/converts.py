from modules.chat.domain.entities import Chat


def convert_chat_to_dict(chat: Chat) -> dict:
    return {
        "id": chat.id,
        "title": chat.title.as_generic_type(),
        "messages": [
            {
                "id": message.id,
                "test": message.text,
            }
            for message in chat.messages
        ],
    }
