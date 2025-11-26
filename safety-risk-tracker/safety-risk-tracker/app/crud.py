from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models import Hazard, ComplianceCheck, SafetyKPI, HazardSeverity, HazardStatus, ComplianceStatus
from app import schemas
from typing import List, Optional

# Hazard CRUD operations
def get_hazard(db: Session, hazard_id: int):
    return db.query(Hazard).filter(Hazard.id == hazard_id).first()

def get_hazards(db: Session, skip: int = 0, limit: int = 100, 
                severity: Optional[HazardSeverity] = None,
                status: Optional[HazardStatus] = None):
    query = db.query(Hazard)
    
    if severity:
        query = query.filter(Hazard.severity == severity)
    if status:
        query = query.filter(Hazard.status == status)
    
    return query.offset(skip).limit(limit).all()

def create_hazard(db: Session, hazard: schemas.HazardCreate):
    db_hazard = Hazard(**hazard.model_dump())
    db.add(db_hazard)
    db.commit()
    db.refresh(db_hazard)
    return db_hazard

def update_hazard(db: Session, hazard_id: int, hazard_update: schemas.HazardUpdate):
    db_hazard = db.query(Hazard).filter(Hazard.id == hazard_id).first()
    if db_hazard:
        update_data = hazard_update.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_hazard, field, value)
        db.commit()
        db.refresh(db_hazard)
    return db_hazard

def delete_hazard(db: Session, hazard_id: int):
    db_hazard = db.query(Hazard).filter(Hazard.id == hazard_id).first()
    if db_hazard:
        db.delete(db_hazard)
        db.commit()
    return db_hazard

# Compliance Check CRUD operations
def get_compliance_check(db: Session, check_id: int):
    return db.query(ComplianceCheck).filter(ComplianceCheck.id == check_id).first()

def get_compliance_checks(db: Session, skip: int = 0, limit: int = 100,
                         department: Optional[str] = None,
                         status: Optional[ComplianceStatus] = None):
    query = db.query(ComplianceCheck)
    
    if department:
        query = query.filter(ComplianceCheck.department == department)
    if status:
        query = query.filter(ComplianceCheck.status == status)
    
    return query.offset(skip).limit(limit).all()

def create_compliance_check(db: Session, check: schemas.ComplianceCheckCreate):
    db_check = ComplianceCheck(**check.model_dump())
    db.add(db_check)
    db.commit()
    db.refresh(db_check)
    return db_check

def update_compliance_check(db: Session, check_id: int, check_update: schemas.ComplianceCheckUpdate):
    db_check = db.query(ComplianceCheck).filter(ComplianceCheck.id == check_id).first()
    if db_check:
        update_data = check_update.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_check, field, value)
        db.commit()
        db.refresh(db_check)
    return db_check

# Safety KPI CRUD operations
def get_safety_kpi(db: Session, kpi_id: int):
    return db.query(SafetyKPI).filter(SafetyKPI.id == kpi_id).first()

def get_safety_kpis(db: Session, skip: int = 0, limit: int = 100,
                   department: Optional[str] = None):
    query = db.query(SafetyKPI)
    
    if department:
        query = query.filter(SafetyKPI.department == department)
    
    return query.offset(skip).limit(limit).all()

def create_safety_kpi(db: Session, kpi: schemas.SafetyKPICreate):
    db_kpi = SafetyKPI(**kpi.model_dump())
    db.add(db_kpi)
    db.commit()
    db.refresh(db_kpi)
    return db_kpi

def update_safety_kpi(db: Session, kpi_id: int, kpi_update: schemas.SafetyKPIUpdate):
    db_kpi = db.query(SafetyKPI).filter(SafetyKPI.id == kpi_id).first()
    if db_kpi:
        update_data = kpi_update.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_kpi, field, value)
        db.commit()
        db.refresh(db_kpi)
    return db_kpi

# Dashboard and Analytics
def get_dashboard_stats(db: Session):
    try:
        total_hazards = db.query(Hazard).count()
        open_hazards = db.query(Hazard).filter(
            Hazard.status.in_([HazardStatus.OPEN, HazardStatus.IN_PROGRESS])
        ).count()
        critical_hazards = db.query(Hazard).filter(Hazard.severity == HazardSeverity.CRITICAL).count()
        
        total_checks = db.query(ComplianceCheck).count()
        compliant_checks = db.query(ComplianceCheck).filter(
            ComplianceCheck.status == ComplianceStatus.COMPLIANT
        ).count()
        compliance_rate = (compliant_checks / total_checks * 100) if total_checks > 0 else 0
        
        total_kpis = db.query(SafetyKPI).count()
        
        return {
            "total_hazards": total_hazards,
            "open_hazards": open_hazards,
            "critical_hazards": critical_hazards,
            "compliance_rate": round(compliance_rate, 2),
            "total_kpis": total_kpis,
            "hazards_by_severity": {},
            "compliance_by_department": {}
        }
    except Exception as e:
        return {
            "total_hazards": 0,
            "open_hazards": 0,
            "critical_hazards": 0,
            "compliance_rate": 0,
            "total_kpis": 0,
            "hazards_by_severity": {},
            "compliance_by_department": {}
        }
