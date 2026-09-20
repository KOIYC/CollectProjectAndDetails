---
type: "project"
title: "Show HN: Tokentoll, a CI gate for LLM API cost regressions"
project_url: "https://github.com/Jwrede/tokentoll"
first_seen: "2026-09-21T02:52:53+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_Jwrede
  - story_48335559
  - show_hn
lang: "en"
---

# Show HN: Tokentoll, a CI gate for LLM API cost regressions

> [!info] 一句话导读
> Catch LLM cost changes in code review. Infracost for LLM spend.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/Jwrede/tokentoll>
> 首次收录：2026-09-21T02:52:53+08:00
> 来源渠道：HN Show HN
> 标签：author_Jwrede, story_48335559, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:27:24+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/d254be4874ba9fce_Show-HN-Tokentoll,-a-CI-gate-for-LLM-API-cost-regr]] |
| 2026-09-21T02:52:53+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/d254be4874ba9fce_Show-HN-Tokentoll,-a-CI-gate-for-LLM-API-cost-regr]] |

## 摘要正文

# Jwrede/tokentoll  Catch LLM cost changes in code review. Infracost for LLM spend.  - Stars: 4 - Forks: 0 - Watchers: 4 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2026-05-03T07:37:10Z  ## Languages  - Dockerfile - Python  ## Topics  - anthropic - cost-optimization - devtools - github-action - llm - mlops - openai - python - static-analysis  ## Top Contributors  - Jwrede (54 contributions)  ---  ## README  # tokentoll  > Prevent LLM cost regressions before production.  CI PyPI version GitHub Marketplace License: MIT Python 3.10+ tokentoll MCP server  tokentoll is a CI gate for LLM cost. It statically analyzes Python, JavaScript, and TypeScript for LLM API calls, scores every pull request against a policy you control, and posts a PASS/WARN/FAIL verdict directly on the PR. Optionally, it fails the workflow when the policy is violated, so cost regressions cannot be merged.  ## Live demo  Jwrede/tokentoll-demo is a small polyglot LLM app (Python + TypeScript) wired up to the tokentoll cost gate. Two PRs are already open against it:  - PR #1: Add Anthropic Haiku translation helper. New call site, well within budget. Verdict: PASS, workflow green. - PR #2: …
