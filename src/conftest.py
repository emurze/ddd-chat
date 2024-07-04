import pytest
from injector import Injector

from fixtures import init_memory_injector, init_infra_injector
from modules.chat.application.repositories import IChatRepository
from seedwork.application.mediator import Mediator


@pytest.fixture(scope="function")
def infra_injector() -> Injector:
    return init_infra_injector()


@pytest.fixture(scope="function")
def memory_injector() -> Injector:
    return init_memory_injector()


@pytest.fixture(scope="function")
def mediator(memory_injector: Injector) -> Mediator:
    return memory_injector.get(Mediator)


@pytest.fixture(scope="function")
def chat_memory_repo(memory_injector: Injector) -> IChatRepository:
    return memory_injector.get(IChatRepository)


@pytest.fixture(scope="function")
def chat_mongo_repo(infra_injector: Injector) -> IChatRepository:
    return infra_injector.get(IChatRepository)
