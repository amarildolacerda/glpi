from core.orchestrator import Orchestrator
from core.schemas import SuggestRequest


def test_orchestrator_uses_request_context_for_suggestion() -> None:
    request = SuggestRequest(
        pergunta="Preciso resetar a senha do usuário e não consigo acessar o sistema.",
        canal="painel",
        agente_id=42,
        solicitante_email="cliente@empresa.com",
        ticket_id=None,
    )

    suggestion = Orchestrator().suggest(request)

    assert suggestion.confianca >= 0.7
    assert "senha" in suggestion.resposta_sugerida.lower()
    assert suggestion.ticket_sugerido.urgency in {3, 4, 5}
    assert suggestion.ticket_sugerido.name
