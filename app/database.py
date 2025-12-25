from db_connection import db
import asyncio
from country_factory import create_country_objects
from pymongo import UpdateOne

countries = db["countries"]
async def upsert_country_data():
    country_objects = await create_country_objects()

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