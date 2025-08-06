from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.service.application_link import application_link
from app.dto.application_link import (
    ApplicationLink,
    ApplicationLinkCreate,
    ApplicationLinkUpdate,
)
from app.api.deps import get_db_dep

router = APIRouter(prefix="/application-links", tags=["application_links"])


@router.post("", response_model=ApplicationLink)
def create_application_link(
    *, db: Session = Depends(get_db_dep), obj_in: ApplicationLinkCreate
):
    return application_link.create(db, obj_in=obj_in)


@router.get("", response_model=List[ApplicationLink])
def read_application_links(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db_dep)
):
    return application_link.get_multi(
        db, skip=skip, limit=limit
    )


@router.get("/{id_}", response_model=ApplicationLink)
def read_application_link(id_: UUID, db: Session = Depends(get_db_dep)):
    db_obj = application_link.get(db, id_)
    if not db_obj:
        raise HTTPException(status_code=404, detail="ApplicationLink not found")
    return db_obj


@router.put("/{id_}", response_model=ApplicationLink)
def update_application_link(
    id_: UUID, *, db: Session = Depends(get_db_dep), obj_in: ApplicationLinkUpdate
):
    db_obj = application_link.get(db, id_)
    if not db_obj:
        raise HTTPException(status_code=404, detail="ApplicationLink not found")
    return application_link.update(
        db, db_obj=db_obj, obj_in=obj_in
    )


@router.delete("/{id_}", response_model=ApplicationLink)
def delete_application_link(id_: UUID, db: Session = Depends(get_db_dep)):
    return application_link.remove(db, id_=id_)
