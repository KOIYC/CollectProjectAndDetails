---
type: "project"
title: "Show HN: Gatekeeper – Persuade a 34MB Jev-like model to let you into the castle"
project_url: "https://gatekeeper.dopp.sh/"
first_seen: "2026-10-01T09:41:49+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_mazlix
  - story_49912849
  - show_hn
lang: "en"
---

# Show HN: Gatekeeper – Persuade a 34MB Jev-like model to let you into the castle

> [!info] 一句话导读
> Upfront caveat: it's English only! but I'm personally still just amazed that 34MB (fine-tuned BAAI/bge-small-en-v1.5 ) can fit so much knowledge that it's possi…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://gatekeeper.dopp.sh/>
> 首次收录：2026-10-01T09:41:49+08:00
> 来源渠道：HN Show HN
> 标签：author_mazlix, story_49912849, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-01T09:41:49+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-10-01/31bd6b4ccdadcf3f_Show-HN-Gatekeeper-–-Persuade-a-34MB-Jev-like-mode]] |

## 摘要正文

Upfront caveat: it's English only! but I'm personally still just amazed that 34MB (fine-tuned BAAI/bge-small-en-v1.5 ) can fit so much knowledge that it's possible to have an iPhone 15 running these classifications entirely client-side on arbitrary english text in 10-30ms.The game is a little trivial but thought it was a cool showcase, you type messages to the guard and they get classified as either friendly, bribe, threats, etc.I've been playing a lot with Jev use-cases since it came out and then learned about fine-tuning my own models.The way I went about it was just using Jev first via a proxy to record my calls and store them as my own training data to make running training easier. I built a whole oss platform around doing that with models (of various sizes) https://github.com/doppsh/dopp.Would love to hear any feedback / discuss more on either that whole training process or the game itself.Also I did get a ton of help from Opus doing all this, so some things might be a little rough around some edges but plenty of human time has been put in too. Very welcoming of any feedback/criticism
