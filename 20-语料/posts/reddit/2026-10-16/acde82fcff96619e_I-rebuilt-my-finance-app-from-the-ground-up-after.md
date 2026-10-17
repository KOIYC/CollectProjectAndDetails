---
type: "corpus"
item_id: "acde82fcff96619e"
title: "I rebuilt my finance app from the ground up after 5,000 users and 166k USD moved through it. Here’s what I learnt."
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/SideProject/comments/1wyq4ff/i_rebuilt_my_finance_app_from_the_ground_up_after/"
project_url: "https://v.redd.it/l3hv85mn2rth1"
author: "Ok-Profession-2432"
published_at: "2026-10-06T09:30:54+08:00"
captured_at: "2026-10-16T09:36:22+08:00"
lang: "en"
kind: "post"
topic: 开发者工具
shard: "2026-10-16"
pub_day: "2026-10-06"
tags:
  - 语料
  - reddit
  - r/SideProject
metrics: {"score": 3, "comments": 1, "upvote_ratio": 1}
comments_count: 0
comments_total: 1
discovered_via: "reddit:14d+settle10"
---

# I rebuilt my finance app from the ground up after 5,000 users and 166k USD moved through it. Here’s what I learnt.

> [!info] 一句话导读
> Chipp is a bill splitting app. Two years in it had over 5,000 sign-ups and $166k had moved through it on Stripe. It looked like a working product. It was not on…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/SideProject/comments/1wyq4ff/i_rebuilt_my_finance_app_from_the_ground_up_after/>
> 指标：得分=3 · 评论=1 · 赞踩比=1
> 作者：Ok-Profession-2432　|　发布：2026-10-06T09:30:54+08:00
> 项目链接：<https://v.redd.it/l3hv85mn2rth1>
> 采集：2026-10-16T09:36:22+08:00　|　id：`acde82fcff96619e`

## 正文

Chipp is a bill splitting app. Two years in it had over 5,000 sign-ups and $166k had moved through it on Stripe. It looked like a working product. It was not one. This is the story of finding that out, and of fixing it one feature at a time.

Last spring I finally pulled a cohort table instead of looking at the sign-up chart. Month-one retention, for every cohort from Feb 2025 to Apr 2026, was between 0 and 4 percent. Out of roughly 4,200 accounts, 359 had ever created an expense. 124 had ever moved money. Everyone else signed up, looked at an empty screen, and left.

What the 124 people leaving told us

Instead of asking what to add, I looked at what the people who stayed were actually doing. They were hosts. The person who pays at dinner, the one who books the Airbnb, the one who fronts the roommates' bills. They did not care about budgets or categories. They cared about three things: logging the thing in seconds, getting friends to pay their part without nagging, and the money landing in their account.

Everything we rebuilt follows from that.

How we rebuilt it

I spent two weeks on Mobbin going through the first run of about fifty apps, screen by screen. The pattern was obvious once you see it. The apps people keep open with a verb. Ours opened with an empty list and a plus button.

So the home screen became a question. What can I do for you, and a box. You type dinner 120 split 4 ways, or say it, or snap a photo, and the expense is drafted for you to confirm. The old flow was six taps across three screens.

Receipts were the next one. Most group spending happens at a table, and the old app made the host type every line. Now you scan the receipt, share one link, and everyone taps their own items. Tax and tip split themselves. Your friends do not need the app. That last part mattered more than anything else we shipped.

Settling up got rebuilt around how people already pay. Apple Pay, Google Pay, Venmo, Cash App, or a bank transfer, in one swipe. The web link does the same for people without the app, and the host sees who paid.

Groups got a full redesign, because about three quarters of all expenses in the database were group expenses and the group page was the ugliest screen we had. Covers, a running balance, and a chat where a message becomes an expense.

Then pools, for collecting money for a gift or a trip deposit, and cards, which show your recent card transactions so you can tap one and split it.

We shipped each of these as its own update and watched the next cohort.

What I learnt

Retention is the only number. Sign-ups and volume both lied to me for a year.

Your retained users tell you what the product is. We thought we were a finance app. We are a tool for the person who pays first.

The first screen is the product. If it does not open with an action, nothing after it matters.

Remove the friend's need to install anything. Every step we took out of the other person's path showed up in the numbers.

Ship one feature at a time and read the cohort, not the dashboard. It is slower and it is the only way we could tell what worked.

We rebuilt the whole app this way and the new version is on iOS and Android now. Happy to answer anything about the numbers or the process.

## 导航

- 项目页：[[10-项目/v.redd.it_9ac172f7]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
