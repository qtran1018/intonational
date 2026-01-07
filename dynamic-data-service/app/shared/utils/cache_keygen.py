def make_weather_key(lat: float, lon: float) -> str:
    return f"weather:{lat}:{lon}"


def make_fx_key(base_currency: str, target_currency: str) -> str:
    return f"fx:{base_currency}:{target_currency}"