from pydantic import BaseModel, Field

class Station(BaseModel):
    id: int
    station_name: str = Field(..., min_length=2)
    location: str