---
type: "corpus"
item_id: "597d3282e4540ade"
title: "Show HN: Seal – Letters and passwords that open for your family after you die"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49763311"
project_url: "https://github.com/jasonepage/Seal"
author: "jpage2"
published_at: "2026-09-19T04:28:22Z"
captured_at: "2026-09-20T14:01:21+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-20"
pub_day: "2026-09-19"
tags:
  - 语料
  - hn_show
  - author_jpage2
  - story_49763311
  - show_hn
metrics: {"points": 11, "comments": 7, "engagement_velocity": 11}
comments_count: 7
comments_total: 7
discovered_via: "hn:show_hn:90d"
---

# Show HN: Seal – Letters and passwords that open for your family after you die

> [!info] 一句话导读
> I'm a CS undergrad who has developed an interest in hardware keys ever since I used them for a school project a few years ago. I made a little chat app that onl…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49763311>
> 指标：点赞=11 · 评论=7 · engagement_velocity=11
> 作者：jpage2　|　发布：2026-09-19T04:28:22Z
> 项目链接：<https://github.com/jasonepage/Seal>
> 采集：2026-09-20T14:01:21+08:00　|　id：`597d3282e4540ade`

## 正文

I'm a CS undergrad who has developed an interest in hardware keys ever since I used them for a school project a few years ago. I made a little chat app that only allows users to chat if they registered a key, nothing else.The backstory of how I came to work on Seal (this project): was that I was generating ideas with Claude to come up with an idea that only hardware keys could make into software. I was thinking about physical house keys and what you could do with those, but in software. I was already making iOS apps with Claude, and I came up with this idea and it sounded good. I had already worked on a few projects involving hardware keys and I already loved them.Today I submitted my latest app, Seal, for review in the app store. Seal is an iOS app for iPhone and iPad that lets you write an Envelope (an encrypted bundle of passwords, photos, voice memos, etc...) for all of your loved ones when you're gone.You can register hardware keys and assign identities for each person. Then you can create Envelopes and assign them to the key that you want to distribute. They plug in the key to their phone and are ready to receive an Envelope from you.If you don't log into the app for months, one of your designated key holders can start the process of opening the Sealed Envelope. You, as the writer of the letters, get weeks of warnings to check in at least once before the letters open.After 90 days of countdown, 21 days of warnings, and 14 days of grace, the envelope opens for each person they met IRL and exchange keys with.No one else can read the envelope or see the photos (even the key holders, Apple, or me) unless that envelope was designated for that person.What's different from a password manager like 1Password: emergency access there hands one person your whole vault through the company's server, so it needs that company to still exist and be honest on the day it matters. Seal gives each person their own envelope nobody else can open, and there's no company in the middle.There's also no server at all besides a free Cloudflare static site. The encrypted bundles of passwords and photos are in Cloud Kit. Sign-in/identity is a passkey Face ID/Touch ID or a Hardware Key. It's all Crypto Kit, so there's no dependencies required.Currently, it's just me and Claude working on this. It hasn't been independently audited by anyone, and it's iPhone only for now. Please do not put a live seed phrase in it yet. If anyone has advice for me as the lead developer for this project, I'm all ears! You can help contribute on the github source code repository page if you'd like. My mom likes this app especially because she's into crypto and she needed a way to pass down or give away the seed phrases for her wallets to all 3 kids without any question about who gets what and when. In the end, there's no confusion or hurt feelings after the fact with just crypto. Thank you for reading and let me know if you have any questions or concerns for me or the project!Source: https://github.com/jasonepage/SealSite with limits and objections pages: https://sealmessenger.comFree on TestFlight while the App Store version is in review: https://testflight.apple.com/join/cYp9JRCG

## 评论（7/7）

> **itake** · 2026-09-19T05:13:56.000Z　
> > the keys never leave the phones, and the record of who did what can be checked with a script that has no Seal in it.What happens if someone loses their phone or buys a new phone? What happens if they forget to tell you that they need a new key?

---

> **sebmellen** · 2026-09-19T05:22:10.000Z　
> > What is not doneRewrite this Readme without Claude?Also> There's also no server at all besides a free Cloudflare static site. The encrypted bundles of passwords and photos are in Cloud Kit. Sign-in/identity is a passkey Face ID/Touch ID or a Hardware Key. It's all Crypto Kit, so there's no dependencies required.To me, this clearly implies that there’s a server involved… Apple’s server. Am I wrong?

---

> **evil-olive** · 2026-09-19T05:41:21.000Z　
> > If you don't log into the app for months> After 90 days of countdown, 21 days of warnings, and 14 days of grace, the envelope opensvs> it needs that company to still exist and be honest on the day it matters> there's no company in the middlewhich is it?there's no middleman, but also I need to log in to your app regularly to avoid being declared dead?

---

> **sicutarinaru** · 2026-09-19T06:22:16.000Z　
> Very coool side project!
> how are you currently sourcing or curating the ads featured on the wall?
> is it an automated scraping pipeline or manual submission?

---

> **skeledrew** · 2026-09-19T08:23:20.000Z　
> > there's no company in the middleYet this seems dependent on Apple's ecosystem. That's a company in the middle.

---

> **skeledrew** · 2026-09-19T08:29:28.000Z　
> > I need to log in to your app regularly to avoid being declared dead?Technically, until we get to a point where we still have embedded "life signal" chips, there's no way to automatically detect that someone has died. Other than those who've actually seen a body, the best we have is "not seen - at Y - for a while".

---

> **pixel_popping** · 2026-09-19T09:16:37.000Z　
> Why it's not also available in the web running client-side?

## 关联链接

- https://github.com/jasonepage/SealSite
- https://sealmessenger.comFree
- https://testflight.apple.com/join/cYp9JRCG

## 导航

- 项目页：[[10-项目/github.com_0fcc6869]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
