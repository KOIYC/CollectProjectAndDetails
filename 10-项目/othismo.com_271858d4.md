---
type: "project"
title: "Show HN: Othismo, a Runtime for Sandboxed Objects"
project_url: "https://othismo.com/"
first_seen: "2026-11-01T09:38:09+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_mamidon
  - story_50319764
  - show_hn
lang: "en"
---

# Show HN: Othismo, a Runtime for Sandboxed Objects

> [!info] 一句话导读
> Othismo is a runtime which has a bunch of sandboxed WASM modules talking to each other + the host environment. It's actually hosting its own website right now a…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://othismo.com/>
> 首次收录：2026-11-01T09:38:09+08:00
> 来源渠道：HN Show HN
> 标签：author_mamidon, story_50319764, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-01T09:38:09+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-11-01/470fcb2ee32f8cbd_Show-HN-Othismo,-a-Runtime-for-Sandboxed-Objects]] |

## 摘要正文

Othismo is a runtime which has a bunch of sandboxed WASM modules talking to each other + the host environment. It's actually hosting its own website right now at othismo.com.This is a project that's been percolating in my head for a while, as a vague desire to make a "better" runtime for software development. But it was never particularly clear for me what that would _actually_ look like. In the last month or so, I felt a bit inspired to ask what such a runtime might look like for agentic development.My hypothesis is that we really can't review 10k+ SLoC pull requests consistently and really understand them. But if we try to have a higher level view of things, we still can't be confident the agent(s) haven't done something stupid and opened a socket or a file somewhere in that 10k+ SLoC.Therefore we need a very clear demarcation between computation and side effects. In Othismo that takes the shape of the image definition files (.oth) which describe the namespace + various type definitions describing what the interface of an object (should) be. It's somewhat like TypeScript, we don't actually do anything to verify an object conforms to this interface.I'd love your feedback on the sy…
