from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.weather_historical.service import search_weather

router = APIRouter(tags=["Historical Weather"])

@router.get("/historical-weather")
async def historical_weather_endpoint(lat: float, lon: float, month: int):
    weather = await search_weather(lat, lon, month)
    return weather