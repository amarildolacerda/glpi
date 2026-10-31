from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from config.settings import settings
from core.schemas import ErrorResponse
from interfaces.v1_agent_api import router as v1_router
from interfaces.v2_client_api import router as v2_router

app = FastAPI(title="GLPI AI Support", version=settings.app_version)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(_: Request, exc: RequestValidationError) -> JSONResponse:
    return JSONResponse(
        status_code=422,
        content=ErrorResponse(
            code="validation_error",
            message="Payload inválido.",
            details=exc.errors(),
        ).model_dump(mode="json"),
    )


@app.exception_handler(Exception)
async def generic_exception_handler(_: Request, exc: Exception) -> JSONResponse:
    return JSONResponse(
        status_code=500,
        content=ErrorResponse(
            code="internal_error",
            message="Ocorreu um erro interno no servidor.",
            details=None,
        ).model_dump(mode="json"),
    )


@app.exception_handler(ValueError)
async def value_error_handler(_: Request, exc: ValueError) -> JSONResponse:
    return JSONResponse(
        status_code=400,
        content=ErrorResponse(
            code="bad_request",
            message=str(exc) or "Requisição inválida.",
            details=None,
        ).model_dump(mode="json"),
    )


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
