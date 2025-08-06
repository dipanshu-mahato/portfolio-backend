import uuid
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base

class ApplicationLink(Base):
    __tablename__ = "application_link"
    __table_args__ = {"schema": "core"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    job_application_id = Column(UUID(as_uuid=True),
                                ForeignKey("core.application.id", ondelete="CASCADE"))
    link = Column(String(100))
    text = Column(String(20))
