from fastapi import APIRouter
from app.services.aggregator_service import test_service

router = APIRouter(tags=["Aggregator"])

@router.get("/aggregator")
async def aggregator_endpoint(search_term: str, month: int):
    places = await test_service(search_term)

    return places