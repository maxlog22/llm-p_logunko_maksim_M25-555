from __future__ import annotations

from pathlib import Path

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.core.config import settings


def _build_sqlite_url(sqlite_path: str) -> str:
    path = Path(sqlite_path)
    if not path.is_absolute():
        path = Path.cwd() / path
    return f"sqlite+aiosqlite:///{path.resolve().as_posix()}"


DATABASE_URL = _build_sqlite_url(settings.sqlite_path)

engine = create_async_engine(DATABASE_URL, echo=False, future=True)
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)