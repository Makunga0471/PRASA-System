class Sensor:
    def __init__(self, sensor_id, type, status):
        self.sensor_id = sensor_id
        self.type = type
        self.status = status

    def detect(self):
        return f"{self.type} detected"

    def send_data(self):
        return "Data sent"