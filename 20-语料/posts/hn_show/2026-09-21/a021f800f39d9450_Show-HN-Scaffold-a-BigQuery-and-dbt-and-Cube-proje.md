---
type: "corpus"
item_id: "a021f800f39d9450"
title: "Show HN: Scaffold a BigQuery and dbt and Cube project an AI agent can operate"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48733674"
project_url: "https://cli.revos.dev/"
author: "zubairov"
published_at: "2026-06-30T15:00:04Z"
captured_at: "2026-09-21T02:53:02+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-06-30"
tags:
  - 语料
  - hn_show
  - author_zubairov
  - story_48733674
  - show_hn
metrics: {"points": 8, "comments": 3, "engagement_velocity": 8}
comments_count: 3
comments_total: 3
discovered_via: "hn:show_hn:113d"
---

# Show HN: Scaffold a BigQuery and dbt and Cube project an AI agent can operate

> [!info] 一句话导读
> Skip to main content

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48733674>
> 指标：点赞=8 · 评论=3 · engagement_velocity=8
> 作者：zubairov　|　发布：2026-06-30T15:00:04Z
> 项目链接：<https://cli.revos.dev/>
> 采集：2026-09-21T02:53:02+08:00　|　id：`a021f800f39d9450`

## 正文

Skip to main content
RevOS CLI Docs
 Platform Docs Website
Getting Started
 Concepts
 Installation
 Authentication
 Configuration
 Project Scaffolding (init)
Resources
Raw API access
 Tutorials
Getting Started
 On this page
 RevOS CLI
Command-line interface for managing RevOS resources — tables, scores, segments, actions, cubes, organizations, and more.
Quick Start ​
# Install
npm install -g @revos/cli
# Login via browser
revos auth login
# Check your organizations
revos org list
# Initialize a new data project
revos init my-project
What You Can Do ​
Authenticate — Browser-based OAuth login, token-based auth for CI/CD
Manage Organizations — List, switch, and inspect orgs
Manage Resources — CRUD tables, scores, segments, actions, AI instructions, and service accounts
Manage Cubes & Pipelines via IaC — Declare Connections and Cubes as YAML; reconcile with revos apply , inspect with revos diff and revos status
Scaffold Projects — Generate data engineering projects with medallion layout, Dev Containers, dbt, and AI companion files
Next Steps ​
From Zero to Semantic Model — End-to-end walkthrough using a real dataset
Installation — Install and verify the CLI
Authentication — Set up your credentials
Configuration — Global options and environment variables
Next
 Concepts
Quick Start
 What You Can Do
 Next Steps
Copyright © 2026 RevOS GmbH.

## 评论（3/3）

> **pnedelko** · 2026-06-30T15:33:28.000Z　
> One of the authors here — happy to answer anything.The short version: we built this for ourselves and our clients. When building data engineering projects, we wanted proper declarative config instead of click-ops and hand-rolled scripts that drift from reality the moment someone touches the UI. It's been a real productivity boost — everything's already set up and ready to go. Because the config is declarative, an LLM can read all of it easily and then verify the result, since the tools are already at hand. That's what makes the output solid.It turned out pretty well, so we figured we'd share it. It's still early, and I'd genuinely like to hear where the model breaks for your workflows.

---

> **virolainenolha** · 2026-06-30T15:34:28.000Z　
> Is Claude Code a hard requirement here, or can I point any agent at the scaffolded project?

---

> **pnedelko** · 2026-06-30T16:36:17.000Z　
> For now we've focused mostly on Claude. It should work with other agents too, but you'd likely need to do a bit of tweaking — adjusting skills, plugins, that kind of thing. Happy to help with that if you run into anything.

## 导航

- 项目页：[[10-项目/cli.revos.dev_fe750ea5]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
