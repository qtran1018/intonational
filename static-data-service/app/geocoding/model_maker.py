from app.geocoding.model import GeoData

def make_geo_model(raw: dict) -> GeoData:
    return GeoData(
        id=raw["id"],
        name=raw["name"],
        admin1=raw.get("admin1"),
        country=raw.get("country"), #TODO: some results from open meteo don't have country for some reason, but may have a country code. Can make a workaround.
        country_code=raw.get("country_code"),
        latitude=raw["latitude"],
        longitude=raw["longitude"]
    )