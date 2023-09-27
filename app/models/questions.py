from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.postgresql import UUID

from app.models.base_model import BaseModel, AuditUpdateModel, AuditCreateModel
from enum import Enum


class Questions(BaseModel, AuditCreateModel, AuditUpdateModel):
    __tablename__ = "questions"
    __table_args__ = (
        {"schema": "application"},
    )
    question = Column("question", String(512), unique=True, nullable=False)
    category = Column(String(20), nullable=False)




