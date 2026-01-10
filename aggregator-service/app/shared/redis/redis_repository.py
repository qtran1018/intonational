from app.shared.redis.connection import redis_client
from typing import Any

async def set_cache(key: str, value: Any, ttl: int):
    await redis_client.set(key,value, ex = ttl)

async def get_cache(key: str):
    stored_value = await redis_client.get(key)
    if stored_value:
        return stored_value
    return None