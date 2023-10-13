from uuid import UUID, uuid4

from fastapi import APIRouter, Path, status
from pydantic import UUID4

from app.models import Combinations
from app.schema import RecommendationRequestBaseModel
from app.service_layer import CombinationService
from app.lib.exception_handler import error_handler
from fastapi.logger import logger
from app.service_layer.common_service import CommonService
from app.service_layer.recommendation_service import RecommendationService

recommendation_router = APIRouter()


@recommendation_router.post("/create", status_code=status.HTTP_201_CREATED,
                            description="Create Recommendation",
                            tags=["Recommendation APIs"]
                            )
@error_handler
async def create_recommendation(request: RecommendationRequestBaseModel):
    logger.info("Calling the create recommendation API.")
    combination = RecommendationService().create_recommendation(request)

    return combination


@recommendation_router.get("/{recommendation_id}", status_code=status.HTTP_200_OK,
                           description="Get Recommendation By Id",
                           tags=["Recommendation APIs"]
                           )
@error_handler
async def get_recommendation_by_id(recommendation_id: UUID = Path(..., example="123e4567-e89b-12d3-a456-426614174000")):
    logger.info("create recommendation service called")
    recommendation = CommonService.get_record_by_id(repo=Combinations, record_id=recommendation_id)
    logger.info("create recommendation service call completed")
    return recommendation


@recommendation_router.get("/user/{user_id}", status_code=status.HTTP_200_OK,
                           description="Get Recommendation for User",
                           tags=["Recommendation APIs"]
                           )
@error_handler
async def get_recommendations_user(user_id: UUID = Path(..., example="123e4567-e89b-12d3-a456-426614174000")):
    logger.info("get recommendation for user service called")
    recommendation = RecommendationService.get_by_user_id(str(user_id))
    logger.info("get recommendation for user service call completed")

    return recommendation
