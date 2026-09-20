---
type: "corpus"
item_id: "1c6254f1f0bc323e"
title: "Hardware advise request"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1w39lfc/hardware_advise_request/"
author: "Rawdochick"
published_at: "2026-08-31T18:18:17+08:00"
captured_at: "2026-09-21T03:05:18+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-08-31"
tags:
  - 语料
  - reddit
  - r/selfhosted
  - Need Help
metrics: {"score": 6, "comments": 10, "upvote_ratio": 0.87}
comments_count: 12
comments_total: 12
discovered_via: "reddit:52d+settle3"
---

# Hardware advise request

> [!info] 一句话导读
> I am looking hardware to host my first selfhosted system. My use planning is to host data like a NAS, my own password vault, an adblock like pi hole, vpn, and m…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/selfhosted/comments/1w39lfc/hardware_advise_request/>
> 指标：得分=6 · 评论=10 · 赞踩比=0.87
> 作者：Rawdochick　|　发布：2026-08-31T18:18:17+08:00
> 项目链接：—
> 采集：2026-09-21T03:05:18+08:00　|　id：`1c6254f1f0bc323e`

## 正文

I am looking hardware to host my first selfhosted system. My use planning is to host data like a NAS, my own password vault, an adblock like pi hole, vpn, and maybe explore with some project to host some automate, and data monitoring apps. In a medium future I want acquire a better independient device to set up a self hosted IA server with some harness, but I said I want to have them sepparated.

My maths to hardware request are enough with 2tb of storage, 16gb RAM, and a N150 cpu. I saw in this Reddit so much hate to umbrel hardware, but I am seeing now the home model with 2 tb of storage from 599€ and the chineese alternative overprice this.

Am I wrong with my assumptions?

## 评论（12/12）

> **asimovs-auditor**（1 分） · 2026-08-31T18:18:27+08:00　
> Expand the replies to this comment to learn how AI was used in this post/project.

---

> **Rawdochick**（1 分） · 2026-08-31T18:19:33+08:00　
> Non used IA

---

> **stack_craft**（2 分） · 2026-08-31T19:13:05+08:00　
> Your specs (16GB RAM + N100/N150) are more than enough for NAS, Vaultwarden, Pi-hole, and monitoring containers.
>
> Where the math falls apart is the 599€ price point. You can buy a barebones N100 mini PC for \~120€, add a quality 2TB NVMe SSD for \~100€, and a 16GB RAM stick for \~30€. That's **under 250€** for the exact same silicon and storage performance.
>
> Bro ditch Umbrel cause they charge a \~350€ premium purely for their metal enclosure and pre-installed OS. Save the extra 350€, buy a standard mini PC, and run Debian with CasaOS or Docker Compose directly. You'll get better hardware flexibility and most importantly full control over your storage.

---

> **gobeye**（2 分） · 2026-08-31T19:43:19+08:00　
> Not sure where you are, but I'm a big fan of older chromeboxes if you can find them in your locale (they are all over eBay in the UK). An Asus CN62 basic unit can be had for under £50, which is plenty for what you are wanting to host and it gives plenty of headroom for more ram and a larger SSD without breaking the bank. They also have very low power consumption.
>
> https://docs.mrchromebox.tech/ makes it pretty easy to repurpose them and put whatever OS on that you would like.

---

> **GolemancerVekk**（3 分） · 2026-08-31T19:53:10+08:00　
> > a 16GB RAM stick for ~30€
>
> Huh, I didn't know you can use DDR3 with N100.

---

> **Joniator**（2 分） · 2026-08-31T21:01:24+08:00　
> Where are you getting these prices from?
>
> Everything you said is at least double the price right now everywhere I checked.

---

> **stack_craft**（1 分） · 2026-09-01T17:03:08+08:00　
> Bro no one is talking about DDR3, definitely meant DDR4 SO-DIMM.
>
> Regarding the price breakdown: the \~250€ math comes from typical deal pricing or importing via AliExpress/Amazon promos rather than buying full local EU retail MSRP):
>
> • Barebones N100 mini PC (Beelink S12 Pro, GMKtec G3, or generic N100 boxes on sale): \~120€–140€
>
> • 16GB DDR4 3200MHz SO-DIMM stick: \~30€–35€
>
> • 2TB NVMe PCIe 3.0 SSD (Fanxiang/Lexar/Crucial sales): \~95€–110€

---

> **stack_craft**（1 分） · 2026-09-01T17:04:48+08:00　
> Buying everything non-discounted directly from local retail distributors, it lands closer to \~320€–350€; which is still roughly half of the 599€ turnkey markup, but regional pricing variance that's another thing though.

---

> **GolemancerVekk**（2 分） · 2026-09-01T17:41:20+08:00　
> Where are you getting 16 GB of DDR4 for 30€? I can only find DDR3 for that. All the DDR4 is 90-100€.

---

> **stack_craft**（3 分） · 2026-09-02T00:05:30+08:00　
> Fair call, just checked live stock and you're totally right. I knew memory was up, but didn't realize DDR4 SO-DIMMs had climbed that high too.
>
> My $35 math was anchored to old clearance pricing. Appreciate the check!

---

> **Rawdochick**（2 分） · 2026-09-02T19:53:58+08:00　
> A 2tb ssd, even the cheapest brand it’s cost almost 250€ + 150€ aprox of ddr4 ram (the umbrel have ddr5), + the barebone 150\~€ makes a 550€ aprox, for a worst device and the brain pain of buy the barebone abroad, duty expenses, delays… I think after the increase of prices make sense the price of umbrel old model, because I think they are keeping the price because have old stock and want sell them.

---

> **stack_craft**（1 分） · 2026-09-03T17:28:23+08:00　
> Probably

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
