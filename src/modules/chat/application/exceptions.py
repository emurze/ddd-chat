from dataclasses import dataclass

from seedwork.application.exceptions import ApplicationException


@dataclass(eq=False)
class ChatTitleAlreadyExistsException(ApplicationException):
    title: str

    @property
    def message(self):
        return f"Chat title <{self.title}> already exists"
