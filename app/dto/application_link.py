from typing import Optional, Annotated
from uuid import UUID
from pydantic import BaseModel, StringConstraints


class ApplicationLinkBase(BaseModel):
    job_application_id: UUID
    link: Optional[Annotated[str, StringConstraints(max_length=100)]]
    text: Optional[Annotated[str, StringConstraints(max_length=20)]]


class ApplicationLinkCreate(ApplicationLinkBase): pass


class ApplicationLinkUpdate(ApplicationLinkBase): pass


class ApplicationLink(ApplicationLinkBase):
    id: UUID

    model_config = {"from_attributes": True}
