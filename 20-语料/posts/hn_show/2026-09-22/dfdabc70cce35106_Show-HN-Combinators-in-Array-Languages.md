---
type: "corpus"
item_id: "dfdabc70cce35106"
title: "Show HN: Combinators in Array Languages"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49790937"
project_url: "https://blog.softwarewrighter.com/2026/09/21/rabbit-hole-sage-y-combinator"
author: "softwarewright"
published_at: "2026-09-21T18:03:58Z"
captured_at: "2026-09-22T12:53:31+08:00"
lang: "en"
kind: "post"
topic: 内容/媒体
shard: "2026-09-22"
pub_day: "2026-09-21"
tags:
  - 语料
  - hn_show
  - author_softwarewright
  - story_49790937
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Combinators in Array Languages

> [!info] 一句话导读
> Raymond Smullyan’s "To Mock a Mockingbird" book's aviary of combinator birds implemented in APL-derived languages and the problem implementing the Sage bird (Fi…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49790937>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：softwarewright　|　发布：2026-09-21T18:03:58Z
> 项目链接：<https://blog.softwarewrighter.com/2026/09/21/rabbit-hole-sage-y-combinator>
> 采集：2026-09-22T12:53:31+08:00　|　id：`dfdabc70cce35106`

## 正文

Raymond Smullyan’s "To Mock a Mockingbird" book's aviary of combinator birds implemented in APL-derived languages and the problem implementing the Sage bird (Fixed Point or Y combinator) in an eagerly evaluated language.Newer APLs support lazy evaluation. My eager language has a workaround for this. The Z combinator is the standard strict-language fix: wrap the self-application in one extra function layer (λv. x x v), so the recursion is a value (a delayed call) rather than an executing expression. sw-MLPL expresses that delay as a named partial — z_step/z_recur/applicative_sage — because the language has no anonymous lambdas.Z has no Smullyan name (and no zebra in the aviary, despite the letter). The book predates and ignores the strictness problem, so it has no applicative-order variant. "Z combinator" is programmer folklore for the eta-expanded Y

## 导航

- 项目页：[[10-项目/blog.softwarewrighter.com_ba931d31]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`内容/媒体`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
