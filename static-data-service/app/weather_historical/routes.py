from fastapi import APIRouter, Depends
from app.weather_historical.service import search_weather
from app.shared.auth import verify_token

router = APIRouter(tags=["Historical Weather"])


@router.get("/historical-weather")
async def historical_weather_endpoint(
    lat: float,
    lon: float,
    month: int,
    _token: dict = Depends(verify_token),
):
    return await search_weather(lat, lon, month)
