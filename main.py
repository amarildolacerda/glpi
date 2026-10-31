from fastapi import FastAPI

from interfaces.phase2_client_api import router as phase2_router
from interfaces.v1_agent_api import router as v1_router

app = FastAPI(title="GLPI AI Support", version="0.1.0")
app.include_router(v1_router, prefix="/v1")
app.include_router(phase2_router, prefix="/v2")


@app.get("/health")
async def health() -> dict:
    return {
        "status": "ok",
        "service": "glpi-ai-support",
        "version": "0.1.0",
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
