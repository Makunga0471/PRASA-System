from pydantic import BaseModel

class Incident(BaseModel):
    id: int
    incident_type: str
    severity: str
    description: str
