from app.advisories.model import CountryData
from app.advisories.scrape import do_scrape

async def create_country_objects():
    country_data_dicts = await do_scrape()
    country_objects = [CountryData(**data) for data in country_data_dicts]
    return country_objects