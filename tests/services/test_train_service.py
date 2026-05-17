from services.train_service import TrainService
from models.train import Train
from fastapi import HTTPException
import pytest

service = TrainService()

def test_create_train_success():

    train = Train(
        id=1,
        train_name="Blue Train",
        status="Active",
        speed=120
    )

    result = service.create_train(train)

    assert result.train_name == "Blue Train"


def test_speed_limit():

    train = Train(
        id=2,
        train_name="Fast Train",
        status="Active",
        speed=250
    )

    with pytest.raises(HTTPException):
        service.create_train(train)