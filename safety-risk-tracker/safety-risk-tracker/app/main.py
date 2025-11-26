from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.database import engine, get_db
from app import models
from app.routers import hazards, compliance, kpis
from app import crud
from app import schemas

app = FastAPI(
    title="Safety & Risk Tracker API",
    description="A comprehensive API for tracking workplace hazards, compliance checks, and safety KPIs",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables on startup
@app.on_event("startup")
def startup_event():
    try:
        models.Base.metadata.create_all(bind=engine)
        print("Database tables created successfully!")
    except Exception as e:
        print(f"Database creation error: {e}")

# Include routers
app.include_router(hazards.router)
app.include_router(compliance.router)
app.include_router(kpis.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Safety & Risk Tracker API"}

@app.get("/dashboard")
def get_dashboard_stats(db: Session = Depends(get_db)):
    try:
        return crud.get_dashboard_stats(db=db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Dashboard error: {str(e)}")

@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
