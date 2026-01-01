from pydantic import BaseModel, Field
from typing import Optional

class GeoData(BaseModel):
    id: int = Field(..., description="Place's ID")
    name: str = Field(..., description="Place's name")
    admin1: Optional[str] = Field(None, description="Administrative zone, such as State")
    country: str = Field(..., description="Place's country")
    latitude: float = Field(..., description="Place's latitude")
    longitude: float = Field(..., description="Place's longitude")

