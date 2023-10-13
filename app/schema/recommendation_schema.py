from typing import List
from uuid import UUID

from pydantic import BaseModel, Field


class RecommendationRequestBaseModel(BaseModel):
    consequence: str = Field(..., min_length=5)
    recommendation: str = Field(..., min_length=5)
    recommendation_id: int = Field(..., le=12, ge=1)


class RecommendationResponseModel(BaseModel):
    id: UUID = Field(..., title="Recommendation id")

    class Config:
        orm_mode = True
