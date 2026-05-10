class Train:

    def __init__(self, train_id, train_name, route):
        self.train_id = train_id
        self.train_name = train_name
        self.route = route

    def __str__(self):
        return f"{self.train_name} - {self.route}"