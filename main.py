from fastapi import FastAPI

from config.settings import settings
from interfaces.v1_agent_api import router as v1_router
from interfaces.v2_client_api import router as v2_router

app = FastAPI(title="GLPI AI Support", version=settings.app_version)
app.include_router(v1_router, prefix="/v1")
app.include_router(v2_router, prefix="/v2")


@app.get("/health")
async def health() -> dict:
    return {
        "status": "ok",
        "service": "glpi-ai-support",
        "version": settings.app_version,
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
