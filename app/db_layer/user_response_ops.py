from app.lib.singleton import Singleton
from app.models import UserResponse
from app.db_layer.common_ops import CommonDbOperations


class UserResponseDBOperations(metaclass=Singleton):
    def __init__(self):
        self.model = UserResponse

    def create(self, register_dict, commit=True):
        ops = CommonDbOperations(self.model)
        user_response = ops.create_record(register_dict, commit)
        return user_response

    def get_all_user_response(self,user_id):
        ops = CommonDbOperations(self.model)
        result = ops.get_by_any_id(user_id)

        return result
