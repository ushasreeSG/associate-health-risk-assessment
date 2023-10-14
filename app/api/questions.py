from uuid import UUID
from app.schema import QuestionRequestModel
from fastapi import APIRouter, Path, status
from app.service_layer import QuestionService
from fastapi.logger import logger
from app.models import Questions
from app.db_layer import CommonDbOperations

from app.lib.exception_handler import error_handler
from app.service_layer import CommonService

question_router = APIRouter()


@question_router.post("/create", status_code=status.HTTP_201_CREATED,
                      summary="Create Question",
                      tags=["Question APIs"]
                      )
@error_handler
async def create_question(request: QuestionRequestModel):
    logger.info("Create question api service called")
    question = QuestionService().create_question(request)
    logger.info("Create question api service call completed")
    return question


@question_router.get("/{question_id}", status_code=status.HTTP_200_OK,
                     summary="Get Question By Id",
                     tags=["Question APIs"]
                     )
@error_handler
async def get_question_by_id(question_id: UUID = Path(..., example="123e4567-e89b-12d3-a456-426614174000")):
    logger.info("Get question by id service called")
    question_details = CommonService.get_record_by_id(repo=CommonDbOperations(Questions), record_id=question_id)
    logger.info("Get question by id service call completed")
    return question_details



