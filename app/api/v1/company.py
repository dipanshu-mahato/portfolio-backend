from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.service.company import company
from app.dto.company import Company, CompanyCreate, CompanyUpdate
from app.api.deps import get_db_dep

router = APIRouter(prefix="/companies", tags=["companies"])

@router.post("", response_model=Company)
def create_company(*, db: Session = Depends(get_db_dep), obj_in: CompanyCreate):
    return company.create(db, obj_in=obj_in)

@router.get("", response_model=List[Company])
def read_companies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_dep)):
    return company.get_multi(db, skip=skip, limit=limit)

@router.get("/{id_}", response_model=Company)
def read_company(id_: UUID, db: Session = Depends(get_db_dep)):
    db_obj = company.get(db, id_)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Company not found")
    return db_obj

@router.put("/{id_}", response_model=Company)
def update_company(id_: UUID, *, db: Session = Depends(get_db_dep), obj_in: CompanyUpdate):
    db_obj = company.get(db, id_)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Company not found")
    return company.update(db, db_obj=db_obj, obj_in=obj_in)

@router.delete("/{id_}", response_model=Company)
def delete_company(id_: UUID, db: Session = Depends(get_db_dep)):
    return company.remove(db, id_=id_)
