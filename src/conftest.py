import pytest
from punq import Container

from fixtures import init_dummy_container

from modules.chat.application.repositories import IChatRepository
from seedwork.application.mediator import Mediator


@pytest.fixture(scope="function")
def container() -> Container:
    return init_dummy_container()


@pytest.fixture(scope="function")
def mediator(container: Container) -> Mediator:
    return container.resolve(Mediator)


@pytest.fixture(scope="function")
def chat_repo(container: Container) -> IChatRepository:
    return container.resolve(IChatRepository)
