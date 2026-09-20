---
type: "corpus"
item_id: "84887b4256bda38a"
title: "I created a web app to help people get over PE, but I am not sure how to market it"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/SaaS/comments/1wi4195/i_created_a_web_app_to_help_people_get_over_pe/"
author: "Odd-Tradition7713"
published_at: "2026-09-17T01:36:32+08:00"
captured_at: "2026-09-20T14:13:34+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-20"
pub_day: "2026-09-17"
tags:
  - 语料
  - reddit
  - r/SaaS
metrics: {"score": 3, "comments": 6, "upvote_ratio": 1}
comments_count: 6
comments_total: 6
discovered_via: "reddit:7d+settle3"
---

# I created a web app to help people get over PE, but I am not sure how to market it

> [!info] 一句话导读
> I have been working on this web app to help people beat PE. About 30% of men suffer from it, and most of them don’t even know it’s possible to fix without pills…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/SaaS/comments/1wi4195/i_created_a_web_app_to_help_people_get_over_pe/>
> 指标：得分=3 · 评论=6 · 赞踩比=1
> 作者：Odd-Tradition7713　|　发布：2026-09-17T01:36:32+08:00
> 项目链接：—
> 采集：2026-09-20T14:13:34+08:00　|　id：`84887b4256bda38a`

## 正文

Hey all,
I have been working on this web app to help people beat PE. About 30% of men suffer from it, and most of them don’t even know it’s possible to fix without pills.
I created a basic free version just for fun and launched it. It was frontend only, so I have no logs except for the logs from the server provider, which shows a steady 300-500 requests a day. Assuming a user makes 10 requests a day (which is a lot considering the nature of the app), that’s about 30-50 users.
And, I have a donation button, and 5 people already donated 40$, so I know people are willing to pay for it.

I am about to launch the new version. It’s better, more secure, and has a bunch of new features, including the ability to create accounts (so their data is never lost). The base app & accounts are free forever, that was a promise I made that I will not break.

I created a premium plan that includes a few extra features and any future feature I will launch that isn’t in the free plan. I priced it on the low end compared to similar apps and products out there (about 50% lower). That’s because A. I don’t think I give enough value now that will justify a higher price, B. I want to get paid customers, and C. I can always increase the price for new users in the future.

The nature of the app means users will not share it with each other in person. Only on forums, subreddits, and stuff like that.

Which is why I am here. I don’t know how to market it.
Only thing I can think of is making reddit posts that promote it, but there are not many places I can do that.
What would you do to market something people are awkward to admit/talk about?

If I forgot to mention anything that will help, please let me know and I will update the post

## 评论（6/6）

> **daniel933912**（2 分） · 2026-09-17T01:42:39+08:00　
> Your free version ran frontend only, so you can't tell which of those 300-500 daily requests came from search, a forum thread, or one person refreshing all day. Wire up referrer tracking before you launch premium, two weeks of that will beat any marketing plan.
>
> And $40 from five donations isn't proof anyone will pay monthly. The five who donated already got what they came for. Someone entering card details for something they're embarrassed about is paying for discretion. Gratitude doesn't renew.

---

> **SecureTangerine5419**（0 分） · 2026-09-17T02:27:19+08:00　
> Reddit is basically built for this use case, so you're on the right track. Find the subreddits where guys are already talking about it, read the threads, and when someone asks "is there anything that actually works without medication" you reply genuinely and mention your app. You've got 5 donors already which means word of mouth is happening somewhere, so figure out where those people came from and scale it.

---

> **Odd-Tradition7713**（1 分） · 2026-09-17T02:53:08+08:00　
> Okay, I hear you. Can you elaborate on the referrer tracking? Should I create an analytics board as well, to track where users are coming from?

---

> **Material-Swimmer-776**（1 分） · 2026-09-17T05:37:03+08:00　
> the point about gratitude not renewing is so real, donating once and committing monthly are completely different decisions

---

> **daniel933912**（1 分） · 2026-09-17T19:42:48+08:00　
> Referrer headers come back empty from in-app browsers and privacy modes, so tag the links you post yourself with a utm_source, that channel you can control. The other half is counting people, one session id on page load tells you whether those 300-500 hits are 40 people or 6, which server logs never show. Hold off on the dashboard, a sheet with date, source and signups is enough for two weeks. Now that accounts are mandatory, can you tie signup back to source in the same sheet?

---

> **daniel933912**（1 分） · 2026-09-17T20:37:00+08:00　
> Pull the donation dates apart. Five gifts inside a day of the same post is one good moment, spread over three weeks it's people coming back to the problem on their own.

## 导航

- 项目页：[[10-项目/I-created-a-web-app-to-help-people-get-over-PE,_84887b42]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
