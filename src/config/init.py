from modules.chat.application.commands.create_chat import CreateChatCommand, \
    CreateChatHandler
from modules.chat.domain.repositories import IChatRepository
from seedwork.application.mediator import Mediator


def init_mediator(
    mediator: Mediator,
    chat_repo: IChatRepository,
) -> None:
    # TODO: Integrate in dependency injector
    mediator.register_command(
        CreateChatCommand,
        [CreateChatHandler(chat_repo=chat_repo)],
    )
