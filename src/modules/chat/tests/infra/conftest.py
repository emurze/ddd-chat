import pytest
from injector import Injector

from fixtures import init_infra_injector


@pytest.fixture(scope="function")
def infra_injector() -> Injector:
    return init_infra_injector()
