from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.geocoding.service import search_place

router = APIRouter(prefix="/geocode", tags=["Geocoding"])

@router.get("/")
async def geocode_endpoint(search_term: str):
    places = await search_place(search_term)

    #TODO: allegedly, FastAPI models will turn my Pydantic model objects into JSON automatically
    # return JSONResponse(content=jsonable_encoder(places))
    return places