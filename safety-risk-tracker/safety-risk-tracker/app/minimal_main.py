from fastapi import FastAPI

app = FastAPI(
    title="Safety & Risk Tracker API",
    description="A comprehensive API for tracking workplace hazards, compliance checks, and safety KPIs",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Welcome to Safety & Risk Tracker API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/test")
def test_endpoint():
    return {"test": "working"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
