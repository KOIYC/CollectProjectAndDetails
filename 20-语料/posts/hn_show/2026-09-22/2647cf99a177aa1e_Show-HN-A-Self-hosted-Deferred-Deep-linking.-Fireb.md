---
type: "corpus"
item_id: "2647cf99a177aa1e"
title: "Show HN: A Self-hosted Deferred Deep linking. Firebase dynamic link model"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49793476"
project_url: "https://github.com/Newtdev/blynk-deferlink"
author: "NewtDev"
published_at: "2026-09-21T21:10:11Z"
captured_at: "2026-09-22T12:53:31+08:00"
lang: "en"
kind: "post"
topic: "未分类"
shard: "2026-09-22"
pub_day: "2026-09-21"
tags:
  - 语料
  - hn_show
  - author_NewtDev
  - story_49793476
  - show_hn
metrics: {"points": 2, "comments": 1, "engagement_velocity": 2}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: A Self-hosted Deferred Deep linking. Firebase dynamic link model

> [!info] 一句话导读
> Show HN: A Self-hosted Deferred Deep linking. Firebase dynamic link model

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49793476>
> 指标：点赞=2 · 评论=1 · engagement_velocity=2
> 作者：NewtDev　|　发布：2026-09-21T21:10:11Z
> 项目链接：<https://github.com/Newtdev/blynk-deferlink>
> 采集：2026-09-22T12:53:31+08:00　|　id：`2647cf99a177aa1e`

## 正文

Show HN: A Self-hosted Deferred Deep linking. Firebase dynamic link model

## 评论（1/1）

> **NewtDev** · 2026-09-21T21:11:05.000Z　
> Sometime around December 2025, I was tasked to build a referral system for Sparkle Nigeria(MFB). The referral system allows user to share their referral link with a code embedded in it and once the app is installed the code is retrieved and auto populated. The classic deferred deep linking! The solution, of course, Firebase dynamic link as been deprecated. Branch and Appflyer were an overkill. So I decided to build Blynk deferred link- a self-hosted deferred half of FDL.The two main approach: Deterministic and Probabilistic(fallback)Android: Play install referrer,100% Deterministic.
> iOS: Clipboard hand-off via UIPasteControl, 100% Deterministic, but needs a user tap- Apple won't let you read the clipboard silently.Fallback(Probabilistic): a scored fingerprint match (IP,device model, screen, timezone, language, recency) against recent clicks. ~85-90% on iOS.I included a doc/decisions.md file and comprehensive readMe file. The decision.md contains all the decisions made during development, with links to researched articles.Blynk deferred link is running in production at sparkle.ng. I also included a demo to help developer understand how Blynk deferred link works.

## 导航

- 项目页：[[10-项目/github.com_91676a3d]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`未分类`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
