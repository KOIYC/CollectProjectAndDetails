---
type: "project"
title: "Show HN: Thaw – Git branch for a running LLM (fork agents, skip prefill)"
project_url: "https://github.com/thaw-ai/thaw"
first_seen: "2026-09-21T02:52:49+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_nilsmatteson
  - story_48341069
  - show_hn
lang: "en"
---

# Show HN: Thaw – Git branch for a running LLM (fork agents, skip prefill)

> [!info] 一句话导读
> git for live agent sessions: snapshot, branch, and diff a running vLLM/SGLang session as a durable file. inspect & diff on a laptop, no GPU; restore skips prefi…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/thaw-ai/thaw>
> 首次收录：2026-09-21T02:52:49+08:00
> 来源渠道：HN Show HN
> 标签：author_nilsmatteson, story_48341069, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:27:24+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-21/a765b68d0360b067_Show-HN-Thaw-–-Git-branch-for-a-running-LLM-(fork]] |
| 2026-09-21T02:52:49+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-21/a765b68d0360b067_Show-HN-Thaw-–-Git-branch-for-a-running-LLM-(fork]] |

## 摘要正文

# thaw-ai/thaw  git for live agent sessions: snapshot, branch, and diff a running vLLM/SGLang session as a durable file. inspect & diff on a laptop, no GPU; restore skips prefill. Rust + CUDA, Apache-2.0. pip install thaw-vllm  - Stars: 6 - Forks: 1 - Watchers: 6 - Open issues: 21 - License: Apache License 2.0 - Homepage: https://thaw.sh - Default branch: main - Created: 2026-04-14T16:43:09Z  ## Languages  - CSS - JavaScript - Jupyter Notebook - Python - Rust - Shell - TeX - TypeScript  ## Topics  - agents - inference - kv-cache - llm - reinforcement-learning - sglang - vllm  ## Top Contributors  - matteso1 (102 contributions)  ---  ## README  # thaw  PyPI Python Tests License: Apache 2.0 Downloads arXiv  **git for live LLM agent sessions.**  An agent's KV cache — its working memory — normally dies with the process. thaw turns a running **vLLM** or **SGLang** session into a *durable file* you can `checkpoint`, `branch`, `diff`, `checkout`, and `log` — like git, but for a living agent.  The part most tools miss: **inspecting, diffing, and tracing sessions needs no GPU** — only `checkout` (rehydrating onto a GPU) does. So the everyday loop runs on your laptop.  ## See it in 10 second…
