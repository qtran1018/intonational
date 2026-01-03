from app.shared.http import get_client
import pandas as pd
from datetime import date
from calendar import monthrange

HISTORICAL_WEATHER_URL = "https://archive-api.open-meteo.com/v1/archive"
async def get_historical_weather(lat: float, lon: float, month: int):
    client = get_client()

    #Should not be an issue. Frontend should limit choices
    if not 1 <= month <= 12:
        raise ValueError("month must be between 1 and 12")

    current_year = date.today().year
    current_month = date.today().month

    start_date = date(current_year, month, 1)
    current_date = date(current_year, current_month, 1)

    # if the month I'm looking for is in the past from today (has full data)
    if start_date < current_date:
        #use current year
        last_day = monthrange(current_year, month)[1]
        end_date = date(current_year, month, last_day)
    else:
        #use previous year
        last_day = monthrange(current_year-1, month)[1]
        start_date = date(current_year-1, month, 1) 
        end_date = date(current_year-1, month, last_day)
    
    start_date_string = start_date.strftime("%Y-%m-%d")
    end_date_string = end_date.strftime("%Y-%m-%d")

    response = await client.get(
        HISTORICAL_WEATHER_URL,
        params = {
            "latitude": lat,
            "longitude": lon,
            "start_date": start_date_string,
            "end_date": end_date_string,
            "daily": ["temperature_2m_max", "temperature_2m_min", "sunrise", "sunset"],
        }
    )
    response.raise_for_status()
    return response.json()