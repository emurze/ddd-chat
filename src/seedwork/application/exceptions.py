from dataclasses import dataclass


@dataclass(eq=False)
class ApplicationException(Exception):
    @property
    def message(self):
        return "Service error occurred"


@dataclass(eq=False)
class EventHandlersNotRegisteredException(ApplicationException):
    event_type: type

    @property
    def message(self):
        return f"Event handlers are not registered to {self.event_type}."


@dataclass(eq=False)
class CommandHandlersNotRegisteredException(ApplicationException):
    command_type: type

    @property
    def message(self):
        return f"Domain handlers are not registered to {self.command_type}."
