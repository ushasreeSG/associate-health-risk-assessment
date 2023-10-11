from fastapi import APIRouter

from app.models import Questions
from app.models.base_model import SessionLocal
from app.schema_models import RegisterUserResponse, RegisterUserRequest

user_router = APIRouter()


@user_router.get("/post",response_model=RegisterUserResponse)
async def register(request:RegisterUserRequest):