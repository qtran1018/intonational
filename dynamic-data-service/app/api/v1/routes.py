from fastapi import APIRouter
from app.weather_forecast.routes import router as weather_forecast_router
from app.fx_rates.routes import router as fx_rates_router

router = APIRouter(prefix="/api/v1")
router.include_router(weather_forecast_router)
router.include_router(fx_rates_router)