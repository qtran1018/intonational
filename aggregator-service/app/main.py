from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.http import init_client, close_client

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_client()  # startup
    yield
    await close_client()  # shutdown

app = FastAPI(lifespan=lifespan)

# include routers here
from app.routes.routes import router as aggregator_router
app.include_router(aggregator_router)