from fastapi import APIRouter, Depends
from app.fx_rates.service import search_rates
from app.fx_rates.model import FXrates
from app.shared.auth import verify_token

router = APIRouter(tags=["FX Rates"])


@router.get("/fxrates", response_model=FXrates)
async def fx_rates_endpoint(_token: dict = Depends(verify_token)):
    return await search_rates()
