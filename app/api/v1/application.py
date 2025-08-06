from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.service.application import application
from app.dto.application import Application, ApplicationCreate, ApplicationUpdate
from app.api.deps import get_db_dep

router = APIRouter(prefix="/applications", tags=["applications"])

@router.post("", response_model=Application)
def create(obj_in: ApplicationCreate, db: Session = Depends(get_db_dep)):
    return application.create(db, obj_in=obj_in)

@router.get("", response_model=List[Application])
def read_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_dep)):
    return application.get_multi(db, skip=skip, limit=limit)

@router.get("/{id_}", response_model=Application)
def read_one(id_: UUID, db: Session = Depends(get_db_dep)):
    obj = application.get(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Application not found")
    return obj

@router.put("/{id_}", response_model=Application)
def update(id_: UUID, obj_in: ApplicationUpdate, db: Session = Depends(get_db_dep)):
    db_obj = application.get(db, id_)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Application not found")
    return application.update(db, db_obj=db_obj, obj_in=obj_in)

@router.delete("/{id_}", response_model=Application)
def delete(id_: UUID, db: Session = Depends(get_db_dep)):
    return application.remove(db, id_=id_)
