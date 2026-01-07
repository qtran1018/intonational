from pydantic import BaseModel, Field
from typing import Optional

class AggregatedData(BaseModel): #TODO: update keys and add others
    city: str = Field(..., description="Location name. Localized following the &language= parameter, if possible")
    admin1: Optional[str] = Field(None, description="Name of hierarchical administrative areas this location resides in. Admin1 is the first administrative level (e.g., state, province, region). Localized following the &language= parameter, if possible")
    country_code: Optional[str] = Field(None, description="2 character ISO-3166-1 alpha2 ")
    latitude: float = Field(..., description="Geographical WGS84 coordinates of this location")
    longitude: float = Field(..., description="Geographical WGS84 coordinates of this location")
    month: int
    year: int
    temp_high_mean: float
    temp_high_median: float
    temp_low_mean: float
    temp_low_median: float
    country: str = Field(..., description="Name of the country")
    link: str = Field(..., description="Link to the state.gov travel advisory page")
    date: str = Field(..., description="Date of the advisory")
    level: str = Field(..., description="Level of the advisory")
    notes: str = Field(..., description="Notes about the advisory")
    visa: str = Field(..., description="Visa requirements")
    vaccinations: str = Field(..., description="Vaccination requirements")
    passport_requirements: str = Field(..., description="Passport requirements")
    currency_restrictions: str = Field(..., description="Currency restrictions")