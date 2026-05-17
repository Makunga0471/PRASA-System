from repositories.station_repository import StationRepository

class StationService:

    def __init__(self):
        self.repo = StationRepository()

    def get_stations(self):
        return self.repo.get_all()

    def create_station(self, station):

        if station.station_name == "":
            raise ValueError("Station name cannot be empty")

        return self.repo.add(station)
