from uuid import UUID

from fastapi import APIRouter, Path

from app.models import Combinations
from app.schema import CombinationRequestBaseModel, CombinationResponseModel
from app.service_layer import CombinationService
from app.lib.exception_handler import error_handler
from fastapi.logger import logger
from app.service_layer.common_service import CommonService
from app.db_layer import CommonDbOperations

combination_router = APIRouter()


@combination_router.post("/create")
@error_handler
async def create_combination(request: CombinationRequestBaseModel):
    logger.info("Calling the create combination API.")
    combination = CombinationService().create_combination(request)

    return combination


@combination_router.get("/{combination_id}")
@error_handler
async def get_combination_by_id(combination_id: UUID = Path(..., example="123e4567-e89b-12d3-a456-426614174000")):
    combination = CommonService.get_record_by_id(repo=CommonDbOperations(Combinations), record_id=combination_id)

    return combination
