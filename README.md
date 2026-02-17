# Road Proximity Engine

[![tests](https://github.com/pamelalunelli/road-proximity-engine/actions/workflows/python-app.yml/badge.svg)](https://github.com/pamelalunelli/road-proximity-engine/actions/workflows/python-app.yml)

High-performance geospatial API that returns nearby road segments given coordinates and search radius.

---

## Demo
![demo](docs/demo.gif)

---

## Overview
Road Proximity Engine is a lightweight spatial microservice designed to perform fast proximity queries against road network data.

It demonstrates how to build a production-style geospatial backend with spatial indexing, API design, and client visualization.

---

## Features
- R-tree spatial indexing for fast lookup
- Radius-based spatial queries
- REST API built with FastAPI
- Interactive map frontend
- GeoJSON responses
- Automated tests with CI pipeline

---

## Architecture

Client → FastAPI → Spatial Engine → Indexed GeoDataFrame

Spatial queries run entirely server-side for performance and scalability.

---

## Tech Stack
- FastAPI
- GeoPandas
- Shapely
- Rtree
- Leaflet
- Pytest
- GitHub Actions

---

## API Example

**Request**
```
GET /near?lat=-25.43&lon=-49.27&radius_m=800
```

**Response**
```json
{
  "count": 5,
  "query_time_ms": 3.2,
  "nearest": {...},
  "features": {...}
}
```

---

## Run locally

```
pip install -r requirements.txt
uvicorn src.main:app --reload
```

Open in browser:
```
http://127.0.0.1:8000/
```

---

## Testing

```
pytest
```

---

## Future Improvements
- Batch query endpoint
- Docker containerization
- PostGIS backend support
- Response caching
- Rate limiting

---

## Purpose
This project demonstrates real-world geospatial backend engineering concepts, including:

- spatial indexing
- API design
- service architecture
- lifecycle resource management
- automated testing
