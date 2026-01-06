from fastapi import APIRouter
from app.geocoding.routes import router as geocode_router
from app.weather_historical.routes import router as weather_router
from app.advisories.routes import router as advisories_router


router = APIRouter(prefix="/api/v1")
router.include_router(geocode_router)
router.include_router(weather_router)
router.include_router(advisories_router)