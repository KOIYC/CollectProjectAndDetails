---
type: "corpus"
item_id: "14a579f233a37ea9"
title: "Show HN: EchoRelay - Reliable HTTP delivery with retries, fan-out, and more"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48730644"
project_url: "https://echorelay.dev/"
author: "miclag"
published_at: "2026-06-30T10:21:42Z"
captured_at: "2026-09-21T02:53:11+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-06-30"
tags:
  - 语料
  - hn_show
  - author_miclag
  - story_48730644
  - show_hn
metrics: {"points": 5, "comments": 0, "engagement_velocity": 5}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:113d"
---

# Show HN: EchoRelay - Reliable HTTP delivery with retries, fan-out, and more

> [!info] 一句话导读
> Minutes to integrate.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48730644>
> 指标：点赞=5 · 评论=0 · engagement_velocity=5
> 作者：miclag　|　发布：2026-06-30T10:21:42Z
> 项目链接：<https://echorelay.dev/>
> 采集：2026-09-21T02:53:11+08:00　|　id：`14a579f233a37ea9`

## 正文

Docs
Pricing
Log in
Docs
Pricing
Log in
Minutes to integrate.
 Seconds to change.
A managed runtime for custom API integrations.
Stop maintaining the adapter, its retries and its credentials. For teams connecting partner, vendor and customer APIs without an integration team.
Build an integration
 Follow one request
Real traffic. No card.
Change the mapping . Not your application.
A field gets renamed. That used to be an engineer's week.
order_id orderId
the API you call · renamed
orderId → order.id
your mapping · edited live
order.id
your application · untouched
Absorbed here .
Preview it, dry-run it, publish while traffic is flowing. No code. No deployment.
No downtime.
Hand us an OpenAPI document or a sample. Your agent writes the mapping over MCP;
the editor is there for humans.
Read the docs
One request.
 Every target.
You send it once. Each target takes it in
the mode that fits its job.
You send
curl -X POST https://your-project.echorelay.cloud/v1/your-endpoint \
 -H "Authorization: Bearer er_live_YOUR_KEY" \
 -H "Content-Type: application/json" \
 -d '{"event":"order.placed","orderId":"ord_42"}'
Queued delivery
The default. Accept now, deliver in the background: fanned out, retried, dead-lettered and replayable. A slow target never
blocks your caller.
Synchronous delivery
For when the answer is the point:
a price, a decision, a lookup. We hold your caller's request, reach the target, and return its answer on the same
call.
Streaming
For answers produced
over time: AI model output, long-running exports. The stream reaches your caller as the target generates it, first byte
to last.
Compare the three modes
Your exposure ends here .
Callers reach an address we run. Nothing behind it is ever handed out.
northwind-events
 your-project
 harbour-billing
.echorelay.cloud
Your project answers on your-project.echorelay.cloud, one address among many.
One way in .
Nothing unauthenticated gets past us. Every request clears an API key you
mint and your rate limit before it moves; schema validation and an IP
allowlist add to that per endpoint. Target addresses stay in your config,
and no caller ever receives one.
Credentials stay sealed in a dedicated store, isolated from everything else,
opened only to authenticate to your target.
 Learn more about how we protect your credentials
If a target goes down, queued deliveries are held with us and retried. Once
it answers, delivery catches up.
How shielding works
Always on . In public .
Our status page probes production around the clock. The number below is fetched live. We did not write it here.
%
 uptime, last days. Measured, not promised.
All systems operational
0">
% · 24 h
Full history
Take it with you.
Live component health, incident history and scheduled maintenance. Push alerts
when something breaks, and a home screen widget.
Start free. Grow when you need to.
Best price. No surprises. Nothing to cancel if you stay.
Free forever · No card · Yours until you outgrow it
Start free
Prepaid
 Buy credits once, spend at your own pace.
Pro
 A monthly plan for steady, predictable traffic.
Scale
 More throughput, more projects, higher ceilings.
Enterprise
 Custom contract, dedicated capacity, signed SLA.
See every plan and what it costs
All prices exclude VAT. Applicable taxes are calculated at checkout. Compare plans in detail.
A managed runtime for custom API integrations.
Start free
Service status
Product
Pricing
Documentation
Help center
Who it’s for
Use cases
Compare
Blog
Agent mode
FAQ
Company
Trust Center
About
Ethos
Contact
Enterprise
Legal
Terms of Service
Privacy Policy
Security
SLA
DPA
Licenses
Report abuse
The EchoRelay newsletter
 What we ship, when there is something worth sending.
Email address
Subscribe
I would like to receive the EchoRelay newsletter by email. I can unsubscribe at any time using the link in every message.
Please tick the box to confirm you want the newsletter.
Thanks. Check your inbox to confirm.
Something went wrong. Please try again.
Currency:
© 2026 EchoRelay . All rights reserved.

## 关联链接

- https://your-project.echorelay.cloud/v1/your-endpoint

## 导航

- 项目页：[[10-项目/echorelay.dev_115bf8e3]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
