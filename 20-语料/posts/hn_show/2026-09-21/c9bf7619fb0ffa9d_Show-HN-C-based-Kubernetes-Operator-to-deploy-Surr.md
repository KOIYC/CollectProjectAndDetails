---
type: "corpus"
item_id: "c9bf7619fb0ffa9d"
title: "Show HN: C# based Kubernetes Operator to deploy SurrealDB"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47945217"
project_url: "https://github.com/stevefan1999-personal/surrealdb-operator"
author: "stevefan1999"
published_at: "2026-04-29T07:35:18Z"
captured_at: "2026-09-21T01:42:23+08:00"
lang: "en"
kind: "post"
topic: AI 工具/Agent
shard: "2026-09-21"
pub_day: "2026-04-29"
tags:
  - 语料
  - hn_show
  - author_stevefan1999
  - story_47945217
  - show_hn
metrics: {"points": 8, "comments": 2, "engagement_velocity": 8}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:174d"
---

# Show HN: C# based Kubernetes Operator to deploy SurrealDB

> [!info] 一句话导读
> Show HN: C# based Kubernetes Operator to deploy SurrealDB

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47945217>
> 指标：点赞=8 · 评论=2 · engagement_velocity=8
> 作者：stevefan1999　|　发布：2026-04-29T07:35:18Z
> 项目链接：<https://github.com/stevefan1999-personal/surrealdb-operator>
> 采集：2026-09-21T01:42:23+08:00　|　id：`c9bf7619fb0ffa9d`

## 正文

Show HN: C# based Kubernetes Operator to deploy SurrealDB

## 评论（2/2）

> **benterix** · 2026-04-29T07:51:01.000Z　
> I have so many questions! Why did you decide to use C# instead of Go? How does the C# Operator SDK compare to the Operator SDK or Kubebuilder?

---

> **stevefan1999** · 2026-04-29T08:32:30.000Z　
> While I'm both fluent in Rust, Golang and C#, I just don't think Golang is a good choice for Kubernetes operator, the code is simply too terse and verbose, and I can't enjoy a lot of good things such as DI and IoC in Golang, where I think C#/Kotlin's approach by using primary constructor is very intuitive for me, and it is really a game changer for the coding mindset, especially when you have LLM, without DI there will be a lot of spagetti code entanglement. I use DI to facilitate functional separation and modularization of code.It is not like I don't know that Golang's interface could do that. It's just C# simply did better. I do enjoy using Golang for writing network application such as network protocols and IO intensive workload, which is where Golang really shine through Goroutines, but if you want a generalist that is famiilar and did all-rounds, I would still consider C#/Java/Kotlin for that purpose.

## 导航

- 项目页：[[10-项目/github.com_f1ef313e]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
