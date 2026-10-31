from core.schemas import SuggestRequest, SuggestResponse, SuggestionArticle, TicketSuggestion


class Orchestrator:
    def suggest(self, request: SuggestRequest) -> SuggestResponse:
        return SuggestResponse(
            resposta_sugerida=(
                "Sugestão inicial gerada para apoiar o agente no atendimento. "
                "Revise a resposta e confirme a criação do ticket quando necessário."
            ),
            artigos=[
                SuggestionArticle(
                    id=12,
                    titulo="Artigo base de suporte",
                    score=0.91,
                )
            ],
            ticket_sugerido=TicketSuggestion(
                name="Solicitação de suporte",
                content=(
                    f"Solicitante: {request.solicitante_email}\n\n"
                    f"Pergunta: {request.pergunta}"
                ),
                type=1,
                urgency=3,
                impact=3,
                itilcategories_id=5,
                users_id_requester=123,
            ),
            confianca=0.87,
            requer_aprovacao=True,
            tickets_similares=[{"id": 100, "titulo": "Ticket similar recente"}],
        )
