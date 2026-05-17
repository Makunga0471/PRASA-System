from fastapi import APIRouter, status
from typing import List

from models.train import Train
from services.train_service import TrainService

router = APIRouter(
    tags=["Train Management"]
)

service = TrainService()

@router.get(
    "/api/trains",
    response_model=List[Train],
    status_code=status.HTTP_200_OK
)
def get_trains():
    return service.get_trains()

@router.get(
    "/api/trains/{train_id}",
    response_model=Train
)
def get_train(train_id: int):
    return service.get_train(train_id)

@router.post(
    "/api/trains",
    response_model=Train,
    status_code=status.HTTP_201_CREATED
)
def create_train(train: Train):
    return service.create_train(train)

@router.put(
    "/api/trains/{train_id}",
    response_model=Train
)
def update_train(train_id: int, train: Train):
    return service.update_train(train_id, train)

@router.delete(
    "/api/trains/{train_id}"
)
def delete_train(train_id: int):
    return service.delete_train(train_id)