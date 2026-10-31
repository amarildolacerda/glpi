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
from feedback.logger import FeedbackLogger
from feedback.metrics import MetricsCollector

router = APIRouter(tags=["v1"])
orchestrator = Orchestrator()
glpi_client = GLPIClient()
feedback_logger = FeedbackLogger()
metrics_collector = MetricsCollector()


@router.post("/sugerir", response_model=SuggestResponse)
async def sugerir(payload: SuggestRequest) -> SuggestResponse:
    return orchestrator.suggest(payload)


@router.post("/aprovar")
async def aprovar(payload: ApprovalRequest) -> dict:
    return glpi_client.create_ticket(payload.ticket, payload.idempotency_key)


@router.post("/feedback")
async def feedback(payload: FeedbackRequest) -> dict:
    recorded = feedback_logger.log(
        payload.interacao_id,
        payload.util,
        payload.editado,
        payload.comentario,
    )
    metric_entry = metrics_collector.record(
        payload.interacao_id,
        confianca=0.0,
        util=payload.util,
        editado=payload.editado,
        comentario=payload.comentario,
    )
    return {
        "status": "registered",
        "interacao_id": payload.interacao_id,
        "feedback": recorded,
        "metrics": metric_entry,
        "summary": metrics_collector.snapshot(),
    }


@router.post("/auto-piloto", response_model=AutoPilotResponse)
async def auto_piloto(payload: AutoPilotRequest) -> AutoPilotResponse:
    return orchestrator.auto_resolve(payload)


@router.post("/atender", response_model=AutoPilotResponse)
async def atender(payload: AutoPilotRequest) -> AutoPilotResponse:
    return orchestrator.auto_resolve(payload)
