from app.geocoding.model import GeoData

def make_geo_model(raw: dict) -> GeoData:
    return GeoData(
        id=raw["id"], #required, almost 100% sure id will always be available
        name=raw["name"], #required, how else would it even get searched
        admin1=raw.get("admin1"), #optional, missing from some
        country=raw.get("country"), #TODO: some results from open meteo don't have country for some reason, but may have a country code. Can make a workaround.
        country_code=raw.get("country_code"), #optional, should have
        latitude=raw["latitude"], #required, for downstream weather data
        longitude=raw["longitude"] #required, for downstream weather data
    )