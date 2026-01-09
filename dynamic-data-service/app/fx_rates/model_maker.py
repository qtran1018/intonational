from app.fx_rates.model import FXrates
from typing import Dict

def make_fxrates_model(
        base_currency: str, 
        rates: Dict[str, float],
        timestamp: int  
    ) -> FXrates:
    
    return FXrates(
        base_currency = base_currency,
        rates = rates,
        timestamp = timestamp
    )