---
type: "corpus"
item_id: "69f7dfdbcee14203"
title: "Show HN: TypeScript parser for AIXM, the FAA/EUROCONTROL aviation data format"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49730243"
project_url: "https://github.com/devladpopov/aixm-parser"
author: "devladpopov"
published_at: "2026-09-16T17:27:53Z"
captured_at: "2026-09-20T09:36:59+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-20"
pub_day: "2026-09-16"
tags:
  - 语料
  - hn_show
  - author_devladpopov
  - story_49730243
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: TypeScript parser for AIXM, the FAA/EUROCONTROL aviation data format

> [!info] 一句话导读
> devladpopov/aixm-parser

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49730243>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：devladpopov　|　发布：2026-09-16T17:27:53Z
> 项目链接：<https://github.com/devladpopov/aixm-parser>
> 采集：2026-09-20T09:36:59+08:00　|　id：`69f7dfdbcee14203`

## 正文

# devladpopov/aixm-parser

TypeScript parser for AIXM 5.1.1 aeronautical data with temporal model and GML geometry

- Stars: 6
- Forks: 0
- Watchers: 6
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-06-04T08:18:10Z

## Languages

- TypeScript

## Top Contributors

- devladpopov (6 contributions)

---

## README

# aixm-parser

npm version
CI
License: MIT
Node.js >=20
TypeScript

First JavaScript/TypeScript parser for AIXM 5.1.1 (Aeronautical Information Exchange Model) with geodesic geometry, temporal model, and GeoJSON output.

## Features

- **Streaming parsing** of large AIXM files (SAX + DOM hybrid)
- **30 typed feature interfaces** (airports, airspaces, navaids, routes, obstacles, services)
- **GML to GeoJSON** conversion with geodesic accuracy on WGS84
- **Temporal model** (BASELINE / PERMDELTA / TEMPDELTA / SNAPSHOT merging)
- **Cross-reference resolution** (xlink:href, circular detection, reverse lookup)
- **Elevation support** (aixm:elevation emitted as third GeoJSON coordinate, meters)
- **CLI**: `aixm-to-geojson input.xml output.geojson`
- **Dual ESM/CJS** build, TypeScript-first

## Install

```bash
npm install aixm-parser
```

## Quick Start

```typescript
import { parse } from 'aixm-parser';
import { readFileSync } from 'fs';

const xml = readFileSync('Donlon.xml', 'utf-8');
const result = await parse(xml);

// High-level accessors
const airports = result.airports();
const airspaces = result.airspaces();
const navaids = result.navaids();

console.log(`${airports.length} airports, ${airspaces.length} airspaces, ${navaids.length} navaids`);

// Access typed properties
for (const apt of airports) {
  console.log(apt.properties.name, apt.properties.locationIndicatorICAO);
}
```

## CLI

```bash
npm install -g aixm-parser   # or: npx -p aixm-parser aixm-to-geojson ...

aixm-to-geojson input.xml output.geojson
aixm-to-geojson input.xml --pretty > out.geojson
aixm-to-geojson input.xml output.geojson --stats --tolerance 50
```

Options: `--keep-null` (keep features without geometry), `--tolerance ` (densification, default 100), `--pretty`, `--stats`.

## GeoJSON Output

```typescript
// Convert all features to a GeoJSON FeatureCollection
const geojson = result.toGeoJSON();

// Skip features without geometry (e.g. organisations, frequencies)
const spatial = result.toGeoJSON({ skipNullGeometry: true });

// Or convert individual features
import { featureToGeoJSON, extractGeometry } from 'aixm-parser';

const feature = result.features[0];
const geoFeature = featureToGeoJSON(feature);
const geometry = extractGeometry(feature.xmlChunk);
```

Supported GML geometry types:
- `gml:Point` / `aixm:ElevatedPoint` (elevation as third coordinate)
- `gml:CircleByCenterPoint` (densified on WGS84 ellipsoid)
- `gml:ArcByCenterPoint` (geodesic arc via Karney algorithm)
- `gml:GeodesicString` / `gml:Geodesic` (great circle segments)
- `gml:Curve` / `aixm:ElevatedCurve` (compound curves with multiple segments)
- `gml:PolygonPatch` with exterior/interior rings
- `aixm:Surface` / `aixm:ElevatedSurface`

`result.toGeoJSON()` additionally:
- resolves arc/circle centers given as ` ` across the whole document
- assembles geometry for `Route` features from their `RouteSegment` LineStrings (`MultiLineString`)

## Temporal Model

AIXM features change over time through TimeSlices. Query the state at any point in time:

```typescript
// Get feature state at a specific timestamp
const state = result.featureAt('uuid.abc-123', new Date('2024-06-01'));
console.log(state.properties.name); // merged from BASELINE + deltas
console.log(state.activeTemporalOverlays); // number of active TEMPDELTAs

// Low-level: compute state from a raw feature
import { computeState, getTimeline } from 'aixm-parser';

const timeline = getTimeline(rawFeature); // all states in chronological order
const current = computeState(rawFeature, new Date());
```

## Cross-References

AIXM features reference each other via `xlink:href`. The built-in registry resolves them:

```typescript
const { registry } = await parse(xml);

// Resolve a single reference
const airport = registry.resolve('urn:uuid:abc-123');
const navaid = registry.resolve('#NAV_DON');

// Resolve all pending references
const resolved = registry.resolveAll();
const unresolved = resolved.filter(r => !r.target);

// Reverse lookup: who references this feature?
const referencing = registry.getReferencingFeatures('uuid-of-airport');

// Build the full reference graph
const graph = registry.buildGraph();

// Detect circular references
const cycles = registry.detectCircularRefs();
```

## Geodesic Geometry

Arc and circle geometry is computed on the WGS84 ellipsoid using the Karney algorithm:

```typescript
import { densifyArcByCenterPoint, densifyCircle, geodesicDistance } from 'aixm-parser';

// Arc from 090 to 270 degrees clockwise, radius 5km
const arc = densifyArcByCenterPoint(
  { lon: -1.0, lat: 51.0 }, 5000, 90, 270, true, 100
);

// Circle with 15 NM radius
const circle = densifyCircle(
  { lon: -22.1, lat: 52.37 }, 15 * 1852, 100
);

// Distance between two points
const dist = geodesicDistance(
  { lon: -0.1278, lat: 51.5074 },  // London
  { lon: 2.3522, lat: 48.8566 }    // Paris
);
```

## Typed Features

30 AIXM feature types with TypeScript interfaces:

| Category | Types |
|----------|-------|
| Aerodromes | AirportHeliport, Runway, RunwayDirection, Taxiway, Apron, AircraftStand, TouchDownLiftOff |
| Airspace | Airspace |
| Navigation | Navaid, VOR, DME, NDB, TACAN, DesignatedPoint, MarkerBeacon, Localizer, Glidepath |
| Routes | Route, RouteSegment, HoldingPattern |
| Obstacles | VerticalStructure, ObstacleArea |
| Services | AirTrafficControlService, SearchRescueService, InformationService, RadioCommunicationChannel |
| Organization | OrganisationAuthority, Unit, GeoBorder, SpecialDate |

## API Reference

### `parse(xml, options?)`

Main entry point. Returns a `ParseResult` with:

| Property | Description |
|----------|-------------|
| `features` | Raw features as extracted from XML |
| `typed` | Typed features with structured properties |
| `registry` | Feature registry for cross-reference resolution |
| `featureAt(id, date?)` | Get feature state at a point in time |
| `airspaces()` | All Airspace features |
| `airports()` | All AirportHeliport features |
| `runways()` | All Runway features |
| `navaids()` | All navaid features (VOR, DME, NDB, TACAN, Navaid) |
| `waypoints()` | All DesignatedPoint features |
| `routes()` | All Route features |
| `routeSegments()` | All RouteSegment features |
| `obstacles()` | All VerticalStructure features |
| `toGeoJSON(options?)` | Convert to GeoJSON FeatureCollection |
| `diagnostics()` | Parse and reference-resolution diagnostics |

### Options

```typescript
interface ParseOptions {
  errorMode?: 'strict' | 'lenient'; // default: 'lenient'
}

interface GmlToGeoJSONOptions {
  toleranceMeters?: number;    // densification tolerance, default: 100
  skipNullGeometry?: boolean;  // omit features without geometry
  pointResolver?: (gmlId: string) => Position | null; // custom center resolver
}
```

## Requirements

- Node.js >= 20.0.0
- TypeScript >= 5.0 (for type definitions)

## License

MIT

# Pixel Agents — Your Claude Code agents, working in a pixel office

## 导航

- 项目页：[[10-项目/github.com_a181b944]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
