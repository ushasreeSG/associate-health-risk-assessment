from datetime import datetime, timedelta
from jose import jwt


SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def generate_token(data: dict, expires_minutes=ACCESS_TOKEN_EXPIRE_MINUTES):
	payload = data.copy()
	expire = datetime.utcnow() + timedelta(minutes=expires_minutes)
	payload.update({"exp": expire})
	encoded_jwt = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
	return encoded_jwt


def verify_token():
	pass
