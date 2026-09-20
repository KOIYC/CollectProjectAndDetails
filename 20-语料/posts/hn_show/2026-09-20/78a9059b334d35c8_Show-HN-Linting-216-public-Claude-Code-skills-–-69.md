---
type: "corpus"
item_id: "78a9059b334d35c8"
title: "Show HN: Linting 216 public Claude Code skills – 69% won't reliably trigger"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49744398"
project_url: "https://skillcrossroads.com/"
author: "sgharlow"
published_at: "2026-09-17T18:06:26Z"
captured_at: "2026-09-20T09:36:48+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-17"
tags:
  - 语料
  - hn_show
  - author_sgharlow
  - story_49744398
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: Linting 216 public Claude Code skills – 69% won't reliably trigger

> [!info] 一句话导读
> Skill Crossroads — Know before you ship.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49744398>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：sgharlow　|　发布：2026-09-17T18:06:26Z
> 项目链接：<https://skillcrossroads.com/>
> 采集：2026-09-20T09:36:48+08:00　|　id：`78a9059b334d35c8`

## 正文

Skill Crossroads — Know before you ship.

# Every skill hits a crossroads before you ship it.

Skill Crossroads grades your Claude Code skills, agents, slash commands, MCP configs, and plugins against an evidence-based rubric — then points you one of three ways: ship, fix, or rethink.

Not on GitHub? Paste a SKILL.md — or scan locally: `npx skillcrossroads ./my-skill`

## A grade is a direction, not a gold star.

Ship A / B

Your artifact is solid. Embed the badge and release with confidence.

Fix C / D

Close, but Skill Crossroads found specific problems — each with the file and line to change.

Rethink F

Deeper issues: it will not trigger, is not safe, or has no way to prove it works.

## How it works

1. 1

### Point Skill Crossroads at your artifact.

`npx skillcrossroads ./my-skill`, a repo URL, or your CI.
2. 2

### It runs the rubric.

Fast deterministic checks plus AI-assisted review across six categories — every finding cited to a file and line.
3. 3

### You get a scorecard, a badge, and a fix list.

Ranked by how much each fix raises your grade.

### Correctness & Structure

Valid frontmatter and manifest, resolvable references, nothing pointing at files that do not exist.

### Triggering & Discoverability

Will the model actually invoke it? The number-one reason good skills look broken.

### Clarity & Instructions

Unambiguous, contradiction-free, and phrased as standing instructions.

### Token & Context Cost

What it costs every turn, and whether it uses progressive disclosure.

### Safety & Security

Over-broad tool grants, injection surface, and secrets that should not be there.

### Verifiability & Maintainability

Are there real evals, or tests that only grep the source?

## Receipts, not vibes.

Every finding cites the file and line, and shows what your artifact claims versus what Skill Crossroads could verify. No hype, no false confidence — Skill Crossroads will tell you when your own skill scores a C, and exactly why.

SKILL.md:1 claimed “fires on notes” → verified: under-triggers

Description too generic to fire reliably.

Fix: lead with the use case, add trigger phrases. +14 → A−

## Put the signpost in your README.

One line embeds your Skill Crossroads badge. Anyone who sees it can click through to the full, evidence-cited scorecard — and run their own. Good work gets shown; the badge does the rest.

```
[![Skill Crossroads: A−](https://skillcrossroads.com/api/badge/OWNER/REPO.svg)](https://skillcrossroads.com/s/OWNER/REPO)
```

### Free

Scan public artifacts and local files, full rubric, local badge, CI GitHub Action + PR gating. This is the whole tool, in the open.

### Pro

Private repos, hosted always-fresh badges, score history, managed AI checks.

### Team

Org-wide custom rules, seats for your team, shared dashboards.

Free covers everything you need to grade and share a public skill.

## The State of Claude Code Skills.

Skill Crossroads publishes evidence-based reports on what actually makes real skills pass or fail across the ecosystem.

## 关联链接

- https://skillcrossroads.com/api/badge/OWNER/REPO.svg
- https://skillcrossroads.com/s/OWNER/REPO

## 导航

- 项目页：[[10-项目/skillcrossroads.com_53f62e72]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
