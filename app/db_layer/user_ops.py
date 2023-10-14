from app.db_layer.sql_context import SqlContext
from app.lib.singleton import Singleton
from app.models import User
from app.db_layer.common_ops import CommonDbOperations


class UserDBOperations(metaclass=Singleton):
    def __init__(self):
        self.model = User

    def create(self, register_dict, commit=True):
        try:
            ops = CommonDbOperations(self.model)
            user = ops.create_record(register_dict, commit)
        except Exception as e:
            raise "An Exception occured while creating an user"
        with SqlContext() as sql_context:
            sql_context.session.add(user)
        return user
