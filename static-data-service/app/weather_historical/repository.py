from app.shared.db.mongo import db
from app.weather_historical.model import HistoricalWeather
from datetime import datetime, timezone

historical_weather = db["historical_weather"]

async def query_weather(lat: float, lon: float, month: int):
    return await historical_weather.find_one(
        {
            "location.latitude": lat,
            "location.longitude": lon,
            "time_period.month": month
        })      

async def save_weather(weather_obj: HistoricalWeather):
    document = weather_obj.model_dump()
    document["inserted_on"] = datetime.now(timezone.utc)

    await historical_weather.replace_one(
        {
            "location.latitude": weather_obj.location.latitude,
            "location.longitude": weather_obj.location.longitude,
            "time_period.month": weather_obj.time_period.month,
        },
        document,
        upsert=True)
    print(f"Document inserted or updated.")