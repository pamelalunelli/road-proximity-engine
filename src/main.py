from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Query, HTTPException
from contextlib import asynccontextmanager
from pathlib import Path
from src.core.engine import SpatialEngine

SHP_PATH = Path("data/roads.shp")

@asynccontextmanager
async def lifespan(app: FastAPI):
    if SHP_PATH.exists():
        app.state.engine = SpatialEngine(str(SHP_PATH))
    else:
        app.state.engine = None
    yield

app = FastAPI(title="Road Proximity Engine", lifespan=lifespan)

@app.get("/health")
def health():
    return {
        "status": "ok",
        "engine_loaded": app.state.engine is not None
    }

@app.get("/near")
def near(lat: float, lon: float, radius_m: float = Query(500, ge=1, le=20000)):
    if app.state.engine is None:
        raise HTTPException(status_code=503, detail="Engine not loaded")
    return app.state.engine.query_radius(lat, lon, radius_m)

app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")