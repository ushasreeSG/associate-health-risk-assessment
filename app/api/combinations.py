from uuid import UUID

from fastapi import APIRouter, Path, status

from app.models import Combinations
from app.schema import CombinationRequestBaseModel, CombinationResponseModel
from app.service_layer import CombinationService
from app.lib.exception_handler import error_handler
from fastapi.logger import logger
from app.service_layer.common_service import CommonService
from app.db_layer import CommonDbOperations

combination_router = APIRouter()


@combination_router.post("/create", status_code=status.HTTP_201_CREATED,
                         description="Create Combination",
                         tags=["Combination APIs"]
                         )
@error_handler
async def create_combination(request: CombinationRequestBaseModel):
    logger.info("API called - /combination/create")
    combination = CombinationService().create_combination(request)
    logger.info("/combination/create API call completed.")
    return combination


@combination_router.get("/{combination_id}", response_model=CombinationResponseModel,
                        status_code=status.HTTP_200_OK,
                        description="Get Combination By Id",
                        tags=["Combination APIs"]
                        )
@error_handler
async def get_combination_by_id(combination_id: UUID = Path(..., example="123e4567-e89b-12d3-a456-426614174000")):
    logger.info("get combination by id service called")
    combination = CommonService.get_record_by_id(repo=CommonDbOperations(Combinations), record_id=combination_id)
    logger.info("get combination by id service call ended")
    return combination
