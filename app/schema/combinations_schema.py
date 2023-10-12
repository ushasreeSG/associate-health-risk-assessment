from typing import List
from uuid import UUID

from pydantic import BaseModel, Field


class CombinationRequestBaseModel(BaseModel):
    combination_id: int = Field(..., le=12, ge=1)
    question_id: UUID = Field(...)
    combination_flag: bool = Field(..., title="True or False")


class CombinationResponseModel(CombinationRequestBaseModel):
    id: UUID = Field(..., example="123e4567-e89b-12d3-a456-426614174000")

    class Config:
        orm_mode = True
