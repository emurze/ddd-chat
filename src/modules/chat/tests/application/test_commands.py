import pytest

from modules.chat.application.commands.create_chat import CreateChatCommand, \
    CreateChatHandler
from modules.chat.infra.repositories import MemoryChatRepository
from seedwork.application.mediator import Mediator


@pytest.mark.unit
async def test_create_chat_success(mediator: Mediator) -> None:
    command = CreateChatCommand(title="New chat")
    [chat] = await mediator.handle_command(command)
    [event] = chat.pull_events()

    assert chat.title.as_generic_type() == "New chat"
    assert event.chat_id == chat.id
    assert event.title == "New chat"

