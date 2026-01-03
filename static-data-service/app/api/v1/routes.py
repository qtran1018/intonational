from fastapi import APIRouter
from app.geocoding.routes import router as geocode_router


router = APIRouter(prefix="/api/v1")
router.include_router(geocode_router)