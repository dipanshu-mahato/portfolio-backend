from decimal import Decimal
from typing import Optional, Annotated
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, PositiveInt, StringConstraints, Field

class ApplicationStageBase(BaseModel):
    job_application_id: UUID
    stage_number: PositiveInt
    stage_title: Annotated[str, StringConstraints(max_length=20)]
    stage_details: Optional[str]
    duration_minutes: Annotated[Decimal, Field(ge=0, le=999)]
    feedback: str

class ApplicationStageCreate(ApplicationStageBase): pass
class ApplicationStageUpdate(ApplicationStageBase): pass

class ApplicationStage(ApplicationStageBase):
    id: UUID
    updated_at: Optional[datetime]
    
    model_config = {"from_attributes": True}
