---
type: "corpus"
item_id: "a20c74f7ea7953a4"
title: "Show HN: Alidade – an open-source Web-GIS where the map is one JSON document"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49737256"
project_url: "https://github.com/AysanZ/alidade"
author: "aysanz"
published_at: "2026-09-17T06:52:20Z"
captured_at: "2026-09-20T09:36:55+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-20"
pub_day: "2026-09-17"
tags:
  - 语料
  - hn_show
  - author_aysanz
  - story_49737256
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: Alidade – an open-source Web-GIS where the map is one JSON document

> [!info] 一句话导读
> Open-source Web-GIS: PostGIS vector tiles, satellite imagery, 3D models on terrain, and a live asset layer. No API keys.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49737256>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：aysanz　|　发布：2026-09-17T06:52:20Z
> 项目链接：<https://github.com/AysanZ/alidade>
> 采集：2026-09-20T09:36:55+08:00　|　id：`a20c74f7ea7953a4`

## 正文

# AysanZ/alidade

Open-source Web-GIS: PostGIS vector tiles, satellite imagery, 3D models on terrain, and a live asset layer. No API keys.

- Stars: 13
- Forks: 1
- Watchers: 13
- Open issues: 0
- License: Apache License 2.0
- Homepage: https://alidade.aysanz.dev/
- Default branch: main
- Created: 2026-08-29T09:59:51Z

## Languages

- CSS
- Dockerfile
- HTML
- PLpgSQL
- Python
- Shell
- TypeScript

## Topics

- 3d-maps
- cartography
- cognito
- fastapi
- geospatial
- geotiff
- gis
- maplibre
- maplibre-gl-js
- mapping
- open-source-gis
- postgis
- raster
- react
- satellite-imagery
- threejs
- typescript
- vector-tiles
- webgis

## Top Contributors

- AysanZ (50 contributions)

---

## README

# Alidade

**An open-source Web-GIS platform.**
PostGIS vector tiles, satellite imagery, full symbology, 3D models on the terrain,
and a real-time asset layer. No API keys anywhere.

ci
licence
no api keys

**▶ Live demo**

---

## What it is

The map is one JSON document. The core diffs two versions of it and emits a list of
operations; an adapter applies those operations to MapLibre. Editing the document
changes the map — and swapping the basemap does not destroy your layers.

That one decision is why undo is sixty whole documents deep, why a drawing survives
a basemap swap, and why the renderer could be replaced without touching the model.

```
packages/core        the arithmetic  ·  knows nothing about any renderer
packages/maplibre    the only folder that knows MapLibre exists
packages/three       the only folder that knows three.js exists
apps/studio          React client
services/api         FastAPI: ingest, vector tiles, imagery, WMS, live feed
```

## Features

| | |
|---|---|
| **Data in** | Drop a GeoJSON, zipped Shapefile, GeoPackage, KML or GPX — reprojected by ogr2ogr into PostGIS and served back as vector tiles in the same request. Or paste a link and GDAL reads it over HTTP. Or point at a WMS and pick a layer from GetCapabilities. |
| **Imagery** | GeoTIFFs converted once to Cloud-Optimised GeoTIFFs and indexed by their real footprint. Tiles are mosaicked on demand under a rule you choose — newest, closest to a date, sharpest, best covering, or one locked image — with band selection, stretch and band maths as query parameters rather than as decisions frozen at import. |
| **Symbology** | Single, graduated and categorised, with markers, labels and per-layer scale ranges. |
| **Filters** | A filter is a structure, not a string, so one filter compiles two ways: a renderer expression and parameterised SQL. The inspector will show you the SQL. |
| **Identify** | Click a feature for its attributes, or the imagery for the pixel values under the cursor. The attribute table pages, searches, sorts and hides columns, and highlights on the map what you select in it. |
| **2D · 2.5D · 3D** | Three projections including a real globe, terrain and hillshade from open elevation tiles, and OSM building footprints raised to their real height. |
| **3D models** | glTF placed the way a surveyor states it — position, height, bearing, scale — standing on the terrain, lit by the real sun for a real instant, casting real shadows. One model can be placed at every point of a layer. |
| **Live assets** | Positions over a WebSocket as an ordinary row in the table of contents. Assets that go quiet are drawn hollow, not deleted. A model can stand in for one and take its heading, climb and bank from the reports. |
| **Drawing** | Geodesic measurement, buffers, snapping, vertex editing. Exports to GeoJSON, KML, GPX, CSV or WKT — and reads all of them back. |
| **Chrome** | Graticule, UTM and metric grids, overview map, scale bar in three unit systems, coordinate readout in DD, DMS or UTM, bookmarks. |

## What it looks like

 Layers, styled. Markers, outlines and a legend that follows what you set, over data loaded from a link a minute earlier.
 Ask it things. Click a feature for what it is; the table pages, searches and finds the same row.

 A real globe, not a picture of one — and a sphere at every zoom if you ask for one.
 3D buildings from OpenStreetMap. Footprints extruded to their real height, lit from where the sun actually was.

 Fly a landing. The aircraft banks because it is turning, not because a keyframe said so.
 A live fleet over a WebSocket, with a connection light, because a stopped feed and a still fleet look identical.

 Imagery. A schematic rather than a screenshot: what is on the map is whatever you loaded. See the imagery notes.
 Basemaps, none of which need a key. Swapping one does not disturb your layers.

## Run it

```bash
cp .env.example .env

# --env-file matters: compose looks for .env next to the compose file, not here.
docker compose --env-file .env -f deploy/docker-compose.yml up -d --build

# Install from the repository root. The studio depends on two workspace packages,
# so installing inside apps/studio cannot see them.
pnpm install
pnpm dev
```

- Studio —
- API health —
- Live feed — `ws://localhost:8000/api/live/assets`, switched on from the **Live assets** row
- Postgres — host port **5433**, because 5432 is usually already taken

The database ships **empty**. There is no seeded demo layer: one cannot be deleted from
the studio, it comes back on every fresh volume, and it makes an install that has
nothing in it look like it already has data. Get data in through **Add data**, or load
straight into PostGIS:

```bash
./data/seed.sh wards.gpkg
```

Two things live on volumes rather than in the database, because they are files:
uploaded `.glb` models and converted imagery. A single satellite scene is a couple of
hundred megabytes, so give the imagery volume room before loading a folder of them.

For a server rather than a laptop, `deploy/docker-compose.prod.yml` runs images
built in CI instead of building anything locally, and publishes nothing but
Caddy. See deployment.

## No API keys

Nothing here needs one, and that is a constraint rather than a boast: a demo that dies
when someone's free tier changes is worse than a demo with fewer basemaps. The canvases
and the buildings are OpenFreeMap, the imagery and terrain
styles are Esri, and the elevation is Mapzen terrarium.

## Tests

```bash
pnpm test        # 585 tests in 37 files, Node only: no browser, no WebGL
pnpm typecheck
pnpm build

cd services/api && pytest    # 70 more; 55 of them want no database at all
```

CI runs the API twice on purpose: once with nothing but Python, for the parsing, the
naming rules, the live feed and every imagery decision that is arithmetic on a
`gdalinfo` document; and once against a real PostGIS with `data/init/` loaded, for the
tiles and the registry.

Core tests assert on the operation array the reconciler emits for a given pair of
project states, so slot ordering, classification, filter compilation and the imagery
rules are all tested without rendering anything. Adapter tests use a fake renderer that
records calls and refuses the same things a real one refuses. Nothing in the suite
touches a GPU.

`packages/core/tests/regressions.test.ts` holds one test per defect that has been
fixed, named after the symptom rather than the cause.

## Documentation

- **Design notes** — why each subsystem is built the way it is,
 at length: the document model, geodesic drawing, the sun, the live feed's contract.
- **Imagery** — the GeoTIFF catalogue, footprints, dates, mosaic
 rules and band maths, and what the endpoints answer.
- **Imagery prior art** — TiTiler, STAC, mosaic datasets
 and EO Browser: what the field already does, what was taken from it, and what is left.
- **Deployment** — production on a small VPS: images built in
 CI, Caddy for TLS, tile caching, and the parts that only fail once you are live.
- **Contributing**

## Licence

Apache-2.0.

# try

## 关联链接

- https://alidade.aysanz.dev/

## 导航

- 项目页：[[10-项目/github.com_7ef76be9]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
