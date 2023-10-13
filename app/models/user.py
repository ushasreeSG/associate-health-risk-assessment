from sqlalchemy import Column, String
from app.models.base_model import BaseModel, AuditCreateModel


class User(BaseModel, AuditCreateModel):
    __tablename__ = "users"
    __table_args__ = (
        {"schema": "application"},
    )
    email = Column(String(255), unique=True, nullable=False)
