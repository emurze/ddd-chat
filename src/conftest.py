import pytest
from injector import Injector

from fixtures import init_memory_injector
from modules.chat.application.repositories import IChatRepository
from seedwork.application.mediator import Mediator


@pytest.fixture(scope="function")
def injector() -> Injector:
    return init_memory_injector()


@pytest.fixture(scope="function")
def mediator(injector: Injector) -> Mediator:
    return injector.get(Mediator)


@pytest.fixture(scope="function")
def chat_repo(injector: Injector) -> IChatRepository:
    return injector.get(IChatRepository)
