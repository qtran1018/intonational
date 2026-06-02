import logging
from app.shared.redis.connection import redis_client
from typing import Any

logger = logging.getLogger("dynamic-data-service")

# Safety expiry — keys unreached for 7 days are evicted to prevent unbounded memory growth
_SAFETY_TTL = 60 * 60 * 24 * 7


async def set_cache(key: str, value: Any) -> None:
    try:
        await redis_client.set(key, value, ex=_SAFETY_TTL)
    except Exception:
        logger.warning("Redis set failed for key=%s — continuing without cache", key)


async def get_cache(key: str) -> Any:
    try:
        stored_value = await redis_client.get(key)
        return stored_value if stored_value else None
    except Exception:
        logger.warning("Redis get failed for key=%s — continuing without cache", key)
        return None
