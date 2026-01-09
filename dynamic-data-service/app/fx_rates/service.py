from app.fx_rates.model_maker import make_fxrates_model
from app.fx_rates.repository import query_rates, save_rates
from app.fx_rates.client import get_fx_rates
import logging

logger = logging.getLogger("fxrates")
DEFAULT_TTL = 28800

async def search_rates():
    cached = await query_rates()
    if cached:
        logger.info("FX rates cache HIT.")
        return cached
    
    else:
        logger.info("FX rates cache MISS.")
        raw = await get_fx_rates()
        fxrates_obj = make_fxrates_model(
            raw["source"],
            raw["quotes"],
            raw["timestamp"]
        )
        
        await save_rates(fxrates_obj, DEFAULT_TTL)
        logger.info("FX rates successfully cached.")
        
    return fxrates_obj