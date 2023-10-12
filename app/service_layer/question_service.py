from app.db_layer.sql_context import SqlContext
from app.lib.custom_exceptions import DuplicateRecordError, CreateRecordException, DBFetchFailureException
from app.lib.custom_exceptions import RecordNotFoundError
from app.lib.singleton import Singleton
from app.db_layer import QuestionDBOperations
from app.db_layer.common_ops import CommonDbOperations
from app.service_layer.common_service import CommonService
from fastapi.logger import logger


class QuestionService(metaclass=Singleton):
    @staticmethod
    def create_question(question_request):
        logger.info("Calling the create_question service.")
        question = question_request.model_dump()

        question = QuestionDBOperations().create_question(
            register_dict=question, commit=False
            )

        try:
            with SqlContext() as sql_context:
                sql_context.session.add(question)

        except Exception as ex:
            logger.error(f"Error: {ex}")
            raise CreateRecordException(
                "An Error has occurred while creating the new question"
                )

        logger.info("Question created successfully")
        return {"status": "success", "message": "Question created successfully"}

    @staticmethod
    def get_question_by_id(email):
        try:
            user_details = UserDetailsViewOperations().get_user_details_by_email_id(email=email)
        except Exception as ex:
            logger.error(f"Error: {ex}")
            raise DBFetchFailureException(
                f"An Error has occurred while fetching the user details with email id - {email}"
                )

        if not user_details:
            logger.info(f"No user found with email id - {email}")
            raise RecordNotFoundError(
                f"No user found with email id - {email}"
                )

        return user_details