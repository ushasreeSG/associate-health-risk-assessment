get

from fastapi import APIRouter

from app.models import UserProfile, User
from app.models.base_model import SessionLocal
from app.schema_models import RegisterUserResponse, RegisterUserRequest

user_router = APIRouter()


@user_router.get("/register",response_model=RegisterUserResponse)
async def register(request:RegisterUserRequest):