---
type: "project"
title: "Show HN: Let agent read files with secrets while redacting values for LLM contex"
project_url: "https://github.com/daniel-sc/contextveil"
first_seen: "2026-09-20T14:06:19+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_daniel-sc
  - story_49713034
  - show_hn
lang: "en"
---

# Show HN: Let agent read files with secrets while redacting values for LLM contex

> [!info] 一句话导读
> daniel-sc/contextveil

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/daniel-sc/contextveil>
> 首次收录：2026-09-20T14:06:19+08:00
> 来源渠道：HN Show HN
> 标签：author_daniel-sc, story_49713034, show_hn
> 最新指标：点赞=4 · 评论=1 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=4 · 评论=1 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-20/e75ff622790e34fe_Show-HN-Let-agent-read-files-with-secrets-while-re]] |
| 2026-09-20T09:37:14+08:00 | HN Show HN | 点赞=4 · 评论=1 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-20/e75ff622790e34fe_Show-HN-Let-agent-read-files-with-secrets-while-re]] |
| 2026-09-20T14:06:19+08:00 | HN Show HN | 点赞=4 · 评论=1 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-20/e75ff622790e34fe_Show-HN-Let-agent-read-files-with-secrets-while-re]] |

## 摘要正文

# daniel-sc/contextveil  Not another secret scanner. Keep local secrets out of your coding agent’s LLM context.  - Stars: 5 - Forks: 0 - Watchers: 5 - Open issues: 5 - License: Apache License 2.0 - Default branch: main - Created: 2026-08-16T08:20:05Z  ## Languages  - Rust - Shell - TypeScript  ## Topics  - claude-code - claude-code-plugin - codex - copilot-cli - opencode - security-tools  ## Top Contributors  - daniel-sc (114 contributions)  ---  ## README  # ContextVeil — The tool can read it. The LLM doesn’t need it.  Coding agents read environment variables, `.env` files, configuration, and command output that may contain credentials. ContextVeil locally replaces the secret values you’ve chosen before supported text reaches the LLM — **without blocking the workflow.**  ```text GITHUB_TOKEN=ghp_secret_example  ->  GITHUB_TOKEN=<SECRET:GITHUB_TOKEN> ```  **The command still runs. The file still gets read.** Only enrolled exact values are replaced; the rest of the output stays intact.  1. **A guided setup helps you choose what to protect.** 2. **Runtime matching is exact and deterministic.** 3. **Keep working. No magic.**  ## Quick Start  Install the latest stable release:  ```bash…
