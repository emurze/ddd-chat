from fastapi import APIRouter, Depends, HTTPException
from punq import Container
from starlette import status

from config.containers import init_container
from api.v1.chats.schemas import (
    CreateChatResponseSchema,
    CreateChatRequestSchema,
)
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
    container: Container = Depends(init_container),
):
    mediator: Mediator = container.resolve(Mediator)

    try:
        command = CreateChatCommand(title=request.title)
        [chat] = await mediator.handle_command(command)
    except (DomainException, ApplicationException) as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": e.message},
        )

    return CreateChatResponseSchema.from_entity(chat)
