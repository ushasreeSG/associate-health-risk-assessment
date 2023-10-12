from app.api.user_response import user_response_router
from app.api.questions import question_router

API_ROUTERS = [
	(user_response_router, {"prefix": "/user_response"}),
	(question_router, {"prefix": "/question"}),
]