---
type: "project"
title: "Show HN: Sonde, a local code graph for AI agents that refuses to guess"
project_url: "https://github.com/anishmoncivarghese/sonde"
first_seen: "2026-09-21T03:11:25+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_anishvarghese
  - story_49507034
  - show_hn
lang: "en"
---

# Show HN: Sonde, a local code graph for AI agents that refuses to guess

> [!info] 一句话导读
> anishmoncivarghese/sonde

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/anishmoncivarghese/sonde>
> 首次收录：2026-09-21T03:11:25+08:00
> 来源渠道：HN Show HN
> 标签：author_anishvarghese, story_49507034, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:33:52+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/9d9432aba9ac5373_Show-HN-Sonde,-a-local-code-graph-for-AI-agents-th]] |
| 2026-09-21T03:11:25+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/9d9432aba9ac5373_Show-HN-Sonde,-a-local-code-graph-for-AI-agents-th]] |

## 摘要正文

# anishmoncivarghese/sonde  Local code-context engine for AI coding agents: structural answers within a token budget.  - Stars: 0 - Forks: 0 - Watchers: 0 - Open issues: 0 - License: Apache License 2.0 - Default branch: main - Created: 2026-08-24T03:25:18Z  ## Languages  - JavaScript - TypeScript  ## Topics  - ai-agents - code-analysis - developer-tools - mcp - mcp-server - python - static-analysis - swift - tree-sitter - typescript  ## Top Contributors  - anishmoncivarghese (196 contributions)  ---  ## README  # Sonde  ci npm license  A local code-context engine for AI coding agents. Sonde indexes a TypeScript, Python, or Swift repository into a symbol-level graph in SQLite and exposes three MCP tools — `find_symbols`, `query_graph`, and `get_impact_radius` — so an agent can answer *who calls this*, *what breaks if I change it*, and *which tests relate to it* in one call instead of a search loop.  ## What the benchmark actually shows  The honest claim is **not** "finds what grep cannot". A competent agentic search loop finds the same structural evidence — we measured it, on a real 19,409-line repository, and it scored 1.000 recall on every task.  The claim is **the same answers fo…
