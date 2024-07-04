from fastapi import APIRouter, HTTPException, Depends
from injector import Injector
from starlette import status

from api.chats.schemas import (
    CreateChatResponseSchema,
    CreateChatRequestSchema,
)
from api.dependencies import get_injector
from modules.chat.application.commands.create_chat import CreateChatCommand
from seedwork.application.exceptions import ApplicationException
from seedwork.application.mediator import Mediator
from seedwork.domain.exceptions import DomainException
from seedwork.presentation.schemas import ErrorSchema

router = APIRouter(prefix="/chats", tags=["Chats"])


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    summary="Endpoint to create a new chat.",
    description=(
        "Create a new chat. If a chat with the same name already exists, "
        "a 400 error is returned."
    ),
    responses={
        status.HTTP_201_CREATED: {"model": CreateChatResponseSchema},
        status.HTTP_400_BAD_REQUEST: {"model": ErrorSchema},
    },
)
async def create_chat(
    request: CreateChatRequestSchema,
    injector: Injector = Depends(get_injector),
):
    mediator: Mediator = injector.get(Mediator)

    try:
        command = CreateChatCommand(title=request.title)
        [chat] = await mediator.handle_command(command)
    except (DomainException, ApplicationException) as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": e.message},
        )

    return CreateChatResponseSchema.from_entity(chat)
