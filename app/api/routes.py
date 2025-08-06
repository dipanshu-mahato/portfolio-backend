from fastapi import APIRouter
from app.api.v1 import company, application, application_link, application_stage

api_router = APIRouter(prefix='/v1', tags=['v1'])
api_router.include_router(company.router)
api_router.include_router(application.router)
api_router.include_router(application_link.router)
api_router.include_router(application_stage.router)
