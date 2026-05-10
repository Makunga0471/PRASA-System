from repositories.station_repository import StationRepository
from models.station import Station
from typing import Optional, List

class InMemoryStationRepository(StationRepository):

    def __init__(self):
        self._storage = {}

    def save(self, station: Station) -> None:
        self._storage[station.station_id] = station

    def find_by_id(self, station_id: str) -> Optional[Station]:
        return self._storage.get(station_id)

    def find_all(self) -> List[Station]:
        return list(self._storage.values())

    def delete(self, station_id: str) -> None:
        if station_id in self._storage:
            del self._storage[station_id]