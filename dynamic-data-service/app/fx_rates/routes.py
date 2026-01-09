from fastapi import APIRouter
from app.fx_rates.service import search_rates
from app.fx_rates.model import FXrates

router = APIRouter(tags=["FX Rates"])

@router.get("/fxrates", response_model = FXrates)
async def fx_rates_endpoint():
    fxrates = await search_rates()
    return fxrates