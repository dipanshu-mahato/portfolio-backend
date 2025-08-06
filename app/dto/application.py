from decimal import Decimal
from typing import Optional, Annotated
from uuid import UUID
from datetime import date, datetime
from pydantic import BaseModel, StringConstraints, PositiveInt, Field

class ApplicationBase(BaseModel):
    company_portal_job_id: Optional[Annotated[str, StringConstraints(max_length=10)]]
    company_id: Optional[UUID]
    role: Annotated[str, StringConstraints(max_length=20)]
    status: str
    rounds_count: Optional[PositiveInt]
    is_referred: Optional[bool] = False
    expected_ctc_lpa: Optional[Annotated[Decimal, Field( strict=True, ge=8, max_digits=5, decimal_places=2)]]
    applied_at: Optional[date]

class ApplicationCreate(ApplicationBase): pass

class ApplicationUpdate(ApplicationBase): pass

class Application(ApplicationBase):
    id: UUID
    updated_at: Optional[datetime]

    model_config = {"from_attributes": True}
