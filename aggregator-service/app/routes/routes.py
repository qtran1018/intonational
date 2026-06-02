from fastapi import APIRouter, Depends
from app.services.aggregator_service import test_service
from app.shared.auth import verify_token

router = APIRouter(tags=["Aggregator"])


@router.get("/aggregator")
async def aggregator_endpoint(
    search_term: str,
    month: int,
    _token: dict = Depends(verify_token),
):
    places = await test_service(search_term)
    return places
