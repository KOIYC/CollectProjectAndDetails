---
type: "corpus"
item_id: "bce6690cd8dca09f"
title: "Show HN: Obvelum – an anonymous hiring portal where companies apply to you"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48733739"
project_url: "https://obvelum.com/"
author: "aviscido"
published_at: "2026-06-30T15:04:16Z"
captured_at: "2026-09-21T01:44:21+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-21"
pub_day: "2026-06-30"
tags:
  - 语料
  - hn_show
  - author_aviscido
  - story_48733739
  - show_hn
metrics: {"points": 2, "comments": 1, "engagement_velocity": 2}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:113d"
---

# Show HN: Obvelum – an anonymous hiring portal where companies apply to you

> [!info] 一句话导读
> Obvelum is a job platform where you don't apply - companies apply to you, and they don't know (in principle) who you are. You create by yourself an anonymous pr…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48733739>
> 指标：点赞=2 · 评论=1 · engagement_velocity=2
> 作者：aviscido　|　发布：2026-06-30T15:04:16Z
> 项目链接：<https://obvelum.com/>
> 采集：2026-09-21T01:44:21+08:00　|　id：`bce6690cd8dca09f`

## 正文

Obvelum is a job platform where you don't apply - companies apply to you, and they don't know (in principle) who you are. You create by yourself an anonymous profile, mark yourself open, and companies could reach out to you based on what you can do. They only learn your name if you decide to tell them, and only after you've seen what the role is about (and what it pays).regarding the privacy:- Your name doesn't come out until you choose to release it, and a company has to show salary and role details first.
- Auth is self-hosted Zitadel. Google sign-in requests only openid+email, no profile scope, so Google never hands us your name. Email sign-up stores just the email address itself.
- Analytics is self-hosted Umami, anonymous. Cookies are functional only.The part I actually want comment about is the threat model: your current employer. They already know your salary, your stack, your seniority, and which tag points at them; so to them your profile is basically a name tag, even though it's anonymous to a stranger. I let you block companies, but I don't think that closes it, and with small enough fields almost any profile is unique. If you can see how to fix that, or break anything else, tell me. I don't have a security background and I'd rather find out now.
About 100 profiles so far with little marketing.

## 评论（1/1）

> **aviscido** · 2026-06-30T16:18:14.000Z　
> If you're interested in knowing a bit more, there's an architectural summary here:https://www.obvelum.com/architecture

## 导航

- 项目页：[[10-项目/obvelum.com_7a5353e5]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
