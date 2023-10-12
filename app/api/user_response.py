import json

from fastapi import APIRouter

from app.db_layer import UserResponseDBOperations, UserDBOperations
# from app.models import Questions
# from app.models.base_model import SessionLocal
# from app.schema import QuestionRequestModel
from app.service_layer import UserResponseService
from app.schema import UserRequestModel, UserCreateRequest
from fastapi.logger import logger

user_response_router = APIRouter()


@user_response_router.post("/create_user")
async def create_user(request: UserCreateRequest):
    user= UserDBOperations().create(
        register_dict=request, commit=False
    )
    return user

@user_response_router.post("/create")
async def create_question(request: UserRequestModel):
    logger.info("Calling the post question API.")
    # parsed_data = json.loads(request)
    parsed_data = request.request_list
    # response = QuestionService().get_all()
    # for each in response:
    user_response = UserResponseService().create(parsed_data)
    return user_response

# @user_response_router.get("/get_all")
# async def get_question_id(request: createQuestionRequest):
#     logger.info("Calling all questions ")
