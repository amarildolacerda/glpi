from fastapi import APIRouter

from core.orchestrator import Orchestrator
from core.schemas import ApprovalRequest, FeedbackRequest, SuggestRequest, SuggestResponse

router = APIRouter(tags=["v1"])
orchestrator = Orchestrator()


@router.post("/sugerir", response_model=SuggestResponse)
async def sugerir(payload: SuggestRequest) -> SuggestResponse:
    return orchestrator.suggest(payload)


@router.post("/aprovar")
async def aprovar(payload: ApprovalRequest) -> dict:
    return {
        "ticket_id": 2048,
        "url": "https://glpi.example/ticket.form.php?id=2048",
    }


@router.post("/feedback")
async def feedback(payload: FeedbackRequest) -> dict:
    return {
        "status": "registered",
        "interacao_id": payload.interacao_id,
    }
