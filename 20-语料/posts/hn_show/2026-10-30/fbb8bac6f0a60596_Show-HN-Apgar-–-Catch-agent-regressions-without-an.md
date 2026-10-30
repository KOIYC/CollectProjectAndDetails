---
type: "corpus"
item_id: "fbb8bac6f0a60596"
title: "Show HN: Apgar – Catch agent regressions without an LLM judge"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50292363"
project_url: "https://github.com/oimo-ai/apgar"
author: "jtkm6"
published_at: "2026-10-29T17:04:06Z"
captured_at: "2026-10-30T09:46:09+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-30"
pub_day: "2026-10-29"
tags:
  - 语料
  - hn_show
  - author_jtkm6
  - story_50292363
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Apgar – Catch agent regressions without an LLM judge

> [!info] 一句话导读
> Hey HN, We build financial AI agents, and Apgar is the tool we wrote to see whether a harness change made an agent better or worse in production. Our offline ev…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50292363>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：jtkm6　|　发布：2026-10-29T17:04:06Z
> 项目链接：<https://github.com/oimo-ai/apgar>
> 采集：2026-10-30T09:46:09+08:00　|　id：`fbb8bac6f0a60596`

## 正文

Hey HN, We build financial AI agents, and Apgar is the tool we wrote to see whether a harness change made an agent better or worse in production. Our offline evals can't cover every kind of question or session real users bring, and the LLM judge we run in Langfuse is too expensive to use on more than a small slice of traffic, so some failures get through.Apgar is a small release health checker that sits on top of our Langfuse data. It picks up the release from the production traces, and for the first hours of each new release it compares the agent's behavior with the previous release on things like tool calls per turn, retries of the same failing call, loops, output length and cost per turn (11 metrics right now). The release page shows what moved in both directions. When something gets worse, we get a Slack message (and a webhook) saying which metric moved and where the change is concentrated, for example only on Telegram or only in long sessions. We've been running it for a while and decided to open-source it: https://github.com/oimo-ai/apgarIt's not meant to be another monitoring tool. We still use Langfuse for that. Apgar only tries to answer "is this release worse than the last one?" It works with Langfuse or with anything that sends OpenTelemetry. There's no LLM judge in it, so it's cheap enough to run on all traffic. The downside is that it can't tell that an answer is wrong if everything else about the turn looks the same. That's still what our evals are for.It runs on Docker Compose (or Helm) with ClickHouse, and it's Apache-2.0. The Agents page can load demo data if you want to try it without connecting anything.Curious how others deal with this. When you change your harness or prompts, how do you find out whether the agent actually got better or worse?

## 关联链接

- https://github.com/oimo-ai/apgarIt

## 导航

- 项目页：[[10-项目/github.com_c82d46b3]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
