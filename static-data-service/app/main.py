from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.shared.http import init_client, close_client
from app.weather_historical.repository import historical_weather
from app.geocoding.repository import geocodes
from app.advisories.repository import advisories
from app.api.v1.routes import router as static_data_router
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
    await advisories.create_index([("inserted_on", 1)], expireAfterSeconds=15768000) #6 month expiry
    await geocodes.create_index([("inserted_on", 1)], expireAfterSeconds=31536000) #1 year expiry
    await historical_weather.create_index([("inserted_on", 1)], expireAfterSeconds=31536000) #1 year expiry
    yield
    await close_client()  # shutdown

app = FastAPI(lifespan=lifespan)

# include routers here
app.include_router(static_data_router)