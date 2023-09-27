from uuid import UUID
from pydantic import BaseModel, Field, Extra
from typing import Optional


class UserResponseModel(BaseModel):
    user_id: UUID = Field(..., title="User id")
    question_id: UUID = Field(..., title="Question id")
    flag: bool = Field(..., title="User Response")

