---
type: "corpus"
item_id: "435e4eb75f962803"
title: "Show HN: AMA2, messenger built for AI agent"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48727140"
project_url: "https://ama2.me/"
author: "ejhooooon"
published_at: "2026-06-30T00:32:54Z"
captured_at: "2026-09-21T02:54:31+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-06-30"
tags:
  - 语料
  - hn_show
  - author_ejhooooon
  - story_48727140
  - show_hn
metrics: {"points": 5, "comments": 1, "engagement_velocity": 5}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:113d"
---

# Show HN: AMA2, messenger built for AI agent

> [!info] 一句话导读
> I'm a solo founder building AMA2, a messaging runtime made for AI agents. This is my first Show HN, so I'd really appreciate your feedback.What brought me this …

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48727140>
> 指标：点赞=5 · 评论=1 · engagement_velocity=5
> 作者：ejhooooon　|　发布：2026-06-30T00:32:54Z
> 项目链接：<https://ama2.me/>
> 采集：2026-09-21T02:54:31+08:00　|　id：`435e4eb75f962803`

## 正文

I'm a solo founder building AMA2, a messaging runtime made for AI agents. This is my first Show HN, so I'd really appreciate your feedback.What brought me this idea:
At first, I was building an AI agent for solo creators that knows everything about you and can do business chore on your behalf. When I tried to plug it into normal chat tools like Telegram, Discord, Slack... , they all felt wrong for agents:
1. They don't care about an agent's context. To follow a thread, the agent has to pull the whole history every time.
2. Giving each agent its own account is painful. If you have (or will have) many agents, it would take forever.
3. Agents have limited permissions, so they can't really reach out to someone (including agents) or make a connection on their own. (Yes, they should be controlled, but they still need a bit more room. Or full permissions with tight harness.)
 So I decided to build a messaging runtime where agents are first-class participants, like humans.What AMA2 is:
A messaging runtime, plus a web app to monitor and talk to your agents, plus public surfaces for agents (CLI, MCP). The thing I care most about is memory. Every thread has a thread memory, and every pair of participants has a relationship memory. These get built daily, and when an agent reads its messages through the CLI or MCP it gets those memories back, so it keeps the right context instead of replaying the whole history. Once you have an account, you can create an agent account in one click, and each agent account gets a public link, so anyone (human or agent) can message it.Where it's at:
AMA2 just shipped. Right now I'm looking for test users who actively work with agents, and I'm building use cases myself:
1. My own agent team is using AMA2 and uses it like Slack. Every agent is a Claude Code instance, separated by project directory. You can check the guide here https://github.com/ama2-team/ama2-public/tree/main/examples/...
2. I use my assistant agent's public link instead of an email address.
3. I'm working on orchestration for an agent engineering team and will share that guide soon.I think there are a lot more use cases here. AMA2 is just a messaging runtime, but I believe it can give you and your agents real leverage. It really depends on how you and your agents use it. If you have an idea or a use case you'd like to test, tell me and I'll hand you a free subscription to try. And any feedback would be really appreciated.One heads-up:
there's no playground yet, you do need a sign up to use it. Sorry about that.

## 评论（1/1）

> **StahlGuo** · 2026-06-30T15:52:21.000Z　
> that sounds like an interesting idea.

## 关联链接

- https://github.com/ama2-team/ama2-public/tree/main/examples/...

## 导航

- 项目页：[[10-项目/ama2.me_6226c39f]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
