from creational_patterns.singleton import DatabaseConnection
from creational_patterns.builder import TrainBuilder

def test_singleton():
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    assert db1 is db2

def test_builder():
    train = TrainBuilder().set_id("T1").set_status("Running").build()
    assert train["id"] == "T1"