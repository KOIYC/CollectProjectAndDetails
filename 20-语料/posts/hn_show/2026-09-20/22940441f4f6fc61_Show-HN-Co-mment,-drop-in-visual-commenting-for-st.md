---
type: "corpus"
item_id: "22940441f4f6fc61"
title: "Show HN: Co-mment, drop-in visual commenting for staging sites"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49740817"
project_url: "https://co-mment.com/"
author: "endtwist"
published_at: "2026-09-17T13:55:37Z"
captured_at: "2026-09-20T09:36:52+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-17"
tags:
  - 语料
  - hn_show
  - author_endtwist
  - story_49740817
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: Co-mment, drop-in visual commenting for staging sites

> [!info] 一句话导读
> co-mment: collaborative visual feedback for the web

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49740817>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：endtwist　|　发布：2026-09-17T13:55:37Z
> 项目链接：<https://co-mment.com/>
> 采集：2026-09-20T09:36:52+08:00　|　id：`22940441f4f6fc61`

## 正文

co-mment: collaborative visual feedback for the web

# Collaborative visual feedback for the web.

Click anywhere, drop a pin, write feedback. No account, no extension, no “third section from the top” email. Two steps in React, one tag without a bundler, or one prompt to your coding agent.

Live demo: this widget is real. What you leave stays in your browser, visible only to you.

That’s the whole install

app/layout.tsx

```
# 1. install
npm install @planetary/co-mment

# 2. add near your app root, behind a check that keeps it off in productionCopy snippetimport { Comment } from "@planetary/co-mment";

{process.env.NEXT_PUBLIC_VERCEL_ENV !== "production" && (
  <Comment projectKey="cmt_pk_..." />
)}
```

Or let your coding agent do it. The prompt has the install command, the production check, the origin allowlist, and how to verify it worked.

## From “this button looks off” to a shipped fix

Feedback starts as a pin on the actual page and ends as a resolved thread, an agent prompt, or a Linear ticket, with the element, the viewport, and the browser carried along the whole way.

## Dense where it counts

Anchoring intelligence

Pins attach to the element under the click, capturing a selector chain, offsets, and a text fingerprint. They survive redeploys and honestly flag drift instead of silently lying.

Screenshots built in

Every comment captures the pinned area automatically. Stored privately, served through short-lived signed URLs to project members only.

One Inbox for everything

Every comment across the project in a single stream. Filter by page, status, commenter, viewport, or browser, with per-editor unread state.

Threads export as structured, agent-ready prompts. Each one has the page, the element, the viewport, and the ask, written for Claude Code, Cursor, or any coding agent.

Linear in one click

Connect a team and any thread becomes a Linear issue with the agent-copy description and the screenshot attached.

Email claim, no passwords

Commenters just type a name and email. The confirmation email doubles as a claim link that keeps their identity across devices and projects.

## Ship the widget before your next review call

Error fetching https://lurescope.com/stats: CRAWL_LIVECRAWL_TIMEOUT

## 关联链接

- https://lurescope.com/stats:

## 导航

- 项目页：[[10-项目/co-mment.com_51d227f6]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
