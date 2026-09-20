---
type: "corpus"
item_id: "8deac700e6eee8b2"
title: "Show HN: AgentPort – Open-source Security Gateway For Agents"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47950752"
project_url: "https://agentport.sh/"
author: "yakkomajuri"
published_at: "2026-04-29T16:33:38Z"
captured_at: "2026-09-21T01:41:41+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-29"
tags:
  - 语料
  - hn_show
  - author_yakkomajuri
  - story_47950752
  - show_hn
metrics: {"points": 8, "comments": 3, "engagement_velocity": 8}
comments_count: 3
comments_total: 3
discovered_via: "hn:show_hn:174d"
---

# Show HN: AgentPort – Open-source Security Gateway For Agents

> [!info] 一句话导读
> Hey HN!I've been wanting to use something like OpenClaw for a while but couldn't get myself to give it access to anything important due to all the risks involve…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47950752>
> 指标：点赞=8 · 评论=3 · engagement_velocity=8
> 作者：yakkomajuri　|　发布：2026-04-29T16:33:38Z
> 项目链接：<https://agentport.sh/>
> 采集：2026-09-21T01:41:41+08:00　|　id：`8deac700e6eee8b2`

## 正文

Hey HN!I've been wanting to use something like OpenClaw for a while but couldn't get myself to give it access to anything important due to all the risks involved. Prompt injection is still a problem (even though some people seem to ignore it) and so are hallucinations and mishaps that cause agents to do things like delete production data [1].Even harnesses like Claude Code and Codex are subject to this, particularly since we're getting progressively looser about how we run them e.g. Conductor is really popular and runs agents without any sandboxing.That means we're in a bit of an all-or-nothing situation. There are people who just ignore the risks and connect everything to their agents and reap benefits from it while being subject to more risk, and there are others that just don't connect anything because they are mindful of the potential issues.I've been quite cautious but have wanted to run more autonomous agents and so I built the component I needed to enable me to do so: AgentPort.AgentPort is a gateway that connects to any service (e.g. Gmail, GitHub, Stripe, PostHog, Linear) and let's you set granular permissions for what the agent can do automatically, what it needs your approval for, and what it can never do.For example, you can set `list_customers` and `get_customer` on the Stripe integration to "Auto-approve" but `create_refund` to "Ask for approval". The agent will thus be able to do a lot in the background independently but when it comes to a potentially destructive operation it will be blocked and receive an approval link to send to you. You can then approve or deny the call with those exact parameters e.g. `create_refund(customer_id: 1234, amount: 12)`.Agents connect via MCP or CLI and have access to all the integrations you connected without ever getting API keys. Kind of like Composio but with granular permissions and open source.The goal with AgentPort is to specifically address two vulnerabilities that agents are subject to:1. Destructive operations on downstream services: It can't delete a database unless you explicitly approve 2. Credential exfiltration: Your agent never sees API keysAgentPort also helps with sensitive data exfiltration, but that is more nuanced and complicated to defend against if the agent has an internet connection [2].Ultimately, AgentPort was the missing piece for me to start running more autonomous agents that have access to third-party services, and hopefully it can unlock use cases for you too. There's a ton more work needed around securing agents (Claws in particular) and I've both been writing about it [3] and intend to do more in this space, so if you're thinking about similar things let's have a chat.The repo is https://github.com/yakkomajuri/agentport and you can run it locally with docker compose in a minute or use the one-liner install to deploy a prod instance (domain, TLS, etc.) in just a few mins as well.[1] "An AI agent deleted our production database. The agent's confession is below" (https://news.ycombinator.com/item?id=47911524)[2] See my post "On agents dropping production databases": https://yakko.dev/blog/on-agents-dropping-production-dbs[3] https://yakko.dev/blog

## 评论（3/3）

> **yakkomajuri** · 2026-04-29T16:54:59.000Z　
> OP here. Happy to answer any questions. Security for autonomous agents/claws is a deep rabbit hole that I've jumped into and I'm really interested in having open discussions about how people are approaching it.

---

> **manojbajaj95** · 2026-04-30T07:29:57.000Z　
> How does this differ from multiple MCP gateways that are available? And how would this work with our custom tools?

---

> **yakkomajuri** · 2026-04-30T16:47:03.000Z　
> Great question. I assume you mean tools like Composio right?So the difference here is the granular permissioning layer. In practice it means AgentPort is basically an open source Composio with granular permissions today. But whereas their focus is on just connecting you to everything my focus here is security. And that leads to pretty different products down the line in my opinion.As for connecting your own tools, I have a feature basically ready to let you create your own integrations. Should launch soon!

## 关联链接

- https://github.com/yakkomajuri/agentport
- https://news.ycombinator.com/item?id=47911524
- https://yakko.dev/blog
- https://yakko.dev/blog/on-agents-dropping-production-dbs[3

## 导航

- 项目页：[[10-项目/agentport.sh_953362db]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
