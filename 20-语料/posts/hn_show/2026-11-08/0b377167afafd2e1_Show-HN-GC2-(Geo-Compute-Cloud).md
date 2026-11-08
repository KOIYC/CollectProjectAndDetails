---
type: "corpus"
item_id: "0b377167afafd2e1"
title: "Show HN: GC2 (Geo Compute Cloud)"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50404243"
project_url: "https://gc2.io/"
author: "mhoegh"
published_at: "2026-11-07T13:07:13Z"
captured_at: "2026-11-08T12:50:31+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-08"
pub_day: "2026-11-07"
tags:
  - 语料
  - hn_show
  - author_mhoegh
  - story_50404243
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: GC2 (Geo Compute Cloud)

> [!info] 一句话导读
> Skip to main content

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50404243>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：mhoegh　|　发布：2026-11-07T13:07:13Z
> 项目链接：<https://gc2.io/>
> 采集：2026-11-08T12:50:31+08:00　|　id：`0b377167afafd2e1`

## 正文

Skip to main content
GC2 Console FAQ Docs Open API
Geospatial BaaS & infrastructure
 The backend for your geospatial applications
 From spatial data to working APIs. GC2 (Geo Compute Cloud) brings together PostGIS, data import, spatial SQL, realtime APIs and OGC map services in one geospatial backend as a service. Build on managed GC2 Cloud or run the platform on your own infrastructure with Docker .
 Start in GC2 Cloud Self-host with Docker Explore data import →
 GeoParquet
 GeoJSON
 Shapefile
 GeoPackage
 FlatGeobuf
 CSV
 GML
 MapInfo
 File Geodatabase
 Open source (AGPLv3) · GitHub · PostgreSQL + PostGIS
{ "name": "Nørrebroparken",
 "distance_m": 420 }
From spatial data to API in three steps
 01 Upload your data
 Import GeoParquet, GeoJSON, Shapefile, GeoPackage, FlatGeobuf, CSV, GML, MapInfo or File Geodatabase into PostGIS tables, with options for coordinate reference systems and reprojection.
 File import →
 02 Get instant APIs
 Query with parameterized SQL over REST or WebSocket and auto-generated GraphQL. Publish layers through OGC API Features & Maps and WMS/WFS.
 SQL API →
 03 Build your app
 TypeScript SDK with OAuth helpers, realtime subscriptions with server-side filtering, and fine-grained access control.
 SDK →
Built for geospatial work, end to end
 ⌖ PostGIS built in
 Find nearby features with ST_DWithin, intersect geometries with ST_Intersects, and transform coordinates with spatial SQL.
 Explore spatial SQL →
 ⛁ Import your spatial data
 Bring GeoParquet, GeoJSON, Shapefile, GeoPackage, FlatGeobuf, CSV or GML into your database and expose it through APIs.
 Explore data import →
 ⏲ Scheduled imports
 Keep tables in sync with files, WFS services and feeds on a cron schedule. Imports are atomic, runs are tracked, and a snapshot can be queued after each one.
 Explore the scheduler →
 ⧉ Snapshots as GeoParquet
 Export tables as dated GeoParquet or FlatGeobuf files with a STAC catalog, and query them straight from DuckDB, Python or a web map over HTTP range requests.
 Explore snapshots →
 ▦ OGC APIs & map services
 Read GeoJSON with OGC API Features, render images with OGC API Maps, and connect GIS tools through WMS/WFS. Edit features via WFS-T.
 Explore the OGC API →
 ⬡ GraphQL, auto-generated
 Queries, mutations and subscriptions derived from your schema.
⇄ Realtime over WebSocket
 Subscribe to table changes with server-side filtering (shapes).
⚿ Control access to your data
 OAuth 2.0 (PKCE, password, device flows), sub-users, table-level privileges and SQL rules.
✳ AI-agent ready
 Connect AI assistants to inspect schemas, query spatial data and manage your backend through the official MCP server.
 Connect AI agents →
 ⌘ Functions for your workflows
 Run Node.js or Python code on demand, on a schedule, or in response to events, with access to your data.
 Explore functions →
 ◍ Open source roots
 Built on Geocloud2 (AGPLv3) by MapCentia, with 10+ years of geospatial domain expertise.
 Explore the open source stack →
Query spatial data. Connect your stack.
 Run PostGIS queries over REST or WebSocket, or use the TypeScript SDK with built-in OAuth helpers. Bind values with named parameters such as :lng , :lat and :radius to find nearby features without building your own API server.
 Read the SQL API docs →
 Build with the TypeScript SDK →
JS / TS SDK AI Agent (MCP) Spatial SQL OGC (WMS/WFS) Self-Host
import { PasswordFlow , Sql } from '@mapcentia/gc2-sdk' ;
// Sign in once — the SDK stores and refreshes tokens for you
 await new PasswordFlow ( {
 host : 'https://api.gc2.io' ,
 clientId : 'your-client-id' ,
 username : 'your-username' ,
 password : process . env . CENTIA_PASSWORD ,
 database : 'your-database' ,
 } ) . signIn ( ) ;
// Parameterized spatial SQL on PostgreSQL + PostGIS
 const { data } = await new Sql ( ) . exec ( {
 q : ` select name, st_asgeojson(geom) as location
 from places
 where st_dwithin(geom::geography,
 st_setsrid(st_makepoint(:lng, :lat), 4326)::geography, :radius) ` ,
 params : { lng : 12.5683 , lat : 55.6761 , radius : 2000 } ,
 } ) ;
{
 "mcpServers" : {
 "gc2" : {
 "command" : "npx" ,
 "args" : [ "-y" , "@mapcentia/gc2-mcp-server" ] ,
 "env" : {
 "API_TOKEN" : "your-access-token" ,
 "API_BASE_URL" : "https://api.gc2.io"
 }
 }
 }
 }
-- POST your SQL to /api/v4/sql with named parameters
 SELECT
 name ,
 category ,
 ST_Distance (
 geom::geography ,
 ST_SetSRID ( ST_MakePoint ( :lng , :lat ) , 4326 ) ::geography
 ) AS distance_meters
 FROM locations
 WHERE ST_DWithin (
 geom::geography ,
 ST_SetSRID ( ST_MakePoint ( :lng , :lat ) , 4326 ) ::geography ,
 :radius
 )
 ORDER BY distance_meters ASC
 LIMIT 10 ;
# Every layer is served through standard OGC services
# Render a styled map image (WMS GetMap)
 https://api.gc2.io/api/v4/ows/schema/parks/database/mydb
 ?SERVICE = WMS & VERSION = 1.1 .0 & REQUEST = GetMap
 & LAYERS = parks.areas & SRS = EPSG:3857
 & BBOX = 1204164,7485240 ,1259200,7534200
 & WIDTH = 1024 & HEIGHT = 768 & FORMAT = image/png
# Fetch the vector features (WFS GetFeature)
 https://api.gc2.io/api/v4/wfs/schema/parks/database/mydb
 ?SERVICE = WFS & VERSION = 1.1 .0 & REQUEST = GetFeature
 & TYPENAME = areas & SRSNAME = EPSG:4326
# Works with QGIS, OpenLayers, Leaflet — WFS-T for editing
# Self-host the full stack: app, WebSockets, PostGIS and Redis
 git clone https://github.com/mapcentia/gc2-docker.git
 cd gc2-docker
 docker compose up --build -d
# Connect with the CLI
 npm install -g @mapcentia/gc2-cli
 gc2 connect http://localhost:81
 gc2 login
Open standards: OGC API, WMS & WFS
 Browse collections and read GeoJSON through OGC API Features , or render styled map images with OGC API Maps . Filter features by bounding box, page through results and choose a supported coordinate reference system. The OGC API provides read-only REST access to your published layers, with the same privileges and geofence rules as WMS/WFS.
 Connect QGIS, OpenLayers, Leaflet and other GIS clients through WMS/WFS, and edit features through WFS-T. Configure map styling with classes, styles and labels through the Layer API.
 Read the OGC API Features & Maps docs →
 Read the WMS/WFS services docs →
 Style layers with the Layer API →
 # Read a collection as GeoJSON (OGC API Features)
 GET https://api.gc2.io/api/v4/ogc/database/mydb/collections/parks.areas/items?limit=10 HTTP/1.1
 Accept : application/geo+json
 Authorization : Bearer your-access-token
# Render a styled map image (OGC API Maps)
 GET https://api.gc2.io/api/v4/ogc/database/mydb/collections/parks.areas/map?width=1024&f=png HTTP/1.1
 Accept : image/png
 Authorization : Bearer your-access-token
What developers build on GC2
 Web maps with live data
 Realtime layers without building a sync pipeline.
Field data collection
 Upload from the field, query from the office.
Open data portals
 Publish spatial datasets as queryable APIs.
GIS + AI workflows
 Let agents query and manage spatial data via MCP.
Desktop GIS integration
 Connect QGIS directly over WMS/WFS and edit with WFS-T.
Analytics on dated snapshots
 Query GeoParquet exports in DuckDB and compare how a dataset looked on any date.
Location-based applications
 Find nearby places, intersect service areas and build spatial queries into your app.
Your geospatial platform. Your choice of deployment.
 Managed geospatial BaaS
 Build on GC2 Cloud
 Start with a managed PostGIS backend. Import your data and connect your apps and GIS tools while GC2 handles the infrastructure.
 Managed PostgreSQL and PostGIS
 Data APIs, OGC services and authentication
 Free during beta — see limits in the FAQ
 Start in GC2 Cloud
 Geospatial infrastructure
 Run it on your infrastructure
 Deploy the open source stack with Docker Compose. Keep control of your runtime, networking and data environment, from local development to production.
 App, WebSockets, PostGIS and Redis
 Your servers and deployment environment
 Open source under AGPLv3
 Explore self-hosting
Build your next geospatial application
 Bring your spatial data. Start with managed cloud or deploy the platform yourself, then connect your maps, apps and GIS tools.
 Start in GC2 Cloud Explore the docs
Docs
 Docs
Community
 Stack Overflow
More
 GitHub
Support
 E-mail
Copyright © 2026 MapCentia

## 关联链接

- http://localhost:81
- https://api.gc2.io
- https://api.gc2.io/api/v4/ogc/database/mydb/collections/parks.areas/items?limit=10
- https://api.gc2.io/api/v4/ogc/database/mydb/collections/parks.areas/map?width=1024&f=png
- https://api.gc2.io/api/v4/ows/schema/parks/database/mydb
- https://api.gc2.io/api/v4/wfs/schema/parks/database/mydb
- https://github.com/mapcentia/gc2-docker.git

## 导航

- 项目页：[[10-项目/gc2.io_88da8dba]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
