from app.advisories.model_maker import create_country_objects
from app.advisories.repository import upsert_country_data

async def run_country_pipeline():
    country_objects = await create_country_objects()
    await upsert_country_data(country_objects)
