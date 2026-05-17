class IncidentRepository:

    def __init__(self):
        self.incidents = []

    def get_all(self):
        return self.incidents

    def add(self, incident):
        self.incidents.append(incident)
        return incident
