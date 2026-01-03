from app.clients.static_client import get_static_data

async def test_service(search_term: str):
    return get_static_data(search_term)