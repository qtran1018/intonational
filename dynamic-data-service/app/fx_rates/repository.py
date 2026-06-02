from app.shared.utils.cache_keygen import make_fx_key
from app.shared.redis.redis_repository import set_cache, get_cache
from app.fx_rates.model import FXrates
from datetime import datetime, timezone
import json


async def query_rates() -> dict | None:
    stored_key = make_fx_key()
    stored_value = await get_cache(stored_key)
    if not stored_value:
        return None
    if isinstance(stored_value, bytes):
        stored_value = stored_value.decode("utf-8")
    return json.loads(stored_value)


async def save_rates(value: FXrates) -> None:
    stored_key = make_fx_key()
    envelope = {
        "data": value.model_dump(mode="json"),
        "fetched_at": datetime.now(timezone.utc).isoformat(),
    }
    await set_cache(stored_key, json.dumps(envelope))
