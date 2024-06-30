from dataclasses import dataclass

from domain.exceptions.base import ApplicationException


@dataclass(eq=False)
class TextIsEmptyException(ApplicationException):
    @property
    def message(self):
        return f"Text is empty."


@dataclass(eq=False)
class TitleIsEmptyException(ApplicationException):
    @property
    def message(self):
        return f"Title is empty."


@dataclass(eq=False)
class TitleTooLongException(ApplicationException):
    text: str

    @property
    def message(self):
        return f"Text is too long {self.text[:255]}..."
