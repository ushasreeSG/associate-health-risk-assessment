from sqlalchemy import select

from app.db_layer.sql_context import SqlContext
from app.lib.singleton import Singleton
from app.models import Questions
from app.db_layer.common_ops import CommonDbOperations


class QuestionDBOperations(metaclass=Singleton):
	def __init__(self):
		self.model = Questions

	def create_question(self, register_dict, commit=True):
		ops = CommonDbOperations(self.model)
		user = ops.create_record(register_dict, commit)
		return user

	def get_all_questions(self):
		ops = CommonDbOperations(self.model)
		result = ops.get_all()
		# return result[0] if result else None
		return result
