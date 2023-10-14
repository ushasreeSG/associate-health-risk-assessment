from app.lib.singleton import Singleton
from app.lib.custom_exceptions import DBFetchFailureException, RecordNotFoundError


class CommonService(metaclass=Singleton):
    @staticmethod
    def get_record_by_id(repo, record_id):
        model_name = repo.model.__name__

        try:
            record = repo.get_by_id(record_id)
        except Exception as ex:
            error_msg = f"Unable to fetch {model_name} details. {model_name} ID - {record_id}"
            raise DBFetchFailureException(error_msg)

        if not record:
            error_msg = f"No {model_name} exists with ID - {record_id}"
            raise RecordNotFoundError(error_msg)

        return record

    @staticmethod
    def get_all(repo):
        model_name = repo.model.__name__

        try:
            record = repo.get_all_rows()
        except Exception as ex:
            error_msg = f"Unable to fetch {model_name} details."
            raise DBFetchFailureException(error_msg)

        if not record:
            error_msg = f"No {model_name} exists with records "
            raise RecordNotFoundError(error_msg)

        return record
