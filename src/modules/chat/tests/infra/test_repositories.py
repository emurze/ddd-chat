import pytest
from faker import Faker

from modules.chat.application.repositories import IChatRepository
from modules.chat.domain.entities import Chat
from modules.chat.domain.values import Title


@pytest.mark.integration
async def test_mongo_repo_add_success(
    chat_mongo_repo: IChatRepository,
    faker: Faker,
) -> None:
    # arrange
    title = Title(faker.text(max_nb_chars=50))
    chat = Chat(title=title)

    # act
    await chat_mongo_repo.add(chat)

    # assert
    # assert chat_mongo_repo.


@pytest.mark.integration
async def test_mongo_repo_check_chat_exists_by_title_success(
    chat_mongo_repo: IChatRepository,
    faker: Faker,
) -> None:
    # arrange
    title = faker.text(max_nb_chars=50)
    chat = Chat(title=Title(title))
    await chat_mongo_repo.add(chat)

    # act
    is_exist = await chat_mongo_repo.check_chat_exists_by_title(title)

    # assert
    assert is_exist is True
