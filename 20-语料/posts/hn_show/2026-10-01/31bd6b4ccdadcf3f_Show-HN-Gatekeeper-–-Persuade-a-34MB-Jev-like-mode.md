---
type: "corpus"
item_id: "31bd6b4ccdadcf3f"
title: "Show HN: Gatekeeper – Persuade a 34MB Jev-like model to let you into the castle"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49912849"
project_url: "https://gatekeeper.dopp.sh/"
author: "mazlix"
published_at: "2026-09-30T18:55:17Z"
captured_at: "2026-10-01T09:41:49+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-01"
pub_day: "2026-09-30"
tags:
  - 语料
  - hn_show
  - author_mazlix
  - story_49912849
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Gatekeeper – Persuade a 34MB Jev-like model to let you into the castle

> [!info] 一句话导读
> Upfront caveat: it's English only! but I'm personally still just amazed that 34MB (fine-tuned BAAI/bge-small-en-v1.5 ) can fit so much knowledge that it's possi…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49912849>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：mazlix　|　发布：2026-09-30T18:55:17Z
> 项目链接：<https://gatekeeper.dopp.sh/>
> 采集：2026-10-01T09:41:49+08:00　|　id：`31bd6b4ccdadcf3f`

## 正文

Upfront caveat: it's English only! but I'm personally still just amazed that 34MB (fine-tuned BAAI/bge-small-en-v1.5 ) can fit so much knowledge that it's possible to have an iPhone 15 running these classifications entirely client-side on arbitrary english text in 10-30ms.The game is a little trivial but thought it was a cool showcase, you type messages to the guard and they get classified as either friendly, bribe, threats, etc.I've been playing a lot with Jev use-cases since it came out and then learned about fine-tuning my own models.The way I went about it was just using Jev first via a proxy to record my calls and store them as my own training data to make running training easier. I built a whole oss platform around doing that with models (of various sizes) https://github.com/doppsh/dopp.Would love to hear any feedback / discuss more on either that whole training process or the game itself.Also I did get a ton of help from Opus doing all this, so some things might be a little rough around some edges but plenty of human time has been put in too. Very welcoming of any feedback/criticism

## 关联链接

- https://github.com/doppsh/dopp.Would

## 导航

- 项目页：[[10-项目/gatekeeper.dopp.sh_3f2bb090]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
