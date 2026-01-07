from app.shared.db.mongo import db
from app.weather_historical.model import HistoricalWeather
from datetime import datetime, timezone

historical_weather = db["historical_weather"]
historical_weather.create_index([("inserted_on", 1)], expireAfterSeconds=31536000) #1 year expiry

async def query_weather(lat: float, lon: float, month: int):
    return historical_weather.find_one(
        {
            "latitude": lat,
            "longitude": lon,
            "month": month
        })

async def save_weather(weather_obj: HistoricalWeather):
    document = weather_obj.model_dump()
    document["inserted_on"] = datetime.now(timezone.utc)

    historical_weather.replace_one(
        {
            "latitude": weather_obj.latitude,
            "longitude": weather_obj.longitude,
            "month": weather_obj.month,
        },
        document,
        upsert=True)
    print(f"Document inserted or updated.")