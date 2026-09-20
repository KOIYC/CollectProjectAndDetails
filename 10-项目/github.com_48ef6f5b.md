---
type: "project"
title: "Show HN: Looplet – a 0-dep agent loop you own"
project_url: "https://github.com/hsaghir/looplet"
first_seen: "2026-09-21T02:52:32+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_hsaghir
  - story_47953850
  - show_hn
lang: "en"
---

# Show HN: Looplet – a 0-dep agent loop you own

> [!info] 一句话导读
> The tool-calling loop for LLM agents; iterator-first, protocol-hooked, one dependency.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/hsaghir/looplet>
> 首次收录：2026-09-21T02:52:32+08:00
> 来源渠道：HN Show HN
> 标签：author_hsaghir, story_47953850, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:09:14+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/fdc2399a4bafd527_Show-HN-Looplet-–-a-0-dep-agent-loop-you-own]] |
| 2026-09-21T01:13:42+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/fdc2399a4bafd527_Show-HN-Looplet-–-a-0-dep-agent-loop-you-own]] |
| 2026-09-21T02:52:32+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/fdc2399a4bafd527_Show-HN-Looplet-–-a-0-dep-agent-loop-you-own]] |

## 摘要正文

# hsaghir/looplet  The tool-calling loop for LLM agents; iterator-first, protocol-hooked, one dependency.  - Stars: 6 - Forks: 4 - Watchers: 6 - Open issues: 10 - License: Apache License 2.0 - Homepage: https://hsaghir.com/looplet/ - Default branch: master - Created: 2026-04-18T08:13:15Z  ## Languages  - Makefile - Python - Shell  ## Topics  - agent-framework - agents - ai-agents - anthropic - asyncio - composable - function-calling - hooks - llm - llm-agent - mcp - observability - ollama - openai - protocol - python - tool-calling - tool-use  ## Top Contributors  - hsaghir (167 contributions) - Copilot (1 contributions) - dependabot[bot] (1 contributions) - k0505 (1 contributions)  ---  ## README  # looplet  looplet pretty trace — agents from a paragraph, then run them  CI codecov PyPI version Python 3.11+ License: Apache 2.0  **Describe an agent in one paragraph. Get a working agent in five minutes.**  ```bash pip install looplet export OPENAI_BASE_URL=https://api.openai.com/v1   # any OpenAI-compatible endpoint export OPENAI_API_KEY=sk-... export OPENAI_MODEL=gpt-5.5  looplet new "An agent that takes a URL and returns the page title and a 2-sentence summary" looplet run-workspac…
