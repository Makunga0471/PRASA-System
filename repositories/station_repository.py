class StationRepository:

    def __init__(self):
        self.stations = []

    def get_all(self):
        return self.stations

    def add(self, station):
        self.stations.append(station)
        return station
