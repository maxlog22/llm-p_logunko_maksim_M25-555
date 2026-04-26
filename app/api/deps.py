from __future__ import annotations

from collections.abc import AsyncGenerator

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import decode_access_token
from app.db.session import AsyncSessionLocal
from app.repositories.chat_messages import ChatMessagesRepository
from app.repositories.users import UsersRepository
from app.services.openrouter_client import OpenRouterClient, build_openrouter_client
from app.usecases.auth import AuthUseCase
from app.usecases.chat import ChatUseCase


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session


def get_users_repository(
    session: AsyncSession = Depends(get_db_session),
) -> UsersRepository:
    return UsersRepository(session)


def get_chat_messages_repository(
    session: AsyncSession = Depends(get_db_session),
) -> ChatMessagesRepository:
    return ChatMessagesRepository(session)


def get_openrouter_client() -> OpenRouterClient:
    return build_openrouter_client()


def get_auth_usecase(
    users_repository: UsersRepository = Depends(get_users_repository),
) -> AuthUseCase:
    return AuthUseCase(users_repository)


def get_chat_usecase(
    messages_repository: ChatMessagesRepository = Depends(get_chat_messages_repository),
    openrouter_client: OpenRouterClient = Depends(get_openrouter_client),
) -> ChatUseCase:
    return ChatUseCase(messages_repository, openrouter_client)


def get_current_user_id(token: str = Depends(oauth2_scheme)) -> int:
    try:
        payload = decode_access_token(token)
        user_id = int(payload["sub"])
    except (KeyError, TypeError, ValueError) as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        ) from exc
    return user_id