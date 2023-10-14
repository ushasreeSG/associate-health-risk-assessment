from sqlalchemy import Column, String, Integer

from app.models.base_model import BaseModel, AuditUpdateModel, AuditCreateModel


class Recommendation(BaseModel, AuditCreateModel, AuditUpdateModel):
    __tablename__ = "recommendation"
    __table_args__ = (
        {"schema": "application"},
    )
    consequence = Column(String(512), unique=True, nullable=False)
    recommendation = Column(String(512), unique=True, nullable=False)
    recommendation_id = Column(Integer, unique=True, nullable=False)
