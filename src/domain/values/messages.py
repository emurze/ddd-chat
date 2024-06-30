from dataclasses import dataclass

from domain.exceptions.messages import (
    TextIsEmptyException,
    TitleIsEmptyException,
    TitleTooLongException,
)
from domain.values.base import ValueObject


@dataclass(frozen=True)
class Text(ValueObject):
    value: str

    def validate(self) -> None:
        if not self.value:
            raise TextIsEmptyException()

    def as_generic_type(self) -> str:
        return str(self.value)


@dataclass(frozen=True)
class Title(ValueObject):
    value: str

    def validate(self) -> None:
        if not self.value:
            raise TitleIsEmptyException()

        if len(self.value) > 255:
            raise TitleTooLongException(self.value)

    def as_generic_type(self) -> str:
        return str(self.value)
