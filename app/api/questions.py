from fastapi import APIRouter

from app.models import Questions
from app.models.base_model import SessionLocal
from app.schemas import QuestionRequestModel
from app.service_layer import QuestionService
from fastapi.logger import logger

user_router = APIRouter()


@user_router.post("/create")
async def create_question(request: QuestionRequestModel):
    logger.info("Calling the register user API.")
    question = QuestionService().create_question(request)

    return question
