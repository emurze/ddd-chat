from collections import defaultdict
from collections.abc import Iterable
from dataclasses import dataclass, field

from seedwork.application.commands import Command, ICommandHandler
from seedwork.application.events import IEventHandler
from seedwork.application.exceptions import (
    EventHandlersNotRegisteredException,
    CommandHandlersNotRegisteredException,
)
from seedwork.domain.events import Event


class Result:
    pass


@dataclass(frozen=True)
class Mediator:
    event_map: dict[type[Event], list[IEventHandler]] = field(
        default_factory=lambda: defaultdict(list),
        kw_only=True,
    )
    command_map: dict[type[Command], list[ICommandHandler]] = field(
        default_factory=lambda: defaultdict(list),  # cool thing
        kw_only=True,
    )  # TODO: one command per handler

    def register_event(
        self,
        event_type: type[Event],
        event_handlers: Iterable[IEventHandler],
    ) -> None:
        self.event_map[event_type] += event_handlers

    def register_command(
        self,
        command_type: type[Command],
        command_handlers: Iterable[ICommandHandler],
    ) -> None:
        self.command_map[command_type] += command_handlers

    async def handle_event(self, event: Event) -> list[Result]:
        event_type = type(event)
        handlers = self.event_map[event_type]

        if not handlers:
            raise EventHandlersNotRegisteredException(event_type)

        return [await handler.handle(event) for handler in handlers]

    async def handle_command(self, command: Command) -> list[Result]:
        command_type = type(command)
        handlers = self.command_map[command_type]

        if not handlers:
            raise CommandHandlersNotRegisteredException(command_type)

        return [await handler.handle(command) for handler in handlers]
