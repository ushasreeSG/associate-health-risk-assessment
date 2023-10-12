import json

from fastapi import APIRouter

from app.db_layer import UserResponseDBOperations, UserDBOperations
from app.service_layer import UserResponseService
from app.schema import UserRequestModel, UserCreateRequest
from fastapi.logger import logger
from app.lib.exception_handler import error_handler

user_response_router = APIRouter()


@user_response_router.post("/create_user")
@error_handler
async def create_user(request: UserCreateRequest):
    user = UserDBOperations().create(
        register_dict=request, commit=False
        )
    return user


@user_response_router.post("/create")
@error_handler
async def create_question(request: UserRequestModel):
    logger.info("Calling the post user response API.")
    # parsed_data = json.loads(request)
    parsed_data = request.request_list
    # response = QuestionService().get_all()
    # for each in response:
    user_response = UserResponseService().create(parsed_data)
    return user_response

# @user_response_router.get("/get_all")
# async def get_question_id(request: createQuestionRequest):
#     logger.info("Calling all questions ")
