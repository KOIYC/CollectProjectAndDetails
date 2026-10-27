---
type: "corpus"
item_id: "ab19d7d967afdb38"
title: "Show HN: Sectr – Serverless backend platform for easy deployment of AI agents"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50260969"
project_url: "https://sectr.dev/"
author: "donald_pinckney"
published_at: "2026-10-27T15:40:07Z"
captured_at: "2026-10-27T23:46:32+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-27"
pub_day: "2026-10-27"
tags:
  - 语料
  - hn_show
  - author_donald_pinckney
  - story_50260969
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Sectr – Serverless backend platform for easy deployment of AI agents

> [!info] 一句话导读
> Hey HN, I've been building Sectr, a backend-as-a-service for making it easy(ier) to develop and deploy AI agents. Deploying agents requires non-trivial systems …

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50260969>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：donald_pinckney　|　发布：2026-10-27T15:40:07Z
> 项目链接：<https://sectr.dev/>
> 采集：2026-10-27T23:46:32+08:00　|　id：`ab19d7d967afdb38`

## 正文

Hey HN, I've been building Sectr, a backend-as-a-service for making it easy(ier) to develop and deploy AI agents. Deploying agents requires non-trivial systems design work. Consider a support agent: how do you stream messages to your frontend, how/where do you persist messages for frontend fetching later (or for auditing), and when the agent wants to issue a refund, do you spin-down the compute infra while it's waiting on human approval? Sectr aims to be the serverless abstraction and platform to provide these systems for you.No sign-up needed to try using the dev server: curl -fsSL https://sectr.dev/install.sh | sh # Install CLI
 sectr init my-agent && cd my-agent # Starter code
 sectr dev # Dev server, with UI to test chatting

Sectr provides:- Streaming of every token, tool call and event, and persistence so they can be loaded fresh later.- Scaling up, and down to zero when the agent needs to wait, and resumption right to the suspended agent's state.- Human approved tools automatically use Sectr's suspension and resumption capabilities, no code needed from you.- AG-UI endpoint for any deployed agent so you can trivially hook up your frontend- Local dev server experience, so you can rapidly debug and iterate on your agent's behaviorAt the core, you can deploy any container image to Sectr as long as it implements a certain shaped HTTP endpoint. In practice, currently Sectr provides adapters to let you deploy your existing OpenAI Agents SDK, LangGraph, or Pydantic AI agents, with only 2 new lines of code: app = AgentApp(name="support")
 app.add_route("/chat", openai_agents(agent))

Certainly the hardest part of building Sectr was getting the resumption logic to be correct and invisible, across the Program State x Model Provider x Agent Framework matrix. For example, an earlier bug was when a model replied with text plus a tool call, Sectr would resume that as two separate messages, instead of one message with a text and tool part. This works, but breaks prompt caching (and might subtly change model behavior).Sectr is free during the beta (and can be tried locally without sign-up); I mainly want feedback, especially on dev & deployment experiences, any bugs, and what features would excite you.Introductory video: https://www.youtube.com/watch?v=H-y3wynkKc0Docs: https://docs.sectr.dev

## 关联链接

- https://docs.sectr.dev
- https://sectr.dev/install.sh
- https://www.youtube.com/watch?v=H-y3wynkKc0Docs:

## 导航

- 项目页：[[10-项目/sectr.dev_5fd003e9]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
