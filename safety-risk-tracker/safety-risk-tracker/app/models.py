from sqlalchemy import Column, Integer, String, Float, DateTime, Text, Boolean, Enum
from sqlalchemy.sql import func
from app.database import Base
import enum

class HazardSeverity(str, enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class HazardStatus(str, enum.Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    CLOSED = "closed"

class ComplianceStatus(str, enum.Enum):
    COMPLIANT = "compliant"
    NON_COMPLIANT = "non_compliant"
    PENDING_REVIEW = "pending_review"

class Hazard(Base):
    __tablename__ = "hazards"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text)
    location = Column(String(100), nullable=False)
    severity = Column(Enum(HazardSeverity), nullable=False)
    status = Column(Enum(HazardStatus), default=HazardStatus.OPEN)
    reported_by = Column(String(100), nullable=False)
    assigned_to = Column(String(100))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    resolution_notes = Column(Text)

class ComplianceCheck(Base):
    __tablename__ = "compliance_checks"
    
    id = Column(Integer, primary_key=True, index=True)
    check_name = Column(String(200), nullable=False)
    description = Column(Text)
    department = Column(String(100), nullable=False)
    status = Column(Enum(ComplianceStatus), nullable=False)
    checked_by = Column(String(100), nullable=False)
    check_date = Column(DateTime(timezone=True), server_default=func.now())
    due_date = Column(DateTime(timezone=True))
    notes = Column(Text)
    corrective_actions = Column(Text)

class SafetyKPI(Base):
    __tablename__ = "safety_kpis"
    
    id = Column(Integer, primary_key=True, index=True)
    kpi_name = Column(String(200), nullable=False)
    description = Column(Text)
    value = Column(Float, nullable=False)
    target = Column(Float, nullable=False)
    unit = Column(String(50), nullable=False)
    period_start = Column(DateTime(timezone=True), nullable=False)
    period_end = Column(DateTime(timezone=True), nullable=False)
    department = Column(String(100))
    recorded_at = Column(DateTime(timezone=True), server_default=func.now())
