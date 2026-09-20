---
type: "project"
title: "Show HN: TypeScript parser for AIXM, the FAA/EUROCONTROL aviation data format"
project_url: "https://github.com/devladpopov/aixm-parser"
first_seen: "2026-09-20T09:36:59+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_devladpopov
  - story_49730243
  - show_hn
lang: "en"
---

# Show HN: TypeScript parser for AIXM, the FAA/EUROCONTROL aviation data format

> [!info] 一句话导读
> devladpopov/aixm-parser

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/devladpopov/aixm-parser>
> 首次收录：2026-09-20T09:36:59+08:00
> 来源渠道：HN Show HN
> 标签：author_devladpopov, story_49730243, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-20/69f7dfdbcee14203_Show-HN-TypeScript-parser-for-AIXM,-the-FAA-EUROCO]] |
| 2026-09-20T09:36:59+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-20/69f7dfdbcee14203_Show-HN-TypeScript-parser-for-AIXM,-the-FAA-EUROCO]] |

## 摘要正文

# devladpopov/aixm-parser  TypeScript parser for AIXM 5.1.1 aeronautical data with temporal model and GML geometry  - Stars: 6 - Forks: 0 - Watchers: 6 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2026-06-04T08:18:10Z  ## Languages  - TypeScript  ## Top Contributors  - devladpopov (6 contributions)  ---  ## README  # aixm-parser  npm version CI License: MIT Node.js >=20 TypeScript  First JavaScript/TypeScript parser for AIXM 5.1.1 (Aeronautical Information Exchange Model) with geodesic geometry, temporal model, and GeoJSON output.  ## Features  - **Streaming parsing** of large AIXM files (SAX + DOM hybrid) - **30 typed feature interfaces** (airports, airspaces, navaids, routes, obstacles, services) - **GML to GeoJSON** conversion with geodesic accuracy on WGS84 - **Temporal model** (BASELINE / PERMDELTA / TEMPDELTA / SNAPSHOT merging) - **Cross-reference resolution** (xlink:href, circular detection, reverse lookup) - **Elevation support** (aixm:elevation emitted as third GeoJSON coordinate, meters) - **CLI**: `aixm-to-geojson input.xml output.geojson` - **Dual ESM/CJS** build, TypeScript-first  ## Install  ```bash npm install aixm-parser ```  ## Quick S…
