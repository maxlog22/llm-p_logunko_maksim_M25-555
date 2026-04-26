from __future__ import annotations

from typing import Any

import httpx

from app.core.config import settings
from app.core.errors import ExternalServiceError


class OpenRouterClient:
    def __init__(
        self,
        *,
        api_key: str,
        base_url: str,
        model: str,
        site_url: str,
        app_name: str,
    ) -> None:
        self._api_key = api_key
        self._base_url = base_url.rstrip("/")
        self._model = model
        self._site_url = site_url
        self._app_name = app_name

    async def create_chat_completion(
        self,
        *,
        messages: list[dict[str, str]],
        temperature: float,
    ) -> str:
        headers = {
            "Authorization": f"Bearer {self._api_key}",
            "HTTP-Referer": self._site_url,
            "X-Title": self._app_name,
        }
        payload: dict[str, Any] = {
            "model": self._model,
            "messages": messages,
            "temperature": temperature,
        }

        try:
            async with httpx.AsyncClient(timeout=60.0) as client:
                response = await client.post(
                    f"{self._base_url}/chat/completions",
                    headers=headers,
                    json=payload,
                )
        except httpx.HTTPError as exc:
            raise ExternalServiceError("Failed to reach OpenRouter") from exc

        if response.status_code >= 400:
            raise ExternalServiceError(
                f"OpenRouter error {response.status_code}: {response.text}"
            )

        data = response.json()
        try:
            return data["choices"][0]["message"]["content"]
        except (KeyError, IndexError, TypeError) as exc:
            raise ExternalServiceError("Unexpected OpenRouter response format") from exc


def build_openrouter_client() -> OpenRouterClient:
    return OpenRouterClient(
        api_key=settings.openrouter_api_key,
        base_url=settings.openrouter_base_url,
        model=settings.openrouter_model,
        site_url=settings.openrouter_site_url,
        app_name=settings.openrouter_app_name,
    )