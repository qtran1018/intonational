def make_weather_key(lat: float, lon: float) -> str:
    return f"weather:{lat}:{lon}"

def make_fx_key(base_currency: str = "USD") -> str:
    return f"fx:rates:{base_currency.lower()}"