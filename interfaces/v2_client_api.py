from fastapi import APIRouter

from core.orchestrator import Orchestrator
from core.schemas import AutoPilotRequest, AutoPilotResponse

router = APIRouter(tags=["v2"])
orchestrator = Orchestrator()


@router.post("/atender", response_model=AutoPilotResponse)
async def atender(payload: AutoPilotRequest) -> AutoPilotResponse:
    return orchestrator.auto_resolve(payload)
