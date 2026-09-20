---
type: "corpus"
item_id: "514fe58e94a2a8a5"
title: "Show HN: BreachScanner – Check if your email has been in data breaches"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49768484"
project_url: "https://github.com/Aaronmike481/BreachScanner"
author: "thewalnut124"
published_at: "2026-09-19T17:30:14Z"
captured_at: "2026-09-20T09:48:16+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-20"
pub_day: "2026-09-19"
tags:
  - 语料
  - hn_show
  - author_thewalnut124
  - story_49768484
  - show_hn
metrics: {"points": 2, "comments": 3, "engagement_velocity": 2}
comments_count: 3
comments_total: 3
discovered_via: "hn:show_hn:3d"
---

# Show HN: BreachScanner – Check if your email has been in data breaches

> [!info] 一句话导读
> Aaronmike481/BreachScanner

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49768484>
> 指标：点赞=2 · 评论=3 · engagement_velocity=2
> 作者：thewalnut124　|　发布：2026-09-19T17:30:14Z
> 项目链接：<https://github.com/Aaronmike481/BreachScanner>
> 采集：2026-09-20T09:48:16+08:00　|　id：`514fe58e94a2a8a5`

## 正文

# Aaronmike481/BreachScanner

This tool checks if your email has been breached on the darkweb

- Stars: 1
- Forks: 0
- Watchers: 1
- Open issues: 0
- Default branch: main
- Created: 2026-09-19T16:19:53Z

## Languages

- Go

## Top Contributors

- mikeaaron1231-star (4 contributions)

---

## README

# 🔍 BreachScanner

A Go tool that checks if your email has been exposed in known data breaches.

## What It Does

- Takes an email address
- Checks against the HackMyIP breach API
- Reports: breach count, affected services, risk score, password exposure
- Generates personalized security recommendations

## Installation

```bash
git clone https://github.com/Aaronmike481/BreachScanner.git
cd BreachScanner
go mod tidy

# Marvy101/reader-source

## 评论（3/3）

> **drknownuffin** · 2026-09-19T18:06:14.000Z　
> Basically a wrapper around hackmyip, which is itself just reliant on the xposedornot db.

---

> **thewalnut124** · 2026-09-19T18:37:12.000Z　
> You're right — it's a wrapper. I picked HackMyIP because it was
> the easiest free API to start with, but you're correct that it
> sits on top of XposedOrNot.

---

> **thewalnut124** · 2026-09-19T18:42:38.000Z　
> I went with HackMyIP because its response includes a risk score and password breakdown, which made the output more useful. But you're right it just proxies XposedOrNot.

## 关联链接

- https://github.com/Aaronmike481/BreachScanner.git

## 导航

- 项目页：[[10-项目/github.com_d222331c]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
