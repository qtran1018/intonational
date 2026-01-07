from app.weather_forecast.model import WeatherForecast
from datetime import date
from typing import List

def make_weather_forecast_model(
    lat: float,
    lon: float,
    date: List[date],
    weather_code: int,
    temp_high: List[float],
    temp_low: List[float],
    temp_high_apparent: List[float],
    temp_low_apparent: List[float],
    max_precip_prob: List[int],
    max_wind_speed: List[float],
) -> WeatherForecast:

    return WeatherForecast(
        latitude = lat,
        longitude = lon,
        date = date,
        weather_code = weather_code,
        temp_high = temp_high,
        temp_low = temp_low,
        temp_high_apparent = temp_high_apparent,
        temp_low_apparent = temp_low_apparent,
        max_precip_prob = max_precip_prob,
        max_wind_speed = max_wind_speed
    )