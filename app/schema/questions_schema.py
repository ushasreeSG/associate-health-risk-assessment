from pydantic import BaseModel, Field


class QuestionRequestModel(BaseModel):
    question: str = Field(..., min_length=5, max_length=255)
    category_id: int = Field(..., le=6, ge=0)
