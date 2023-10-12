from uuid import UUID

from fastapi import APIRouter, Path

from app.models import Combinations
from app.schema import CombinationRequestBaseModel, CombinationResponseModel
from app.service_layer import CombinationService
from app.lib.exception_handler import error_handler
from fastapi.logger import logger
from app.service_layer.common_service import CommonService

recommendation_router = APIRouter()


@recommendation_router.post("/create")
@error_handler
async def create_recommendation(request: CombinationRequestBaseModel):
    logger.info("Calling the create recommendation API.")
    combination = RecommendationService().create_recommendation(request)

    return combination


@recommendation_router.get("/{recommendation_id}")
@error_handler
async def get_recommendation_by_id(recommendation_id: UUID = Path(..., example="123e4567-e89b-12d3-a456-426614174000")):
    recommendation = CommonService.get_record_by_id(repo=Combinations, record_id=recommendation_id)

    return recommendation
