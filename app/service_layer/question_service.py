from app.db_layer.sql_context import SqlContext
from app.lib.custom_exceptions import CreateRecordException
from app.lib.singleton import Singleton
from app.db_layer import QuestionDBOperations
from fastapi.logger import logger


class QuestionService(metaclass=Singleton):
    @staticmethod
    def create_question(question_request):
        logger.info("Calling the create_question service.")

        question = QuestionDBOperations().create_question(
            register_dict=question_request, commit=False
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
