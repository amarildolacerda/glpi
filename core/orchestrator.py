from config.settings import settings
from core.guardrails import Guardrails
from core.llm import LLMAdapter
from core.rag import RAGKnowledgeBase
from core.schemas import (
    AutoPilotRequest,
    AutoPilotResponse,
    SuggestRequest,
    SuggestResponse,
    SuggestionArticle,
    TicketSuggestion,
)


class Orchestrator:
    def __init__(self) -> None:
        self.rag = RAGKnowledgeBase()
        self.llm = LLMAdapter()
        self.guardrails = Guardrails()

    def suggest(self, request: SuggestRequest) -> SuggestResponse:
        pergunta = request.pergunta.lower()
        artigos_relevantes = self.rag.search(request.pergunta, limit=3)
        llm_result = self.llm.generate(request.pergunta, artigos_relevantes)

        if any(token in pergunta for token in ["senha", "login", "acesso", "autentic"]):
            urgency = llm_result["urgencia"]
            impact = llm_result["impacto"]
            confidence = llm_result["confianca"]
            resposta = llm_result["resposta"]
            ticket_name = "Solicitação de acesso e senha"
        elif any(token in pergunta for token in ["erro", "falha", "indispon", "quebra"]):
            urgency = llm_result["urgencia"]
            impact = llm_result["impacto"]
            confidence = llm_result["confianca"]
            resposta = llm_result["resposta"]
            ticket_name = "Falha operacional"
        else:
            urgency = llm_result["urgencia"]
            impact = llm_result["impacto"]
            confidence = llm_result["confianca"]
            resposta = llm_result["resposta"]
            ticket_name = "Solicitação de suporte"

        if not artigos_relevantes:
            artigos_relevantes = [{"id": 12, "titulo": "Artigo base de suporte", "score": 0.91}]

        guardrail = self.guardrails.validate(resposta, requires_approval=True)
        if not guardrail["seguro"]:
            resposta = (
                "A resposta foi bloqueada por segurança. Solicite revisão humana antes de proceder com "
                "qualquer ação de acesso ou privilégio."
            )

        return SuggestResponse(
            resposta_sugerida=resposta,
            artigos=[
                SuggestionArticle(
                    id=item["id"],
                    titulo=item["titulo"],
                    score=item["score"],
                )
                for item in artigos_relevantes
            ],
            ticket_sugerido=TicketSuggestion(
                name=ticket_name,
                content=(
                    f"Solicitante: {request.solicitante_email}\n\n"
                    f"Pergunta: {request.pergunta}"
                ),
                type=1,
                urgency=urgency,
                impact=impact,
                itilcategories_id=5,
                users_id_requester=123,
            ),
            confianca=confidence,
            requer_aprovacao=True,
            tickets_similares=[{"id": 100, "titulo": "Ticket similar recente"}],
        )

    def auto_resolve(self, request: AutoPilotRequest) -> AutoPilotResponse:
        if not settings.auto_pilot_enabled:
            return AutoPilotResponse(
                auto_pilot=False,
                resolvido=False,
                resposta="Auto-piloto desativado. Solicite apoio humano para continuar.",
                confianca=0.0,
            )

        pergunta = request.pergunta.lower()
        if any(token in pergunta for token in ["senha", "login", "acesso", "autentic"]):
            return AutoPilotResponse(
                auto_pilot=True,
                resolvido=True,
                resposta=(
                    "Reset de senha solicitado. Siga o fluxo de recuperação de senha, valide a "
                    "identidade do usuário e, se necessário, confirme a possibilidade de bloqueio de conta."
                ),
                confianca=0.93,
                ticket_id=None,
            )

        return AutoPilotResponse(
            auto_pilot=True,
            resolvido=False,
            resposta=(
                "A demanda exige revisão humana. O auto-piloto só resolve casos simples de acesso "
                "e senha quando o contexto é suficiente para uma resposta segura."
            ),
            confianca=0.42,
            ticket_id=None,
        )
