from enum import Enum

from pydantic import BaseModel, Field, Extra
from typing import Optional


class CategoryEnum(str, Enum):
    nutrition = "Nutrition"
    fitness = "Fitness"
    sleep = "Sleep"
    stress = "Stress"
    safety = "Safety"


class QuestionsModel(BaseModel):
    question: str = Field(..., min_length=5, max_length=255)
    category: CategoryEnum
