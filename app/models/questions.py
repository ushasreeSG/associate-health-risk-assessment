from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.postgresql import UUID

from app.models.base_model import BaseModel, AuditUpdateModel, AuditCreateModel
from enum import Enum


class CategoryEnum(str, Enum):
    I = "Nutrition"
    II = "Fitness"
    III = "Sleep"
    IV = "Stress"
    V = "Safety"


class Questions(BaseModel, AuditCreateModel, AuditUpdateModel):
    __tablename__ = "questions"
    __table_args__ = (
        {"schema": "application"},
    )
    question = Column("question", String(512), unique=True, nullable=False)
    category: CategoryEnum



