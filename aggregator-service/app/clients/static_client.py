from app.http import get_client

STATIC_DATA_URL = "http://127.0.0.1:8000/geocode" #TODO setup containers to run
async def get_static_data(search_term: str):
    client = get_client()

    response = await client.get(
        STATIC_DATA_URL,
        params={
            "search_term": search_term,
        }
    )
    response.raise_for_status()
    return response.json()