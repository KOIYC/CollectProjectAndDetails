---
type: "corpus"
item_id: "12a116331f465a73"
title: "carders kept targeting my $9 plan. here's how I stopped most of them"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/SaaS/comments/1x6mqxc/carders_kept_targeting_my_9_plan_heres_how_i/"
author: "ImplementMiserable74"
published_at: "2026-10-15T22:12:52+08:00"
captured_at: "2026-10-25T23:28:28+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-10-25"
pub_day: "2026-10-15"
tags:
  - 语料
  - reddit
  - r/SaaS
metrics: {"score": 15, "comments": 12, "upvote_ratio": 1}
comments_count: 10
comments_total: 12
discovered_via: "reddit:14d+settle10"
---

# carders kept targeting my $9 plan. here's how I stopped most of them

> [!info] 一句话导读
> turns out a $9 subscription is pretty attractive to carders. a lot of small US card payments go through without 3DS, so stolen cards were getting approved way t…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/SaaS/comments/1x6mqxc/carders_kept_targeting_my_9_plan_heres_how_i/>
> 指标：得分=15 · 评论=12 · 赞踩比=1
> 作者：ImplementMiserable74　|　发布：2026-10-15T22:12:52+08:00
> 项目链接：—
> 采集：2026-10-25T23:28:28+08:00　|　id：`12a116331f465a73`

## 正文

turns out a $9 subscription is pretty attractive to carders. a lot of small US card payments go through without 3DS, so stolen cards were getting approved way too easily. then the real owner would dispute the charge, I'd lose the $9 and get hit with another $50 in fees. this was happening 5-6 times every single month.

what fixed it:

1. card country must match billing address
2. IP country must match card country
3. no payments via vpn or proxy

now it's about one dispute every two months. I also tried Stripe radar before this and on default settings it let stuff slip.

link is still a pain as it doesn’t have sms check at almost any amount and the smart ones use residential IPs and the right address. a fresh account trying to pay 2k with Link is most likely a stolen account and for that reason I killed amazon pay a year ago.

free trials got farmed too. I capped signups at 3 per IP, they rotated vpns and made 300-500 accounts, so I had to block vpn signups last month.

processors want disputes under 0.5% and you can't ignore this.

if every stolen card had been real, I'd be rich rich

## 评论（10/12）

> **Meracle_Byte**（-2 分） · 2026-10-16T00:02:02+08:00　
> the $9 was never the loss. the $50 dispute fee was. 5 or 6 of those a month is the whole plan.
>
> 3ds on the first charge is ugly and it'll kill some real signups. still cheaper than the fee. country match will also block someone on a trip, so watch the support tickets before you celebrate the dispute rate.

---

> **Informal-Dust4499**（0 分） · 2026-10-16T00:15:44+08:00　
> Good breakdown, worth adding that most processors let you trigger 3DS selectively (new customer, first payment over a threshold, risk score above X) instead of forcing it on everyone, which gets you the liability shift without adding friction to returning legit customers. Residential IP proxies beating your geo check is the real ceiling here, nothing catches those reliably from IP alone. Worth asking your processor what their own risk engine flags before you build more rules on top, since a lot of this overlaps with what Radar or similar already scores, just not surfaced by default.

---

> **Joubaud-Taxas**（1 分） · 2026-10-16T00:19:12+08:00　
> curious what your dispute rate looked like before you added the IP/country match. that one seems like it would catch the most volume since a lot of carders dont bother with geo-matching proxies for a $9 charge

---

> **aei__ou___**（1 分） · 2026-10-16T00:39:07+08:00　
> don't you have a stronger signal based on activity? surely nobody just goes straight to the payment page, they look around, try things out, take time, then pay?

---

> **LostLeek1304**（0 分） · 2026-10-16T01:03:44+08:00　
> Two things from payments work that fit your case. For the trial farm, if you ask for a card at signup, Stripe gives every card number a fingerprint, so you can allow one trial per card. 300 accounts then need 300 real cards, which costs them a lot more than VPNs. For the disputes, Stripe passes on early fraud warnings from the card networks, and refunding one of those right away can stop the dispute and the fee. The warning itself stays on your record. Stripe's docs say the refund pays off when the charge is about the size of the dispute fee or smaller, and a $9 plan always is.

---

> **TheCeilingAbove**（1 分） · 2026-10-16T03:05:16+08:00　
> Them 3 conditions are pretty shit. I could easily get passed all of them. Regarding point 3 - it takes seconds to setup a residential proxy which wouldn't be detected as a proxy.

---

> **wasay-inc**（0 分） · 2026-10-16T03:58:12+08:00　
> forcing 3ds on all first time checkout attempts under $10 cut like 90% of this for us. stripe radar default rules are way too lax out of the box, but adding a custom rule to require 3d secure whenever risk score is over 20 or if card country != ip country makes a huge difference. for those residential proxy rotations, passing signup IPs through an API like maxmind or ipqs stops the script farms pretty fast too.

---

> **ImplementMiserable74**（1 分） · 2026-10-16T22:22:56+08:00　
> before the geo checks it was around 5-6 disputes a month. after adding them it dropped to roughly one every couple months.
>
> for cheap charges most of them really weren’t trying that hard, which is kinda why such basic rules helped so much.

---

> **ImplementMiserable74**（1 分） · 2026-10-16T22:25:03+08:00　
> yeah of course they’re bypassable lol, i’m not pretending i invented fraud prevention.
>
> the point is they killed most of the lazy $9 attempts. once someone is using clean residential IPs + matching billing data, that’s a different fight.

---

> **ImplementMiserable74**（1 分） · 2026-10-16T22:28:17+08:00　
> yeah selective 3ds is probably the next thing i’d test. forcing it on everyone feels like overkill for a $9 plan

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
