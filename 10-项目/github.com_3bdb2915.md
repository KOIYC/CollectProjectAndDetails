---
type: "project"
title: "Show HN: Crudio – Turn an OpenAPI spec into a stateful mock back end"
project_url: "https://github.com/enricodeleo/crudio"
first_seen: "2026-09-21T03:11:01+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_enricodeleo
  - story_48726455
  - show_hn
lang: "en"
---

# Show HN: Crudio – Turn an OpenAPI spec into a stateful mock back end

> [!info] 一句话导读
> Crudio turns an OpenAPI/Swagger spec into a real, stateful CRUD backend with persistence, strict validation, and optional fake-data seeding.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/enricodeleo/crudio>
> 首次收录：2026-09-21T03:11:01+08:00
> 来源渠道：HN Show HN
> 标签：author_enricodeleo, story_48726455, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:29:55+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-21/2b236d4b341372b7_Show-HN-Crudio-–-Turn-an-OpenAPI-spec-into-a-state]] |
| 2026-09-21T03:11:01+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-21/2b236d4b341372b7_Show-HN-Crudio-–-Turn-an-OpenAPI-spec-into-a-state]] |

## 摘要正文

# enricodeleo/crudio  Crudio turns an OpenAPI/Swagger spec into a real, stateful CRUD backend with persistence, strict validation, and optional fake-data seeding.  - Stars: 2 - Forks: 1 - Watchers: 2 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2026-04-23T14:12:34Z  ## Languages  - JavaScript - Shell  ## Top Contributors  - enricodeleo (92 contributions)  ---  ## README   Crudio   Turn an OpenAPI 3.x spec into a working, stateful mock backend.   Spec-driven and stateful and validating — the one cell other mock tools leave empty.   Quick Start · How It Works · Scope · Full API Docs · Configuration  ---  ## Demo  One command turns any OpenAPI 3.x spec into a running, **stateful** backend — seed it, write to it, and it remembers what you did:  Crudio demo  ```console $ npx @enricodeleo/crudio ./openapi.yaml --seed 3 Crudio running on port 3000  $ curl -s localhost:3000/pets                 # 3 seeded records — schema-shaped, real IDs [{"name":"ea","tag":"dog","id":1},{"name":"accommodo","tag":"cat","id":2},{"name":"tui","tag":"bird","id":3}]  $ curl -s -XPOST localhost:3000/pets -H content-type:application/json -d '{"name":"Rex","tag":"dog"}' {"name":"Rex"…
