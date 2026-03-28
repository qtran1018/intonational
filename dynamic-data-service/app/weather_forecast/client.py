from app.shared.http import get_client

WEATHER_FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
async def get_weather_forecast(lat: float, lon: float):
    client = get_client()

    response = await client.get(
        WEATHER_FORECAST_URL,
        params = {
            "latitude": lat,
            "longitude": lon,
            "daily": [
                "temperature_2m_max",
                "temperature_2m_min",
                "apparent_temperature_max",
                "apparent_temperature_min",
                "precipitation_probability_max",
                "wind_speed_10m_max",
                "weather_code",
                "relative_humidity_2m_max"],
            "forecast_days": 14,
        }
    )
    response.raise_for_status()
    return response.json()