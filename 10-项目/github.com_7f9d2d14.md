---
type: "project"
title: "Show HN: Jev routing coding tasks to Grok Build or Codex Astra"
project_url: "https://github.com/jcpsimmons/jev-model-router-demo"
first_seen: "2026-09-20T09:36:45+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_joshcsimmons
  - story_49747155
  - show_hn
lang: "en"
---

# Show HN: Jev routing coding tasks to Grok Build or Codex Astra

> [!info] 一句话导读
> jcpsimmons/jev-model-router-demo

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/jcpsimmons/jev-model-router-demo>
> 首次收录：2026-09-20T09:36:45+08:00
> 来源渠道：HN Show HN
> 标签：author_joshcsimmons, story_49747155, show_hn
> 最新指标：点赞=4 · 评论=0 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-20/bbf1ff64c1d8ae00_Show-HN-Jev-routing-coding-tasks-to-Grok-Build-or]] |
| 2026-09-20T09:36:45+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-20/bbf1ff64c1d8ae00_Show-HN-Jev-routing-coding-tasks-to-Grok-Build-or]] |

## 摘要正文

# jcpsimmons/jev-model-router-demo  Throwaway Jev demo: route coding tasks to Grok Build or Codex Astra  - Stars: 2 - Forks: 0 - Watchers: 2 - Open issues: 0 - Default branch: master - Created: 2026-09-17T21:49:25Z  ## Languages  - JavaScript  ## Top Contributors  - jcpsimmons (1 contributions)  ---  ## README  # Jev model router demo  This is a throwaway local prototype for one question: can Jev reliably send complex or uncertain coding tasks to Codex Astra while routing contained mechanical work to Grok Build?  The router uses Jev only for the decision. It asks three typed questions in one request:  - Choice: Grok Build or Codex Astra - Score: complexity from mechanical to high consequence - Boolean: whether planning or investigation should happen before code changes  The final policy is intentionally conservative. If Jev is uncertain, the complexity score is high, or planning is likely, the task goes to Astra.  ## Targets  - **Grok Build:** installed locally, default model `grok-4.6` - **Codex Astra:** installed locally as model `gpt-6-astra`  ## Set up  ```bash cd /Users/simsies/github/jev-model-router-demo npm install ```  Add a Vercel AI Gateway key to the already gitignored …
