from sqlalchemy import select

from app.db_layer.sql_context import SqlContext
from app.lib.singleton import Singleton


class CommonDbOperations:
	def __init__(self, model):
		self.model = model
		self.query = select(model)

	def get_by_id(self, record_id):
		result = self.query.where(
			self.model.id == str(record_id)
		)

		with SqlContext() as sql_context:
			result = sql_context.execute(result)

		return result.scalar()

	def get_by_col(self, col, value):
		query = self.query.where(
			getattr(self.model, col) == value
		)

		with SqlContext() as sql_context:
			result = sql_context.execute(query)

		return result.all()

	def search_by_col(self, col, value):
		result = self.query.where(
			getattr(self.model, col).ilike(value)
		)

		with SqlContext() as sql_context:
			result = sql_context.execute(result)

		return result.all()

	def get_all(self):
		with SqlContext() as sql_context:
			result = sql_context.execute(self.query)

		return result.all()

	@staticmethod
	def update_record(record, record_data, commit=True):
		record.set_attributes(record_data)

		if commit:
			with SqlContext() as sql_context:
				sql_context.session.add(record)

		return record

	def create_record(self, record_data, commit=True):
		record = self.model()
		record = self.update_record(record, record_data, commit)

		return record

	@staticmethod
	def delete_record(record, commit=True):
		if commit:
			with SqlContext() as sql_context:
				sql_context.session.delete(record)

		return record

	@staticmethod
	def activate_deactivate_record(record, is_active=True, commit=True):
		record.is_active = is_active

		if commit:
			with SqlContext() as sql_context:
				sql_context.session.add(record)

		return record
