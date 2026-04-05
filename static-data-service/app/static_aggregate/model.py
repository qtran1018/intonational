from __future__ import annotations
from pydantic import BaseModel
from app.advisories.model import CountryData
from app.weather_historical.model import HistoricalWeather

class StaticDataResponse(BaseModel):
    advisory: CountryData
    historical_weather: HistoricalWeather

    @classmethod
    def from_api_reponse(cls, advisory_obj: CountryData, historical_weather_obj: HistoricalWeather) -> StaticDataResponse:
        return cls(
            advisory=advisory_obj,
            historical_weather=historical_weather_obj
        )