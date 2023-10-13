from uuid import UUID
from app.schema import QuestionRequestModel
from fastapi import APIRouter, Path
from app.service_layer import QuestionService
from fastapi.logger import logger
from app.models import Questions
from app.db_layer import CommonDbOperations

from app.lib.exception_handler import error_handler
from app.service_layer import CommonService

question_router = APIRouter()


@question_router.post("/create")
@error_handler
async def create_question(request: QuestionRequestModel):
    logger.info("Calling the post question API.")
    question = QuestionService().create_question(request)

    return question


@question_router.get("/{question_id}")
@error_handler
async def get_question_by_id(question_id: UUID = Path(..., example="123e4567-e89b-12d3-a456-426614174000")):
    question_details = CommonService.get_record_by_id(repo=CommonDbOperations(Questions), record_id=question_id)

    return question_details



