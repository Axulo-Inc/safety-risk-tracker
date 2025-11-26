from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from app import schemas
from app import crud
from app.database import get_db

router = APIRouter(prefix="/kpis", tags=["kpis"])

@router.post("/", response_model=schemas.SafetyKPI)
def create_safety_kpi(kpi: schemas.SafetyKPICreate, db: Session = Depends(get_db)):
    return crud.create_safety_kpi(db=db, kpi=kpi)

@router.get("/", response_model=List[schemas.SafetyKPI])
def read_safety_kpis(
    skip: int = 0, 
    limit: int = 100,
    department: Optional[str] = None,
    db: Session = Depends(get_db)
):
    kpis = crud.get_safety_kpis(
        db=db, 
        skip=skip, 
        limit=limit,
        department=department
    )
    return kpis

@router.get("/{kpi_id}", response_model=schemas.SafetyKPI)
def read_safety_kpi(kpi_id: int, db: Session = Depends(get_db)):
    db_kpi = crud.get_safety_kpi(db=db, kpi_id=kpi_id)
    if db_kpi is None:
        raise HTTPException(status_code=404, detail="Safety KPI not found")
    return db_kpi

@router.put("/{kpi_id}", response_model=schemas.SafetyKPI)
def update_safety_kpi(kpi_id: int, kpi_update: schemas.SafetyKPIUpdate, db: Session = Depends(get_db)):
    db_kpi = crud.update_safety_kpi(db=db, kpi_id=kpi_id, kpi_update=kpi_update)
    if db_kpi is None:
        raise HTTPException(status_code=404, detail="Safety KPI not found")
    return db_kpi
