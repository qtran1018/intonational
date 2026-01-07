from fastapi import APIRouter
from app.routes.routes import router as aggregator_router

router = APIRouter(prefix="/api/v1")
router.include_router(aggregator_router)