from app.shared.db.mongo import db
from datetime import datetime, timezone

historical_weather = db["historical_weather"]

async def query_weather(lat: float, lon: float, month: int):
    return historical_weather.find_one(
        {
            "latitude": lat,
            "longitude": lon,
            "month": month
        })

#TODO: save_weather needs complete remake, below is geocode
async def save_weather(search_city: str, results: list):
    document = {
        "search_term": search_city.strip().lower(),
        "results": results,
        "inserted_on": datetime.now(timezone.utc)
    }
    historical_weather.replace_one(
        {"search_term": search_city}, 
        document,
        upsert=True)
    print(f"Document for {search_city} inserted or updated.")