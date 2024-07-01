import pytest
from faker import Faker

from modules.chat.application.commands.create_chat import CreateChatCommand
from modules.chat.application.exceptions import ChatTitleAlreadyExistsException
from modules.chat.domain.entities import Chat
from modules.chat.application.repositories import IChatRepository
from modules.chat.domain.values import Title
from seedwork.application.mediator import Mediator


@pytest.mark.unit
async def test_create_chat_success(
    chat_repo: IChatRepository,
    mediator: Mediator,
    faker: Faker,
) -> None:
    command = CreateChatCommand(title=faker.text())
    [chat] = await mediator.handle_command(command)
    chat_title = chat.title.as_generic_type()

    assert await chat_repo.check_chat_exists_by_title(chat_title)


@pytest.mark.unit
async def test_create_chat_command_events(
    mediator: Mediator,
    faker: Faker,
) -> None:
    command = CreateChatCommand(title=faker.text())
    [chat] = await mediator.handle_command(command)
    [event] = chat.pull_events()

    assert event.chat_id == chat.id
    assert event.title == command.title


@pytest.mark.unit
async def test_create_chat_command_title_already_exists(
    chat_repo: IChatRepository,
    mediator: Mediator,
    faker: Faker,
) -> None:
    chat_title = faker.text()
    chat = Chat(title=Title(chat_title))
    await chat_repo.add(chat)

    with pytest.raises(ChatTitleAlreadyExistsException):
        await mediator.handle_command(CreateChatCommand(title=chat_title))

    assert len(chat_repo.identity_map) == 1
