from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from app.models import HazardSeverity, HazardStatus
from app import schemas
from app import crud
from app.database import get_db

router = APIRouter(prefix="/hazards", tags=["hazards"])

@router.post("/", response_model=schemas.Hazard)
def create_hazard(hazard: schemas.HazardCreate, db: Session = Depends(get_db)):
    return crud.create_hazard(db=db, hazard=hazard)

@router.get("/", response_model=List[schemas.Hazard])
def read_hazards(
    skip: int = 0, 
    limit: int = 100,
    severity: Optional[HazardSeverity] = None,
    status: Optional[HazardStatus] = None,
    db: Session = Depends(get_db)
):
    hazards = crud.get_hazards(
        db=db, 
        skip=skip, 
        limit=limit,
        severity=severity,
        status=status
    )
    return hazards

@router.get("/{hazard_id}", response_model=schemas.Hazard)
def read_hazard(hazard_id: int, db: Session = Depends(get_db)):
    db_hazard = crud.get_hazard(db=db, hazard_id=hazard_id)
    if db_hazard is None:
        raise HTTPException(status_code=404, detail="Hazard not found")
    return db_hazard

@router.put("/{hazard_id}", response_model=schemas.Hazard)
def update_hazard(hazard_id: int, hazard_update: schemas.HazardUpdate, db: Session = Depends(get_db)):
    db_hazard = crud.update_hazard(db=db, hazard_id=hazard_id, hazard_update=hazard_update)
    if db_hazard is None:
        raise HTTPException(status_code=404, detail="Hazard not found")
    return db_hazard

@router.delete("/{hazard_id}")
def delete_hazard(hazard_id: int, db: Session = Depends(get_db)):
    db_hazard = crud.delete_hazard(db=db, hazard_id=hazard_id)
    if db_hazard is None:
        raise HTTPException(status_code=404, detail="Hazard not found")
    return {"message": "Hazard deleted successfully"}
