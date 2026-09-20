---
type: "project"
title: "Show HN: Interakt – open-source self-hosted search and AI chat for your website"
project_url: "https://github.com/alphasolutionsrepo/interakt"
first_seen: "2026-09-20T14:03:45+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_interakt
  - story_49732963
  - show_hn
lang: "en"
---

# Show HN: Interakt – open-source self-hosted search and AI chat for your website

> [!info] 一句话导读
> alphasolutionsrepo/interakt

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/alphasolutionsrepo/interakt>
> 首次收录：2026-09-20T14:03:45+08:00
> 来源渠道：HN Show HN
> 标签：author_interakt, story_49732963, show_hn
> 最新指标：点赞=2 · 评论=1 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=2 · 评论=1 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/10aae03ccb7c0805_Show-HN-Interakt-–-open-source-self-hosted-search]] |
| 2026-09-20T09:36:57+08:00 | HN Show HN | 点赞=2 · 评论=1 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/10aae03ccb7c0805_Show-HN-Interakt-–-open-source-self-hosted-search]] |
| 2026-09-20T14:03:33+08:00 | HN Show HN | 点赞=2 · 评论=1 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/10aae03ccb7c0805_Show-HN-Interakt-–-open-source-self-hosted-search]] |
| 2026-09-20T14:03:45+08:00 | HN Show HN | 点赞=2 · 评论=1 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/10aae03ccb7c0805_Show-HN-Interakt-–-open-source-self-hosted-search]] |

## 摘要正文

# alphasolutionsrepo/interakt  - Stars: 8 - Forks: 1 - Watchers: 8 - Open issues: 2 - License: MIT License - Homepage: https://interakt.app - Default branch: main - Created: 2026-06-01T20:51:42Z  ## Languages  - CSS - Dockerfile - JavaScript - Shell - TypeScript  ## Top Contributors  - naalpha (20 contributions) - alpharv (4 contributions) - hjaAlpha (1 contributions)  ---  ## README  # Interakt — Local Developer Setup  AI-powered search and chat platform. This README gets a new developer running the full stack locally — backend admin/API + demo site — and walks through first-boot configuration.  📖 **Documentation:** docs.interakt.app  ## Repo layout  ``` interakt/ ├── backend/      # Admin dashboard + REST APIs (Next.js, Drizzle, Postgres + Elasticsearch) │   └── infra/    # docker-compose for local Postgres + Elasticsearch └── demo-site/    # Example consumer app built against the Interakt APIs (Next.js) ```  Both apps are Next.js. Backend runs on **3000**, demo-site on **3001**.  ## Prerequisites  - Node.js 24 LTS (see `.nvmrc`) - Docker + Docker Compose (for local Postgres + Elasticsearch)  ## 1. Backend  ```bash cd backend  # Runtime config — fill in the three openssl-generate…
