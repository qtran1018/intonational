from app.shared.http import http_client

GEOCODER_URL = "https://geocoding-api.open-meteo.com/v1/search"
async def get_geocode(search_city: str):
    if http_client is None:
        raise RuntimeError("HTTP client not initialized")
    
    response = await http_client.get(
        GEOCODER_URL,
        params={
            "name": search_city,
            "language": "en",
            "format": "json",
            "count": 15
        }
    )
    response.raise_for_status()
    return response.json()