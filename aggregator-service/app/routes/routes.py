from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.services.aggregator_service import test_service

router = APIRouter(prefix="/search", tags=["Aggregator"])

@router.get("/")
async def aggregator_endpoint(search_term: str):
    places = await test_service(search_term)

    #TODO: allegedly, FastAPI models will turn my Pydantic model objects into JSON automatically
    # return JSONResponse(content=jsonable_encoder(places))
    return places