from app.weather_forecast.repository import query_weather, save_weather
from app.weather_forecast.client import get_weather_forecast
from app.weather_forecast.model import WeatherForecast
import logging

logger = logging.getLogger("weather_forecast")
DEFAULT_TTL = 86400

async def search_weather(lat: float, lon: float):
    cached = await query_weather(lat, lon)

    if cached:
        logger.info("Weather cache HIT for %s, %s", lat, lon)
        return cached
    
    else:
        logger.info("Weather cache MISS for %s, %s", lat, lon)
        results = await get_weather_forecast(lat, lon)
        weather_obj = WeatherForecast.from_api_response(lat, lon, results)
        await save_weather(lat, lon, weather_obj, DEFAULT_TTL)
        logger.info("Weather successfully cached for %s, %s", lat, lon)

    return weather_obj