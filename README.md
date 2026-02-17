# Road Proximity Engine

Geospatial microservice that returns nearby road segments given coordinates and radius.

## Features
- Spatial indexing (R-tree)
- Fast proximity queries
- REST API
- Interactive map client
- GeoJSON responses

## Tech Stack
- FastAPI
- GeoPandas
- Shapely
- Rtree
- Leaflet

## Run
```bash
uvicorn src.main:app --reload