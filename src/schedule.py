class Schedule:
    def __init__(self):
        self.schedules = [
            {
                "train": "PRASA001",
                "route": "JHB-Pretoria",
                "departure": "08:00",
                "arrival": "09:00",
                "platform": "1",
                "frequency": "Weekdays",
                "status": "On Time"
            },
            {
                "train": "PRASA002",
                "route": "JHB-Soweto",
                "departure": "09:30",
                "arrival": "10:15",
                "platform": "2",
                "frequency": "Daily",
                "status": "Delayed"
            }
        ]

    def display(self):
        return self.schedules

    def get_updates(self):
        updates = []
        for s in self.schedules:
            if s["status"] != "On Time":
                updates.append(f"{s['train']} is {s['status']}")
        return updates