---
type: "project"
title: "Show HN: jevc – compile policy prompts into deterministic verdict programs"
project_url: "https://github.com/doronp/jevc"
first_seen: "2026-09-21T09:44:03+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_doronp
  - story_49777057
  - show_hn
lang: "en"
---

# Show HN: jevc – compile policy prompts into deterministic verdict programs

> [!info] 一句话导读
> Compile agent policy prose into deterministic verdict programs: narrow evidence questions for the model, the verdict computed in code. Install: npm i -g jev-com…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/doronp/jevc>
> 首次收录：2026-09-21T09:44:03+08:00
> 来源渠道：HN Show HN
> 标签：author_doronp, story_49777057, show_hn
> 最新指标：点赞=2 · 评论=1 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T09:44:03+08:00 | HN Show HN | 点赞=2 · 评论=1 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/52c9c40b28a6ae8d_Show-HN-jevc-–-compile-policy-prompts-into-determi]] |

## 摘要正文

# doronp/jevc  Compile agent policy prose into deterministic verdict programs: narrow evidence questions for the model, the verdict computed in code. Install: npm i -g jev-compiler  - Stars: 3 - Forks: 0 - Watchers: 3 - Open issues: 0 - License: Apache License 2.0 - Homepage: https://www.npmjs.com/package/jev-compiler - Default branch: main - Created: 2026-09-18T07:53:01Z  ## Languages  - TypeScript  ## Topics  - agent-security - agents - ai-agents - ai-safety - ai-sdk - claude-code - cli - deterministic - developer-tools - guardrails - langchain - llm - llm-guardrails - llm-security - policy-as-code - policy-engine - prompt-injection - tool-calling - typesafe - typescript  ## Top Contributors  - doronp (94 contributions)  ---  ## README  jevc compiles natural-language rules into typed questions plus a reducer in ordinary code  # jevc  **Turn the rules your agent keeps ignoring into gates you can test.**  Your `CLAUDE.md` says *NEVER commit unless the user explicitly asks*, and the agent commits anyway — because a markdown rule is a suggestion the model re-reads fresh every turn. `jevc` compiles a rule like that into a **Jev program**: a few narrow typed questions answered by TypeS…
