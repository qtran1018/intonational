from app.db.mongo import db
from app.models.country import CountryData
from pymongo import UpdateOne
from typing import List

countries = db["countries"]
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
        result = countries.bulk_write(operations)
        print(f"Upserted {result.upserted_count} documents, Modified {result.modified_count} documents.")

async def get_all_countries() -> list[dict]:
    return list(countries.find({}, {"_id": 0}))

def get_country_by_name(country_name: str) -> CountryData | None:
    result = countries.find_one({"name": {"$regex": f"^{country_name}$", "$options": "i"}}, {"_id": 0})
    if result:
        return CountryData(**result)
    return None
    