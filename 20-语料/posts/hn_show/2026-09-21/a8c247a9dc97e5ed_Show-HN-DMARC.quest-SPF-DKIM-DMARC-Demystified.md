---
type: "corpus"
item_id: "a8c247a9dc97e5ed"
title: "Show HN: DMARC.quest SPF/DKIM/DMARC Demystified"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49118940"
project_url: "https://dmarc.quest/"
author: "junkDrawer_ai"
published_at: "2026-07-31T04:15:59Z"
captured_at: "2026-09-21T03:11:09+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-07-31"
tags:
  - 语料
  - hn_show
  - author_junkDrawer_ai
  - story_49118940
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:83d"
---

# Show HN: DMARC.quest SPF/DKIM/DMARC Demystified

> [!info] 一句话导读
> Skip to content dmarc . quest Begin

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49118940>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：junkDrawer_ai　|　发布：2026-07-31T04:15:59Z
> 项目链接：<https://dmarc.quest/>
> 采集：2026-09-21T03:11:09+08:00　|　id：`a8c247a9dc97e5ed`

## 正文

Skip to content dmarc . quest Begin
every domain, a kingdom
 Your domain name is
 the keys to your kingdom.
 You registered your name for a reason. So, two things worth knowing: anyone on the internet can send email signed with it — and whether your own messages reach inboxes or rot in spam folders depends on proving they're really yours. We'll read your records, explain them in plain English, and tell you exactly what to fix.
⌖ Check →
Try ▾ theonion.com craigslist.org npr.org substack.com ycombinator.com huggingface.co
 A Report Card grade in seconds — free, no sign-up. Then, if you want it, an AI deep analysis goes line by line through your setup: what each record says, which services send as you, and what to fix first.
why any of this matters Two reasons to care,
 even if you've never heard of DMARC.
The imposter problem Anyone can sign your name.
 Email's oldest flaw: the From line is just text. Anyone, anywhere, can put your domain on a message — fake invoices to your customers, password resets to your team — and it arrives wearing your good name. SPF and DKIM are the fix: a list of couriers allowed to carry your letters, and a wax seal that proves a message left your hand. DMARC is your standing decree telling Gmail, Outlook, and the rest what to do when mail shows up in your name without the seal: deliver it, quarantine it, or burn it.
The reputation problem Your reputation decides where your mail lands.
 Every major mailbox keeps score on your domain. Messages that prove their origin build that reputation; messages that can't, erode it — and quietly steer your real mail toward spam folders. Since 2024, Google and Yahoo flat-out require authentication from anyone sending in volume. If your invoices, newsletters, or quotes keep landing in spam, this is very often why — and it's fixable.
three things, done plainly Built for people who own a domain,
 not a compliance budget.
 Grade what's there now. Translate the strange acronyms into language you can actually act on. Then keep an eye on things — quietly — until something changes.
I
A quick verdict
 Free, no sign-up
 Type a domain. We read your SPF, DKIM, DMARC, MX, BIMI and transport policy and hand back a Report Card grade with the weak spots highlighted.
II
The arcane, translated
 AI deep analysis
 Most of this stuff was designed by committee in 1998. Our AI scribe unpacks every record and chain, names the actual services sending as you, and explains it the way you wish someone had the first time.
III
Quiet watch
 One DNS line
 Add one line we generate for your domain. Daily reports from Google, Yahoo, Microsoft, and the rest start flowing in. We read them so you don't have to — and tell you when something changes.
exhibit: the scribe's hand Not a wall of checkmarks.
 An actual diagnosis.
 Every other checker hands you a row of red ✗s and a shrug. Ours reads the whole setup — the records, the services behind them, how they fit together — and writes you a verdict in plain English. As far as we can tell, no other tool, free or enterprise, does anything like it.
 Read the full report on theonion.com →
 Unedited excerpt · AI deep analysis theonion.com
 Your DMARC policy is set to p=quarantine , which tells receivers to put unauthorized mail into the spam folder. However, the pct=50 flag means this only applies to half of the failing messages; the other half are delivered normally. This is a common setting during a rollout to ensure nothing breaks, but for an established domain, it's like locking only every other door in the building.
 Monitoring is in a good place: you're sending reports to DMARC Digests , a recognized processing service. However, you're also carbon-copying itservices@theonion.com . Unless someone on that team enjoys manually parsing thousands of daily XML attachments (a rare hobby), that address is likely just a graveyard for automated noise.
one line in DNS Add one line.
 We'll handle the rest.
 Every major mail provider — Google, Yahoo, Microsoft, Mail.ru, Mimecast, Proofpoint — already produces daily DMARC reports for your domain. They just go wherever you tell them. Point them at the address we generate for you, and we read every one as it arrives. You hear from us only when something actually deserves your attention.
 Begin the quest → Have an account?
DNS · TXT _dmarc.yourdomain.com
 Preview — your account gets a unique token
 v=DMARC1 ; p=none; rua=mailto:rua+your-token@dmarc.quest ;
Your real record is generated after sign-up with a unique token, so reports route to your dashboard. Nothing in your existing email setup breaks. Remove us anytime by deleting one DNS record.
 See a real report, decoded — and what it can't contain →
dmarc . quest Get your email setup right, and keep it right.
Tools
 Check a domain Live send test Header checker
 Learn
 What's in a DMARC report Blog
 Account
 Dashboard Sign in hello@dmarc.quest
 Studio
 About junkDrawer.ai Privacy Terms
Also from junkDrawer.ai
 letsList.ai ↗ An AI-native workspace for eBay sellers
everSpan.ai ↗ A calendar that measures from anywhere
junkDrawer.ai ↗ AI eBay search for buyers
FlipCast.tv ↗ Reseller video, and the stores behind it
treasure.pics ↗ A photographic record of what you own
shelfMonster ↗ Know what is in the box without opening it
newPad.app ↗ Rescue your inkFrog photos and listings
unStacked.ai ↗ A plain page for something you have
dmarc.quest is a junkDrawer.ai product · © 2026 Cheaney Consulting

## 导航

- 项目页：[[10-项目/dmarc.quest_a0d6fa1c]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
