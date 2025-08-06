import enum, uuid
from sqlalchemy import Column, String, Numeric, Text, TIMESTAMP, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base

class EnumInterviewFeedback(str, enum.Enum):
    waiting = "waiting"
    strong_yes = "strong_yes"
    lean_yes = "lean_yes"
    neutral = "neutral"
    hold = "hold"
    lean_no = "lean_no"
    strong_no = "strong_no"
    eliminated = "eliminated"
    red_flag = "red_flag"

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
    feedback = Column(Enum(EnumInterviewFeedback), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True))
