from fastapi import APIRouter

from core.glpi_client import GLPIClient
from core.orchestrator import Orchestrator
from core.schemas import (
    ApprovalRequest,
    AutoPilotRequest,
    AutoPilotResponse,
    FeedbackRequest,
    SuggestRequest,
    SuggestResponse,
)

router = APIRouter(tags=["v1"])
orchestrator = Orchestrator()
glpi_client = GLPIClient()


@router.post("/sugerir", response_model=SuggestResponse)
async def sugerir(payload: SuggestRequest) -> SuggestResponse:
    return orchestrator.suggest(payload)


@router.post("/aprovar")
async def aprovar(payload: ApprovalRequest) -> dict:
    return glpi_client.create_ticket(payload.ticket, payload.idempotency_key)


@router.post("/feedback")
async def feedback(payload: FeedbackRequest) -> dict:
    return {
        "status": "registered",
        "interacao_id": payload.interacao_id,
    }


@router.post("/auto-piloto", response_model=AutoPilotResponse)
async def auto_piloto(payload: AutoPilotRequest) -> AutoPilotResponse:
    return orchestrator.auto_resolve(payload)


@router.post("/atender", response_model=AutoPilotResponse)
async def atender(payload: AutoPilotRequest) -> AutoPilotResponse:
    return orchestrator.auto_resolve(payload)
