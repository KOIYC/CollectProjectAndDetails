---
type: "project"
title: "Show HN: Apgar – Catch agent regressions without an LLM judge"
project_url: "https://github.com/oimo-ai/apgar"
first_seen: "2026-10-30T09:46:09+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_jtkm6
  - story_50292363
  - show_hn
lang: "en"
---

# Show HN: Apgar – Catch agent regressions without an LLM judge

> [!info] 一句话导读
> Hey HN, We build financial AI agents, and Apgar is the tool we wrote to see whether a harness change made an agent better or worse in production. Our offline ev…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/oimo-ai/apgar>
> 首次收录：2026-10-30T09:46:09+08:00
> 来源渠道：HN Show HN
> 标签：author_jtkm6, story_50292363, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-30T09:46:09+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-10-30/fbb8bac6f0a60596_Show-HN-Apgar-–-Catch-agent-regressions-without-an]] |

## 摘要正文

Hey HN, We build financial AI agents, and Apgar is the tool we wrote to see whether a harness change made an agent better or worse in production. Our offline evals can't cover every kind of question or session real users bring, and the LLM judge we run in Langfuse is too expensive to use on more than a small slice of traffic, so some failures get through.Apgar is a small release health checker that sits on top of our Langfuse data. It picks up the release from the production traces, and for the first hours of each new release it compares the agent's behavior with the previous release on things like tool calls per turn, retries of the same failing call, loops, output length and cost per turn (11 metrics right now). The release page shows what moved in both directions. When something gets worse, we get a Slack message (and a webhook) saying which metric moved and where the change is concentrated, for example only on Telegram or only in long sessions. We've been running it for a while and decided to open-source it: https://github.com/oimo-ai/apgarIt's not meant to be another monitoring tool. We still use Langfuse for that. Apgar only tries to answer "is this release worse than the las…
