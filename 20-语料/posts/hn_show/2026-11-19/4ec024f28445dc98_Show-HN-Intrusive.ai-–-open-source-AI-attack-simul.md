---
type: "corpus"
item_id: "4ec024f28445dc98"
title: "Show HN: Intrusive.ai – open-source AI attack simulation"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50550896"
project_url: "https://intrusive.ai/"
author: "tomhavoc"
published_at: "2026-11-18T19:29:25Z"
captured_at: "2026-11-19T09:43:31+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-19"
pub_day: "2026-11-18"
tags:
  - 语料
  - hn_show
  - author_tomhavoc
  - story_50550896
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Intrusive.ai – open-source AI attack simulation

> [!info] 一句话导读
> I created the INTRUSIVE.AI platform to give agent builders the ability to evaluate their agents against OWASP's Top 10 for Agentic Applications (and more genera…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50550896>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：tomhavoc　|　发布：2026-11-18T19:29:25Z
> 项目链接：<https://intrusive.ai/>
> 采集：2026-11-19T09:43:31+08:00　|　id：`4ec024f28445dc98`

## 正文

I created the INTRUSIVE.AI platform to give agent builders the ability to evaluate their agents against OWASP's Top 10 for Agentic Applications (and more generally, just to allow for comprehensive testing in a non-production environment).Through my own experience with evaluating agents, I found indirect prompt injection testing to be especially difficult due to the architectural nature of it. To overcome that challenge, I created Interceptor Sandbox - a sandbox that runs agents in a simulated environment where all of the services an agent might rely on (HTTP, MCP, Postgres/pgvector to name a few) can be "intercepted" via an injection API to inject malicious payloads.Interceptor Sandbox:
https://github.com/intrusiveai/interceptor_sandboxAdditionally, I found that existing open source AI testing and attack simulation solutions didn't provide the breadth of capabilities I needed so I created Attack Harness for that purpose. But it also had to be sandboxed because any sufficiently capable attack harness can't be trusted to play nice once it's been given nefarious goals and so that led to Operator Sandbox. I haven't seen other people talking about the sandboxing method that I've employed in Operator so it seems to be a somewhat novel approach that might shake up the way people are thinking about sandboxing AI agents.Operator Sandbox:
https://github.com/intrusiveai/operator_sandboxThe full suite is documented here:
https://docs.intrusive.aiThe platform is still very much in its alpha stage so your mileage may vary but I would sure appreciate any feedback that comes my way. Feel free to use GitHub Issues on the respective repos to provide feedback.

## 关联链接

- https://docs.intrusive.aiThe
- https://github.com/intrusiveai/interceptor_sandboxAdditionally,
- https://github.com/intrusiveai/operator_sandboxThe

## 导航

- 项目页：[[10-项目/intrusive.ai_dd8574f3]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
