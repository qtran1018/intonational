from app.services.country_factory import create_country_objects
from app.repositories.country_repository import upsert_country_data
# import asyncio

async def run_country_pipeline():
    country_objects = await create_country_objects()
    await upsert_country_data(country_objects)

# asyncio.run(run_country_pipeline())