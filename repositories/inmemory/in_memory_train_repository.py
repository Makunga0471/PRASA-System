from repositories.inmemory import RepositoryFactory
from repositories.train_repository import TrainRepository
from models.train import Train
from typing import Optional, List

class InMemoryTrainRepository(TrainRepository):

    def __init__(self):
        self._storage = {}

    def save(self, train: Train) -> None:
        self._storage[train.train_id] = train

    def find_by_id(self, train_id: str) -> Optional[Train]:
        return self._storage.get(train_id)

    def find_all(self) -> List[Train]:
        return list(self._storage.values())

    def delete(self, train_id: str) -> None:
        if train_id in self._storage:
            del self._storage[train_id]