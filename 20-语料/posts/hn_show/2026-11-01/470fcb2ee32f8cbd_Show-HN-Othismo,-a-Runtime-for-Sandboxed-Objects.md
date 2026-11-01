---
type: "corpus"
item_id: "470fcb2ee32f8cbd"
title: "Show HN: Othismo, a Runtime for Sandboxed Objects"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50319764"
project_url: "https://othismo.com/"
author: "mamidon"
published_at: "2026-10-31T20:23:15Z"
captured_at: "2026-11-01T09:38:09+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-01"
pub_day: "2026-10-31"
tags:
  - 语料
  - hn_show
  - author_mamidon
  - story_50319764
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Othismo, a Runtime for Sandboxed Objects

> [!info] 一句话导读
> Othismo is a runtime which has a bunch of sandboxed WASM modules talking to each other + the host environment. It's actually hosting its own website right now a…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50319764>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：mamidon　|　发布：2026-10-31T20:23:15Z
> 项目链接：<https://othismo.com/>
> 采集：2026-11-01T09:38:09+08:00　|　id：`470fcb2ee32f8cbd`

## 正文

Othismo is a runtime which has a bunch of sandboxed WASM modules talking to each other + the host environment. It's actually hosting its own website right now at othismo.com.This is a project that's been percolating in my head for a while, as a vague desire to make a "better" runtime for software development. But it was never particularly clear for me what that would _actually_ look like. In the last month or so, I felt a bit inspired to ask what such a runtime might look like for agentic development.My hypothesis is that we really can't review 10k+ SLoC pull requests consistently and really understand them. But if we try to have a higher level view of things, we still can't be confident the agent(s) haven't done something stupid and opened a socket or a file somewhere in that 10k+ SLoC.Therefore we need a very clear demarcation between computation and side effects. In Othismo that takes the shape of the image definition files (.oth) which describe the namespace + various type definitions describing what the interface of an object (should) be. It's somewhat like TypeScript, we don't actually do anything to verify an object conforms to this interface.I'd love your feedback on the syntax used to define images overall, I feel like it doesn't do a great job giving me a clear notion of the environment lexically.
I'm more comfortable about the syntax for describing the behavior of objects, although things like `operator` and `readonly` are really only necessary because I've not done anything to support auth at the protocol layer yet.You can run the same website hosted at othismo.com with`git clone git@github.com:mamidon/othismo.git``task run:example:static`You can also play with the namespace interactively with```
task build:example:static
target/debug/othismo shell examples/static/static.rti# print out the namespace(s)
target/debug/othismo --check examples/static/static.rti
```You'll need rust, task (it's like make), and node+npm.

## 导航

- 项目页：[[10-项目/othismo.com_271858d4]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
