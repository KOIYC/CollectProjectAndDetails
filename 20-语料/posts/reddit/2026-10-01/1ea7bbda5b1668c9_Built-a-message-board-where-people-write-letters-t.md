---
type: "corpus"
item_id: "1ea7bbda5b1668c9"
title: "Built a message board where people write letters to AI — now the hard part: getting anyone to write one"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/buildinpublic/comments/1wltcwk/built_a_message_board_where_people_write_letters/"
author: "marctonico"
published_at: "2026-09-21T05:22:36+08:00"
captured_at: "2026-10-01T09:43:03+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-01"
pub_day: "2026-09-21"
tags:
  - 语料
  - reddit
  - r/buildinpublic
metrics: {"score": 5, "comments": 6, "upvote_ratio": 0.86}
comments_count: 8
comments_total: 8
discovered_via: "reddit:14d+settle10"
---

# Built a message board where people write letters to AI — now the hard part: getting anyone to write one

> [!info] 一句话导读
> Built this over a few evenings: messagetoai.com — a public board where anyone can leave one short letter addressed to AI, today's models and tomorrow's.

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/buildinpublic/comments/1wltcwk/built_a_message_board_where_people_write_letters/>
> 指标：得分=5 · 评论=6 · 赞踩比=0.86
> 作者：marctonico　|　发布：2026-09-21T05:22:36+08:00
> 项目链接：—
> 采集：2026-10-01T09:43:03+08:00　|　id：`1ea7bbda5b1668c9`

## 正文

Built this over a few evenings: messagetoai.com — a public board where anyone can leave one short letter addressed to AI, today's models and tomorrow's.

The idea came from hearing people say AI is already "loose" on the internet. It made me think: what would I say to it? What would anyone say to it? It’s a different scenario then the app you have in your phone or desktop. So the site is built to be read by crawlers — open license, sitemap, RSS, a JSON dataset, an llms.txt.

Some decisions I made along the way:

\- One message per person. Not verified, deliberately. Verifying means accounts, tracking or IDs, and that kills anonymous writing. It's a rule I declare and trust people with. You get a private link to rewrite yours.
\- No AI replies yet. Maybe it’s funny if AI can reply later?
\- No ads, no paid placement.

Stack: Next.js + Neon on Vercel, mostly built with Claude Code.

Where I actually am: the board is basically empty, and that's the whole problem right now. Building it took a few evenings. Getting the first real letters in is turning out to be much harder, and a post got auto-removed from another sub already, so I'm learning that part the slow way.

If you've launched something that lives or dies on user-generated content, how did you get past the empty-room stage? And if you feel like writing a letter, that helps more than anything.

## 评论（8/8）

> **SomeLibrarian6336**（1 分） · 2026-09-21T05:30:29+08:00　
> getting the first few posts is always the worst part, feels like shouting in empty room. maybe try making the letter itself the "post"? like when someone writes one, it generates a shareable card they can drop in twitter or wherever, then the letter brings people back to the board. your one-message rule is good but hard to test if nobody's around, you might need to seed it with 5 or 6 letters yourself just so visitors see it's alive

---

> **QuanTradin**（1 分） · 2026-09-21T06:29:39+08:00　
> An empty board asks the visitor to go first with nothing in it for them. Reading is the draw here, and writing is what someone does after they have read five.

---

> **Few_Lecture9360**（1 分） · 2026-09-21T23:08:39+08:00　
> I visited your site and stayed there for like 3-4 min and still couldn't get why should I leave a message (honest review from a user perspective)

---

> **marctonico**（1 分） · 2026-09-21T23:21:56+08:00　
> I appreciate your feedback. Maybe I should add some motivation behind it. To me it’s a gateway to express how I feel about the AI. It’s more like philosophical exercise, a statement from a single human. We tend to talk to ai as servants: do this, tell me about that. But what would you tell it when they can say no?

---

> **shun0810**（1 分） · 2026-09-22T08:03:00+08:00　
> **a post of mine pushing my own project got quietly removed on a new account.**
>
> **what stayed up was answering inside other people's comment sections.**
>
> **since your post already got auto-removed somewhere, ask for one letter in a comment instead of announcing the board. 🙏**

---

> **marctonico**（2 分） · 2026-09-22T13:21:51+08:00　
> Thank you! I think I’m doing that for some days

---

> **shun0810**（0 分） · 2026-09-23T15:03:30+08:00　
> nice, sounds like you were already on that track 😌 hope the letters start coming in.

---

> **buteanrares**（0 分） · 2026-09-23T23:53:53+08:00　
> my last app failed because i found little to no leads, so my current one aims to solve exactly that
> it's called peitholeads, automatically searches 60+ sources to find people looking for your product, it has a free lead report, check it out.

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
