from app.shared.redis.redis_repository import set_cache, get_cache
from app.weather_forecast.model import WeatherForecast
from app.shared.utils.cache_keygen import make_weather_key
import json

async def query_weather(lat: float, lon: float):
    stored_key = make_weather_key(lat, lon)
    stored_value = await get_cache(stored_key)
    if not stored_value:
        return None
    if isinstance(stored_value, bytes):
        stored_value = stored_value.decode("utf-8")
    return WeatherForecast.model_validate(json.loads(stored_value))

async def save_weather(lat: float, lon: float, value: WeatherForecast, ttl: int):
    stored_key = make_weather_key(lat,lon)

    # turns value from object-->python data-->JSON. Object itself is not JSON-serializable
    stored_value = json.dumps(value.model_dump(mode="json"))
    await set_cache(stored_key, stored_value, ttl)