from functools import wraps

from fastapi import status
from fastapi.logger import logger
from fastapi.responses import JSONResponse

from app.lib.custom_exceptions import (
    RecordNotFoundError, CreateRecordException, DeleteRecordException,
    DuplicateRecordError, UpdateRecordException, DBFetchFailureException,
    InvalidDataException, InvalidPasswordException
)

DEFAULT_ERROR_MESSAGE = """
An unexpected error has occurred while processing your request.
"""


def error_handler(func):
    @wraps(func)
    async def inner(*args, **kwargs):
        try:
            result = await func(*args, **kwargs)

        except (
                CreateRecordException, UpdateRecordException, DBFetchFailureException, DeleteRecordException
        ) as ex:
            return JSONResponse(content={"Error": str(ex)}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except (RecordNotFoundError, InvalidDataException) as ex:
            return JSONResponse(content={"Error": str(ex)}, status_code=status.HTTP_400_BAD_REQUEST)

        except DuplicateRecordError as ex:
            return JSONResponse(content={"Error": str(ex)}, status_code=status.HTTP_409_CONFLICT)

        except InvalidPasswordException as ex:
            return JSONResponse(content={"Error": str(ex)}, status_code=status.HTTP_401_UNAUTHORIZED)

        except Exception as ex:
            import traceback
            traceback.print_exc()
            logger.error(f"Error: {ex}")
            return JSONResponse(content={"Error": DEFAULT_ERROR_MESSAGE}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return result

    return inner

