from repositories.train_repository import TrainRepository
from fastapi import HTTPException

class TrainService:

    def __init__(self):
        self.repo = TrainRepository()

    def get_trains(self):
        return self.repo.get_all()

    def get_train(self, train_id):

        train = self.repo.get_by_id(train_id)

        if not train:
            raise HTTPException(status_code=404, detail="Train not found")

        return train

    def create_train(self, train):

        existing_train = self.repo.get_by_id(train.id)

        if existing_train:
            raise HTTPException(status_code=400, detail="Train ID already exists")

        if train.speed > 180:
            raise HTTPException(status_code=400, detail="Train speed exceeds limit")

        return self.repo.add(train)

    def update_train(self, train_id, train):

        updated = self.repo.update(train_id, train)

        if not updated:
            raise HTTPException(status_code=404, detail="Train not found")

        return updated

    def delete_train(self, train_id):

        deleted = self.repo.delete(train_id)

        if not deleted:
            raise HTTPException(status_code=404, detail="Train not found")

        return {"message": "Train deleted successfully"}