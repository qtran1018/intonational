from __future__ import annotations
from pydantic import BaseModel, Field
from datetime import datetime, timezone
import statistics


class MetaData(BaseModel):
    source: str = "open-meteo-historical-weather"
    calculated_on: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    
    #Create inline, no arguments needed since values are defaulted

class Location(BaseModel):  
    latitude: float
    longitude: float

    #Create inline, is given a lat and lon

class TimePeriod(BaseModel):
    month: int
    year: int

    #Created inline, year is save_year when calculating which year to pull from.

class DailyStats(BaseModel):
    mean: float = Field(..., description="Average daily stat")
    median: float = Field(..., description="Median daily stat")

    @classmethod
    def from_values(cls, raw_daily_stat: list[float]) -> DailyStats:
        return cls(
            mean=statistics.mean(raw_daily_stat),
            median=statistics.median(raw_daily_stat)
        )

class WeatherData(BaseModel):
    temp_high: DailyStats
    temp_low: DailyStats
    apparent_high: DailyStats
    apparent_low: DailyStats
    wind_speed: DailyStats
    humidity: DailyStats
    precipitation: float
    weather_code_mode: int

    @classmethod
    def from_raw(cls, raw_daily: dict[str, list]) -> WeatherData:
        return cls(
            temp_high=DailyStats.from_values(raw_daily["temperature_2m_max"]),
            temp_low=DailyStats.from_values(raw_daily["temperature_2m_min"]),
            apparent_high=DailyStats.from_values(raw_daily["apparent_temperature_max"]),
            apparent_low=DailyStats.from_values(raw_daily["apparent_temperature_min"]),
            wind_speed=DailyStats.from_values(raw_daily["wind_speed_10m_mean"]),
            humidity=DailyStats.from_values(raw_daily["relative_humidity_2m_mean"]),
            precipitation=statistics.mean(raw_daily["precipitation_sum"]),
            weather_code_mode=statistics.mode(raw_daily["weather_code"])
        )


class HistoricalWeather(BaseModel):
    meta_data: MetaData
    location: Location
    time_period: TimePeriod
    weather_data: WeatherData

    @classmethod
    def from_api_response(cls, lat, lon, month, year, raw_data) -> HistoricalWeather:
        return cls(
            meta_data=MetaData(),
            location=Location(latitude=lat, longitude=lon),
            time_period=TimePeriod(month=month, year=year),
            weather_data=WeatherData.from_raw(raw_data["daily"])

        )