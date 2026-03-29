from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.shared.http import init_client, close_client
from app.weather_historical.repository import historical_weather
from app.geocoding.repository import geocodes
from app.api.v1.routes import router as static_data_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_client()  # startup
    await geocodes.create_index([("inserted_on", 1)], expireAfterSeconds=31536000) #1 year expiry
    await historical_weather.create_index([("inserted_on", 1)], expireAfterSeconds=31536000) #1 year expiry
    yield
    await close_client()  # shutdown

app = FastAPI(lifespan=lifespan)

# include routers here
app.include_router(static_data_router)