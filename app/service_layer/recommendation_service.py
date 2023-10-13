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
        user_response = UserResponseDBOperations.get_all_user_response(user_id)
        combinations_details = CommonService.get_all(repo=CommonDbOperations(Combinations))
        objects_by_combination_id = {}
        for obj_tuple in combinations_details:
            obj = obj_tuple[0]  # Extracting the object from the tuple
            combination_id = obj.combination_id  # Assuming there's an attribute named 'combination_id' in the object
            if combination_id not in objects_by_combination_id:
                objects_by_combination_id[combination_id] = []
            objects_by_combination_id[combination_id].append(obj)
        try:
            store = []
            for combination_id, objects in objects_by_combination_id.items():
                count = 0
                for each in objects:
                    print(each)
                    for each_detail in user_response:
                        print(each_detail)
                        if each_detail[0].question_id == each[0].question_id and each[0].combination_flag == each[
                            0].response_flag:
                            count = count + 1
                        else:
                            break
                print(count)
                if count == len(objects):
                    CommonService.get_record_by_id(repo=CommonDbOperations(Recommendation), record_id=combination_id)
        except Exception as ex:
            raise DBFetchFailureException("An Error occurred while fetching the details")

