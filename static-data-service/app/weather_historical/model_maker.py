from app.weather_historical.model import TempStats, HistoricalWeather
from datetime import datetime, timezone

def make_temp_stats(mean: float, median: float) -> TempStats:
    return TempStats(
        mean = mean,
        median = median
    )

#TODO sunrise sunset median
def make_weather_model(
    lat: float, 
    lon: float, 
    month: int, 
    year: int, 
    temp_highs: TempStats, 
    temp_lows: TempStats
    ) -> HistoricalWeather:
    
    return HistoricalWeather(
        latitude = lat,
        longitude = lon,
        month = month,
        year = year,
        temp_high = temp_highs,
        temp_low = temp_lows,
        calculated_on = datetime.now(timezone.utc)
    )