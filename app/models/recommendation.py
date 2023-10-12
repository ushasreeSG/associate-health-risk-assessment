from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.models.base_model import BaseModel, AuditUpdateModel, AuditCreateModel
from enum import Enum
from app.models.combinations import Combinations


# class CategoryEnum(str, Enum):
#     I = "Nutrition"
#     II = "Fitness"
#     III = "Sleep"
#     IV = "Stress"
#     V = "Safety"


class Recommendation(BaseModel, AuditCreateModel, AuditUpdateModel):
    __tablename__ = "recommendation"
    __table_args__ = (
        {"schemas": "application"},
    )
    consequence = Column(String(512), unique=True, nullable=False)
    recommendation = Column(String(512), unique=True, nullable=False)
    combination_id = Column(UUID(as_uuid=True), ForeignKey(Combinations.id))
