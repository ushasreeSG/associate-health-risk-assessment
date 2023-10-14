from app.api.combinations import combination_router
from app.api.recommendations import recommendation_router
from app.api.user import user_router
from app.api.user_response import user_response_router
from app.api.questions import question_router

API_ROUTERS = [
	(user_router, {"prefix": "/user"}),
	(user_response_router, {"prefix": "/user_response"}),
	(question_router, {"prefix": "/question"}),
	(combination_router, {"prefix": "/combination"}),
	(recommendation_router, {"prefix": "/recommendation"})
	]
