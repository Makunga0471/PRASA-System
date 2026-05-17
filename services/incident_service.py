from repositories.incident_repository import IncidentRepository

class IncidentService:

    def __init__(self):
        self.repo = IncidentRepository()

    def get_incidents(self):
        return self.repo.get_all()

    def create_incident(self, incident):

        allowed = ["Low", "Medium", "High"]

        if incident.severity not in allowed:
            raise ValueError("Invalid severity level")

        return self.repo.add(incident)
