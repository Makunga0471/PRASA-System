class Track:
    def __init__(self, track_id, condition, location):
        self.track_id = track_id
        self.condition = condition
        self.location = location

    def update_condition(self, condition):
        self.condition = condition