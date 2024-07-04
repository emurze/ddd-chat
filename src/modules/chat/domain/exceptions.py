from dataclasses import dataclass

from seedwork.domain.exceptions import DomainException


@dataclass(eq=False)
class TextIsEmptyException(DomainException):
    @property
    def message(self):
        return f"Text is an empty."


@dataclass(eq=False)
class TitleIsEmptyException(DomainException):
    @property
    def message(self):
        return f"Title is an empty."


@dataclass(eq=False)
class TitleTooLongException(DomainException):
    text: str

    @property
    def message(self):
        return f"Title is too long {self.text[:255]}..."
