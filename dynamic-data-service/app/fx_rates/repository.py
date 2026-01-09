from app.shared.utils.cache_keygen import make_fx_key
from app.shared.redis.redis_repository import set_cache, get_cache
from app.fx_rates.model import FXrates
import json

async def query_rates():
    stored_key = make_fx_key()
    stored_value = await get_cache(stored_key)

    if not stored_value:
        return None
    if isinstance(stored_value, bytes):
        stored_value = stored_value.decode("utf-8")
    
    return FXrates.model_validate(json.loads(stored_value))

async def save_rates(value: FXrates, ttl: int):
    stored_key = make_fx_key()
    stored_value = json.dumps(value.model_dump(mode="json"))
    await set_cache(stored_key, stored_value, ttl)
    