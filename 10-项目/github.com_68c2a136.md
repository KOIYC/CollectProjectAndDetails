---
type: "project"
title: "l-desantis/dev-trend"
project_url: "https://github.com/l-desantis/dev-trend"
first_seen: "2026-09-20T09:36:30+08:00"
sources:
  - github_new
tags:
  - 项目
  - github_new
  - HTML
  - topic:indie-hacker
lang: "en"
---

# l-desantis/dev-trend

> [!info] 一句话导读
> v4.D — Stable production.** Identity resolution calibrated for NVIDIA NIM embeddings, lifecycle fixes applied, and daily digest evolution restored.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/l-desantis/dev-trend>
> 首次收录：2026-09-20T09:36:30+08:00
> 来源渠道：GitHub 新星仓库
> 标签：HTML, topic:indie-hacker
> 最新指标：stars=2 · forks=0 · open_issues=0

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:24:07+08:00 | GitHub 新星仓库 | stars=2 · forks=0 · open_issues=0 | [[20-语料/posts/github_new/2026-09-20/68c2a136a39796de_l-desantis-dev-trend]] |
| 2026-09-20T09:36:30+08:00 | GitHub 新星仓库 | stars=2 · forks=0 · open_issues=0 | [[20-语料/posts/github_new/2026-09-20/68c2a136a39796de_l-desantis-dev-trend]] |

## 摘要正文

# DevTrend  > **v4.D — Stable production.** Identity resolution calibrated for NVIDIA NIM embeddings, lifecycle fixes applied, and daily digest evolution restored.  [![Python](https://img.shields.io/badge/Python-3.11+-3776ab?style=flat-square&logo=python&logoColor=white)](https://python.org) [![License](https://img.shields.io/badge/license-Apache%20License%202.0-blue)](LICENSE) [![Tests](https://img.shields.io/badge/tests-pytest-green?style=flat-square)](tests/)  An **opportunity discovery engine** for indie developers. DevTrend continuously ingests developer chatter (Reddit, HN, GitHub, Play Store reviews), extracts pain-points via LLM, clusters them into app-opportunity hypotheses, scores them, and delivers the top candidates via a Telegram-first interface — no editorial curation required.  ---  ## What it is  DevTrend is a **staged pipeline monolith driven by a scheduler** — not a microservice system. Ingestion connectors write `SourceItem` rows; the pipeline then runs as an ordered sequence of stages (extract → embed → identity-resolve → cluster → label), followed by scoring, GitHub validation and Telegram delivery. APScheduler orchestrates ingestion, the pipeline, scoring, the…
