from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.shared.http import init_client, close_client

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_client()  # startup
    yield
    await close_client()  # shutdown

app = FastAPI(lifespan=lifespan)

# include routers here
from app.api.v1.routes import router as dynamic_data_router
app.include_router(dynamic_data_router)