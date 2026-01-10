#TODO may need date requested month too or other param, due to weather-forecast. 
    # shouldn't be a big issue but may have problems on month change.
def make_aggregate_key(search_city: str, month: int) -> str:
    return f"aggregate:{search_city}:{month}"