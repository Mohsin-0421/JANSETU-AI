from fastapi import FastAPI

from app.routers.intelligence import router as intelligence_router


app = FastAPI(
    title="JANSETU Intelligence Engine",
    description="AI-powered problem intelligence, matching and innovation engine",
    version="1.0.0"
)


app.include_router(
    intelligence_router,
    prefix="/api/v1",
    tags=["JANSETU Intelligence"]
)


@app.get("/")
def root():
    return {
        "message": "JANSETU Intelligence Engine is running",
        "status": "active"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "engine": "JANSETU Intelligence Engine"
    }