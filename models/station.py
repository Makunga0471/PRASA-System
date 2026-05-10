class Station:

    def __init__(self, station_id, station_name, location):
        self.station_id = station_id
        self.station_name = station_name
        self.location = location

    def __str__(self):
        return f"{self.station_name} - {self.location}"