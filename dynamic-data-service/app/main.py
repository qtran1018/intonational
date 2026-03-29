from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.shared.http import init_client, close_client
from app.api.v1.routes import router as dynamic_data_router
import logging

# Only show WARNING+ for third-party libs
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)
logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
logging.getLogger("uvicorn.error").setLevel(logging.WARNING)

# Show INFO+ for your app
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_client()  # startup
    yield
    await close_client()  # shutdown

app = FastAPI(lifespan=lifespan)

# include routers here
app.include_router(dynamic_data_router)