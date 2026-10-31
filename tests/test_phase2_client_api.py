from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_phase2_client_can_route_simple_request() -> None:
    payload = {
        "pergunta": "Preciso recuperar minha senha para entrar no portal.",
        "canal": "portal",
        "cliente_token": "phase2-demo-token",
    }

    response = client.post("/v2/atender", json=payload)

    assert response.status_code == 200
    body = response.json()
    assert "auto_pilot" in body
    assert "resposta" in body
    assert body["auto_pilot"] is True
