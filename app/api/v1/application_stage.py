from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.service.application_stage import application_stage
from app.dto.application_stage import (
    ApplicationStage,
    ApplicationStageCreate,
    ApplicationStageUpdate,
)
from app.api.deps import get_db_dep

router = APIRouter(prefix="/application-stages", tags=["application_stages"])


@router.post("", response_model=ApplicationStage)
def create_application_stage(
    *, db: Session = Depends(get_db_dep), obj_in: ApplicationStageCreate
):
    return application_stage.create(db, obj_in=obj_in)


@router.get("", response_model=List[ApplicationStage])
def read_application_stages(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db_dep)
):
    return application_stage.get_multi(
        db, skip=skip, limit=limit
    )


@router.get("/{id_}", response_model=ApplicationStage)
def read_application_stage(id_: UUID, db: Session = Depends(get_db_dep)):
    db_obj = application_stage.get(db, id_)
    if not db_obj:
        raise HTTPException(status_code=404, detail="ApplicationStage not found")
    return db_obj


@router.put("/{id_}", response_model=ApplicationStage)
def update_application_stage(
    id_: UUID, *, db: Session = Depends(get_db_dep), obj_in: ApplicationStageUpdate
):
    db_obj = application_stage.get(db, id_)
    if not db_obj:
        raise HTTPException(status_code=404, detail="ApplicationStage not found")
    return application_stage.update(
        db, db_obj=db_obj, obj_in=obj_in
    )


@router.delete("/{id_}", response_model=ApplicationStage)
def delete_application_stage(id_: UUID, db: Session = Depends(get_db_dep)):
    return application_stage.remove(db, id_=id_)
