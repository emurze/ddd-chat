import abc
from dataclasses import dataclass
from typing import Generic, TypeVar, Any

VT = TypeVar("VT", bound=Any)


@dataclass(frozen=True)
class ValueObject(abc.ABC, Generic[VT]):
    value: VT

    def __post_init__(self) -> None:
        self.validate()

    @abc.abstractmethod
    def validate(self) -> None: ...

    @abc.abstractmethod
    def as_generic_type(self) -> Any: ...
