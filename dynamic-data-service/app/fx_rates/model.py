from pydantic import BaseModel, Field
from typing import Dict
from datetime import datetime, timezone

class FXrates(BaseModel):
    base_currency: str
    rates: Dict[str, float]
    source: str = "exchangerate.host"
    timestamp: int
    retrieved_on: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))