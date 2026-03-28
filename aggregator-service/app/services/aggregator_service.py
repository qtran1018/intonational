from app.models.aggregator_model_maker import make_aggregate_model, make_temp_stats
from app.clients.static_client import get_advisories, get_geocodes, get_historical_weather
from app.clients.dynamic_client import get_fx, get_weaather_forecast
from app.repository.repository import query_aggregate, save_aggregate
from datetime import datetime, date, timezone
import logging

logger = logging.getLogger("aggregator")
DEFAULT_TTL = 3600

#TODO CRITICAL: geodata returns a list, need to send list to user, they select 1, and then backend selects 1, probably via geodata ID
async def search_aggregate(search_city: str, month: int):
    cached = await query_aggregate(search_city, month)

    if cached:
        return cached
    else:

        #GEOCODES
        geodata = await get_geocodes(search_city)
        lat = geodata["latitude"]
        lon = geodata["longitude"]
        admin1 = geodata["admin1"]
        year = datetime.now(timezone.utc).year #TODO Check if this is needed.
        country = geodata["country"]
        country_code = geodata["country_code"]

        #TODO: advisories, may need some type of mapping

        #HISTORICAL WEATHER
        historical_weather = await get_historical_weather(lat, lon, month)
        weather_year = historical_weather["year"]

        temp_high_mean = historical_weather["temp_high"]["mean"]
        temp_high_median = historical_weather["temp_high"]["median"]
        temp_low_mean = historical_weather["temp_low"]["mean"]
        temp_low_median = historical_weather["temp_low"]["median"]
        weather_code_mode = historical_weather["weather_code_mode"]

        temp_stats_highs = make_temp_stats(temp_high_mean, temp_high_median) # INCLUDE INTO AGGREGATE MODEL
        temp_stats_lows = make_temp_stats(temp_low_mean, temp_low_median)

        #ADVISORIES

        #TODO: may need some mapping. openmeteo geocode country names may not match advisory names
        
        #advisories = get_advisories(country)

        #WEATHER FORECAST
        weather_forecast = get_weaather_forecast(lat, lon)

        
        #FX Rates
        fx_rates = get_fx() #gets all FX rates.


        

























    
    aggregate_obj = make_aggregate_model(

    )
    return aggregate_obj