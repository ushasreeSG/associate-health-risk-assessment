from typing import List
from uuid import UUID

from pydantic import BaseModel, Field


class RecommendationRequestBaseModel(BaseModel):
    combination_id: int = Field(..., le=12, ge=1)


class RecommendationResponseModel(BaseModel):
    recommendation: str = Field(..., title="Recommendation")

    class Config:
        orm_mode = True
