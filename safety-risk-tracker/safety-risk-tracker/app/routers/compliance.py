from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from app.models import ComplianceStatus
from app import schemas
from app import crud
from app.database import get_db

router = APIRouter(prefix="/compliance", tags=["compliance"])

@router.post("/checks/", response_model=schemas.ComplianceCheck)
def create_compliance_check(check: schemas.ComplianceCheckCreate, db: Session = Depends(get_db)):
    return crud.create_compliance_check(db=db, check=check)

@router.get("/checks/", response_model=List[schemas.ComplianceCheck])
def read_compliance_checks(
    skip: int = 0, 
    limit: int = 100,
    department: Optional[str] = None,
    status: Optional[ComplianceStatus] = None,
    db: Session = Depends(get_db)
):
    checks = crud.get_compliance_checks(
        db=db, 
        skip=skip, 
        limit=limit,
        department=department,
        status=status
    )
    return checks

@router.get("/checks/{check_id}", response_model=schemas.ComplianceCheck)
def read_compliance_check(check_id: int, db: Session = Depends(get_db)):
    db_check = crud.get_compliance_check(db=db, check_id=check_id)
    if db_check is None:
        raise HTTPException(status_code=404, detail="Compliance check not found")
    return db_check

@router.put("/checks/{check_id}", response_model=schemas.ComplianceCheck)
def update_compliance_check(check_id: int, check_update: schemas.ComplianceCheckUpdate, db: Session = Depends(get_db)):
    db_check = crud.update_compliance_check(db=db, check_id=check_id, check_update=check_update)
    if db_check is None:
        raise HTTPException(status_code=404, detail="Compliance check not found")
    return db_check
