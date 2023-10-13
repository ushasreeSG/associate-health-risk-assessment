from typing import List
from uuid import UUID

from pydantic import BaseModel, Field


class CombinationRequestBaseModel(BaseModel):
    user_id: UUID = Field(..., example="123e4567-e89b-12d3-a456-426614174000")


class CombinationResponseModel(CombinationRequestBaseModel):
    id: UUID = Field(..., example="123e4567-e89b-12d3-a456-426614174000")

    class Config:
        orm_mode = True