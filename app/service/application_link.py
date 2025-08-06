from app.model.application_link import ApplicationLink
from app.dto.application_link import ApplicationLinkCreate, ApplicationLinkUpdate
from app.service.base import Base

application_link = Base[ApplicationLink, ApplicationLinkCreate, ApplicationLinkUpdate](ApplicationLink)
