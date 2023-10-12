from app.lib.singleton import Singleton
from app.models import Recommendation
from app.db_layer.common_ops import CommonDbOperations


class RecommendationDBOperations(metaclass=Singleton):
    def __init__(self):
        self.model = Recommendation

    def create_recommendation(self, register_dict, commit=True):
        ops = CommonDbOperations(self.model)
        user = ops.create_record(register_dict, commit)
        return user

