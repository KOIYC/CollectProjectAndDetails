---
type: "project"
title: "Show HN: What sandboxing an AI coding agent in a VM costs"
project_url: "https://veloworkspaces.com/blog/vm-sandboxing-cost"
first_seen: "2026-09-20T09:36:52+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_michael_luog
  - story_49740053
  - show_hn
lang: "en"
---

# Show HN: What sandboxing an AI coding agent in a VM costs

> [!info] 一句话导读
> What Sandboxing an AI Coding Agent in a VM Actually Costs on Apple Silicon — Velo Workspaces

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://veloworkspaces.com/blog/vm-sandboxing-cost>
> 首次收录：2026-09-20T09:36:52+08:00
> 来源渠道：HN Show HN
> 标签：author_michael_luog, story_49740053, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/fa982e2264ff7f82_Show-HN-What-sandboxing-an-AI-coding-agent-in-a-VM]] |
| 2026-09-20T09:36:52+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/fa982e2264ff7f82_Show-HN-What-sandboxing-an-AI-coding-agent-in-a-VM]] |

## 摘要正文

What Sandboxing an AI Coding Agent in a VM Actually Costs on Apple Silicon — Velo Workspaces  # What Sandboxing an AI Coding Agent in a VM Actually Costs on Apple Silicon  I benchmarked the same sandboxing architecture against two different inference engines and got two different answers about what it costs under load. Both are real. Here's why they disagree, and why I'm showing you both instead of picking the one that sounds better.  ## The problem  Most people running an AI coding agent locally give it a `subprocess` or `exec()` call with full access to their filesystem, network, and credentials. Docker's own engineering blog has documented real incidents from exactly this. Indirect prompt injection makes it worse — a hostile instruction hidden in a file the agent reads can trigger commands with your full permissions, not just the ones you typed.  The "correct" fix is to run the agent in a VM. On Apple Silicon this runs into a real wall: `Virtualization.framework` doesn't expose the host GPU to a Linux guest. Confirmed directly by Apple's own container team when people asked for it. A Linux guest gets `virtio-gpu`, a paravirtualized 2D framebuffer with no path to the host's Metal…
