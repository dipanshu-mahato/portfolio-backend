from app.model.application import Application
from app.dto.application import ApplicationCreate, ApplicationUpdate
from app.service.base import Base

application = Base[Application, ApplicationCreate, ApplicationUpdate](Application)
