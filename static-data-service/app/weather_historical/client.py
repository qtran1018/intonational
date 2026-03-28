from app.shared.http import get_client
import pandas as pd
from datetime import date
from calendar import monthrange

HISTORICAL_WEATHER_URL = "https://archive-api.open-meteo.com/v1/archive"
async def get_historical_weather(lat: float, lon: float, start_date_string: str, end_date_string: str):
    client = get_client()

    response = await client.get(
        HISTORICAL_WEATHER_URL,
        params = {
            "latitude": lat,
            "longitude": lon,
            "start_date": start_date_string,
            "end_date": end_date_string,
            "daily": 
                [
                    "temperature_2m_max",
                    "temperature_2m_min",
                    "weather_code",
                    "apparent_temperature_max",
                    "apparent_temperature_min",
                    "relative_humidity_2m_mean",
                    "precipitation_sum",
                    "wind_speed_10m_mean"
                ],
        }
    )
    response.raise_for_status()
    return response.json()