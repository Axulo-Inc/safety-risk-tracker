from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional
from app.models import HazardSeverity, HazardStatus, ComplianceStatus

class HazardBase(BaseModel):
    title: str
    description: Optional[str] = None
    location: str
    severity: HazardSeverity
    reported_by: str
    assigned_to: Optional[str] = None

class HazardCreate(HazardBase):
    pass

class HazardUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    severity: Optional[HazardSeverity] = None
    status: Optional[HazardStatus] = None
    assigned_to: Optional[str] = None
    resolution_notes: Optional[str] = None

class Hazard(HazardBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    status: HazardStatus
    created_at: datetime
    updated_at: Optional[datetime] = None
    resolution_notes: Optional[str] = None

class ComplianceCheckBase(BaseModel):
    check_name: str
    description: Optional[str] = None
    department: str
    status: ComplianceStatus
    checked_by: str
    due_date: Optional[datetime] = None
    notes: Optional[str] = None
    corrective_actions: Optional[str] = None

class ComplianceCheckCreate(ComplianceCheckBase):
    pass

class ComplianceCheckUpdate(BaseModel):
    check_name: Optional[str] = None
    description: Optional[str] = None
    department: Optional[str] = None
    status: Optional[ComplianceStatus] = None
    notes: Optional[str] = None
    corrective_actions: Optional[str] = None

class ComplianceCheck(ComplianceCheckBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    check_date: datetime

class SafetyKPIBase(BaseModel):
    kpi_name: str
    description: Optional[str] = None
    value: float
    target: float
    unit: str
    period_start: datetime
    period_end: datetime
    department: Optional[str] = None

class SafetyKPICreate(SafetyKPIBase):
    pass

class SafetyKPIUpdate(BaseModel):
    kpi_name: Optional[str] = None
    description: Optional[str] = None
    value: Optional[float] = None
    target: Optional[float] = None
    unit: Optional[str] = None
    department: Optional[str] = None

class SafetyKPI(SafetyKPIBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    recorded_at: datetime

class DashboardStats(BaseModel):
    total_hazards: int
    open_hazards: int
    critical_hazards: int
    compliance_rate: float
    total_kpis: int
    hazards_by_severity: dict
    compliance_by_department: dict
