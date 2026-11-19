---
type: "corpus"
item_id: "787dd23d3aa67ada"
title: "Building a vertical SaaS for tattoo artists in Latin America: what I'm learning before the first paying users"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/EntrepreneurRideAlong/comments/1xr50uk/building_a_vertical_saas_for_tattoo_artists_in/"
author: "Buy_Waste"
published_at: "2026-11-09T02:16:20+08:00"
captured_at: "2026-11-19T09:44:35+08:00"
lang: "en"
kind: "post"
topic: AI 工具/Agent
shard: "2026-11-19"
pub_day: "2026-11-09"
tags:
  - 语料
  - reddit
  - r/EntrepreneurRideAlong
  - Ride Along Story
metrics: {"score": 3, "comments": 20, "upvote_ratio": 1}
comments_count: 17
comments_total: 20
discovered_via: "reddit:14d+settle10"
---

# Building a vertical SaaS for tattoo artists in Latin America: what I'm learning before the first paying users

> [!info] 一句话导读
> I'm a solo founder building a SaaS for tattoo artists. It's very early, so I wanted to share the reasoning and get torn apart a bit.

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/EntrepreneurRideAlong/comments/1xr50uk/building_a_vertical_saas_for_tattoo_artists_in/>
> 指标：得分=3 · 评论=20 · 赞踩比=1
> 作者：Buy_Waste　|　发布：2026-11-09T02:16:20+08:00
> 项目链接：—
> 采集：2026-11-19T09:44:35+08:00　|　id：`787dd23d3aa67ada`

## 正文

I'm a solo founder building a SaaS for tattoo artists. It's very early, so I wanted to share the reasoning and get torn apart a bit.

**Why this niche**

- Tattoo artists are small businesses that don't see themselves as businesses. Bookings, quotes, deposits and aftercare all happen in Instagram DMs and WhatsApp.
- The established tools (US/EU) are English-only and assume email-first clients who book through a website. In Latin America almost everything happens on WhatsApp and Instagram.
- Going vertical lets me speak their language: "stop losing bookings in your DMs", not "CRM with omnichannel inbox".

**What I built (Tatu.Ink)**

A unified inbox (Instagram, Messenger, WhatsApp), a calendar with deposits and multi-session tracking, client history, aftercare/reminder automations, simple finances and a public portfolio page. Free plan + Pro plan with a 1-month trial.

**What I'm unsure about**

1. Pricing in a market where many artists work informally. Free → Pro, or a cheaper middle tier?
2. Distribution: I'm doing manual outreach on Instagram. Has anyone scaled a vertical SaaS through one niche community like this?
3. Go after studios first, or independent artists?

Any brutal feedback welcome. Happy to share the link in the comments if anyone wants to see it.

## 评论（17/20）

> **Similar_Anteater2568**（0 分） · 2026-11-09T02:34:28+08:00　
> another inbox app, now with ink. bold.

---

> **Buy_Waste**（0 分） · 2026-11-09T02:38:33+08:00　
> Ha, fair, that's on me for leading with the inbox. It's honestly the least interesting part.
>
> The core is an AI receptionist on top of it: someone DMs "how much for a forearm piece?" at 2am, it answers right away in the artist's tone, asks for the idea, size, placement and style, looks at the reference pics, and pings the artist with a summary once the client is ready to book.
>
> From there it covers the rest of the job: calendar with deposits and multi-session pieces, client history and payments, automated prep/reminders/day-by-day aftercare/review requests, finances, and the artist's own website with portfolio, reviews and booking. Basically everything from the first DM to the review, in one place, in Spanish.

---

> **AutoModerator**（1 分） · 2026-11-09T03:08:02+08:00　
> Your [comment](https://www.reddit.com/r/EntrepreneurRideAlong/comments/1xr50uk/building_a_vertical_saas_for_tattoo_artists_in/19sc8te9l1xb7/) in /r/EntrepreneurRideAlong was automatically removed because it contained a URL or a markdown link.
>
> To keep our community focused and prevent spam, we do not allow URLs or links (including Reddit internal links) in comments at this time.
> If you believe this removal was a mistake, please [contact the moderators](https://www.reddit.com/message/compose?to=/r/EntrepreneurRideAlong).
>
> *I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/EntrepreneurRideAlong) if you have any questions or concerns.*

---

> **AutoModerator**（1 分） · 2026-11-09T03:52:32+08:00　
> Your [comment](https://www.reddit.com/r/EntrepreneurRideAlong/comments/1xr50uk/building_a_vertical_saas_for_tattoo_artists_in/19scasu4o6xnm/) in /r/EntrepreneurRideAlong was automatically removed because it contained a URL or a markdown link.
>
> To keep our community focused and prevent spam, we do not allow URLs or links (including Reddit internal links) in comments at this time.
> If you believe this removal was a mistake, please [contact the moderators](https://www.reddit.com/message/compose?to=/r/EntrepreneurRideAlong).
>
> *I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/EntrepreneurRideAlong) if you have any questions or concerns.*

---

> **Ok-Library1020**（2 分） · 2026-11-09T04:10:58+08:00　
> The strongest wedge sounds like turning a late-night DM into a consultation-ready booking, not being another inbox. I'd test that with a few artists and track inquiry-to-deposit conversion before choosing between solo artists and studios.

---

> **No_Bell_3546**（2 分） · 2026-11-09T05:03:23+08:00　
> The automations are where this quietly gets expensive. Birthday and win-back messages fire outside the 24h customer service window, so on the WhatsApp Business API those are template messages, billed per send, copy pre-approved by Meta. Nobody is opting a client in for a tattoo anniversary. And Fresha hands the calendar out free, so "cheaper than Booksy" isn't the wedge, the WhatsApp inbox is, which is exactly the part that costs you money per conversation.

---

> **ramonharrisjr**（2 分） · 2026-11-09T08:18:38+08:00　
> I’d start with independent artists who handle their own DMs, so you can see exactly where they step in. For a custom piece, test whether the assistant can collect placement, approximate size and references, then leave the quote to the artist. Give artists a way to mark each summary as ready to quote or missing something. Their corrections will tell you which questions the assistant should ask next time.

---

> **Buy_Waste**（1 分） · 2026-11-09T11:07:01+08:00　
> Agreed, that's the metric to watch. Right now the assistant asks for design, size, placement and style (the artist can change that list), looks at the reference pics, and pings the artist with a summary. What I don't track yet is how many of those summaries end in a paid deposit, so that's next. Leaning toward solo artists first, since they're the ones answering DMs at 2am.

---

> **Buy_Waste**（1 分） · 2026-11-09T11:07:22+08:00　
> Fair point, it's a real constraint. Two paths today: if the artist links their own WhatsApp/Instagram account, messages go out as them, so the 24h window doesn't apply. If they're on the official Business API, each automation gets its own WhatsApp template that's submitted to Meta automatically, and once it's approved it's used after the window closes. If it isn't approved, the message goes out by email when the client has one.
>
> You're right that birthday/win-back are the weakest and should be opt-in. The ones that matter are appointment reminders, confirmations and aftercare follow-ups. Also fair on Fresha, the calendar alone isn't the wedge.

---

> **Buy_Waste**（1 分） · 2026-11-09T11:07:42+08:00　
> That's close to how it works now. It collects design, size, placement and style plus references, doesn't give prices by default (the quote stays with the artist), and sends them a summary. There's no way yet to mark a summary as "ready to quote / missing something", and I really like the idea. Using those corrections to tune what the assistant asks is going straight onto the list.

---

> **hmamlook13**（1 分） · 2026-11-09T14:13:23+08:00　
> The replies have the solo versus studio question mostly settled, so on distribution: in tattooing, the people every artist already trusts are the supply distributors and the convention organisers. Ink and needle suppliers in Mexico, Colombia or Argentina talk to hundreds of artists a month, and a deal where they include a free first month with every order puts you in front of artists who already spend on their business. Conventions are the other route, because artists sit at a booth for two or three days answering DMs between sessions, which is the exact moment your receptionist sells itself if you set it up on their phone right there. On pricing, I'd tie the middle tier to the part that costs you per conversation: a cheaper plan with the calendar and inbox, and Pro adding the 24/7 receptionist on WhatsApp. Keeping each tier under what one lost deposit is worth makes the math easy for an artist working informally. Which country are you starting in?

---

> **Buy_Waste**（1 分） · 2026-11-09T14:20:34+08:00　
> thanks a lot, really like these ideas. the supplier angle is great, hadn't thought about bundling a free month with ink orders. same with conventions, setting it up on their phone right at the booth is a way better demo than any landing page. on pricing there's already a free plan and Pro is where the AI receptionist lives, so it's pretty close to what you describe.
>
> starting in Chile, but I'd like to move to Argentina next and then the other LATAM countries with a bigger tattoo culture.

---

> **SimonMX**（1 分） · 2026-11-09T16:39:59+08:00　
> Free and Pro seems enough to me, as long as the free plan properly fixes the DM mess, since that's the pain they already feel. Deposits look like the natural thing to charge for, because an artist only needs them once bookings are coming in, and it's money they'd otherwise lose to no-shows. I guess a cheaper middle tier mostly gives informal artists one more thing to decide on.

---

> **Buy_Waste**（1 分） · 2026-11-09T23:17:32+08:00　
> makes sense. I did think about charging on deposits, but an artist could just set a tiny deposit in the app and collect the real amount in person at the session, so it's too easy to route around and we'd end up making nothing. that's why deposits are only recorded on the appointment for now.
>
> putting the inbox in the free plan is tempting, since that's the pain they already feel, but the provider I use to connect social accounts charges per connected account, so it gets expensive fast. for now free is the calendar, portfolio and the artist's own page, and the inbox + AI are in Pro. agree on skipping a middle tier though

---

> **SimonMX**（1 分） · 2026-11-10T03:20:07+08:00　
> The per-account cost settles it really. Anything that costs you each time an artist connects belongs in Pro, and the calendar and page cost you next to nothing to give away. The catch is that free no longer touches the DM mess, so the upgrade has to land when that bites. I'd guess that's the week their page starts bringing in more messages than they can answer by hand.

---

> **Ok-Library1020**（1 分） · 2026-11-10T05:07:28+08:00　
> That sounds like a solid first test. Tracking the time from summary to deposit could also show whether interested clients are dropping off because the follow-up comes too late.

---

> **hmamlook13**（1 分） · 2026-11-10T14:50:57+08:00　
> Chile first makes sense: smaller scene, easier to know everyone, and more stable for pricing. Two things to plan for before Argentina:
>
> 1. **Pricing in pesos.** With Argentina’s inflation, a local price can lose a lot of its value within months. Most SaaS there either charges in USD or sets a peso price with a scheduled adjustment. Decide which before your first Argentine customer, because changing it later feels like a price hike.
> 2. **WhatsApp costs by country.** If the receptionist runs on the WhatsApp Business API, Meta charges per conversation, and rates differ by country. Check them for Chile and Argentina so Pro’s margin holds up when an artist answers a lot of enquiries.
>
> Are there any tattoo conventions coming up in Chile in the next couple of months? One weekend at a booth there could get you your first 10 paying artists faster than months of DMs.

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
