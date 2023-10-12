import logging.config

import uvicorn
from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware

from app.api import API_ROUTERS
# from logging_config.config import LOGGING_CONF
from app.lib.cache import redis_cache

# logging.config.dictConfig(LOGGING_CONF)

app = FastAPI()

for router, kwargs in API_ROUTERS:
	app.include_router(router, **kwargs)


if __name__ == "__main__":
	uvicorn.run(app, port=5010, debug=True)