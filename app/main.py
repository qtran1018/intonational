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
from app.geocoding.routes import router as geocode_router
app.include_router(geocode_router)
