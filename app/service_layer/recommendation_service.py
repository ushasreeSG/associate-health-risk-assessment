from app.db_layer.sql_context import SqlContext
from app.lib.custom_exceptions import CreateRecordException, DBFetchFailureException
from app.lib.singleton import Singleton
from app.db_layer import RecommendationDBOperations, UserResponseDBOperations, CommonDbOperations
from fastapi.logger import logger

from app.models import Combinations, Recommendation
from app.service_layer import CommonService


class RecommendationService(metaclass=Singleton):
    @staticmethod
    def create_recommendation(request):
        logger.info("Calling the  service.")
        # recommendation = recommendation.model_dump()

        recommendation = RecommendationDBOperations().create_recommendation(register_dict=request, commit=False)

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

    @staticmethod
    def get_by_user_id(user_id):
        user_response = UserResponseDBOperations().get_all_user_response(user_id)
        print(user_response)
        combinations_details = CommonService.get_all(repo=CommonDbOperations(Combinations))
        objects_by_combination_id = {}
        for obj_tuple in combinations_details:
            obj = obj_tuple[0]  # Extracting the object from the tuple
            combination_id = obj.combination_id  # Assuming there's an attribute named 'combination_id' in the object
            if combination_id not in objects_by_combination_id:
                objects_by_combination_id[combination_id] = []
            objects_by_combination_id[combination_id].append(obj)
        records = []
        print(objects_by_combination_id)
        try:
            for combination_id, objects in objects_by_combination_id.items():
                count = 0
                print(objects)
                for obj in objects:
                    for each_detail in user_response:
                        user_obj = each_detail[0]
                        print(user_obj)
                        if user_obj.question_id == obj.question_id and obj.combination_flag == user_obj.response_flag:
                            count = count + 1
                print(count)
                print(len(objects))
                if count == len(objects):
                    record = RecommendationDBOperations().get_record_by_id(combination_id)
                    records.append(record)
        except Exception as ex:
            raise DBFetchFailureException("An Error occurred while fetching the details")
        return record
