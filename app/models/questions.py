from sqlalchemy import Column, String, Boolean, Integer

from app.models.base_model import BaseModel, AuditUpdateModel, AuditCreateModel


class Questions(BaseModel, AuditCreateModel, AuditUpdateModel):
    __tablename__ = "questions"
    __table_args__ = (
        {"schema": "application"},
    )
    # __table_args__ = {'extend_existing': True}
    question = Column(String(512), unique=True, nullable=False)
    category_id = Column(Integer, nullable=False)


