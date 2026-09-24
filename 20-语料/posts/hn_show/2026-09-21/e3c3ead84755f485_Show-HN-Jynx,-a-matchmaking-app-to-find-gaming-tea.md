---
type: "corpus"
item_id: "e3c3ead84755f485"
title: "Show HN: Jynx, a matchmaking app to find gaming teammates"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48336119"
project_url: "https://jynx.app/"
author: "akiro____"
published_at: "2026-05-30T13:45:34Z"
captured_at: "2026-09-22T13:13:21+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-05-30"
tags:
  - 语料
  - hn_show
  - author_akiro____
  - story_48336119
  - show_hn
metrics: {"points": 5, "comments": 3, "engagement_velocity": 5}
comments_count: 2
comments_total: 3
discovered_via: "hn:show_hn:144d"
---

# Show HN: Jynx, a matchmaking app to find gaming teammates

> [!info] 一句话导读
> TL;DR: Jynx is a gaming social platform that matches you with compatible teammates based on skill level, play style and schedule. Swipe to find players (Tinder-…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48336119>
> 指标：点赞=5 · 评论=3 · engagement_velocity=5
> 作者：akiro____　|　发布：2026-05-30T13:45:34Z
> 项目链接：<https://jynx.app/>
> 采集：2026-09-22T13:13:21+08:00　|　id：`e3c3ead84755f485`

## 正文

TL;DR: Jynx is a gaming social platform that matches you with compatible teammates based on skill level, play style and schedule. Swipe to find players (Tinder-style), create or join game sessions (LFG), chat, and build your squad. 214k lines of Dart, 23 feature modules, built entirely with Claude Code as my entry into agentic engineering.Live on App Store and Play Store:
https://play.google.com/store/apps/details?id=app.jynx
https://apps.apple.com/fr/app/jynx-where-gaming-gets-social/...---Hi HN, long time lurker, first time poster, be gentle.Developer by day, vibe coder by night: Jynx is the project I used to ease into agentic engineering.AI talks are mitigated, at best. But I'll talk about my experience here. Forgive my erratic style, it is what it is.Working with Claude from the very beginning, it's been a blast. I had the "chance" to have the time necessary to learn and use AI a lot. Lots of different techniques that quickly became completely obsolete today.Without LLMs, it would have been extremely hard to have the same app than I have today. I used Flutter (Dart) to avoid having to dev and maintain two codebases. It is not a language I knew. Learning the language first would have severely hindered the process.For me, from copy/paste to using MCP then Roo Code, then Claude Code was an ecstatic process. I always loved having ideas but the time it would take me to build the thing and test it always felt too long. Not anymore.So we carefully designed, iterated and implemented the two codebases for Jynx. One for the flutter app, one for the firebase backend. I chose Firebase to avoid having to maintain a server and be able to focus on the UI/UX of the app.We started thinking about it in December 2024 and started devs early 2025; not working on it full time at all. We really poured our heart into it and we truly tried to make it as secure as possible. Even though we mean business, it is a passion project. By using the excuse of learning agentic flows, I took the time to inspect each aspects of the app's systems thoroughly.Tech stack:
- Flutter 3.41 / Dart 3.11 (single codebase, iOS + Android)
- Firebase (Firestore, Cloud Functions in TypeScript, Auth, Storage, FCM)
- Riverpod 3.1 + Freezed + json_serializable for state management & immutable models
- Drift for encrypted local SQLite caching (offline-first architecture to optimize Firebase costs)
- Clean Architecture with feature modules and mixin-based repositories
- Sentry + Firebase Crashlytics for production error reporting
- Freerasp for runtime app self-protection (tamper detection, root/jailbreak)Agentic engineering artifacts:
- Claude Code (Claude + GLM) as primary coding agent
- 22 hooks, 18 skills, 13 instincts, 8 rule files, custom subagents, slash commands, MCP servers and plugins (instincts system from Affaan's https://github.com/affaan-m/everything-claude-code)
- GitNexus
- MemPalace for persistent context across sessionsStats: 1,239 Dart files, 214k lines of code (excluding generated boilerplate), 30k lines of comments across the Flutter codebase.I made a detailed cheatsheet document about my whole setup if you want it. I could post it or you DM me.If you have questions, ask away, I'll gladly answer.Test it and tell me what you think of it honestly, I won't get offended!Take care,
Antoine

## 评论（2/3）

> **tom-wal** · 2026-05-30T15:16:32.000Z　
> Great project.
> | Good:
> * Confirmation email didn't land in spam
> * Easy setup
> * Lightweight app, quick install
> | Improvements:
> * Add a large default gallery of profile portraits matching the app's style (manga characters)
> * Improve onboarding navigation consistency; avoid flows that go right, then left
> * Older users like me may not be familiar with Tinder-style swipe actions; a quick tutorial/modal would help
> * Ensure every game has a logo image
> * Default username should not be derived from the email address

---

> **akiro____** · 2026-05-30T17:35:55.000Z　
> It means a lot you took the time to test it.
> I thought about implementing a quick tutorial whenever users land for the first time on a feature, that's definitely coming soon.
> Thank you for the feedback, I'll get around to it

## 关联链接

- https://apps.apple.com/fr/app/jynx-where-gaming-gets-social/...---Hi
- https://github.com/affaan-m/everything-claude-code
- https://play.google.com/store/apps/details?id=app.jynx

## 导航

- 项目页：[[10-项目/jynx.app_147d821e]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
