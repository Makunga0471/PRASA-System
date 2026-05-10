from factories.repository_factory import RepositoryFactory
from models.train import Train

repo = RepositoryFactory.get_train_repository("MEMORY")

train1 = Train("T001", "Blue Train", "Johannesburg to Pretoria")
train2 = Train("T002", "Metro Rail", "Soweto to Johannesburg")

repo.save(train1)
repo.save(train2)

print("All Trains:")
for train in repo.find_all():
    print(train)

print("\nFind Train By ID:")
print(repo.find_by_id("T001"))

repo.delete("T002")

print("\nAfter Delete:")
for train in repo.find_all():
    print(train)