from sqlalchemy import Column, String, Boolean, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID

from app.models.base_model import BaseModel, AuditUpdateModel, AuditCreateModel
from app.models.questions import Questions


class Combinations(BaseModel, AuditCreateModel,AuditUpdateModel):
    __tablename__ = "combinations"
    __table_args__ = (
        {"schemas": "application"},
    )
    combination_id = Column(Integer, nullable=False)
    question_id = Column(UUID(as_uuid=True), ForeignKey(Questions.id))
    combination_flag = Column(Boolean, nullable=False)

