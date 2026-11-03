---
type: "corpus"
item_id: "9b95ffd10351b682"
title: "Race Ratings - I couldn't find a Yelp for triathlons and marathons, so I built one from ~5,800 race reports"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/SideProject/comments/1xdw14a/race_ratings_i_couldnt_find_a_yelp_for_triathlons/"
project_url: "https://moku.coach/race-ratings"
author: "cullenp768"
published_at: "2026-10-24T09:38:23+08:00"
captured_at: "2026-11-03T09:41:54+08:00"
lang: "en"
kind: "post"
topic: AI 工具/Agent
shard: "2026-11-03"
pub_day: "2026-10-24"
tags:
  - 语料
  - reddit
  - r/SideProject
metrics: {"score": 6, "comments": 9, "upvote_ratio": 1}
comments_count: 7
comments_total: 9
discovered_via: "reddit:14d+settle10"
---

# Race Ratings - I couldn't find a Yelp for triathlons and marathons, so I built one from ~5,800 race reports

> [!info] 一句话导读
> I've been looking for a Yelp-style place to check out triathlons and marathons before signing up and couldn't find one. The info is out there, it's just scatter…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/SideProject/comments/1xdw14a/race_ratings_i_couldnt_find_a_yelp_for_triathlons/>
> 指标：得分=6 · 评论=9 · 赞踩比=1
> 作者：cullenp768　|　发布：2026-10-24T09:38:23+08:00
> 项目链接：<https://moku.coach/race-ratings>
> 采集：2026-11-03T09:41:54+08:00　|　id：`9b95ffd10351b682`

## 正文

I've been looking for a Yelp-style place to check out triathlons and marathons before signing up and couldn't find one. The info is out there, it's just scattered across race reports on personal blogs, Slowtwitch threads, review sites and hotel reviews.

So I pulled it together. Right now it covers 1,079 races: 116 full-distance and 221 70.3 triathlons, 164 Olympic, 230 sprint, 297 marathons and 51 ultras, built from about 5,800 reports and reviews. Every race gets a 1-5 score on things like swim, bike, run, conditions and travel, and each review links back to where it came from. You can filter for stuff like flat bike courses, wetsuit-legal swims or first-timer friendly races, and compare up to three side by side.

https://moku.coach/race-ratings/

Full disclosure: it lives on the site for Moku Coach, the training app my cofounder and I are building. The ratings are free and you don't need an account to browse.

Two things I'd love help with:

- If you've raced one of these, leave a review on its page. A lot of races only have a handful of reports, so first-hand reviews help a ton.
- If a score looks off for a race you know, tell me. I'd rather fix it than leave it wrong.

Any feedback on the site itself is welcome too.

## 评论（7/9）

> **Fast_Wrap930**（1 分） · 2026-10-24T10:01:44+08:00　
> Linking each review back to its source is a useful touch. One thing I’d look for beside each score is the number of reports and the race years they cover. A 4.5 from two older reports is quite different from a 4.5 across 80 recent ones. Could you also separate editions when a course or organizer changes? That would make the side-by-side comparison easier to trust.

---

> **QuanTradin**（0 分） · 2026-10-24T10:26:24+08:00　
> pulling 5,800 scattered reports into one score sounds like months of cleanup. how do you handle races that changed course since the older reviews were written?

---

> **smithey2012**（1 分） · 2026-10-24T10:36:12+08:00　
> No it doesn’t, grok can do that for you within an hour or two.

---

> **CutDry6295**（1 分） · 2026-10-24T11:45:22+08:00　
> The source links are a good start. Since course conditions and race organization can change each year, I would show the year and number of reports beside each category score. A 4.5 from two older reports should look different from a 4.5 from thirty recent ones. An easy “this course changed” flag could also help keep the wetsuit/terrain filters trustworthy. I have not raced these events, so this is feedback on how I would evaluate the ratings.

---

> **cullenp768**（2 分） · 2026-10-24T21:12:27+08:00　
> Yup yup. I had a swarm of agents searching across the internet to help me aggregate qualitative feedback into quantitative.

---

> **cullenp768**（1 分） · 2026-10-24T21:12:31+08:00　
> There's an evidence label and every review shows year raced but personally I don't think course changes really impact the fundamentals of the ratings and feedback. There's always exceptions of course.

---

> **QuanTradin**（1 分） · 2026-10-24T21:26:00+08:00　
> grok gets you the pile fast. the slow part is matching, same race under three names, or a course that moved two years ago and still carries the old reviews.

## 关联链接

- https://moku.coach/race-ratings/

## 导航

- 项目页：[[10-项目/moku.coach_afd1b67d]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
