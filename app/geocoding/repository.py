from app.shared.db.mongo import db
from datetime import datetime, timezone

geocodes = db["geocodes"]
geocodes.create_index([("inserted_on", 1)], expireAfterSeconds=31536000)

async def query_city(search_city: str):
    return geocodes.find_one({"search_term":search_city.strip().lower()})

async def save_results(search_city: str, results: list):
    document = {
        "search_term": search_city.strip().lower(),
        "results": results,
        "inserted_on": datetime.now(timezone.utc)
    }
    geocodes.replace_one(
        {"search_term": search_city}, 
        document,
        upsert=True)
    print(f"Document for {search_city} inserted or updated.")