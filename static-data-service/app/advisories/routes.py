from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.advisories.repository import get_country_by_name

router = APIRouter(tags=["Advisories"])

@router.get("/advisories")
async def advisories_endpoint(country_name: str):
    advisory = await get_country_by_name(country_name)

    return advisory