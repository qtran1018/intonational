from app.weather_forecast.repository import query_weather, save_weather
from app.weather_forecast.model_maker import make_weather_forecast_model
from app.weather_forecast.client import get_weather_forecast
import logging

logger = logging.getLogger("weather")
DEFAULT_TTL = 86400

async def search_weather(lat: float, lon: float):
    cached = await query_weather(lat, lon)

    if cached:
        logger.info("Weather cache hit for %s,%s", lat, lon)
        return cached
    
    else:
        logger.info("Weather cache miss for %s,%s", lat, lon)
        raw = await get_weather_forecast(lat, lon)
        weather_obj = make_weather_forecast_model(
            lat,
            lon,
            raw["daily"]["time"],
            raw["daily"]["weather_code"],
            raw["daily"]["temperature_2m_max"],
            raw["daily"]["temperature_2m_min"],
            raw["daily"]["apparent_temperature_max"],
            raw["daily"]["apparent_temperature_min"],
            raw["daily"]["precipitation_probability_max"],
            raw["daily"]["wind_speed_10m_max"],
        )
        await save_weather(lat, lon, weather_obj, DEFAULT_TTL)
        logger.info("Weather successfully cached for %s,%s", lat, lon)

    return weather_obj
