---
type: "corpus"
item_id: "bdcaa2c6cd8b9bb0"
title: "Show HN: Ear Training Exercise"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49737154"
project_url: "https://clarena.app/app/try"
author: "AlexFromClarena"
published_at: "2026-09-17T06:35:38Z"
captured_at: "2026-09-20T09:36:55+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-17"
tags:
  - 语料
  - hn_show
  - author_AlexFromClarena
  - story_49737154
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: Ear Training Exercise

> [!info] 一句话导读
> Clarena

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49737154>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：AlexFromClarena　|　发布：2026-09-17T06:35:38Z
> 项目链接：<https://clarena.app/app/try>
> 采集：2026-09-20T09:36:55+08:00　|　id：`bdcaa2c6cd8b9bb0`

## 正文

Clarena · Cognitive Practice

 // Honor OS dark-mode preference. Inline + synchronous so the dark
 // palette is applied BEFORE first paint, preventing a light-flash on
 // dark-preferring devices. Reviewer Sonnet 4.6 caught that the dark
 // CSS in index.css was previously dead code (no theme switcher).
 (function () {
 try {
 var saved = localStorage.getItem('clarena-theme');
 var prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
 var theme = saved === 'dark' || saved === 'light'
 ? saved
 : (prefersDark ? 'dark' : 'light');
 document.documentElement.setAttribute('data-theme', theme);
 } catch (_) {
 // localStorage may be unavailable in private browsing — fall
 // through to default (light) gracefully.
 }
 })();

## 导航

- 项目页：[[10-项目/clarena.app_6789d958]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
