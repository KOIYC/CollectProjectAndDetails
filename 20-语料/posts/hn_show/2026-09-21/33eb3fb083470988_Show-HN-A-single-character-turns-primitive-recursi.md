---
type: "corpus"
item_id: "33eb3fb083470988"
title: "Show HN: A single character turns primitive recursion into general recursion"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49113798"
project_url: "https://github.com/raoofha/pr"
author: "raoof"
published_at: "2026-07-30T18:30:50Z"
captured_at: "2026-09-21T03:11:13+08:00"
lang: "en"
kind: "post"
topic: "未分类"
shard: "2026-09-21"
pub_day: "2026-07-30"
tags:
  - 语料
  - hn_show
  - author_raoof
  - story_49113798
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:83d"
---

# Show HN: A single character turns primitive recursion into general recursion

> [!info] 一句话导读
> a single character turns a universal primitive recursive function into a universal general recursive function

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49113798>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：raoof　|　发布：2026-07-30T18:30:50Z
> 项目链接：<https://github.com/raoofha/pr>
> 采集：2026-09-21T03:11:13+08:00　|　id：`33eb3fb083470988`

## 正文

# raoofha/pr

a single character turns a universal primitive recursive function into a universal general recursive function

- Stars: 0
- Forks: 0
- Watchers: 0
- Open issues: 0
- Default branch: main
- Created: 2026-07-30T17:19:44Z

## Languages

- Haskell

## Top Contributors

- raoofha (3 contributions)

---

## README

# a single character change a universal primitive recursive function into a universal general recursive function
an implementation of LOOP programming language as a list of pairs of natural numbers
* 0 0 -- noop
* r 0 -- inc r
* 0 r -- dec r
* r p -- repeat program number p r times

```hs
_pr :: Natural -> [(Natural,Natural)] -> [Natural] -> [Natural]
_pr i p rs =
  if i < (fromIntegral (length p)) then
    let
      (op1,op2) = (p!!(fromIntegral i))
      _op1 = (fromIntegral (op1-1))
      _op2 = (fromIntegral (op2-1))
      _i = (fromIntegral i)
      vop1 = (listGet rs _op1 0)
      vop2 = (listGet rs _op2 0)
    in
      if op1 /= 0 && op2 /= 0 then 
        let q = (map cantorUnpair (cantorUnpairAll op2)) -- changing op2 to vop2 enable self-reference and pr becomes a universal general recursive function
        in _pr (i+1) p ((iterate (\rs -> _pr 0 q rs) rs)!!(fromIntegral vop1))
      else if op1==0 && op2==0 then rs
      else if op2==0 then _pr (i+1) p (listSet rs _op1 (vop1 +1))
      else _pr (i+1) p (listSet rs _op2 (if vop2>0 then vop2-1 else 0))
  else rs

pr rs = 
  case (map cantorUnpair (cantorUnpairAll (listGet rs 0 0))) of
    []-> listGet (_pr 0 [(0,0)] (tail rs)) 0 0
    q -> listGet (_pr 0 q (tail rs)) 0 0
```

## 导航

- 项目页：[[10-项目/github.com_211b6fa7]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`未分类`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
