import requests
import json
from datetime import datetime, timedelta

BASE_URL = "http://localhost:8000"

def create_sample_data():
    print("Creating sample data...")
    
    # Create a hazard
    hazard_data = {
        "title": "Slippery floor in main hallway",
        "description": "Water leakage causing slippery conditions near the coffee machine",
        "location": "Main hallway - 2nd floor",
        "severity": "high",
        "reported_by": "John Smith"
    }
    
    response = requests.post(f"{BASE_URL}/hazards/", json=hazard_data)
    print(f"✓ Created hazard: {response.status_code}")
    
    # Create a compliance check
    compliance_data = {
        "check_name": "Fire Extinguisher Monthly Inspection",
        "description": "Monthly inspection of all fire extinguishers in building A",
        "department": "Facilities",
        "status": "compliant",
        "checked_by": "Mike Wilson",
        "notes": "All extinguishers charged and accessible, expiration dates checked"
    }
    
    response = requests.post(f"{BASE_URL}/compliance/checks/", json=compliance_data)
    print(f"✓ Created compliance check: {response.status_code}")
    
    # Create a safety KPI
    kpi_data = {
        "kpi_name": "Lost Time Injury Frequency Rate",
        "description": "Number of lost time injuries per million hours worked",
        "value": 2.1,
        "target": 1.8,
        "unit": "per million hours",
        "period_start": "2024-01-01T00:00:00",
        "period_end": "2024-01-31T23:59:59",
        "department": "Manufacturing"
    }
    
    response = requests.post(f"{BASE_URL}/kpis/", json=kpi_data)
    print(f"✓ Created safety KPI: {response.status_code}")
    
    print("Sample data created successfully!")

def test_endpoints():
    print("\nTesting endpoints...")
    
    # Test getting all hazards
    response = requests.get(f"{BASE_URL}/hazards/")
    print(f"✓ Hazards endpoint: {response.status_code} - {len(response.json())} hazards")
    
    # Test getting all compliance checks
    response = requests.get(f"{BASE_URL}/compliance/checks/")
    print(f"✓ Compliance checks endpoint: {response.status_code} - {len(response.json())} checks")
    
    # Test getting all KPIs
    response = requests.get(f"{BASE_URL}/kpis/")
    print(f"✓ KPIs endpoint: {response.status_code} - {len(response.json())} KPIs")
    
    # Test dashboard
    response = requests.get(f"{BASE_URL}/dashboard")
    dashboard_data = response.json()
    print(f"✓ Dashboard endpoint: {response.status_code}")
    total_hazards = dashboard_data.get("total_hazards", 0)
    compliance_rate = dashboard_data.get("compliance_rate", 0)
    print(f"  - Total hazards: {total_hazards}")
    print(f"  - Compliance rate: {compliance_rate}%")

if __name__ == "__main__":
    create_sample_data()
    test_endpoints()
