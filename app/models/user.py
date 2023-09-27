from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.postgresql import UUID

from app.models.base_model import BaseModel, AuditUpdateModel, AuditCreateModel


class User(BaseModel, AuditCreateModel):
    __tablename__ = "users"
    __table_args__ = (
        {"schema": "application"},
    )
    email = Column("email", String(255), unique=True, nullable=False)
    password = Column("password", String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    phone = Column(String(64), nullable=True)
