from repositories.inmemory.in_memory_train_repository import InMemoryTrainRepository
from repositories.database.database_train_repository import DatabaseTrainRepository
from repositories.inmemory import RepositoryFactory

class RepositoryFactory:

    @staticmethod
    def get_train_repository(storage_type):

        if storage_type == "MEMORY":
            return InMemoryTrainRepository()

        elif storage_type == "DATABASE":
            return DatabaseTrainRepository()

        else:
            raise ValueError("Invalid storage type")