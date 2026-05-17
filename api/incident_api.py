from fastapi import APIRouter
from models.incident import Incident
from services.incident_service import IncidentService

router = APIRouter()

service = IncidentService()

@router.get("/api/incidents")
def get_incidents():
    return service.get_incidents()

@router.post("/api/incidents")
def create_incident(incident: Incident):
    return service.create_incident(incident)
