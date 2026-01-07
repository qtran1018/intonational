from app.shared.http import get_client

async def get_advisories(country_name: str):
    client = get_client()
    ADVISORIES_DATA_URL = "http://127.0.0.1:8000/api/v1/advisories"
    response = await client.get(
        ADVISORIES_DATA_URL,
        params={
            "country_name": country_name,
        }
    )
    response.raise_for_status()
    return response.json()

async def get_geocodes(search_term: str):
    client = get_client()
    GEOCODES_DATA_URL = "http://127.0.0.1:8000/api/v1/geocode"
    response = await client.get(
        GEOCODES_DATA_URL,
        params={
            "search_term": search_term,
        }
    )
    response.raise_for_status()
    return response.json()

async def get_historical_weather(lat: float, lon: float, month: int):
    client = get_client()
    HISTORICAL_WEATHER_DATA_URL = "http://127.0.0.1:8000/api/v1/historical-weather"
    response = await client.get(
        HISTORICAL_WEATHER_DATA_URL,
        params={
            "lat": lat,
            "lon": lon,
            "month": month
        }
    )
    response.raise_for_status()
    return response.json()