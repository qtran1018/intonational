import logging
from app.shared.redis.connection import redis_client
from typing import Any

logger = logging.getLogger("aggregator")


async def set_cache(key: str, value: Any, ttl: int) -> None:
    try:
        await redis_client.set(key, value, ex=ttl)
    except Exception:
        logger.warning("Redis set failed for key=%s — continuing without cache", key)


async def get_cache(key: str) -> Any:
    try:
        stored_value = await redis_client.get(key)
        return stored_value if stored_value else None
    except Exception:
        logger.warning("Redis get failed for key=%s — continuing without cache", key)
        return None
