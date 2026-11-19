---
type: "project"
title: "Show HN: Intrusive.ai – open-source AI attack simulation"
project_url: "https://intrusive.ai/"
first_seen: "2026-11-19T09:43:31+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_tomhavoc
  - story_50550896
  - show_hn
lang: "en"
---

# Show HN: Intrusive.ai – open-source AI attack simulation

> [!info] 一句话导读
> I created the INTRUSIVE.AI platform to give agent builders the ability to evaluate their agents against OWASP's Top 10 for Agentic Applications (and more genera…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://intrusive.ai/>
> 首次收录：2026-11-19T09:43:31+08:00
> 来源渠道：HN Show HN
> 标签：author_tomhavoc, story_50550896, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-19T09:43:31+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-11-19/4ec024f28445dc98_Show-HN-Intrusive.ai-–-open-source-AI-attack-simul]] |

## 摘要正文

I created the INTRUSIVE.AI platform to give agent builders the ability to evaluate their agents against OWASP's Top 10 for Agentic Applications (and more generally, just to allow for comprehensive testing in a non-production environment).Through my own experience with evaluating agents, I found indirect prompt injection testing to be especially difficult due to the architectural nature of it. To overcome that challenge, I created Interceptor Sandbox - a sandbox that runs agents in a simulated environment where all of the services an agent might rely on (HTTP, MCP, Postgres/pgvector to name a few) can be "intercepted" via an injection API to inject malicious payloads.Interceptor Sandbox: https://github.com/intrusiveai/interceptor_sandboxAdditionally, I found that existing open source AI testing and attack simulation solutions didn't provide the breadth of capabilities I needed so I created Attack Harness for that purpose. But it also had to be sandboxed because any sufficiently capable attack harness can't be trusted to play nice once it's been given nefarious goals and so that led to Operator Sandbox. I haven't seen other people talking about the sandboxing method that I've employe…
