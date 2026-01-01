from app.shared.db.mongo import db
from pymongo import UpdateOne
from typing import List
from app.advisories.model import CountryData

advisories = db["country_advisories"]
async def upsert_country_data(country_objects: List[CountryData]) -> None:
    operations =  [
        UpdateOne(
            {"name": country.name},
            {"$set": country.model_dump()},
            upsert=True
        )
        for country in country_objects
    ]
    if operations:
        result = advisories.bulk_write(operations)
        print(f"Upserted {result.upserted_count} documents, Modified {result.modified_count} documents.")

async def get_all_countries() -> list[dict]:
    print("Querying MongoDB now...")
    return list(advisories.find({}, {"_id": 0}))

def get_country_by_name(country_name: str) -> CountryData | None:
    print("Querying MongoDB now...")
    result = advisories.find_one({"name": {"$regex": f"^{country_name}$", "$options": "i"}}, {"_id": 0})
    if result:
        return CountryData(**result)
    return None
    