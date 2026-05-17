class TrainRepository:

    def __init__(self):
        self.trains = []

    def get_all(self):
        return self.trains

    def get_by_id(self, train_id):
        for train in self.trains:
            if train.id == train_id:
                return train
        return None

    def add(self, train):
        self.trains.append(train)
        return train

    def update(self, train_id, updated_train):

        for index, train in enumerate(self.trains):
            if train.id == train_id:
                self.trains[index] = updated_train
                return updated_train

        return None

    def delete(self, train_id):

        for train in self.trains:
            if train.id == train_id:
                self.trains.remove(train)
                return True

        return False