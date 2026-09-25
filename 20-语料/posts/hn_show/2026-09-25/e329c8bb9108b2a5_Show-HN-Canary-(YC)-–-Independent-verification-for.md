---
type: "corpus"
item_id: "e329c8bb9108b2a5"
title: "Show HN: Canary (YC) – Independent verification for AI code"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49836632"
project_url: "https://runcanary.ai/"
author: "Visweshyc"
published_at: "2026-09-24T20:57:52Z"
captured_at: "2026-09-25T13:42:25+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-25"
pub_day: "2026-09-24"
tags:
  - 语料
  - hn_show
  - author_Visweshyc
  - story_49836632
  - show_hn
metrics: {"points": 5, "comments": 0, "engagement_velocity": 5}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Canary (YC) – Independent verification for AI code

> [!info] 一句话导读
> Hey HN, we are Aakash and Viswesh and we are building Canary (https://www.runcanary.ai/) - independent verification for AI code. Claude/Codex calls Canary with …

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49836632>
> 指标：点赞=5 · 评论=0 · engagement_velocity=5
> 作者：Visweshyc　|　发布：2026-09-24T20:57:52Z
> 项目链接：<https://runcanary.ai/>
> 采集：2026-09-25T13:42:25+08:00　|　id：`e329c8bb9108b2a5`

## 正文

Hey HN, we are Aakash and Viswesh and we are building Canary (https://www.runcanary.ai/) - independent verification for AI code. Claude/Codex calls Canary with the changesets, intended behaviour and team knowledge. Canary then deploys agent swarms to investigate potential failures and test suspected runtime bugs in remote sandboxes.To try it on your repository, paste this into your coding agent: Install the Canary CLI with npm i -g @runcanary/cli,
 then run canary skills and follow its instructions
 to onboard this repository.

Verification starts with what software is supposed to do and most importantly what it must never allow. This means investigating how inputs, permissions, state, timing, dependencies etc interact with each other. Intent is not always fully declared as well but many expectations are clear: private files should stay private, credentials should not leak, and retries should not create unintended duplicate effects.We believe the future is a unified and independent verification system that starts with all those expectations and then chooses how to investigate each suspected failure. Source-only code reviews catches static issues in the implementation but even a clean review leaves a good chunk of behavioral only issues untested. Unit tests, integrations, E2E, static analysis, runtime experiments and formal verification are all means to establish that behavior thereby generating different kinds of evidence and guarantees.This is why we believe a dedicated verification harness that can think and reason through all these modalities and invariants is necessary on top of general intelligence. The harness needs to start with the system’s intended behavior, develop a series of potential failure scenarios and choose how to investigate them. It’s sole functionality is to pressure test and challenge the assumptions behind a change, create the conditions needed to test suspected failures and assess what the resulting evidence establishesHow Canary works: it takes a cold snapshot of the codebase when called, combining the supplied intent and team knowledge with requirements, decisions, prior issues from tools like Notion, Linear. It can also route questions to you through the coding agents if anything is ambiguous.Canary’s harness coordinates agent swarms by leveraging the different strengths across model families. It compares the code before and after, traces the effects through callers, dependencies, state transitions etc. and each suspected failure becomes a concrete scenario with an actor, state, trigger, outcomes and many more runtime states.,For each suspected failure, Canary chooses the best way to provide evidence through methods like runtime verification, static analysis, unit, integration or sometimes even combination of these as necessary. The agent executes these checks in remote sandboxes by seeding data, configuring permissions, mocking dependencies and third party integrations and much more. Canary then returns these findings and supporting evidence back to the coding agents which then fixes these failures and requests reverifications against the failed scenarios.To get started, give your coding agent this setup instruction and tell us what it caught and how we can do better. Install the Canary CLI with npm i -g @runcanary/cli,
 then run canary skills and follow its instructions
 to onboard this repository.

We are still pretty early in our journey and would love feedback on the product and how we can do better.

## 关联链接

- https://www.runcanary.ai/

## 导航

- 项目页：[[10-项目/runcanary.ai_55297d5b]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
