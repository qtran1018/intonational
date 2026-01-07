from app.shared.redis.connection import redis_client
from typing import Any
import json

DEFAULT_TTL = 86400

async def set_cache(key: str, value: Any, ttl: int = DEFAULT_TTL):
    stored_value = json.dumps(value)
    await redis_client.set(key,stored_value, ex = DEFAULT_TTL)

async def get_cache(key: str):
    stored_value = await redis_client.get(key)
    if stored_value:
        return stored_value
    return None