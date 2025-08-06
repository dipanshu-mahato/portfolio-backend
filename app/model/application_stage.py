import enum, uuid
from sqlalchemy import Column, String, Numeric, Text, TIMESTAMP, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base
from app.model.enums import pg_feedback_enum


class ApplicationStage(Base):
    __tablename__ = "application_stage"
    __table_args__ = {"schema": "core"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    job_application_id = Column(UUID(as_uuid=True),
                                ForeignKey("core.application.id", ondelete="RESTRICT"))
    stage_number = Column(Numeric(2, 0), nullable=False)
    stage_title = Column(String(20), nullable=False)
    stage_details = Column(Text)
    duration_minutes = Column(Numeric(3, 0), nullable=False)
    feedback = Column(pg_feedback_enum, nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True))
