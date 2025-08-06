from app.model.application_stage import ApplicationStage
from app.dto.application_stage import ApplicationStageCreate, ApplicationStageUpdate
from app.service.base import Base

application_stage = Base[ApplicationStage, ApplicationStageCreate, ApplicationStageUpdate](ApplicationStage)
