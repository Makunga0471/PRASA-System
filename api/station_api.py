from fastapi import APIRouter
from models.station import Station
from services.station_service import StationService

router = APIRouter()

service = StationService()

@router.get("/api/stations")
def get_stations():
    return service.get_stations()

@router.post("/api/stations")
def create_station(station: Station):
    return service.create_station(station)
