---
type: "corpus"
item_id: "893ccc39b97299aa"
title: "I built an invoice-extraction tool and have no paying customers yet. Do I keep going or stop?"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/SaaS/comments/1xr8yhd/i_built_an_invoiceextraction_tool_and_have_no/"
author: "Hashtag_Maybe"
published_at: "2026-11-09T04:58:30+08:00"
captured_at: "2026-11-19T09:44:32+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-11-19"
pub_day: "2026-11-09"
tags:
  - 语料
  - reddit
  - r/SaaS
metrics: {"score": 4, "comments": 14, "upvote_ratio": 1}
comments_count: 11
comments_total: 14
discovered_via: "reddit:14d+settle10"
---

# I built an invoice-extraction tool and have no paying customers yet. Do I keep going or stop?

> [!info] 一句话导读
> I’m a student building Paprly on the side. It reads supplier invoices (PDFs, scans, photos), pulls out the line items, and exports to Xero or QuickBooks. It’s l…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/SaaS/comments/1xr8yhd/i_built_an_invoiceextraction_tool_and_have_no/>
> 指标：得分=4 · 评论=14 · 赞踩比=1
> 作者：Hashtag_Maybe　|　发布：2026-11-09T04:58:30+08:00
> 项目链接：—
> 采集：2026-11-19T09:44:32+08:00　|　id：`893ccc39b97299aa`

## 正文

I’m a student building Paprly on the side. It reads supplier invoices (PDFs, scans, photos), pulls out the line items, and exports to Xero or QuickBooks. It’s live, but I have no paying customers.

What I’ve done so far: a handful of early testers gave useful feedback, I fixed things like European date formats and credit notes, and I’ve just emailed about 20 small accountancy firms.

What I’m hearing: one practice owner told me that invoice extraction will probably be overtaken by people writing their own tools, with the price heading to zero in 6 to 12 months. I think that’s partly right for raw extraction, but I’m not sure the review, error-flagging and clean-export side gets commoditised as fast.

I’d like honest opinions on a few things:

1. Is a standalone invoice parser still worth pursuing, or is it a race to the bottom?
2. If you’ve been through this, how did you decide when to stop, and what evidence made up your mind?
3. If you’d keep going, would you narrow to a specific niche?

I’m happy to hear “stop”. I’d just rather decide on real experience than on a bad week.

## 评论（11/14）

> **raj6126**（1 分） · 2026-11-09T05:19:20+08:00　
> This is built into most software now on the procurement side. They market it as the digital mail room I think. The invoices get scanned into the system as XML files.

---

> **Hashtag_Maybe**（1 分） · 2026-11-09T05:50:47+08:00　
> Fair point, and agreed for larger orgs, where capture is bundled into procurement suites. I’m focused on small practices and bookkeepers, where the invoices still arrive as PDFs and phone photos from small suppliers rather than XML. Do you see e-invoicing mandates reaching that tier soon, or is it mostly mid-market and up?

---

> **Klassy_Coder**（1 分） · 2026-11-09T06:35:11+08:00　
> You'll be lucky to get a 1-2% response rate on cold emails. That's just how it is in general. Don't judge your results yet based on that.
>
> Most people don't want to build their own tools. They're busy enough running their own business and are happy to pay for a simple tool that they'll get use from. But why would they use your tool instead of something from any of the other million people on the Internet selling the same thing? And how would they come across it?
>
> The best path to your first few customers is warm outreach. Ask friends and family if they know the owners of any local small accounting firms (assuming that's who you're initially targeting) and they wouldn't mind giving you an introduction. Then email the referrals asking for a coffee and a chat. But don't just pitch, ask about their business and pain points. Even if the first few don't sign up, it's still excellent feedback that you can use for the next pitch, or to adjust your product. One warm lead is worth thousands of cold emails.

---

> **AllenHere112**（1 分） · 2026-11-09T06:57:04+08:00　
> cold emails to a practice die at the processor question, not at the parser. no partner is going to point a tool at client ledgers without a data processing agreement in place, and a student side project is usually where that conversation stops. the part they'd pay for is the review log, who flagged the invoice and who signed it off.

---

> **churn_gremlin**（1 分） · 2026-11-09T08:30:25+08:00　
> Ask one of your early testers to let you watch them process a real batch into Xero or QuickBooks. You'll see right away whether your error review saves them time or if they still double-check every line by hand. If they stop opening it next week without a reminder, that's your signal to stop.

---

> **crimzohhh**（0 分） · 2026-11-09T10:24:05+08:00　
> this isn't even a niche its like a tiny piece of a part on tons of platforms

---

> **R3duceReuseThrowaway**（1 分） · 2026-11-09T13:05:34+08:00　
> That accountant is half right imo

---

> **SagarKhanapurkar**（1 分） · 2026-11-09T15:33:08+08:00　
> So heavy on SEO and wait for it.

---

> **mantasn**（1 分） · 2026-11-09T17:04:46+08:00　
> On "would you narrow": yes, and most probably by the kind of invoice rather than the kind of company. Line items matter most where costs are per item and change often, e.g. restaurants and cafes buying from food suppliers, construction subcontractors, salons buying stock. A bookkeeper with ten restaurant clients has a weekly pain your parser fits, and price-change alerts per supplier are something a generic tool won't bother with.
>
> On when to stop: set the rule before the next round, not after. Something like "if none of the next 20 conversations turns into a paid pilot by mid-December, I stop or change the niche." Then a bad week can't decide for you. GL.

---

> **gerald_gerez**（1 分） · 2026-11-10T00:30:53+08:00　
> accountant’s kinda right on raw extraction, xero already bundles hubdoc. i’d niche into line items where they actually matter, like restaurants with 40-line supplier invoices
>
> for stop vs keep going: try to get 3 firms paying for a small pilot in 30 days. if not, that’s your answer

---

> **tmaleh**（1 分） · 2026-11-13T02:56:36+08:00　
> Before keep going or stop, a smaller question: has anyone put their own real invoices through it this month, and what did they do next? No paying customers can mean two very different things. Nobody has tried it on real work, so you haven't learned anything yet. Or people tried it and went back to typing line items by hand, which means the pain isn't sharp enough at your price, or it's sharp for a different person than you thought. Those need different moves. The first needs conversations with the people who do this task every week. The second needs you to ask the ones who left why they left. Who on the other end hates this task the most, and have you watched them do it?

## 导航

- 项目页：[[10-项目/I-built-an-invoice-extraction-tool-and-have-no-p_893ccc39]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
