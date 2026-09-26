---
type: "corpus"
item_id: "068ff250398a3ec9"
title: "Show HN: Misheard turns \"recognize speech\" into \"wreck a nice beach\""
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49845788"
project_url: "https://wordlab.rickinto.place/misheard"
author: "rickintoplace"
published_at: "2026-09-25T15:14:25Z"
captured_at: "2026-09-26T09:41:08+08:00"
lang: "en"
kind: "post"
topic: AI 工具/Agent
shard: "2026-09-26"
pub_day: "2026-09-25"
tags:
  - 语料
  - hn_show
  - author_rickintoplace
  - story_49845788
  - show_hn
metrics: {"points": 2, "comments": 3, "engagement_velocity": 2}
comments_count: 3
comments_total: 3
discovered_via: "hn:show_hn:3d"
---

# Show HN: Misheard turns "recognize speech" into "wreck a nice beach"

> [!info] 一句话导读
> Type anything. The output below sounds like what you typed.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49845788>
> 指标：点赞=2 · 评论=3 · engagement_velocity=2
> 作者：rickintoplace　|　发布：2026-09-25T15:14:25Z
> 项目链接：<https://wordlab.rickinto.place/misheard>
> 采集：2026-09-26T09:41:08+08:00　|　id：`068ff250398a3ec9`

## 正文

wordlab
Spoonerize
 Misheard
Type anything. The output below sounds like what you typed.
Mishear it
Settings
Pronunciations from the CMU Pronouncing Dictionary ,
 word frequencies from OpenSubtitles ,
 word pairs counted in 40 million lines of OpenSubtitles .
 Confusion costs start from Miller & Nicely (1955)
 and depend on the neighbouring sounds.
Privacy & imprint
 rickinto.place

## 评论（3/3）

> **rickintoplace** · 2026-09-25T15:16:58.000Z　
> I initially built this as a toy and it turned into an interesting small phonetics project.Enter a sentence and it finds other ways to break down the same sounds into English words: “kiss the sky” gives you “kiss this guy”. “Four candles” turns to “fork handles”. “Ice bank mice elf” ... I think you get the ideaEach word is looked up in the CMU Pronouncing Dictionary. The sentence is converted into a sequence of phonemes, and a beam search breaks it back down into words. Exact re-parsing is rare, so sounds may be distorted under certain conditions. For example, keep in mind that a double consonant at a word boundary sounds like a single one (mistake/miss steak). A /ɡ/ before a nasal almost completely disappears (recognize -> “reco'nize”). The sound alone is not enough to distinguish “wreck a nice beach” from “reckon eyes beach,” so variations that actually appear in 40 million lines of movie subtitles are also taken into account.The system was calibrated using 42 known oronyms (38 in the top 12, 25 in first place), and I disabled each rule individually to see how much it contributed.What doesn’t work: long sentences, proper nouns (“Euthanasia” -> “Youth in Asia” is impossible, since names are filtered out), and it only works with American English, since CMUdict only contains that.Static site, no server, no LLM. Code: https://github.com/rickintoplace/wordlab

---

> **4d4m** · 2026-09-25T17:32:07.000Z　
> Neat, and weirdly useful for refining lyrics in the same way I'd use a rhyming dictionary on occasion.

---

> **rickintoplace** · 2026-09-25T18:03:54.000Z　
> Thanks :)
> I'm also building a tool for spoonerisms that might be useful for rhyming:
> https://wordlab.rickinto.place/spoonerizeIt uses the same data as the misheard tool and produces cross-pairs like these:
> Be known
> Knee boneNo guts
> Go nutsAnd there is a rude word filter for SFW that can also be inverted for extra "edginess"

## 导航

- 项目页：[[10-项目/wordlab.rickinto.place_c866a64c]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
