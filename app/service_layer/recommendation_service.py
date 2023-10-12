from app.db_layer.sql_context import SqlContext
from app.lib.custom_exceptions import CreateRecordException
from app.lib.singleton import Singleton
from app.db_layer import RecommendationDBOperations
from fastapi.logger import logger


class RecommendationService(metaclass=Singleton):
    @staticmethod
    def create_recommendation(recommendation):
        logger.info("Calling the  service.")
        recommendation = recommendation.model_dump()

        recommendation = RecommendationDBOperations().create_recommendation(register_dict=recommendation, commit=False)

        try:
            with SqlContext() as sql_context:
                sql_context.session.add(recommendation)

        except Exception as ex:
            logger.error(f"Error: {ex}")
            raise CreateRecordException(
                "An Error has occurred while creating the new recommendation"
                )

        logger.info("Recommendation created successfully")
        return {"status": "success", "message": "recommendation created successfully"}
