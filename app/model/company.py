import enum, uuid
from sqlalchemy import Column, String, Boolean, Integer, Enum
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base
from app.model.enums import pg_tier_enum


class Company(Base):
    __tablename__ = "company"
    __table_args__ = {"schema": "core"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(20), nullable=False)
    about = Column(String(100))
    tier = Column(pg_tier_enum, nullable=True)
    cool_off_period_days = Column(Integer)
    is_blocked = Column(Boolean, default=False)
