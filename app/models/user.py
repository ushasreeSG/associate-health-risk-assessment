from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.postgresql import UUID

from app.models.base_model import BaseModel, AuditCreateModel


class User(BaseModel, AuditCreateModel):
    __tablename__ = "users"
    __table_args__ = (
        {"schema": "application"},
    )
    email = Column(String(255), unique=True, nullable=False)
