---
type: "corpus"
item_id: "295e40135f527342"
title: "Show HN: TaskView – self-hosted project management for teams"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49115078"
project_url: "https://github.com/Gimanh/taskview-community"
author: "rg1527"
published_at: "2026-07-30T20:07:21Z"
captured_at: "2026-09-21T03:11:12+08:00"
lang: "en"
kind: "post"
topic: 开发者工具
shard: "2026-09-21"
pub_day: "2026-07-30"
tags:
  - 语料
  - hn_show
  - author_rg1527
  - story_49115078
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:83d"
---

# Show HN: TaskView – self-hosted project management for teams

> [!info] 一句话导读
> Gimanh/taskview-community

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49115078>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：rg1527　|　发布：2026-07-30T20:07:21Z
> 项目链接：<https://github.com/Gimanh/taskview-community>
> 采集：2026-09-21T03:11:12+08:00　|　id：`295e40135f527342`

## 正文

# Gimanh/taskview-community

TaskView is a self-hosted project and task management platform focused on clarity, ownership, and control. TaskView is built for teams that want a transparent, self-hosted alternative to SaaS task managers.

- Stars: 100
- Forks: 7
- Watchers: 100
- Open issues: 2
- License: Other
- Homepage: https://taskview.tech/
- Default branch: main
- Created: 2025-12-29T21:09:59Z

## Languages

- CSS
- HTML
- Java
- JavaScript
- PLpgSQL
- Ruby
- SCSS
- Shell
- Swift
- TypeScript
- Vue

## Topics

- graphview
- kanban-board
- nodejs
- productivity
- project-management
- self-hosted
- task
- task-management
- task-manager
- todoapp

## Top Contributors

- Gimanh (170 contributions)

---

## README

# TaskView™

TaskView Logo

TaskView is a self-hosted project and task management platform focused on clarity, ownership, and control.
TaskView is built for teams that want a transparent, self-hosted alternative to SaaS task managers.

License
Active Development

**Live demo** · **Documentation** · **iOS** · **Android**

## Apps
* Docs
* Web
* iOS
* Android

It is designed for teams and individuals who want:
- full control over their data
- transparent architecture
- predictable workflows
- the ability to run the system on their own infrastructure

## Key Features
- Projects, lists, tasks, and subtasks
- Kanban boards
- Clear responsibility assignment
- Permissions and roles
- Web and mobile clients
- Self-hosted by design

## Licensing

TaskView uses a source-available license.

You may:
- self-host TaskView
- modify the source code
- use it internally within your organization

You may not:
- offer TaskView as a hosted SaaS
- sell TaskView as a service
- create a competing commercial product
- use the TaskView name or branding for derivative products

See LICENSE for full terms.
TaskView is a trademark of its authors.

## Architecture

This repository is a monorepo.

Main product packages:

 - `api` – backend (Node.js)
 - `web` – web client and mobile
 - `taskview-packages/taskview-api` – API client library for building integrations and making HTTP requests
 - `taskview-packages/taskview-db-schemas` - Drizzle ORM schemas

Product packages share a single version.

## Versioning

TaskView follows semantic versioning:
 - `MAJOR` – breaking API or data changes
 - `MINOR` – new features
 - `PATCH` – bug fixes
The version represents the entire product, not individual packages.

## Status

TaskView is under active development.
Breaking changes may occur between versions.

## Getting started

This setup is intended for local development.

### Development

**Prerequisites:**
- Docker
- PostgreSQL
 - On macOS you can use https://postgresapp.com/
- Bun (used for API development)
- pnpm

**Steps:**
1. Install dependencies:
```sh
pnpm install
```

2. Create an `.env` file in the **api** directory based on `.env.example` and configure your local credentials.

3. Run the web application:
```sh
cd web
pnpm dev
```

1. Run the API locally (API uses Bun in development mode):
```sh
cd api
pnpm start
```

## Building Docker Images

You can build Docker images using the provided bash script. The image version is automatically taken from the root `package.json`.

**Steps:**
1. Build images:
```sh
./build-dockers.sh
```

2. Verify built images:
```sh
docker images
```
You should see the following images:

`gimanhead/taskview-ce-api-server`
`gimanhead/taskview-ce-webapp`
`gimanhead/taskview-ce-db-migration`

3. Test images locally using Docker Compose:
```sh
cd api/dev-containers-test
docker-compose up
```

Make sure the image versions match the version defined in the root package.json.

## Roadmap

- [X] Migrate to NuxtUI or similar ui library
- [X] Enterprise SSO and identity integrations
- [X] Redesign
- [X] API tokens
- [X] Webhooks
- [X] MCP server
- [X] Notifications
- [X] Analytics
- [X] API client
- [ ] Desktop version
- [ ] Plugin / extension system

Note for contributors: contributions are accepted under the CLA (see CONTRIBUTING.md). The Project is distributed under the TaskView Source-Available License.

---

TaskView is developed and maintained by Nikolai Giman.

Copyright © 2026 Nikolai Giman

# ElhamBadri2411/aina

## 关联链接

- https://postgresapp.com/
- https://taskview.tech/

## 导航

- 项目页：[[10-项目/github.com_f414b9c4]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
