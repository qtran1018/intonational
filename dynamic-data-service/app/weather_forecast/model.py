from pydantic import BaseModel, Field
from typing import List
from datetime import datetime, date, timezone

#TODO add unit measurements (C, km/h)
class WeatherForecast(BaseModel):
    latitude: float
    longitude: float
    dates: List[date]
    weather_code: List[int]
    temp_high: List[float]
    temp_low: List[float]
    temp_high_apparent: List[float]
    temp_low_apparent: List[float]
    max_precip_prob: List[int]
    max_wind_speed: List[float]
    source: str = "open-meteo-historical-weather"
    timezone: str = "UTC"
    retrieved_on: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))