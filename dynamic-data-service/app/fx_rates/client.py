from app.shared.http import get_client
from app.config import settings

FX_RATES_URL = "https://api.exchangerate.host/live"
async def get_fx_rates():
    client = get_client()

    response = await client.get(
        FX_RATES_URL,
        params = {
            "access_key": settings.FX_API_KEY
        }
    )
    response.raise_for_status()
    return response.json()