from datetime import date
from calendar import monthrange
from app.weather_historical.model import HistoricalWeather
from app.weather_historical.client import get_historical_weather
from app.weather_historical.repository import query_weather, save_weather
import logging

logger = logging.getLogger("weather_historical")

async def search_weather(lat: float, lon: float, month: int):
    #Should not be an issue. Frontend should limit choices
    if not 1 <= month <= 12:
        raise ValueError("month must be between 1 and 12")

    cached = await query_weather(lat, lon, month)

    if cached:
        print("IN CACHE")
        logger.info("Weather cache HIT for %s,%s,%s", lat, lon, month)
        return cached
    else:
        print("NOT IN CACHE")
        logger.info("Weather cache MISS for %s, %s ,%s", lat, lon, month)
        current_year = date.today().year
        current_month = date.today().month

        start_date = date(current_year, month, 1)
        current_date = date(current_year, current_month, 1)

        # if the month I'm looking for is in the past from today (has full data)
        if start_date < current_date:
            #use current year
            last_day = monthrange(current_year, month)[1]
            end_date = date(current_year, month, last_day)
            save_year = current_year
        else:
            #use previous year
            last_day = monthrange(current_year-1, month)[1]
            start_date = date(current_year-1, month, 1) 
            end_date = date(current_year-1, month, last_day)
            save_year = current_year-1
    
        start_date_string = start_date.strftime("%Y-%m-%d")
        end_date_string = end_date.strftime("%Y-%m-%d")
        
        results = await get_historical_weather(lat, lon, start_date_string, end_date_string)

        weather_object = HistoricalWeather.from_api_response(lat, lon, month, save_year, results)
        await save_weather(weather_object)
        print("NOW IN CACHE")
        logger.info("Weather successfully cached for %s,%s,%s", lat, lon, month)

    return weather_object