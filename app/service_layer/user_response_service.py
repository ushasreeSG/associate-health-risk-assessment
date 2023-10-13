from app.db_layer.sql_context import SqlContext
from app.lib.custom_exceptions import DuplicateRecordError, CreateRecordException, DBFetchFailureException
from app.lib.custom_exceptions import RecordNotFoundError
from app.lib.singleton import Singleton
from app.db_layer import UserResponseDBOperations, CommonDbOperations
from fastapi.logger import logger

from app.models import Combinations
from app.service_layer import CommonService


class UserResponseService(metaclass=Singleton):
    @staticmethod
    def create(request):
        logger.info("Calling the create_question service.")

        for response_request in request:
            user_response = UserResponseDBOperations().create(
                register_dict=response_request, commit=False
                )
            try:
                with SqlContext() as sql_context:
                    sql_context.session.add(user_response)

            except Exception as ex:
                logger.error(f"Error: {ex}")
                raise CreateRecordException(
                    "An Error has occurred while creating the new question"
                    )
        logger.info("Records  created successfully")
        return {"status": "success", "message": "User Response created successfully"}

    # @staticmethod
    # def get_all():
    #     try:
    #         user_details = QuestionDBOperations().get_all_questions()
    #     except Exception as ex:
    #         logger.error(f"Error: {ex}")
    #         raise DBFetchFailureException(
    #             f"An Error has occurred while fetching the questions"
    #             )
    #
    #     if not user_details:
    #         logger.info(f"No user found with email id - {email}")
    #         raise RecordNotFoundError(
    #             f"No user found with email id - {email}"
    #             )
    #
    #     return user_detailss
