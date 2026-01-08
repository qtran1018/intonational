from fastapi import APIRouter, Query
from app.weather_forecast.service import search_weather
from app.weather_forecast.model import WeatherForecast

router = APIRouter(tags=["Weather Forecast"])

@router.get("/weather-forecast", response_model = WeatherForecast)
async def weather_forecast_endpoint(lat: float = Query(..., ge=-90, le=90), lon: float = Query(..., ge=-180, le=180)):
    weather = await search_weather(lat, lon)
    return weather