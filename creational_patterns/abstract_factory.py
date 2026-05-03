class TrainFactory:
    def create_train(self):
        pass

class PassengerTrainFactory(TrainFactory):
    def create_train(self):
        return "Passenger Train"

class CargoTrainFactory(TrainFactory):
    def create_train(self):
        return "Cargo Train"