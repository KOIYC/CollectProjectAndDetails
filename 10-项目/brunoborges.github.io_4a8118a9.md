---
type: "project"
title: "Show HN: Ghx – A caching proxy for GitHub CLI, built for AI agents"
project_url: "https://brunoborges.github.io/ghx"
first_seen: "2026-10-16T09:35:18+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_brunoborges
  - story_50105322
  - show_hn
lang: "en"
---

# Show HN: Ghx – A caching proxy for GitHub CLI, built for AI agents

> [!info] 一句话导读
> ⚡ Built for AI agent workflows

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://brunoborges.github.io/ghx>
> 首次收录：2026-10-16T09:35:18+08:00
> 来源渠道：HN Show HN
> 标签：author_brunoborges, story_50105322, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-16T09:35:18+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-10-16/d77feccb36fed5cd_Show-HN-Ghx-–-A-caching-proxy-for-GitHub-CLI,-buil]] |

## 摘要正文

⚡ ghx Features  How It Works  Install  gh Shim  Agent Plugin  Security  Docs GitHub ⚡ Built for AI agent workflows Stop hitting  GitHub rate limits A caching proxy for the GitHub CLI that makes repeated commands instant.  Singleflight coalescing means 10 agents asking the same thing triggers just 1 API call. Get Started  View on GitHub Why ghx? 🚀 10x Faster Cached responses return in ~0.1s instead of ~1s. Your scripts and agents feel instant. 🔄 Singleflight Coalescing Five agents requesting the same PR list simultaneously? Only one API call is made. All five get the result. 🎯 Allowlist-Based Only known-safe read-only commands are cached. Mutations pass through directly and invalidate related cache entries. 🔌 Drop-In Replacement Just use ghx instead of gh . The daemon auto-starts. No configuration needed. 📊 Built-In Dashboard Real-time web dashboard shows hit rates, per-command stats, and a live request log. Helps you tune your TTL. 🛡️ Safe by Design Context-aware cache keys prevent cross-repo collisions. Unix socket with strict permissions. No tokens stored. How It Works Agent 1 ghx Agent 2 ghx Agent 3 ghx IPC ghxd daemon Cache  Singleflight  Metrics exec gh GitHub CLI 1 You run gh…
