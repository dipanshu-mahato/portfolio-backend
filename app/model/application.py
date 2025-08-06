import enum, uuid
from sqlalchemy import Column, String, Boolean, Numeric, Date, TIMESTAMP, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base

class EnumApplicationStatus(str, enum.Enum):
    applied = "applied"
    shortlisted = "shortlisted"
    assessment = "assessment"
    phone_screen = "phone_screen"
    interview = "interview"
    hr = "hr"
    offered = "offered"
    accepted = "accepted"
    rejected = "rejected"
    ghosted = "ghosted"

class Application(Base):
    __tablename__ = "application"
    __table_args__ = {"schema": "core"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    company_portal_job_id = Column(String(10))
    company_id = Column(UUID(as_uuid=True),
                        ForeignKey("core.company.id", ondelete="SET NULL"))
    role = Column(String(20), nullable=False)
    status = Column(Enum(EnumApplicationStatus), nullable=False)
    rounds_count = Column(Numeric(2, 0))
    is_referred = Column(Boolean, default=False)
    expected_ctc_lpa = Column(Numeric(5, 2))
    applied_at = Column(Date, nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True))
