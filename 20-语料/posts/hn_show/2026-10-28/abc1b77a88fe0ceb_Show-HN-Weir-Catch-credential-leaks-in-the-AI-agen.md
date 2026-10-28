---
type: "corpus"
item_id: "abc1b77a88fe0ceb"
title: "Show HN: Weir - Catch credential leaks in the AI agents you build and use"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50261335"
project_url: "https://github.com/IdoGol24/weir"
author: "CodeNinja778"
published_at: "2026-10-27T16:07:29Z"
captured_at: "2026-10-28T09:39:16+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-28"
pub_day: "2026-10-27"
tags:
  - 语料
  - hn_show
  - author_CodeNinja778
  - story_50261335
  - show_hn
metrics: {"points": 3, "comments": 1, "engagement_velocity": 3}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Weir - Catch credential leaks in the AI agents you build and use

> [!info] 一句话导读
> Hi HN. Weir is for one problem: credentials crossing the boundaries of your AI agent.For agents you build, Weir plants fake credentials where real ones would li…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50261335>
> 指标：点赞=3 · 评论=1 · engagement_velocity=3
> 作者：CodeNinja778　|　发布：2026-10-27T16:07:29Z
> 项目链接：<https://github.com/IdoGol24/weir>
> 采集：2026-10-28T09:39:16+08:00　|　id：`abc1b77a88fe0ceb`

## 正文

Hi HN. Weir is for one problem: credentials crossing the boundaries of your AI agent.For agents you build, Weir plants fake credentials where real ones would live, runs the agent's normal flows, and checks what comes out: telemetry, logs, console output, model requests, and requests to other services. It looks for those exact values, including common encoded forms, and reports where they went without printing the credential.pip install weir-scan
weir canary judge --sampleThat sample shows a planted key leaking into a trace. On your own agent: pip install weir-run.For agents you use, Weir can inventory your real credentials (it stores keyed fingerprints, never the values) and show when one enters your session or leaves in a tool call. Right now, this is supported for Claude Code. Its optional hook redacts those known credentials from tool results before the model sees them. Setup is weir statusline setup, on Linux and macOS for now.So the two modes are deliberately different:Build: plant → run → prove where the credential went.
Use: observe → warn → optionally redact before the model sees it.The test mode is deterministic and offline. On Linux it can also run the agent without outside network access, so direct exfiltration attempts are caught. If a required path wasn't exercised, Weir reports incomplete, never clean.It doesn't try to detect every possible secret. It matches known whole values, so hashed, split, truncated, or otherwise transformed credentials aren't covered. The Claude Code hook only protects the tool-result boundary: it can't undo a credential already pasted into the conversation, and a failed command's output reaches the model as is.Apache-2.0, no model in the loop, and Weir itself sends nothing anywhere. It found GHSA-j7qq-vr8c-xvw3 in MLflow (fixed in 3.17.0).Built with AI assistance; every security finding was reproduced before I reported it.

## 评论（1/1）

> **CarryOn1212** · 2026-10-27T16:11:02.000Z　
> Awesome tool! Really liked that status line. Definitely going to give it a go. Will you also support Codex?

## 导航

- 项目页：[[10-项目/github.com_4918cb13]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
