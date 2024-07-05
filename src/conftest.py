import pytest
from injector import Injector
from motor.motor_asyncio import AsyncIOMotorClient

from config.config import AppConfig
from fixtures import init_memory_injector, init_infra_injector
from modules.chat.application.repositories import IChatRepository
from seedwork.application.mediator import Mediator


# Infrastructure amd Presentation


@pytest.fixture(scope="function")
def infra_injector() -> Injector:
    return init_infra_injector()


@pytest.fixture(scope="function")
async def mongo_client(infra_injector: Injector) -> AsyncIOMotorClient:
    client = infra_injector.get(AsyncIOMotorClient)
    yield client
    client.close()


@pytest.fixture(scope="function")
def chat_mongo_repo(
    mongo_client: AsyncIOMotorClient,
    infra_injector: Injector,
) -> IChatRepository:
    yield infra_injector.get(IChatRepository)
    config = infra_injector.get(AppConfig)
    mongo_client.drop_database(config.mongodb_chat_database)


# Application and Domain


@pytest.fixture(scope="function")
def memory_injector() -> Injector:
    return init_memory_injector()


@pytest.fixture(scope="function")
def mediator(memory_injector: Injector) -> Mediator:
    return memory_injector.get(Mediator)


@pytest.fixture(scope="function")
def chat_repo(memory_injector: Injector) -> IChatRepository:
    return memory_injector.get(IChatRepository)
