from app.weather_forecast.repository import query_weather, save_weather
from app.weather_forecast.client import get_weather_forecast
from app.weather_forecast.model import WeatherForecast
from datetime import datetime, timezone
import asyncio
import logging

logger = logging.getLogger("weather_forecast")

STALE_AFTER_SECONDS = 86400  # 24 hours — matches original TTL


def _is_stale(fetched_at: str) -> bool:
    age = (datetime.now(timezone.utc) - datetime.fromisoformat(fetched_at)).total_seconds()
    return age > STALE_AFTER_SECONDS


async def _refresh_weather(lat: float, lon: float) -> None:
    try:
        results = await get_weather_forecast(lat, lon)
        weather_obj = WeatherForecast.from_api_response(lat, lon, results)
        await save_weather(lat, lon, weather_obj)
        logger.info("Weather background refresh complete for %s, %s", lat, lon)
    except Exception:
        logger.warning("Weather background refresh failed for %s, %s", lat, lon)


async def search_weather(lat: float, lon: float) -> WeatherForecast:
    envelope = await query_weather(lat, lon)

    if envelope is None:
        logger.info("Weather cache MISS for %s, %s — fetching live", lat, lon)
        results = await get_weather_forecast(lat, lon)
        weather_obj = WeatherForecast.from_api_response(lat, lon, results)
        await save_weather(lat, lon, weather_obj)
        return weather_obj

    if _is_stale(envelope["fetched_at"]):
        logger.info("Weather cache STALE for %s, %s — returning stale + refreshing", lat, lon)
        asyncio.create_task(_refresh_weather(lat, lon))
    else:
        logger.info("Weather cache HIT for %s, %s", lat, lon)

    return WeatherForecast.model_validate(envelope["data"])