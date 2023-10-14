import json

from fastapi import APIRouter, status

from app.service_layer import UserResponseService
from app.schema import UserRequestModel, UserCreateRequest
from fastapi.logger import logger
from app.lib.exception_handler import error_handler

user_response_router = APIRouter()


@user_response_router.post("/create", status_code=status.HTTP_201_CREATED,
                           summary="Record User Response",
                           tags=["User Response API"]
                           )
@error_handler
async def create_question(request: UserRequestModel):
    logger.info("Calling the create user response API.")
    parsed_data = request.request_list
    user_response = UserResponseService().create(parsed_data)
    logger.info("Create user response call completed")
    return user_response
