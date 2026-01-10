from app.shared.redis.redis_repository import set_cache, get_cache
from app.models.aggregator_model import AggregatedData
from app.shared.utils.cache_keygen import make_aggregate_key
import json

async def query_aggregate(search_city: str, month: int):
    stored_key = make_aggregate_key(search_city, month)
    stored_value = await get_cache(stored_key)
    if not stored_value:
        return None
    if isinstance(stored_value, bytes):
        stored_value = stored_value.decode("utf-8")
    return AggregatedData.model_validate(json.loads(stored_value))

async def save_aggregate(search_city: str, month: int, value: AggregatedData, ttl: int):
    stored_key = make_aggregate_key(search_city, month)

    # turns value from object-->python data-->JSON. Object itself is not JSON-serializable
    stored_value = json.dumps(value.model_dump(mode="json"))
    await set_cache(stored_key, stored_value, ttl)