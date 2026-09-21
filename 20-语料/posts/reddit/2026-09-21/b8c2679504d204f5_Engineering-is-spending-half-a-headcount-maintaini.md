---
type: "corpus"
item_id: "b8c2679504d204f5"
title: "Engineering is spending half a headcount maintaining our docs pipeline"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/SaaS/comments/1wj9c9x/engineering_is_spending_half_a_headcount/"
author: "Upstairs-Crab-2611"
published_at: "2026-09-18T07:07:11+08:00"
captured_at: "2026-09-21T13:04:39+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-09-18"
tags:
  - 语料
  - reddit
  - r/SaaS
metrics: {"score": 23, "comments": 9, "upvote_ratio": 0.93}
comments_count: 8
comments_total: 9
discovered_via: "reddit:7d+settle3"
---

# Engineering is spending half a headcount maintaining our docs pipeline

> [!info] 一句话导读
> Did an audit on where engineering time is actually going and docs infrastructure was higher than I expected. two engineers are spending roughly 30% of their tim…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/SaaS/comments/1wj9c9x/engineering_is_spending_half_a_headcount/>
> 指标：得分=23 · 评论=9 · 赞踩比=0.93
> 作者：Upstairs-Crab-2611　|　发布：2026-09-18T07:07:11+08:00
> 项目链接：—
> 采集：2026-09-21T13:04:39+08:00　|　id：`b8c2679504d204f5`

## 正文

Did an audit on where engineering time is actually going and docs infrastructure was higher than I expected. two engineers are spending roughly 30% of their time on builds, deploys, search indexing and fixing things when the pipeline breaks. that's 0.6 FTE on something that isn't our product.

on top of that our support team tagged every ticket last quarter and about 40% had an answer somewhere in our docs. users just can't find it, search is bad and we don't have any kind of AI assistant on the docs.

the other thing that came up is that our docs aren't set up for AI agents at all. no llms.txt, no MCP server, nothing structured. with most of our developers now building through Cursor and Claude Code that's starting to matter.

looking at managed platforms vs continuing to maintain what we have. mainly want to understand what companies in the 300-500 engineer range are actually using and whether the migration pain is worth it at our scale.

## 评论（8/9）

> **VariousFoothold**（1 分） · 2026-09-18T07:12:58+08:00　
> before switching platforms I would check whether the problem is the tool or the process. we tied docs updates to the PR review checklist and made it a merge blocker. cut the stale docs problem significantly without changing platforms. the AI agent readiness part is a different question though, that does need tooling.

---

> **lemontree882**（1 分） · 2026-09-18T07:41:38+08:00　
> The 0.6 FTE and the 40% are two different bills. Two engineers on builds and indexing is infra you own, and no managed platform pays that down if you keep bolting custom indexing on top. The 40% is retrieval, and the test for it is cheaper than a migration. Sort your docs search log for last quarter by zero results. If they cluster on a dozen pages it is nav, if they are spread out it is search. Which one is it?

---

> **WhyAmIDoingThis1000**（4 分） · 2026-09-18T09:13:42+08:00　
> just keep what you have. .6 fte is nothing in 200-500 person company.

---

> **francksiduo**（2 分） · 2026-09-18T10:09:21+08:00　
> the search problem is usually cheaper to fix than the migration. 40% of tickets already have an answer in the docs, so content coverage isn't the gap, retrieval is. before ripping out the whole pipeline, worth testing if a better search index alone moves that support number, separate from the llms.txt/MCP question which is really about whether coding agents can consume the docs at all, not whether humans can find them.

---

> **SirLanceShallot**（1 分） · 2026-09-18T10:44:05+08:00　
> half a headcount on docs infra is usually a smell that the pipeline has become a product without a product owner.
>
> i'd separate the work into "must be custom" and "we are babysitting glue." in my old enterprise docs teams, the expensive bits were never markdown or publishing. it was conditional content rules, versioned reuse, permissions, broken link checks, and release branching. if your engineer is mostly fixing builds, auth, search indexing, or one-off scripts, buy/replace that layer. if theyre encoding product-specific release logic, keep that close and document the contract. do a 2-week ticket audit first. the answer gets obvious fast.

---

> **pushpendraagrawal**（1 分） · 2026-09-18T18:38:20+08:00　
> the agent-readability thing (llms.txt, MCP) is a separate decision from the pipeline rebuild and way cheaper. that's a day of work, do it regardless of what you pick for search or hosting. the 0.6 FTE and the 40% ticket number are the real fork - one is infra you're stuck maintaining, the other is a retrieval problem you could test without touching the pipeline at all. don't let the agent stuff wait on the bigger migration call, it's not blocked by it.

---

> **Ok_Pride_6746**（1 分） · 2026-09-18T23:12:39+08:00　
> 0.6 fte is fine but 40% of support tickets having answers that users just can't find is the one I'd pay attention too, that compounds every quarter

---

> **Spidey-007**（0 分） · 2026-09-19T08:50:37+08:00　
> the thread split this well. the 0.6 FTE is infra, the 40 percent is retrieval. one thing nobody picked up: you already built the eval set.
>
> if the ticket tags point at the page that answered each ticket, that is a labeled list of real user questions with known correct pages. run every option against it before you commit. current search, a managed platform on trial, an assistant over the docs. score how often the right page lands in the top three.
>
> that turns the migration debate into a number, and it keeps running as a regression test after you ship.
>
> did the tagging record the page, or only that an answer existed?

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
