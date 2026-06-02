from fastapi import APIRouter, Depends
from app.geocoding.service import search_place
from app.shared.auth import verify_token

router = APIRouter(tags=["Geocoding"])


@router.get("/geocode")
async def geocode_endpoint(
    search_term: str,
    _token: dict = Depends(verify_token),
):
    return await search_place(search_term)
