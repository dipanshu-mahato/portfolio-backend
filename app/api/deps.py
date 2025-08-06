from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db

def get_db_dep(db: Session = Depends(get_db)):
    return db
