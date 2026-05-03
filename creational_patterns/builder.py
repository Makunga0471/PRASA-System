class TrainBuilder:
    def __init__(self):
        self.train = {}

    def set_id(self, train_id):
        self.train["id"] = train_id
        return self

    def set_status(self, status):
        self.train["status"] = status
        return self

    def set_location(self, location):
        self.train["location"] = location
        return self

    def build(self):
        return self.train