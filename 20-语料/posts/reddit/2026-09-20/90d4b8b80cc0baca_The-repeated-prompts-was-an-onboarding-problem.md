---
type: "corpus"
item_id: "90d4b8b80cc0baca"
title: "The repeated prompts was an onboarding problem"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/SaaS/comments/1wi68ns/the_repeated_prompts_was_an_onboarding_problem/"
author: "Real-Mix-7055"
published_at: "2026-09-17T02:54:42+08:00"
captured_at: "2026-09-20T14:13:41+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-17"
tags:
  - 语料
  - reddit
  - r/SaaS
metrics: {"score": 12, "comments": 7, "upvote_ratio": 1}
comments_count: 7
comments_total: 7
discovered_via: "reddit:7d+settle3"
---

# The repeated prompts was an onboarding problem

> [!info] 一句话导读
> People kept rephrasing the same request three or four times. The first response was technically correct but it never made the next step obvious. Support macros …

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/SaaS/comments/1wi68ns/the_repeated_prompts_was_an_onboarding_problem/>
> 指标：得分=12 · 评论=7 · 赞踩比=1
> 作者：Real-Mix-7055　|　发布：2026-09-17T02:54:42+08:00
> 项目链接：—
> 采集：2026-09-20T14:13:41+08:00　|　id：`90d4b8b80cc0baca`

## 正文

People kept rephrasing the same request three or four times. The first response was technically correct but it never made the next step obvious. Support macros had described the same issue for months, yet we had no shared view of the pattern.

We used Braintrust to have trace filters to separate task retries from exploration. The pattern was concentrated in newer accounts and lined up with lower activation. Reviewing representative sessions made the cause pretty concrete. People were not asking for a new capability, but rather trying to discover what the current one could do.

After that, we changed the onboarding flow and the first response so it names the next valid actions in plain language. Repeat attempts fell and CX could finally explain the change without a folder of screenshots. How are other teams distinguishing healthy exploration from repeated prompts that signal an unclear path?

## 评论（7/7）

> **CauseNo254**（2 分） · 2026-09-17T03:01:12+08:00　
> Did support already suspect this was an onboarding issue, or did the trace review change their mind?

---

> **Affectionate_Log1745**（2 分） · 2026-09-17T03:06:55+08:00　
> Support macros being ahead of the product signal is kind of telling. They had already seen the pattern, it just wasn’t connected to product data yet.

---

> **Primary-Life-4291**（1 分） · 2026-09-17T03:21:34+08:00　
> If people keep rephrasing after a technically correct answer, that usually means the response did not reduce uncertainty enough for them to act

---

> **Real-Mix-7055**（2 分） · 2026-09-17T03:27:11+08:00　
> They had been seeing it for a while, but we didn’t really know how widespread it was until we looked at the traces.

---

> **Real-Mix-7055**（2 分） · 2026-09-17T03:30:26+08:00　
> Pretty much. CX knew something was off before we had a clean way to measure it.

---

> **daniel933912**（1 分） · 2026-09-17T04:37:51+08:00　
> The newer-account cluster you found is the easiest place to split retry from exploration, and the signal sits in the second prompt. Above roughly 0.8 token overlap with the first one, arriving a few seconds later with nothing clicked in between, means the person is re-lexing the same request and the intent has not moved. Exploration looks different, the follow-up carries a new entity, a new constraint or a date range and the slots actually change. Tag every follow-up with that overlap score and the time gap, then read activation off that instead of raw repeat count. Did the repeats in those newer accounts ever touch the output at all, or did they just keep typing?

---

> **Real-Mix-7055**（1 分） · 2026-09-17T06:56:20+08:00　
> Mostly they just kept typing. That’s part of what made the onboarding angle stand out.

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
