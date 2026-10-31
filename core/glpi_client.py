import hashlib
from typing import Any

import httpx

from config.settings import settings


class GLPIClient:
    def __init__(self, base_url: str | None = None, api_token: str | None = None) -> None:
        self.base_url = (base_url or settings.glpi_base_url).rstrip("/")
        self.api_token = api_token or settings.glpi_api_token

    def create_ticket(self, payload: dict[str, Any], idempotency_key: str) -> dict[str, Any]:
        if not self.api_token or not self.base_url or self.base_url == "https://glpi.example":
            ticket_id = int.from_bytes(
                hashlib.sha256(idempotency_key.encode("utf-8")).digest()[:4],
                byteorder="big",
                signed=False,
            ) % 9000 + 1000
            return {
                "ticket_id": ticket_id,
                "url": f"{self.base_url}/front/ticket.form.php?id={ticket_id}",
                "mode": "mock",
            }

        url = f"{self.base_url}/apirest.php/Ticket"
        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json",
            "X-GLPI-Idempotency-Key": idempotency_key,
        }

        response = httpx.post(url, json=payload, headers=headers, timeout=10.0)
        response.raise_for_status()

        data = response.json()
        if isinstance(data, dict):
            ticket_id = (
                data.get("id")
                or data.get("ticket_id")
                or data.get("data", {}).get("id")
            )
            if ticket_id is not None:
                return {
                    "ticket_id": int(ticket_id),
                    "url": f"{self.base_url}/front/ticket.form.php?id={ticket_id}",
                    "mode": "live",
                }

        raise ValueError("Resposta inesperada da API do GLPI ao criar ticket.")
