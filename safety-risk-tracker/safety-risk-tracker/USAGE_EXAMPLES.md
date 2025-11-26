# Safety & Risk Tracker - API Usage Examples (Fish Shell)

## Create a Hazard
curl -X POST "http://localhost:8000/hazards/" \
  -H "Content-Type: application/json" \
  -d '{"title": "Exposed electrical wires", "location": "Server room", "severity": "critical", "reported_by": "Sarah Johnson"}'

## Create a Compliance Check
curl -X POST "http://localhost:8000/compliance/checks/" \
  -H "Content-Type: application/json" \
  -d '{"check_name": "Emergency Exit Inspection", "department": "Safety", "status": "compliant", "checked_by": "Mike Wilson"}'

## Create a Safety KPI
curl -X POST "http://localhost:8000/kpis/" \
  -H "Content-Type: application/json" \
  -d '{"kpi_name": "Near Miss Reports", "value": 5, "target": 3, "unit": "per month", "period_start": "2024-01-01T00:00:00", "period_end": "2024-01-31T23:59:59"}'

## Get Dashboard Stats
curl "http://localhost:8000/dashboard"

## View API Documentation
# Open in browser: http://localhost:8000/docs
