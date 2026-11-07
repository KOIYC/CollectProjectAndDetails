---
type: "corpus"
item_id: "89b66622a1a5f9f5"
title: "Cancelled every paid AI video tool I had. Built a free one that draws my explainer reels from one sentence instead. Ride along."
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/EntrepreneurRideAlong/comments/1xh3512/cancelled_every_paid_ai_video_tool_i_had_built_a/"
author: "_haiderfarooq"
published_at: "2026-10-28T04:03:34+08:00"
captured_at: "2026-11-07T09:44:37+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-07"
pub_day: "2026-10-28"
tags:
  - 语料
  - reddit
  - r/EntrepreneurRideAlong
  - Ride Along Story
metrics: {"score": 7, "comments": 9, "upvote_ratio": 0.8181818181818182}
comments_count: 7
comments_total: 9
discovered_via: "reddit:14d+settle10"
---

# Cancelled every paid AI video tool I had. Built a free one that draws my explainer reels from one sentence instead. Ride along.

> [!info] 一句话导读
> Short ride along. I make explainer and product spotlight reels, and I was paying for AI video tools to do it. The clips looked like everyone else's AI clips and…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/EntrepreneurRideAlong/comments/1xh3512/cancelled_every_paid_ai_video_tool_i_had_built_a/>
> 指标：得分=7 · 评论=9 · 赞踩比=0.8181818181818182
> 作者：_haiderfarooq　|　发布：2026-10-28T04:03:34+08:00
> 项目链接：—
> 采集：2026-11-07T09:44:37+08:00　|　id：`89b66622a1a5f9f5`

## 正文

Short ride along. I make explainer and product spotlight reels, and I was paying for AI video tools to do it. The clips looked like everyone else's AI clips and I was still doing most of the work by hand around them. So I cancelled all of them and built the thing I actually needed.

What it does: you type one line about what the reel should say. It writes a six or seven line script, reads it in a free voice, and draws every scene in code: paper cutout props, a small mascot in a different hat each scene, a headline sign, captions that pop on each word, all timed to the voice. One command renders the video. About a minute on a laptop, no credits, no watermark.

Why paper cutouts: it's a style, not a failed attempt at realism. People can tell it's drawn, and that reads as made on purpose. It fits explainers, how it works reels and product spotlights. It does not fit anything that needs real footage or a face.

The honest catch: the first render is never right. You look at it, say what to move, and render again. Two or three rounds is normal. It also runs inside the AI coding assistants (Claude Code, Codex or Gemini) on a Mac, so if you don't already use one of those it's not for you yet.

I open sourced it, free, no account needed. Links aren't allowed here so: it's called paper-reel, it's on GitHub under my name, and the link is on my profile.

Happy to answer questions about the workflow or what it's bad at.

## 评论（7/9）

> **Quiet-Carpet-**（1 分） · 2026-10-28T08:40:08+08:00　
> Pretty cool! but how does it handle revisions when the script or scene needs changing?

---

> **_haiderfarooq**（1 分） · 2026-10-28T17:54:07+08:00　
> everything is text so a revision is an edit, not a regen. the script is a json file with one line per scene, and each scene is a small block of code. change a line and it regenerates the voice for just that line and retimes the words, so the props still land on the right word. change a scene and you just render again. first version is never right, usually two or three rounds.

---

> **Bitter_Regular7406**（1 分） · 2026-10-28T19:31:31+08:00　
> the "it's a style not a failed attempt at realism" line is the whole game tbh, so many AI video tools are fighting an uphill battle trying to look real and just end up in uncanny valley hell. leaning into a recognizable art style instead of chasing photoreal is the smarter move imo.

---

> **_haiderfarooq**（1 分） · 2026-10-29T05:55:23+08:00　
> yeah that was the unlock for me. once it stopped trying to look real, people stopped judging it as a bad real video and just watched it

---

> **Bitter_Regular7406**（1 分） · 2026-10-29T06:22:04+08:00　
> yeah the judgment criteria completely shifts once you remove "is this real" from the equation. same reason cartoons and anime never had to deal with uncanny valley, nobody's comparing it to reality in their head while watching.

---

> **AutoModerator**（1 分） · 2026-10-30T13:03:41+08:00　
> Your [comment](https://www.reddit.com/r/EntrepreneurRideAlong/comments/1xh3512/cancelled_every_paid_ai_video_tool_i_had_built_a/19rv53t265f8i/) in /r/EntrepreneurRideAlong was automatically removed because it contained a URL or a markdown link.
>
> To keep our community focused and prevent spam, we do not allow URLs or links (including Reddit internal links) in comments at this time.
> If you believe this removal was a mistake, please [contact the moderators](https://www.reddit.com/message/compose?to=/r/EntrepreneurRideAlong).
>
> *I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/EntrepreneurRideAlong) if you have any questions or concerns.*

---

> **JamesAtKindword**（1 分） · 2026-10-31T06:01:39+08:00　
> i like that you went for a deliberately drawn style instead of trying to make everything look realistic. Does it let you keep the same character and visual style consistent across multiple videos?

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
