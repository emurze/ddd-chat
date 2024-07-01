import pytest

from config.config import AppConfig
from config.container import container
from config.init import init_mediator
from modules.chat.domain.repositories import IChatRepository
from modules.chat.infra.repositories import MemoryChatRepository
from seedwork.application.mediator import Mediator

test_config = AppConfig(
    app_title="Test App",
    secret_key="Test Key",
)
container.config.override(test_config)


@pytest.fixture
def chat_repo() -> IChatRepository:
    return MemoryChatRepository()


@pytest.fixture
def mediator(chat_repo: IChatRepository) -> Mediator:
    mediator = Mediator()
    init_mediator(
        mediator,
        chat_repo=chat_repo,
    )
    return mediator
