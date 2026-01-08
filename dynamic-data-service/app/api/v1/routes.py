from fastapi import APIRouter
from app.weather_forecast.routes import router as weather_forecast_router

router = APIRouter(prefix="/api/v1")
router.include_router(weather_forecast_router)