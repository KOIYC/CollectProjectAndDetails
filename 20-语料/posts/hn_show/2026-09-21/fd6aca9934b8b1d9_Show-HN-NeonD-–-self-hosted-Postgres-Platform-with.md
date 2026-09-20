---
type: "corpus"
item_id: "fd6aca9934b8b1d9"
title: "Show HN: NeonD – self-hosted Postgres Platform with branching, PITR and backups"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47947389"
project_url: "https://github.com/matisiekpl/neond"
author: "matisiekpl"
published_at: "2026-04-29T12:27:13Z"
captured_at: "2026-09-21T02:52:39+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-29"
tags:
  - 语料
  - hn_show
  - author_matisiekpl
  - story_47947389
  - show_hn
metrics: {"points": 2, "comments": 2, "engagement_velocity": 2}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:174d"
---

# Show HN: NeonD – self-hosted Postgres Platform with branching, PITR and backups

> [!info] 一句话导读
> DX-focused control plane for Postgres dedicated to non-critical workloads. Your postgres:latest replacement 🐘

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47947389>
> 指标：点赞=2 · 评论=2 · engagement_velocity=2
> 作者：matisiekpl　|　发布：2026-04-29T12:27:13Z
> 项目链接：<https://github.com/matisiekpl/neond>
> 采集：2026-09-21T02:52:39+08:00　|　id：`fd6aca9934b8b1d9`

## 正文

# matisiekpl/neond

DX-focused control plane for Postgres dedicated to non-critical workloads. Your postgres:latest replacement 🐘

- Stars: 113
- Forks: 8
- Watchers: 113
- Open issues: 0
- License: Apache License 2.0
- Default branch: main
- Created: 2026-03-27T09:58:43Z

## Languages

- Rust
- Vue

## Topics

- branches
- neon
- pitr
- postgres
- s3
- storage

## Top Contributors

- matisiekpl (253 contributions)

---

## README

 DX-focused control plane for PostgreSQL
 NeonD is an open-source Neon-based control plane daemon for PostgreSQL. It offers S3-based layer durability, instant branching, precise Point-in-time recovery in seconds. Runs as a single Docker container, handles multi-tenant PostgreSQL instances seamlessly.

PostgreSQL
Apache 2.0 License
Self Hosted
Open Source

 Features •
 Installation •
 Usage •
 Documentation •
 Motivation •
 License

## ✨ Features

- **Launch PostgreSQL instances** - versions v14, v15, v16, v17 supported
- **Branching** - branch your **production** timeline to multiple **development** or **preview** branches
- **S3 Checkpoints** - your data are durably stored on Amazon S3 - checkpoint interval fully configurable
- **Easy migration** - moving NeonD between servers is super easy. Shutdown the server and copy a single directory.
- **TLS SNI Routing** - NeonD generates `{instance-slug}.your-company.com` endpoints. Multiple Postgres instances a
 under single domain.
- **Full Security** - control plane takes care about SSL certificates and keys to enable secure connection
- **Multi-Tenancy** - create multiple users and share compute to other developers with configured roles
- **PgBouncer built-in** - connection pooling out of the box for every endpoint
- **Import existing PostgreSQL** - import an external Postgres database into a new branch
- **Extensions** - ships with `pgvector` and compiled Postgres contrib extensions
- **Observability** - per-branch logs and storage size metrics in the dashboard

> NeonD is not designed to be deployed in critical application environments. Its purpose is to
> provide a DX-oriented PostgreSQL platform for early-stage startup projects, where innovation and velocity are more
> important than reliability. The recommended deployment environment is bare metal VPS Server.

---

## 📦 Installation

The easiest way of deployment is to spin-up NeonD using Docker Compose.

```bash
# Skip on macOS
mkdir neond_data
sudo chown -R 600:600 neond_data
```

```yaml
services:
  neond:
    image: neond/neond:latest
    environment:
      PORT: 3000
      SERVER_SECRET: "SuperSecret" # you should change this
      PORT_RANGE: 50000-50010
    ports:
      - "3000:3000"
      - "50000-50010:50000-50010"
    restart: unless-stopped
    stop_grace_period: 1h
    healthcheck:
      test: ["CMD", "curl", "-fsS", "http://127.0.0.1:3000/api/auth/setup"]
      interval: 30s
      timeout: 5s
      retries: 3
      start_period: 5m
    volumes:
      - ./neond_data:/neond
```

Or, if you want to use TLS SNI Router with custom domain:

```yaml
services:
  neond:
    image: neond/neond:latest
    environment:
      PORT: 3000
      SERVER_SECRET: "SuperSecret" # you should change this
      PG_PROXY_PORT: "5432"
      PG_HOSTNAME: company.com # would generate {instance-slug}.company.com endpoints
    ports:
      - "3000:3000"
      - "5432:5432"
    restart: unless-stopped
    stop_grace_period: 1h
    healthcheck:
      test: ["CMD", "curl", "-fsS", "http://127.0.0.1:3000/api/auth/setup"]
      interval: 30s
      timeout: 5s
      retries: 3
      start_period: 5m
    volumes:
      - ./neond_data:/neond
```

If you want to switch to S3 durable storage, pass following environment variables:

```yaml
services:
  neond:
    ...
    environment:
      ...
      AWS_ACCESS_KEY_ID:
      AWS_SECRET_ACCESS_KEY:
      AWS_S3_BUCKET:
      AWS_REGION:
    ...
```

---

## 🚀 Usage

1. After launch, navigate to `http://localhost:3000`
2. Sign up and name a new organization
3. Create new project and go to it.
4. Click on options of default `production` branch and click "Start endpoint".
5. Click on options of branch and "Copy Connection String".
6. Connect to database - for example `psql '<connection_string>'`

## 📚 Documentation

Full user guide lives in `docs/`:

- **Getting started** — Installation, Quickstart, Configuration, Accounts & organizations
- **Using neond** — Branching & PITR, Importing PostgreSQL, PgBouncer, TLS SNI routing
- **Operating neond** — Startup, Storage, Backups

## ⚠️ Caveats

- `SERVER_SECRET` can't be changed after initial launch!
- Architecture is intentionally tightly-coupled to provide ease of use.
- It is recommended to launch only one instance of NeonD per server.

## 🚀 Motivation

This project has been founded by Mateusz Woźniak, because he found particurly hard to
quickly spinup PostgreSQL instances on small VPS Servers. Project heavily depends
on neondatabase/neon project - neond is the control plane layer for it. Big
kudos for entire Neon team!

## 📝 License

This project is licensed under the Apache 2.0 License - see the LICENSE file for details

## 评论（2/2）

> **matisiekpl** · 2026-04-29T12:27:24.000Z　
> Hey HN, Mateusz here.I built NeonD for myself and figured it might be useful to others. It's a control plane for PostgreSQL that runs as a single Docker container.The problem: I often need to spin up Postgres instances for small side projects. They usually have to run 24/7 for the whole month, and RDS gets expensive fast for that kind of thing. I wanted something that replaces my docker-compose with `postgres:latest`, but adds the few features I actually miss: PITR, proper backups, branching for preview environments.The solution: NeonD is a rich Postgres Control Plane you drop on a dedicated server / VPS. It manages multiple Postgres instances under one host inside single container.What's in the box:- Multi-tenancy and management of multiple Postgres instances- Branching — spin up an isolated DB environment for a preview branch in seconds- PITR with arbitrary-LSN precision, fully configurable retention- S3 backups (layer durability)- Fully automated TLS certificate management- TLS SNI routing — every instance gets its own subdomain, e.g. instance-a.your-company.com- Built-in metrics + log monitoring with PrometheusInstall takes less than 5 minutes using docker compose. Feel free to test it and put some feedback. Thanks

---

> **gajo357** · 2026-05-04T12:23:56.000Z　
> Nice work. I had this issue as well, several times.Making a small project, needed a DB for quick proof oc concept."Proper" DBs are too expensive, free ones are bound with some random compute-unit mathematics. Everything self hosted takes time that I'd rather spend coding.

## 关联链接

- http://127.0.0.1:3000/api/auth/setup
- http://localhost:3000`

## 导航

- 项目页：[[10-项目/github.com_860ae52c]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
