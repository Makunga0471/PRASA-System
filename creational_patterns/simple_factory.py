from src.sensor import Sensor

class SensorFactory:
    @staticmethod
    def create_sensor(sensor_type):
        return Sensor("S1", sensor_type, "Active")