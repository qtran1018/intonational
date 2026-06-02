from app.fx_rates.model_maker import make_fxrates_model
from app.fx_rates.repository import query_rates, save_rates
from app.fx_rates.client import get_fx_rates
from app.fx_rates.model import FXrates
from datetime import datetime, timezone
import asyncio
import logging

logger = logging.getLogger("fxrates")

STALE_AFTER_SECONDS = 28800  # 8 hours — matches original TTL, keep conservative for limited API quota


def _is_stale(fetched_at: str) -> bool:
    age = (datetime.now(timezone.utc) - datetime.fromisoformat(fetched_at)).total_seconds()
    return age > STALE_AFTER_SECONDS


async def _refresh_rates() -> None:
    try:
        raw = await get_fx_rates()
        fxrates_obj = make_fxrates_model(raw["source"], raw["quotes"], raw["timestamp"])
        await save_rates(fxrates_obj)
        logger.info("FX rates background refresh complete.")
    except Exception:
        logger.warning("FX rates background refresh failed.")


async def search_rates() -> FXrates:
    envelope = await query_rates()

    if envelope is None:
        logger.info("FX rates cache MISS — fetching live.")
        raw = await get_fx_rates()
        fxrates_obj = make_fxrates_model(raw["source"], raw["quotes"], raw["timestamp"])
        await save_rates(fxrates_obj)
        return fxrates_obj

    if _is_stale(envelope["fetched_at"]):
        logger.info("FX rates cache STALE — returning stale + refreshing.")
        asyncio.create_task(_refresh_rates())
    else:
        logger.info("FX rates cache HIT.")

    return FXrates.model_validate(envelope["data"])