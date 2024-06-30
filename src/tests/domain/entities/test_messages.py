from datetime import datetime

import pytest

from domain.entities.messages import Message, Chat
from domain.exceptions.messages import TextIsEmptyException, \
    TitleTooLongException, TitleIsEmptyException
from domain.values.messages import Text, Title


@pytest.mark.unit
def test_create_message_success() -> None:
    text = Text("Hello, boy!")
    message = Message(text=text)

    assert message.text == text
    assert message.created_at.date() == datetime.today().date()


@pytest.mark.unit
def test_create_message_long_text_success() -> None:
    text = Text("Hello, boy!" * 100)
    message = Message(text=text)

    assert message.text == text


@pytest.mark.unit
def test_create_message_empty_text() -> None:
    with pytest.raises(TextIsEmptyException):
        _ = Text("")


@pytest.mark.unit
def test_create_chat_success() -> None:
    title = Title("Best Chat")
    chat = Chat(title=title)

    assert chat.title == title
    assert chat.created_at.date() == datetime.today().date()


@pytest.mark.unit
def test_create_chat_title_too_long() -> None:
    with pytest.raises(TitleTooLongException):
        _ = Title("S" * 500)


@pytest.mark.unit
def test_create_chat_empty_title() -> None:
    with pytest.raises(TitleIsEmptyException):
        _ = Title("")


@pytest.mark.unit
def test_chat_can_add_message() -> None:
    text = Text("Hello, boy!")
    message = Message(text=text)

    title = Title("Best Chat")
    chat = Chat(title=title)

    chat.add_message(message)

    assert message in chat.messages
