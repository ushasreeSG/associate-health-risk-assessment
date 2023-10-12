from uuid import UUID
from pydantic import BaseModel, Field, Extra
from typing import Optional, List


class UserResponseModel(BaseModel):
    user_id: UUID = Field(..., title="User id")
    question_id: UUID = Field(..., title="Question id")
    response_flag: bool = Field(..., title="User Response")

class UserRequestModel(BaseModel):
    request_list: List[UserResponseModel]

class UserCreateRequest(BaseModel):
    email: str = Field(
        None, min_length=8, max_length=255, pattern="[a-zA-Z_.]@senecaglobal.com",
        example="ushasree.koneti@senecaglobal.com"
        )