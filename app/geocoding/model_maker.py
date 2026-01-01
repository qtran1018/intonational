from app.geocoding.model import GeoData

def make_geo_model(raw: dict) -> GeoData:
    return GeoData(
        id=raw["id"],
        name=raw["name"],
        admin1=raw["admin1"],
        country=raw["country"],
        latitude=raw["latitude"],
        longitude=raw["longitude"]
    )