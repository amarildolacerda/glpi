from core.glpi_client import GLPIClient


def test_glpi_client_returns_mock_ticket_when_not_configured() -> None:
    client = GLPIClient()

    result = client.create_ticket(
        payload={"name": "Reset de senha", "content": "Solicitação de acesso"},
        idempotency_key="demo-key-123",
    )

    assert result["ticket_id"] > 0
    assert "ticket.form.php" in result["url"]
