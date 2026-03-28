from pydantic import BaseModel, Field
from typing import Optional

class TempStats(BaseModel):
    mean: float = Field(..., description="Average daily temperature")
    median: float = Field(..., description="Median daily temperature")

class GeographicData(BaseModel):
    city: str = Field(..., description="Location name. Localized following the &language= parameter, if possible")
    admin1: Optional[str] = Field(None, description="Name of hierarchical administrative areas this location resides in. Admin1 is the first administrative level (e.g., state, province, region). Localized following the &language= parameter, if possible")
    country_code: Optional[str] = Field(None, description="2 character ISO-3166-1 alpha2 ")
    latitude: float = Field(..., description="Geographical WGS84 coordinates of this location")
    longitude: float = Field(..., description="Geographical WGS84 coordinates of this location")

class WeatherHistorical(BaseModel):
    weather_code_mode: int = Field(..., description="Mode for weather code")
    temp_high: TempStats
    temp_low: TempStats
    humidity: TempStats

class WeatherForecast(BaseModel):
    pass

class Weather(BaseModel):
    historical: WeatherHistorical
    forecast: WeatherForecast
    
class AggregatedData(BaseModel): #TODO: update keys and add others
    geography: GeographicData
    weather: Weather
    month: int
    year: int

    

    country: str = Field(..., description="Name of the country")
    link: str = Field(..., description="Link to the state.gov travel advisory page")
    date: str = Field(..., description="Date of the advisory")
    level: str = Field(..., description="Level of the advisory")
    notes: str = Field(..., description="Notes about the advisory")
    visa: str = Field(..., description="Visa requirements")
    vaccinations: str = Field(..., description="Vaccination requirements")
    passport_requirements: str = Field(..., description="Passport requirements")
    currency_restrictions: str = Field(..., description="Currency restrictions")


