---
type: "corpus"
item_id: "f7359ee240c7cb0c"
title: "I told my cofouner usage pricing was a scam. 5 months later i owe him an apology."
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/microsaas/comments/1xh17l5/i_told_my_cofouner_usage_pricing_was_a_scam_5/"
author: "Beneficial-Parsnip52"
published_at: "2026-10-28T02:52:14+08:00"
captured_at: "2026-11-07T09:44:31+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-07"
pub_day: "2026-10-28"
tags:
  - 语料
  - reddit
  - r/microsaas
metrics: {"score": 8, "comments": 4, "upvote_ratio": 1}
comments_count: 3
comments_total: 4
discovered_via: "reddit:14d+settle10"
---

# I told my cofouner usage pricing was a scam. 5 months later i owe him an apology.

> [!info] 一句话导读
> Back in May my cofounder wanted to stop charging 39$ flat and charge per document processed. I fought him hard because my argument was customers hate unpredicta…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/microsaas/comments/1xh17l5/i_told_my_cofouner_usage_pricing_was_a_scam_5/>
> 指标：得分=8 · 评论=4 · 赞踩比=1
> 作者：Beneficial-Parsnip52　|　发布：2026-10-28T02:52:14+08:00
> 项目链接：—
> 采集：2026-11-07T09:44:31+08:00　|　id：`f7359ee240c7cb0c`

## 正文

Back in May my cofounder wanted to stop charging 39$ flat and charge per document processed. I fought him hard because my argument was customers hate unpredictable bills, flat is simple and flat is what everyone does.

We're 2 people building an AI tool that reads supplier invoices for small ecommerce brands.

However seeing our data, i change  my stance. We pulled 5 months of usage and our top 8 customers were doing over 1,100+ invoices a month on the same 39$ plans as other people doing 40. Infact one account cost us 212$ in API last month while doing on 39$ plan.

And the light users? 3 of them churned saying it was too expensive for how little they used it.

So flat was overcharging the people who left and undercharging the people who stayed, urghh the worst of both worlds.

Now we're moving to 19$ base with 200 invoices included and per invoice after that. The pricing page update was 30 mins of work but the billing side taking longer, you need usage counted per customer, an overage line on the invoice and something that tells people where they are before the bill shows up. We are looking at flexprice or lago for that since its open source and handles the included units plus overage thing.

Still not fully sold for everything but i was wrong about being thr safe option.

Also, how did switching from one billing system to another affect your users and their churn?

## 评论（3/4）

> **LocalPlotTwist**（2 分） · 2026-10-28T03:46:58+08:00　
> Great story, I’ll definitely remember it. But I noticed something else: you had a disagreement, and it seems one of you stopped a good idea from moving forward. Maybe there are other ideas you haven’t tried yet because you couldn’t agree.

---

> **daniel933912**（2 分） · 2026-10-28T04:31:30+08:00　
> That 212 dollar month on a 39 plan is the whole argument. When you cut over, add the new tier as a new price instead of editing the old one, billing systems usually won't let you change an amount once it's live and existing subs keep pointing at the old one, so grandfathering is free to set up. What bites is the first invoice, half a period on the old plan plus overage off a counter that started at zero. Expect one confused email per customer.

---

> **john006868**（1 分） · 2026-10-28T05:32:35+08:00　
> count documents that actually parsed, not uploads. a lot of what pushes an account over the limit is the same invoice sent twice or a scan that failed OCR, and that is the line people screenshot when they argue about overage.
>
> for the 1100 a month crowd a hard stop beats a nicer invoice. let them set their own ceiling and pause at it, nobody wants to find out on the bill.
>
> what does the $212 account do when it hits 200, those are usually the first to shout.

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
