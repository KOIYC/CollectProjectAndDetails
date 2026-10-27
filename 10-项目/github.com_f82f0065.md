---
type: "project"
title: "Show HN: Ulak – Run Docker without a local Docker daemon"
project_url: "https://github.com/syy/ulak"
first_seen: "2026-10-27T23:46:32+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_xorxor
  - story_50256831
  - show_hn
lang: "en"
---

# Show HN: Ulak – Run Docker without a local Docker daemon

> [!info] 一句话导读
> Run a local compose project's Docker workloads on a server you control

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/syy/ulak>
> 首次收录：2026-10-27T23:46:32+08:00
> 来源渠道：HN Show HN
> 标签：author_xorxor, story_50256831, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-27T23:46:32+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-10-27/5eabde14fb7c03cf_Show-HN-Ulak-–-Run-Docker-without-a-local-Docker-d]] |

## 摘要正文

# syy/ulak  Run a local compose project's Docker workloads on a server you control  - Stars: 5 - Forks: 0 - Watchers: 5 - Open issues: 0 - License: Apache License 2.0 - Default branch: main - Created: 2026-09-07T07:43:06Z  ## Languages  - Dockerfile - Python - Rust - Shell  ## Topics  - compose - docker - rsync - ssh  ## Top Contributors  - syy (61 contributions)  ---  ## README  # Ulak  CI crates.io license  Run the Docker workloads for a local project on a server you control.  A Mac with no Docker runs ulak docker compose up -d on demo-server, opens the app on localhost:8525, edits a page that goes live on the server, then opens ulak ui  Ulak keeps your editor and source checkout on your computer. It synchronizes the files that Docker needs, runs Docker commands over SSH, and forwards published ports back to `localhost`. Builds and containers use the CPU, memory, disk, and architecture of the server.  You do not need a local Docker daemon or Docker Desktop. Ulak itself installs nothing on the server and opens no network port there.  ```text local checkout  ⇄  sync over SSH   ⇄  remote workspace                                              │                                        …
