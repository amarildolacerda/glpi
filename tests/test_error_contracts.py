from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_invalid_payload_returns_standardized_422_response() -> None:
    response = client.post("/v1/sugerir", json={})

    assert response.status_code == 422
    body = response.json()
    assert body["code"] == "validation_error"
    assert body["message"] == "Payload inválido."
    assert "details" in body


def test_unexpected_error_returns_standardized_500_response() -> None:
    response = client.post("/v1/atender", json={})

    assert response.status_code == 422
    body = response.json()
    assert body["code"] == "validation_error"


def test_value_error_returns_standardized_400_response() -> None:
    response = client.post(
        "/v1/aprovar",
        json={"ticket": {"name": "Teste"}, "idempotency_key": "demo-key", "interacao_id": "abc"},
    )

    assert response.status_code == 200
