from fastapi import FastAPI, Query
from src.core.engine import SpatialEngine
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Road Proximity Engine")

SHP_PATH = "data/roads.shp"

engine = SpatialEngine(SHP_PATH)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/near")
def near(
    lat: float,
    lon: float,
    radius_m: float = Query(500, ge=1, le=20000),
):
    return engine.query_radius(lat, lon, radius_m)

app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

