from app.geocoding.client import get_geocode
from app.geocoding.repository import query_city, save_results
from app.geocoding.model_maker import make_geo_model
from app.geocoding.model import GeoData
from typing import List
import logging

logger = logging.getLogger("Geocoding")

async def search_place(search_term: str) -> List[GeoData]:

    #normalize search term
    term = search_term.strip().lower()
    
    #check db for documents with search term
    cached = await query_city(term)
    if cached and len(cached["results"]) <= 20:
        logger.info("Geocode cache HIT for %s", term)
        results = cached["results"]

    #no results from db. call open-meteo, save the results to db
    else:
        logger.info("Geocode cache MISS for %s", term)
        raw = await get_geocode(term)
        results = raw.get("results", [])
        if results:
            await save_results(term, results)
            logger.info("Geocode successfully cached for %s", term)
    
    #make a list of geodata objects to validate and return
    geo_data_objects = [make_geo_model(geodata) for geodata in results]

    return geo_data_objects