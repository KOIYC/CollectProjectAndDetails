---
type: "project"
title: "Show HN: Relay – A multi-agent pipeline for AI-assisted front end engineering"
project_url: "https://github.com/rgadda/frontend-eng-team"
first_seen: "2026-11-11T13:37:17+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_rajivgadda
  - story_50444140
  - show_hn
lang: "en"
---

# Show HN: Relay – A multi-agent pipeline for AI-assisted front end engineering

> [!info] 一句话导读
> rgadda/frontend-eng-team

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/rgadda/frontend-eng-team>
> 首次收录：2026-11-11T13:37:17+08:00
> 来源渠道：HN Show HN
> 标签：author_rajivgadda, story_50444140, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-11T13:37:17+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-11-11/b37fb1a240806cf8_Show-HN-Relay-–-A-multi-agent-pipeline-for-AI-assi]] |

## 摘要正文

# rgadda/frontend-eng-team  Multi-agent pipeline for AI-assisted frontend engineering. Six roles, human-gated, tool-neutral. Runs in Claude Code, GitHub Copilot, and any AGENTS.md-aware tool.  - Stars: 5 - Forks: 0 - Watchers: 5 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2026-04-25T16:51:09Z  ## Languages  - CSS - HTML - JavaScript - Shell - TypeScript  ## Topics  - agents-md-template - ai-agents - ai-coding - claude-code - claude-code-plugin - developer-tools - frontend - multi-agent - reactjs - typescript  ## Top Contributors  - rgadda (30 contributions)  ---  ## README  # Relay  > A six-role multi-agent pipeline for shipping frontend changes with AI assistance — tool-neutral, cache-efficient, and gated by humans at the right moments.  CI License: MIT  > **Note:** the GitHub repo slug is `frontend-eng-team` for historical reasons. The project name is **Relay**.  ```mermaid flowchart LR     T([Task]) --> PM[PM]     PM --> A[Architect]     A --> G{Human<br/>approval}     G -->|approve| I[Implementer]     I --> R[Reviewer]     R --> P[Prod-Readiness]     P --> V[Verifier]     R -.-> V     V --> O([PR ready])      classDef conditional stroke-dasharray: …
