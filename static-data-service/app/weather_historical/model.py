from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime, timezone

class TempStats(BaseModel):
    mean: float = Field(..., description="Average daily temperature")
    median: float = Field(..., description="Median daily temperature")

class HistoricalWeather(BaseModel):
    latitude: float
    longitude: float
    month: int
    year: int
    temp_high: TempStats
    temp_low: TempStats
    source: str = "open-meteo-historical-weather"
    calculated_on: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    