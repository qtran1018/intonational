from app.shared.http import get_client

async def get_fx():
    client = get_client()
    FX_DATA_URL = "http://127.0.0.1:8000/api/v1/fx"
    response = await client.get(
        FX_DATA_URL,
        params={
            "country_name": country_name,
        }
    )
    response.raise_for_status()
    return response.json()

async def get_weaather_forecast():
    client = get_client()
    WEATHER_FORECAST_DATA_URL = "http://127.0.0.1:8000/api/v1/weather-forecast"
    response = await client.get(
        WEATHER_FORECAST_DATA_URL,
        params={
            "search_term": search_term,
        }
    )
    response.raise_for_status()
    return response.json()
