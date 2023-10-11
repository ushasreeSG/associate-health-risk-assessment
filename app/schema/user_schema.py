from pydantic import BaseModel, Field, Extra
from typing import Optional
from uuid import UUID


class UserModel(BaseModel):
    email: Optional[str] = Field(
        None, min_length=8, max_length=255, pattern="[a-zA-Z_.]@senecaglobal.com",
        example="ushasree.koneti@senecaglobal.com"
        )
