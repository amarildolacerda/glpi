from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_sugerir_v1() -> None:
    payload = {
        "pergunta": "Preciso resetar a senha do usuário.",
        "canal": "painel",
        "agente_id": 42,
        "solicitante_email": "cliente@empresa.com",
        "ticket_id": None,
    }

    response = client.post("/v1/sugerir", json=payload)
    assert response.status_code == 200
    body = response.json()
    assert body["requer_aprovacao"] is True
    assert "resposta_sugerida" in body
    assert body["confianca"] >= 0.0
