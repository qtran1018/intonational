from app.geocoding.client import get_geocode
from app.geocoding.repository import query_city, save_results

async def search_place(search_city: str):

    term = search_city.strip().lower()
    
    #check if city name has been searched before and cached.
    #entire list of results from open-meteo are saved for that search term.
    cached = await query_city(term)
    if cached:
        results = cached["results"]
    else:
        raw = await get_geocode(term)
        results = raw.get("results", [])
        if results:
            await save_results(term, results)

    if len(results) == 1:
        response = {
            "status": "resolved",
            "place": resolve_place(results[0])
        }
        return response
    
    elif len(results) > 1:
        response = {
            "status": "ambiguous",
            "options": results
        }
        return response
    
    else:
        response = {
            "status": "not_found", 
            "options": []
        }
        return response
    
def resolve_place(result: dict):

    return {
        "id": result["id"],
        "name": result["name"],
        "admin1": result["admin1"],
        "country": result["country"],
        "latitude": result["latitude"],
        "longitude": result["longitude"]
    }