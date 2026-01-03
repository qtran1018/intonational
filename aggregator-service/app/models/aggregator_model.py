from pydantic import BaseModel, Field
from typing import Optional

class AggregatedData(BaseModel): #TODO: update keys and add others
    id: int = Field(..., description="Unique ID for this location")
    name: str = Field(..., description="Location name. Localized following the &language= parameter, if possible")
    admin1: Optional[str] = Field(None, description="Name of hierarchical administrative areas this location resides in. Admin1 is the first administrative level (e.g., state, province, region). Localized following the &language= parameter, if possible")
    country: Optional[str] = Field(None, description="Country name. Localized following the &language= parameter, if possible")
    country_code: Optional[str] = Field(None, description="2 character ISO-3166-1 alpha2 ")
    latitude: float = Field(..., description="Geographical WGS84 coordinates of this location")
    longitude: float = Field(..., description="Geographical WGS84 coordinates of this location")