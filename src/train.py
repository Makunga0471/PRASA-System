class Train:
    def __init__(self, train_id, status, location):
        self.train_id = train_id
        self.status = status
        self.location = location

    def start(self):
        self.status = "Running"

    def stop(self):
        self.status = "Stopped"

    def update_location(self, location):
        self.location = location