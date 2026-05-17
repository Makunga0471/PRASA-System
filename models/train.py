from pydantic import BaseModel, Field

class Train(BaseModel):
    id: int
    train_name: str = Field(..., min_length=2)
    status: str
    speed: int = Field(..., ge=0, le=180)
