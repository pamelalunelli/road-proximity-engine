import time
import geopandas as gpd
from shapely.geometry import Point
import math

class SpatialEngine:
    def __init__(self, shp_path: str):
        gdf = gpd.read_file(shp_path)

        gdf = gdf.to_crs(3857)

        keep_cols = [c for c in ["name", "ref", "fclass", "geometry"] if c in gdf.columns]
        self.gdf = gdf[keep_cols].copy()

        self.sindex = self.gdf.sindex

    def query_radius(self, lat: float, lon: float, radius_m: float):
        t0 = time.perf_counter()

        pt = gpd.GeoSeries([Point(lon, lat)], crs=4326).to_crs(3857).iloc[0]

        bbox = pt.buffer(radius_m).bounds
        idx = list(self.sindex.intersection(bbox))
        candidates = self.gdf.iloc[idx].copy()

        if candidates.empty:
            return {"count": 0, "query_time_ms": round((time.perf_counter()-t0)*1000, 2), "features": {"type": "FeatureCollection", "features": []}}

        candidates["dist_m"] = candidates.distance(pt)
        hits = candidates[candidates["dist_m"] <= radius_m].sort_values("dist_m").head(50)

        hits4326 = hits.to_crs(4326)
        geojson = hits4326.__geo_interface__

        result = {
            "count": int(len(hits4326)),
            "query_time_ms": round((time.perf_counter() - t0) * 1000, 2),
            "features": geojson,
            "nearest": None if hits4326.empty else {
                "dist_m": float(hits4326.iloc[0]["dist_m"]),
                "name": hits4326.iloc[0].get("name"),
                "ref": hits4326.iloc[0].get("ref"),
                "fclass": hits4326.iloc[0].get("fclass"),
            }
        }

        return _clean_json(result)

    
def _clean_json(obj):
    if isinstance(obj, float):
        if math.isnan(obj) or math.isinf(obj):
            return None
        return obj
    if isinstance(obj, dict):
        return {k: _clean_json(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_clean_json(v) for v in obj]
    return obj
