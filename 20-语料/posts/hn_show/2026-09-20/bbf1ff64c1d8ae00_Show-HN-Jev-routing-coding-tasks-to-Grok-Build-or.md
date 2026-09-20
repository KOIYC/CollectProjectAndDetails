---
type: "corpus"
item_id: "bbf1ff64c1d8ae00"
title: "Show HN: Jev routing coding tasks to Grok Build or Codex Astra"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49747155"
project_url: "https://github.com/jcpsimmons/jev-model-router-demo"
author: "joshcsimmons"
published_at: "2026-09-17T21:55:28Z"
captured_at: "2026-09-20T09:36:45+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-17"
tags:
  - 语料
  - hn_show
  - author_joshcsimmons
  - story_49747155
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: Jev routing coding tasks to Grok Build or Codex Astra

> [!info] 一句话导读
> jcpsimmons/jev-model-router-demo

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49747155>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：joshcsimmons　|　发布：2026-09-17T21:55:28Z
> 项目链接：<https://github.com/jcpsimmons/jev-model-router-demo>
> 采集：2026-09-20T09:36:45+08:00　|　id：`bbf1ff64c1d8ae00`

## 正文

# jcpsimmons/jev-model-router-demo

Throwaway Jev demo: route coding tasks to Grok Build or Codex Astra

- Stars: 2
- Forks: 0
- Watchers: 2
- Open issues: 0
- Default branch: master
- Created: 2026-09-17T21:49:25Z

## Languages

- JavaScript

## Top Contributors

- jcpsimmons (1 contributions)

---

## README

# Jev model router demo

This is a throwaway local prototype for one question: can Jev reliably send complex or uncertain coding tasks to Codex Astra while routing contained mechanical work to Grok Build?

The router uses Jev only for the decision. It asks three typed questions in one request:

- Choice: Grok Build or Codex Astra
- Score: complexity from mechanical to high consequence
- Boolean: whether planning or investigation should happen before code changes

The final policy is intentionally conservative. If Jev is uncertain, the complexity score is high, or planning is likely, the task goes to Astra.

## Targets

- **Grok Build:** installed locally, default model `grok-4.6`
- **Codex Astra:** installed locally as model `gpt-6-astra`

## Set up

```bash
cd /Users/simsies/github/jev-model-router-demo
npm install
```

Add a Vercel AI Gateway key to the already gitignored `.env.local`:

```text
AI_GATEWAY_API_KEY=your_key_here
```

## Run the six-task demo

```bash
npm run demo
```

This classifies six tasks in parallel and prints the chosen harness, route probability, complexity score, planning probability, and latency. It does not launch either coding agent.

## Route your own task

```bash
npm run route -- "Add an aria-label to the close button and run its existing test."
```

## Route and launch

```bash
npm run route -- \
  "Trace the intermittent authentication failure without weakening security." \
  --cwd /Users/simsies/github/example-project \
  --launch
```

Launches are deliberately safe for the demo:

- Codex Astra runs ephemerally with a read-only sandbox.
- The Codex launch accepts an explicitly selected non-Git demo directory.
- Grok Build runs in plan mode with web search and subagents disabled.

Neither route edits code in this prototype. After the routing policy is calibrated on real tasks, execution permissions can be designed separately.

## Privacy

Jev requests enable Zero Data Retention and disallow prompt training. Do not paste secrets, credentials, private customer data, or unredacted logs into a filmed task.

# Page Rage

## 导航

- 项目页：[[10-项目/github.com_7f9d2d14]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
