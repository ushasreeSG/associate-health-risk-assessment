from sqlalchemy import select

from app.db_layer.sql_context import SqlContext
from app.lib.singleton import Singleton
from app.models import Recommendation
from app.db_layer.common_ops import CommonDbOperations


class RecommendationDBOperations(metaclass=Singleton):
    def __init__(self):
        self.model = Recommendation
        self.query = select(self.model)

    def create_recommendation(self, register_dict, commit=True):
        ops = CommonDbOperations(self.model)
        user = ops.create_record(register_dict, commit)
        return user
    def get_record_by_id(self, recommendation_id):
            result = self.query.where(
                self.model.recommendation_id == str(recommendation_id)
            )

            with SqlContext() as sql_context:
                result = sql_context.execute(result)

            return result.scalar()




