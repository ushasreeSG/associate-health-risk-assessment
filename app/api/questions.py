from fastapi import APIRouter

from app.models import Questions
from app.models.base_model import SessionLocal
from app.schema import QuestionRequestModel
from app.service_layer import QuestionService
from fastapi.logger import logger

question_router = APIRouter()


@question_router.post("/create")
async def create_question(request: QuestionRequestModel):
    logger.info("Calling the post question API.")
    question = QuestionService().create_question(request)

    return question


@question_router.get("/get_all")
async def get_all_question():
    logger.info("Calling all questions ")
    response=QuestionService().get_all()
    return response

