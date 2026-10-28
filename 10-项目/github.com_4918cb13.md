---
type: "project"
title: "Show HN: Weir - Catch credential leaks in the AI agents you build and use"
project_url: "https://github.com/IdoGol24/weir"
first_seen: "2026-10-28T09:39:16+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_CodeNinja778
  - story_50261335
  - show_hn
lang: "en"
---

# Show HN: Weir - Catch credential leaks in the AI agents you build and use

> [!info] 一句话导读
> Hi HN. Weir is for one problem: credentials crossing the boundaries of your AI agent.For agents you build, Weir plants fake credentials where real ones would li…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/IdoGol24/weir>
> 首次收录：2026-10-28T09:39:16+08:00
> 来源渠道：HN Show HN
> 标签：author_CodeNinja778, story_50261335, show_hn
> 最新指标：点赞=3 · 评论=1 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-28T09:39:16+08:00 | HN Show HN | 点赞=3 · 评论=1 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-10-28/abc1b77a88fe0ceb_Show-HN-Weir-Catch-credential-leaks-in-the-AI-agen]] |

## 摘要正文

Hi HN. Weir is for one problem: credentials crossing the boundaries of your AI agent.For agents you build, Weir plants fake credentials where real ones would live, runs the agent's normal flows, and checks what comes out: telemetry, logs, console output, model requests, and requests to other services. It looks for those exact values, including common encoded forms, and reports where they went without printing the credential.pip install weir-scan weir canary judge --sampleThat sample shows a planted key leaking into a trace. On your own agent: pip install weir-run.For agents you use, Weir can inventory your real credentials (it stores keyed fingerprints, never the values) and show when one enters your session or leaves in a tool call. Right now, this is supported for Claude Code. Its optional hook redacts those known credentials from tool results before the model sees them. Setup is weir statusline setup, on Linux and macOS for now.So the two modes are deliberately different:Build: plant → run → prove where the credential went. Use: observe → warn → optionally redact before the model sees it.The test mode is deterministic and offline. On Linux it can also run the agent without outsi…
