class DuplicateRecordError(Exception):
	def __init__(self, message):
		super().__init__(message)


class RecordNotFoundError(Exception):
	def __init__(self, message):
		super().__init__(message)


class CreateRecordException(Exception):
	def __init__(self, message):
		super().__init__(message)


class UpdateRecordException(Exception):
	def __init__(self, message):
		super().__init__(message)


class DeleteRecordException(Exception):
	def __init__(self, message):
		super().__init__(message)


class DBFetchFailureException(Exception):
	def __init__(self, message):
		super().__init__(message)


class InvalidDataException(Exception):
	def __init__(self, message):
		super().__init__(message)


class InvalidPasswordException(Exception):
	def __init__(self, message):
		super().__init__(message)
