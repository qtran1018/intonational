from pydantic import BaseModel, Field
from typing import Optional

class CountryData(BaseModel):
    name: str = Field(..., description="Name of the country")
    link: str = Field(..., description="Link to the state.gov travel advisory page")
    date: str = Field(..., description="Date of the advisory")
    level: str = Field(..., description="Level of the advisory")
    notes: str = Field(..., description="Notes about the advisory")
    visa: str = Field(..., description="Visa requirements")
    vaccinations: str = Field(..., description="Vaccination requirements")
    passport_requirements: str = Field(..., description="Passport requirements")
    currency_restrictions: str = Field(..., description="Currency restrictions")
