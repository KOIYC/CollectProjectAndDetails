---
type: "project"
title: "Show HN: Co-mment, drop-in visual commenting for staging sites"
project_url: "https://co-mment.com/"
first_seen: "2026-09-20T09:36:52+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_endtwist
  - story_49740817
  - show_hn
lang: "en"
---

# Show HN: Co-mment, drop-in visual commenting for staging sites

> [!info] 一句话导读
> co-mment: collaborative visual feedback for the web

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://co-mment.com/>
> 首次收录：2026-09-20T09:36:52+08:00
> 来源渠道：HN Show HN
> 标签：author_endtwist, story_49740817, show_hn
> 最新指标：点赞=4 · 评论=0 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-20/22940441f4f6fc61_Show-HN-Co-mment,-drop-in-visual-commenting-for-st]] |
| 2026-09-20T09:36:52+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-20/22940441f4f6fc61_Show-HN-Co-mment,-drop-in-visual-commenting-for-st]] |

## 摘要正文

co-mment: collaborative visual feedback for the web  # Collaborative visual feedback for the web.  Click anywhere, drop a pin, write feedback. No account, no extension, no “third section from the top” email. Two steps in React, one tag without a bundler, or one prompt to your coding agent.  Live demo: this widget is real. What you leave stays in your browser, visible only to you.  That’s the whole install  app/layout.tsx  ``` # 1. install npm install @planetary/co-mment  # 2. add near your app root, behind a check that keeps it off in productionCopy snippetimport { Comment } from "@planetary/co-mment";  {process.env.NEXT_PUBLIC_VERCEL_ENV !== "production" && (   <Comment projectKey="cmt_pk_..." /> )} ```  Or let your coding agent do it. The prompt has the install command, the production check, the origin allowlist, and how to verify it worked.  ## From “this button looks off” to a shipped fix  Feedback starts as a pin on the actual page and ends as a resolved thread, an agent prompt, or a Linear ticket, with the element, the viewport, and the browser carried along the whole way.  ## Dense where it counts  Anchoring intelligence  Pins attach to the element under the click, capturing…
