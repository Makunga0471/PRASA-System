class Booking:
    def __init__(self, user, train):
        self.user = user
        self.train = train

    def create_booking(self):
        return f"Booking confirmed for {self.user} on {self.train}"