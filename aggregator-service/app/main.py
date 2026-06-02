import logging

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
import httpx

from app.shared.http import init_client, close_client

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)

logger = logging.getLogger("aggregator")


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_client()
    yield
    await close_client()


app = FastAPI(lifespan=lifespan)


@app.exception_handler(httpx.HTTPStatusError)
async def upstream_http_error_handler(request: Request, exc: httpx.HTTPStatusError):
    logger.error("Upstream API error %s for %s", exc.response.status_code, str(request.url))
    return JSONResponse(
        status_code=502,
        content={"error": "Upstream service error.", "upstream_status": exc.response.status_code},
    )


@app.exception_handler(httpx.TimeoutException)
async def upstream_timeout_handler(request: Request, exc: httpx.TimeoutException):
    logger.error("Upstream API timeout for %s", str(request.url))
    return JSONResponse(status_code=504, content={"error": "Upstream service timed out."})


@app.exception_handler(Exception)
async def generic_error_handler(request: Request, exc: Exception):
    logger.exception("Unhandled exception for %s", str(request.url))
    return JSONResponse(status_code=500, content={"error": "An unexpected error occurred."})


from app.api.v1.routes import router as aggregator_router
app.include_router(aggregator_router)
