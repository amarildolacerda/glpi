from typing import Optional

from pydantic import BaseModel, Field


class SuggestRequest(BaseModel):
    pergunta: str = Field(..., min_length=1)
    canal: str = Field(..., examples=["painel", "teams", "email"])
    agente_id: int
    solicitante_email: str = Field(..., min_length=1)
    ticket_id: Optional[int] = None


class SuggestionArticle(BaseModel):
    id: int
    titulo: str
    score: float


class TicketSuggestion(BaseModel):
    name: str
    content: str
    type: int
    urgency: int
    impact: int
    itilcategories_id: int
    users_id_requester: int


class SuggestResponse(BaseModel):
    resposta_sugerida: str
    artigos: list[SuggestionArticle] = []
    ticket_sugerido: TicketSuggestion
    confianca: float
    requer_aprovacao: bool = True
    tickets_similares: list[dict] = []


class ApprovalRequest(BaseModel):
    ticket: dict
    idempotency_key: str
    interacao_id: str


class FeedbackRequest(BaseModel):
    interacao_id: str
    util: bool
    editado: bool = False
    comentario: str | None = None
