from app.shared.redis.redis_repository import set_cache, get_cache
from app.weather_forecast.model import WeatherForecast
from app.shared.utils.cache_keygen import make_weather_key
from datetime import datetime, timezone
import json


async def query_weather(lat: float, lon: float) -> dict | None:
    stored_key = make_weather_key(lat, lon)
    stored_value = await get_cache(stored_key)
    if not stored_value:
        return None
    if isinstance(stored_value, bytes):
        stored_value = stored_value.decode("utf-8")
    return json.loads(stored_value)


async def save_weather(lat: float, lon: float, value: WeatherForecast) -> None:
    stored_key = make_weather_key(lat, lon)
    envelope = {
        "data": value.model_dump(mode="json"),
        "fetched_at": datetime.now(timezone.utc).isoformat(),
    }
    await set_cache(stored_key, json.dumps(envelope))