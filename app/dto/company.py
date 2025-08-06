from typing import Optional, Annotated
from uuid import UUID
from pydantic import BaseModel, StringConstraints, PositiveInt
from app.model.enums import EnumCompanyTier

class CompanyBase(BaseModel):
    name: Annotated[str, StringConstraints(max_length=20)]
    about: Optional[Annotated[str, StringConstraints(max_length=100)]] = None
    tier: EnumCompanyTier
    cool_off_period_days: Optional[PositiveInt] = None
    is_blocked: bool = False


class CompanyCreate(CompanyBase):
    pass


class CompanyUpdate(CompanyBase):
    pass


class Company(CompanyBase):
    id: UUID
    
    model_config = {
        "from_attributes": True, # replaces orm_mode
    }
