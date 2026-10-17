---
type: "project"
title: "Show HN: Squishling (Ruby gem) – Keep code only when it's cheaper than tokens"
project_url: "https://github.com/Coolhand-Labs/squishling"
first_seen: "2026-10-16T09:35:18+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_mikecarroll
  - story_50105742
  - show_hn
lang: "en"
---

# Show HN: Squishling (Ruby gem) – Keep code only when it's cheaper than tokens

> [!info] 一句话导读
> Coolhand-Labs/squishling

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/Coolhand-Labs/squishling>
> 首次收录：2026-10-16T09:35:18+08:00
> 来源渠道：HN Show HN
> 标签：author_mikecarroll, story_50105742, show_hn
> 最新指标：点赞=2 · 评论=1 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-16T09:35:18+08:00 | HN Show HN | 点赞=2 · 评论=1 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-10-16/61824a20da299d47_Show-HN-Squishling-(Ruby-gem)-–-Keep-code-only-whe]] |

## 摘要正文

# Coolhand-Labs/squishling  - Stars: 9 - Forks: 0 - Watchers: 9 - Open issues: 6 - License: Apache License 2.0 - Default branch: main - Created: 2026-10-06T11:04:56Z  ## Languages  - HTML - Ruby - Shell  ## Top Contributors  - mikecarroll (22 contributions) - dependabot[bot] (1 contributions)  ---  ## README   📖 Read the Squishling explainer →  CI Gem Version  **Don't just use AI to write code. Use AI to not need code.** Write code only where it's worth maintaining.  A squished method either runs its Ruby implementation, with the LLM as a failover, or routes some callers through an LLM as a way of eliminating (or discovering) the cost of maintaining them as deterministic code. Either way it returns the same strict-schema-validated, typed result, so callers can't tell the difference.  Think of code as a cache for AI judgment. Every line you write is something to maintain, so the LLM is the default and code has to earn its place: you build it for the inputs that carry the volume, and the LLM keeps handling the rest. New to the idea? Read Elastic Software or browse the talk slides.  Or try it on the explainer site:  - Spectrum slider: drag from traditional software to fully  LLM and s…
