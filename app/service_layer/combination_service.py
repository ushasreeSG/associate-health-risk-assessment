from app.db_layer.sql_context import SqlContext
from app.lib.custom_exceptions import CreateRecordException
from app.lib.singleton import Singleton
from app.db_layer import CombinationDBOperations
from fastapi.logger import logger


class CombinationService(metaclass=Singleton):
    @staticmethod
    def create_combination(combination):
        logger.info("Calling the create combination service.")
        combination = combination.model_dump()

        combination = CombinationDBOperations().create_combination(register_dict=combination, commit=False)

        try:
            with SqlContext() as sql_context:
                sql_context.session.add(combination)

        except Exception as ex:
            logger.error(f"Error: {ex}")
            raise CreateRecordException(
                "An Error has occurred while creating the new combination"
                )

        logger.info("Combination created successfully")
        return {"status": "success", "message": "Combination created successfully"}
