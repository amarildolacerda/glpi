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


def test_auto_piloto_v1() -> None:
    payload = {
        "pergunta": "Preciso resetar minha senha e não consigo entrar no sistema.",
        "cliente_token": "token-cliente-demo",
        "canal": "portal",
    }

    response = client.post("/v1/auto-piloto", json=payload)
    assert response.status_code == 200
    body = response.json()
    assert body["auto_pilot"] is True
    assert body["resolvido"] is True
    assert "senha" in body["resposta"].lower()
