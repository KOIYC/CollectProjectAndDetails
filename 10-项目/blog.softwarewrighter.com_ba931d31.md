---
type: "project"
title: "Show HN: Combinators in Array Languages"
project_url: "https://blog.softwarewrighter.com/2026/09/21/rabbit-hole-sage-y-combinator"
first_seen: "2026-09-22T12:53:31+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_softwarewright
  - story_49790937
  - show_hn
lang: "en"
---

# Show HN: Combinators in Array Languages

> [!info] 一句话导读
> Raymond Smullyan’s "To Mock a Mockingbird" book's aviary of combinator birds implemented in APL-derived languages and the problem implementing the Sage bird (Fi…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://blog.softwarewrighter.com/2026/09/21/rabbit-hole-sage-y-combinator>
> 首次收录：2026-09-22T12:53:31+08:00
> 来源渠道：HN Show HN
> 标签：author_softwarewright, story_49790937, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-22T12:53:31+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-22/dfdabc70cce35106_Show-HN-Combinators-in-Array-Languages]] |

## 摘要正文

Raymond Smullyan’s "To Mock a Mockingbird" book's aviary of combinator birds implemented in APL-derived languages and the problem implementing the Sage bird (Fixed Point or Y combinator) in an eagerly evaluated language.Newer APLs support lazy evaluation. My eager language has a workaround for this. The Z combinator is the standard strict-language fix: wrap the self-application in one extra function layer (λv. x x v), so the recursion is a value (a delayed call) rather than an executing expression. sw-MLPL expresses that delay as a named partial — z_step/z_recur/applicative_sage — because the language has no anonymous lambdas.Z has no Smullyan name (and no zebra in the aviary, despite the letter). The book predates and ignores the strictness problem, so it has no applicative-order variant. "Z combinator" is programmer folklore for the eta-expanded Y
