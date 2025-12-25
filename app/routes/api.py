from fastapi import APIRouter, HTTPException
# from app.db.mongo import db
from app.repositories.country_repository import get_all_countries, get_country_by_name
from typing import List
from app.models.country import CountryData

router = APIRouter(prefix="/countries", tags=["Countries"])

#TODO: add in-memory caching for these routes

@router.get("/", response_description="List of all countries.", response_model=List[dict])
async def list_countries():
    countries = await get_all_countries()
    return countries

@router.get("/{country_name}", response_description="Get one country.", response_model=CountryData)
def get_country(country_name: str):
    # country_name = country_name.lower()
    country = get_country_by_name(country_name)
    if not country:
        raise HTTPException(status_code=404, detail=f"Country '{country_name}' not found.")
    return country