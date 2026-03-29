from __future__ import annotations
from pydantic import BaseModel, Field
from typing import List
from datetime import datetime, date, timezone

class MetaData(BaseModel):
    source: str = "open-meteo-weather-forecast"
    retrieved_on: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class Location(BaseModel):  
    latitude: float
    longitude: float
    timezone: str = "UTC"

class DailyForecast(BaseModel):
    date: str
    weather_code: int
    temp_high: float
    temp_low: float
    temp_high_apparent: float
    temp_low_apparent: float
    max_precip_prob: int
    max_wind_speed: float

class ForecastData(BaseModel):
    daily_forecast: List[DailyForecast]

    @classmethod
    def from_raw(cls, raw_daily: dict) -> ForecastData:

        expected_length = len(raw_daily["time"])
        assert all(
            len(raw_daily[key]) == expected_length
            for key in ["weather_code", "temperature_2m_max", "temperature_2m_min",
                    "apparent_temperature_max", "apparent_temperature_min",
                    "precipitation_probability_max", "wind_speed_10m_max"]
        ), "Mismatched list lengths in raw forecast data."

        daily_forecast = []
        for i in range(expected_length):
            daily_forecast.append(
                DailyForecast(
                    date=raw_daily["time"][i],
                    weather_code=raw_daily["weather_code"][i],
                    temp_high=raw_daily["temperature_2m_max"][i],
                    temp_low=raw_daily["temperature_2m_min"][i],
                    temp_high_apparent=raw_daily["apparent_temperature_max"][i],
                    temp_low_apparent=raw_daily["apparent_temperature_min"][i],
                    max_precip_prob=raw_daily["precipitation_probability_max"][i],
                    max_wind_speed=raw_daily["wind_speed_10m_max"][i]
                )
            )
        return cls(daily_forecast=daily_forecast)

#TODO add unit measurements (C, km/h)
class WeatherForecast(BaseModel):
    meta_data: MetaData
    location: Location
    forecast_data: ForecastData

    @classmethod
    def from_api_response(cls, lat:float, lon:float, raw_data:dict) -> WeatherForecast:
        return cls(
            meta_data=MetaData(),
            location=Location(latitude=lat, longitude=lon),
            forecast_data=ForecastData.from_raw(raw_data["daily"])
        )
