from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes_auth import router as auth_router
from app.api.routes_chat import router as chat_router
from app.core.config import settings
from app.db.base import Base
from app.db import models as db_models  # noqa: F401
from app.db.session import engine


def create_app() -> FastAPI:
    app = FastAPI(title=settings.app_name)

    if settings.cors_enabled:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=settings.cors_allow_origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    app.include_router(auth_router)
    app.include_router(chat_router)

    @app.on_event("startup")
    async def on_startup() -> None:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    @app.get("/health")
    async def health() -> dict[str, str]:
        return {"status": "ok", "env": settings.env}

    return app


app = create_app()