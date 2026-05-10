import unittest

from repositories.inmemory.in_memory_train_repository import InMemoryTrainRepository
from models.train import Train

class TestTrainRepository(unittest.TestCase):

    def setUp(self):
        self.repo = InMemoryTrainRepository()

    def test_save_train(self):
        train = Train("T001", "Blue Train", "Johannesburg to Pretoria")

        self.repo.save(train)

        self.assertIsNotNone(self.repo.find_by_id("T001"))

    def test_delete_train(self):
        train = Train("T001", "Blue Train", "Johannesburg to Pretoria")

        self.repo.save(train)

        self.repo.delete("T001")

        self.assertIsNone(self.repo.find_by_id("T001"))

if __name__ == '__main__':
    unittest.main()