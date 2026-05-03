class Maintenance:
    def __init__(self, maintenance_id, schedule, status):
        self.maintenance_id = maintenance_id
        self.schedule = schedule
        self.status = status

    def schedule_repair(self):
        return "Repair scheduled"

    def perform_repair(self):
        return "Repair completed"