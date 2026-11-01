---
type: "corpus"
item_id: "a2e81c2156f99d2b"
title: "I built a social app for just your actual friends: no algorithm, no strangers. Looking for honest feedback."
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/buildinpublic/comments/1xc1o5h/i_built_a_social_app_for_just_your_actual_friends/"
project_url: "https://v.redd.it/7lsifi0n2wwh1"
author: "FriendTechLLC"
published_at: "2026-10-22T06:36:35+08:00"
captured_at: "2026-11-01T09:39:33+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-11-01"
pub_day: "2026-10-22"
tags:
  - 语料
  - reddit
  - r/buildinpublic
metrics: {"score": 3, "comments": 1, "upvote_ratio": 1}
comments_count: 1
comments_total: 1
discovered_via: "reddit:14d+settle10"
---

# I built a social app for just your actual friends: no algorithm, no strangers. Looking for honest feedback.

> [!info] 一句话导读
> I’ve been building FRiENDS, a social app that’s only the people you actually know: no algorithm, no strangers. It just went live on both stores, so here’s the b…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/buildinpublic/comments/1xc1o5h/i_built_a_social_app_for_just_your_actual_friends/>
> 指标：得分=3 · 评论=1 · 赞踩比=1
> 作者：FriendTechLLC　|　发布：2026-10-22T06:36:35+08:00
> 项目链接：<https://v.redd.it/7lsifi0n2wwh1>
> 采集：2026-11-01T09:39:33+08:00　|　id：`a2e81c2156f99d2b`

## 正文

I’ve been building FRiENDS, a social app that’s only the people you actually know: no algorithm, no strangers. It just went live on both stores, so here’s the behind-the-scenes.

**The stack and why**

* **React Native + Expo**, so one codebase ships to iPhone and Android. Over-the-air updates let me fix most bugs the same day without waiting on store review.
* **FastAPI on Railway** for the backend, with photos and videos on Cloudflare R2.
* **Game moves are checked on the server.** The arcade (8 Ball Pool, Pong, Snake) replays your moves server-side before it counts a score, so a modified app can’t fake one.

**Biggest learning:** store policies and onboarding take as long as features. Every reviewer reads your app differently.

What I’d love to hear: if you’ve launched a social app, how did you get past the empty-app problem with your first users?

Free on iPhone and Android, Pro is $0.99/month: [App Store](https://apps.apple.com/app/id6785718744) · [Google Play](https://play.google.com/store/apps/details?id=com.alexander.friendmediaapp)

Website: [https://joinfriendsapp.com/](https://joinfriendsapp.com/)

## 评论（1/1）

> **QuanTradin**（1 分） · 2026-10-22T10:28:01+08:00　
> the first five minutes of a friends-only app are the invite, because the feed is empty until someone joins. a pong link a friend can play in the browser before installing would do more than any onboarding screen.

## 关联链接

- https://apps.apple.com/app/id6785718744
- https://joinfriendsapp.com/
- https://play.google.com/store/apps/details?id=com.alexander.friendmediaapp

## 导航

- 项目页：[[10-项目/v.redd.it_fa43a466]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
