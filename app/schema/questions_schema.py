from enum import Enum

from pydantic import BaseModel, Field, Extra
from typing import Optional


class CategoryEnum(str, Enum):
    nutrition = "Nutrition"
    fitness = "Fitness"
    sleep = "Sleep"
    stress = "Stress"
    safety = "Safety"


class QuestionRequestModel(BaseModel):
    question: str = Field(..., min_length=5, max_length=255)
    category_id: int = Field(..., le=6, ge=0)
