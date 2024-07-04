from collections.abc import Callable
from injector import singleton, provider


def singleton_provider(fn: Callable) -> Callable:
    return singleton(provider(fn))
