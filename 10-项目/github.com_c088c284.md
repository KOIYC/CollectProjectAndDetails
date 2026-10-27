---
type: "project"
title: "Show HN: Tinyjobs – Python background jobs and cron on SQLite, optional brokers"
project_url: "https://github.com/Piergiuseppe/tinyjobs"
first_seen: "2026-10-27T23:46:32+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_TheBuc
  - story_50257479
  - show_hn
lang: "en"
---

# Show HN: Tinyjobs – Python background jobs and cron on SQLite, optional brokers

> [!info] 一句话导读
> Piergiuseppe/tinyjobs

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/Piergiuseppe/tinyjobs>
> 首次收录：2026-10-27T23:46:32+08:00
> 来源渠道：HN Show HN
> 标签：author_TheBuc, story_50257479, show_hn
> 最新指标：点赞=2 · 评论=2 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-27T23:46:32+08:00 | HN Show HN | 点赞=2 · 评论=2 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-10-27/74fad5d068ccb047_Show-HN-Tinyjobs-–-Python-background-jobs-and-cron]] |

## 摘要正文

# Piergiuseppe/tinyjobs  Background jobs and cron for Python, on SQLite, with zero dependencies  - Stars: 0 - Forks: 0 - Watchers: 0 - Open issues: 0 - License: MIT License - Homepage: https://pypi.org/project/tinyjobs/ - Default branch: main - Created: 2026-09-01T15:32:29Z  ## Languages  - Lua - Python  ## Topics  - background-jobs - background-jobs-processing - background-jobs-python - cron - cronjob - cronjob-scheduler - job-queue - job-queue-management - job-queues - python - scheduled-jobs - scheduled-tasks - scheduler - scheduling - sqlite - task-queue - task-queues - worker - worker-pool  ## Top Contributors  - Piergiuseppe (36 contributions)  ---  ## README  # tinyjobs  PyPI Downloads  Background jobs and cron for Python, backed by SQLite, with no dependencies.  ```bash pip install tinyjobs ```  That's the whole setup. No broker, no result backend, no daemon. The queue is a file.  Celery is the right tool for a lot of systems, but it asks for a Redis or RabbitMQ instance before it will run a single job. This is for the projects that never needed that: a Django app that sends emails, a scraper with a nightly refresh, a CLI that offloads slow work. When you outgrow SQLite you…
