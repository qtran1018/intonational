from fastapi import APIRouter
from app.geocoding.service import search_place
from app.geocoding.model import GeoData

router = APIRouter(tags=["Geocoding"])

@router.get("/geocode")
async def geocode_endpoint(search_term: str):
    places = await search_place(search_term)

    return places