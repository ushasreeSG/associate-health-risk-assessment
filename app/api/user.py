from fastapi import APIRouter, status

from app.db_layer import UserDBOperations
from app.schema import UserModel, UserCreateRequest
from app.lib.exception_handler import error_handler

user_router = APIRouter()


@user_router.post("/create", status_code=status.HTTP_201_CREATED,
                  response_model=UserModel,
                  summary="Create User",
                  tags=["User API"]
                  )
@error_handler
async def create_user(request: UserCreateRequest):
    user = UserDBOperations().create(
        register_dict=request, commit=False
        )
    return user
