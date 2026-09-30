---
type: "project"
title: "Show HN: Runtape – counterfactual debugging and regression tests for AI agents"
project_url: "https://github.com/RehanMohammed985/runtape"
first_seen: "2026-09-30T18:57:07+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_rehanmoin91
  - story_49904620
  - show_hn
lang: "en"
---

# Show HN: Runtape – counterfactual debugging and regression tests for AI agents

> [!info] 一句话导读
> RehanMohammed985/runtape

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/RehanMohammed985/runtape>
> 首次收录：2026-09-30T18:57:07+08:00
> 来源渠道：HN Show HN
> 标签：author_rehanmoin91, story_49904620, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-30T18:28:30+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-30/ea2d500209ce230b_Show-HN-Runtape-–-counterfactual-debugging-and-reg]] |
| 2026-09-30T18:57:07+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-30/ea2d500209ce230b_Show-HN-Runtape-–-counterfactual-debugging-and-reg]] |

## 摘要正文

# RehanMohammed985/runtape  Record AI agent runs locally and find which part of the context caused a decision.  - Stars: 0 - Forks: 0 - Watchers: 0 - Open issues: 0 - License: MIT License - Homepage: https://pypi.org/project/runtape/ - Default branch: main - Created: 2026-09-28T22:36:17Z  ## Languages  - Python  ## Topics  - ai-agents - anthropic - debugging - debugging-tool - llm - mcp - observability - ollama - openai - prompt-injection - python  ## Top Contributors  - RehanMohammed985 (45 contributions)  ---  ## README  # runtape  tests PyPI License: MIT  Counterfactual debugging and regression tests for AI agents.  Give runtape a bad agent run. It finds the part of the context that caused the bad decision, checks candidate fixes against the exact context that failed, and writes a regression test so it stays fixed.  ``` runtape why  last tool:forward_email      # what caused it runtape fix  last tool:forward_email      # which fixes hold, measured runtape fix  last tool:forward_email --write-test tests/test_inbox.py ```  runtape on the inbox example  An email assistant forwards an invoice to an outside address. `runtape why` traces the call to one sentence in an HTML comment ins…
