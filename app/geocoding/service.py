from app.geocoding.client import get_geocode
from app.geocoding.repository import query_city, save_results
from app.geocoding.model_maker import make_geo_model
from app.geocoding.model import GeoData
from typing import List

async def search_place(search_term: str) -> List[GeoData]:

    #normalize search term
    term = search_term.strip().lower()
    
    #check db for documents with search term
    cached = await query_city(term)
    if cached:
        results = cached["results"]

    #no results from db. call open-meteo, save the results to db
    else:
        raw = await get_geocode(term)
        results = raw.get("results", [])
        if results:
            await save_results(term, results)
    
    #make a list of geodata objects to validate and return
    geo_data_objects = [make_geo_model(geodata) for geodata in results]

    return geo_data_objects