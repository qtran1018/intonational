from datetime import date
from calendar import monthrange
import statistics
from app.weather_historical.model import HistoricalWeather
from app.weather_historical.client import get_historical_weather
from app.weather_historical.repository import query_weather, save_weather
from app.weather_historical.model_maker import make_weather_model, make_temp_stats


async def search_weather(lat: float, lon: float, month: int):
    #Should not be an issue. Frontend should limit choices
    if not 1 <= month <= 12:
        raise ValueError("month must be between 1 and 12")

    cached = await query_weather(lat, lon, month)

    if cached:
        print("IN CACHE")
        cached.pop("_id", None)
        return HistoricalWeather.model_validate(cached)
    else:
        print("NOT IN CACHE")
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

        high_temps = results["daily"]["temperature_2m_max"]
        high_mean = statistics.mean(high_temps)
        high_median = statistics.median(high_temps)
        high_stats_obj = make_temp_stats(high_mean, high_median)

        low_temps = results["daily"]["temperature_2m_min"]
        low_mean = statistics.mean(low_temps)
        low_median = statistics.median(low_temps)
        low_stats_obj = make_temp_stats(low_mean, low_median)

        weather_object = make_weather_model(lat, lon, month, save_year, high_stats_obj, low_stats_obj)
        await save_weather(weather_object)
        print("NOW IN CACHE")

    return weather_object



