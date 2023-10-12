from sqlalchemy import select

from app.db_layer.sql_context import SqlContext
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

    def get_all_user_response(self):
        ops = CommonDbOperations(self.model)
        result = ops.get_all()

        return result


class UserProfileOperations(metaclass=Singleton):
    def __init__(self):
        self.model = UserProfile

    def create_user_profile(self, profile_dict, commit=True):
        profile = self.model()
        profile.set_attributes(profile_dict)

        if commit:
            with SqlContext() as sql_context:
                sql_context.session.add(profile)

        return profile


class UserDetailsViewOperations(metaclass=Singleton):
    def __init__(self):
        self.model = UserDetailView
        self.query = select(UserDetailView)

    def get_user_details_by_user_id(self, user_id):
        result = self.query.where(
            self.model.id == str(user_id)
        )

        with SqlContext() as sql_context:
            result = sql_context.execute(result)

        return result.scalar()

    def get_user_details_by_email_id(self, email):
        result = self.query.where(
            self.model.email == str(email)
        )

        with SqlContext() as sql_context:
            result = sql_context.execute(result)

        return result.scalar()

# TODO: Add type annotations for all the methods in all files.
# TODO: async/await
