from fastapi import APIRouter, Depends, Query
from app.weather_forecast.service import search_weather
from app.weather_forecast.model import WeatherForecast
from app.shared.auth import verify_token

router = APIRouter(tags=["Weather Forecast"])


@router.get("/weather-forecast", response_model=WeatherForecast)
async def weather_forecast_endpoint(
    lat: float = Query(..., ge=-90, le=90),
    lon: float = Query(..., ge=-180, le=180),
    _token: dict = Depends(verify_token),
):
    return await search_weather(lat, lon)
