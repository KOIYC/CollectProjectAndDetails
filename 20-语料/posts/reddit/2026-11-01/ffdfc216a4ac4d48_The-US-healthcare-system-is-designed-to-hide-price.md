---
type: "corpus"
item_id: "ffdfc216a4ac4d48"
title: "The US healthcare system is designed to hide prices from you. I built a tool to expose them and got 10k users in 15 days"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/SideProject/comments/1xc59jz/the_us_healthcare_system_is_designed_to_hide/"
project_url: "https://momentarylab.com/healthcare-navigator"
author: "DependentRun6816"
published_at: "2026-10-22T09:23:28+08:00"
captured_at: "2026-11-01T09:39:24+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-01"
pub_day: "2026-10-22"
tags:
  - 语料
  - reddit
  - r/SideProject
metrics: {"score": 263, "comments": 42, "upvote_ratio": 0.9781818181818182}
comments_count: 36
comments_total: 42
discovered_via: "reddit:14d+settle10"
---

# The US healthcare system is designed to hide prices from you. I built a tool to expose them and got 10k users in 15 days

> [!info] 一句话导读
> Insurers are legally required to publish their negotiated rates with hospitals (Transparency in Coverage Act), but they bury it in massive, nearly impossible to…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/SideProject/comments/1xc59jz/the_us_healthcare_system_is_designed_to_hide/>
> 指标：得分=263 · 评论=42 · 赞踩比=0.9781818181818182
> 作者：DependentRun6816　|　发布：2026-10-22T09:23:28+08:00
> 项目链接：<https://momentarylab.com/healthcare-navigator>
> 采集：2026-11-01T09:39:24+08:00　|　id：`ffdfc216a4ac4d48`

## 正文

Insurers are legally required to publish their negotiated rates with hospitals (Transparency in Coverage Act), but they bury it in massive, nearly impossible to access files.

So I scraped 100TB+ of this data and built a AI chat-based tool that makes it searchable:

* Estimate costs for medical procedures, visits, labs, imaging before you go
* Find cheaper providers nearby and see exactly how much you'd save
* Check if they're in-network and see reviews

The price gaps are insane. Same MRI can be $400 at one place and $2,800 ten minutes away. Insurers hope you won't shop around.

Try it out: [https://momentarylab.com/healthcare-navigator](https://momentarylab.com/healthcare-navigator)

Got to 10K users through SEO and the product is still rough around the edges, but would love feedback on what would make it more useful! Happy to chat about what worked well for us regarding distribution :)

## 评论（36/42）

> **Street_Report_6656**（15 分） · 2026-10-22T09:28:35+08:00　
> The price gap you mentioned is exactly what keeps people from even trying to shop around, most just assume it's all expensive and give up. What's the plan for keeping the data fresh since insurers update those files constantly

---

> **DependentRun6816**（11 分） · 2026-10-22T09:31:44+08:00　
> Insurers update the pricing per month, so i have a scheduler which scrapes the data. Since the data is huge (100+ TB), I'm currently not doing it per month but every 3 months!

---

> **-ankeri-**（2 分） · 2026-10-22T09:57:36+08:00　
> This is really interesting, thanks for sharing!

---

> **DependentRun6816**（1 分） · 2026-10-22T09:59:25+08:00　
> Hope it is helpful!

---

> **putaro3000**（37 分） · 2026-10-22T10:05:14+08:00　
> love a project that makes someone's life better. keep up the good work

---

> **DifferenceTimely8292**（1 分） · 2026-10-22T10:08:43+08:00　
> Doesn’t price vary by network n plan? How do you just scrap data off of their website and turquoise health?

---

> **DependentRun6816**（3 分） · 2026-10-22T10:22:05+08:00　
> It's an aggregate of pricing of multiple insurance companies. All of them upload the pricing as JSON files on their website! You can google search "name of insurer" + "Transparency in Coverage Files" and you'll get the data.
>
> I agree, the price will vary on the network - but this is still directionally accurate and more helpful for folks on a High deductible health plan or folks looking to use cash pay

---

> **DependentRun6816**（2 分） · 2026-10-22T10:22:18+08:00　
> Appreciate the kind words, thanks!

---

> **QuanTradin**（2 分） · 2026-10-22T10:27:49+08:00　
> the gap matters most to people still under their deductible, since they pay the negotiated rate itself. once you're into coinsurance that $2,400 difference shrinks to whatever your percentage is.

---

> **weeyummy1**（1 分） · 2026-10-22T10:37:04+08:00　
> Wow. They should really add regulations that this data be made fresh and publically available. With AI there is no reason for the lack of transparency

---

> **sagivo**（2 分） · 2026-10-22T10:57:21+08:00　
> Where did you get the data?

---

> **DependentRun6816**（5 分） · 2026-10-22T11:12:48+08:00　
> All insurers upload the pricing data as JSON files on their website! You can google search "name of insurer" + "Transparency in Coverage Files" and you'll get the data.

---

> **bunguardian**（1 分） · 2026-10-22T11:20:54+08:00　
> Nice!!! This is going to help so many people!!

---

> **mtjoseph**（2 分） · 2026-10-22T11:33:31+08:00　
> First. Thank you for this tool. Transparency in medical and health care expenses can only empower the consumer.
> Second. Where’s the donate button?

---

> **BeillotCordarrel**（3 分） · 2026-10-22T11:45:27+08:00　
> is the freshness problem more about the rates themselves changing or providers dropping in and out of network?

---

> **Numerous-Life-1939**（18 分） · 2026-10-22T11:47:12+08:00　
> Main feedback is that chat is not the right interaction method for this. It’s clunky and untrustworthy. Make it a searchable DB.
>
> Also every procedure/thing I searched for just told me it couldn’t find anything

---

> **DependentRun6816**（2 分） · 2026-10-22T12:03:17+08:00　
> Thanks for the feedback, looking into it! Can you tell me what procedure you looked for?

---

> **DanManPanther**（2 分） · 2026-10-22T12:27:13+08:00　
> This is a fantastic project. How are you handling the scraping logic? What language(s) are you using? Any frameworks? Is there any way to narrow down what files out of the TBs of data you actually need to scrape/process when it changes monthly - or do you need to do a full scan every time?

---

> **TitleNo1715**（1 分） · 2026-10-22T13:21:15+08:00　
> are you sure you didnt get 150000k users?

---

> **asivee**（1 分） · 2026-10-22T16:05:23+08:00　
> Hey! Can I DM you about this project? I know a use case!

---

> **nnpoker**（1 分） · 2026-10-22T17:04:20+08:00　
> I think your pitch on this post and comments is better than the slogan you have on the website. Good work.

---

> **geistererscheinung**（1 分） · 2026-10-22T18:58:22+08:00　
> That's part of the absurdity of the American medical system, though

---

> **TheMansterMD**（1 分） · 2026-10-22T19:12:34+08:00　
> I was thinking of making the exact thing. I was using the scraped data to look at what insurers paid different facilities. You beat me to it, congrats

---

> **BR1M570N3**（1 分） · 2026-10-22T19:17:01+08:00　
> GREAT idea but built on an absolute fallacy. Payors ABSOLUTELY want people to shop for cheaper services when medically equivalent because it reduces their per member per month costs.
> Also it is legally required for hospitals to make their charges transparent. In fact it's frequently a point of competition between health systems to work with customers to provide upfront costs prior to service for this very reason.

---

> **OnlyFreshBrine**（1 分） · 2026-10-22T19:27:03+08:00　
> Wow. Most insurers offer this kind of thing but it's insular: meaning not comparing to other plans. This gives patients ammo to demand better from their insurers. Shit gonna get messy.

---

> **QuanTradin**（2 分） · 2026-10-22T20:25:17+08:00　
> yeah, nobody designing it from scratch would land anywhere near this. it only makes sense as forty years of patches on patches.

---

> **iolairemcfadden**（6 分） · 2026-10-22T20:41:03+08:00　
> This chat was fairly useless as it offered up see providers then responded it could not show providers. https://momentarylab.com/app/chat/c9ce076d-4cdf-4fcf-8754-fbf7118f080e
>
> I agree chat is poor for this.  Search should have type ahead and allow you to not use it and do some sort of smart lookup with suggestions if the search doesn’t match an exact item.
>
> Here is chat.
> Ask me what a procedure, scan, lab test, or doctor visit costs. Include your ZIP code, and I can look up local estimates and lower-cost providers.
> You:
> MRI lower abdomen
> Momentary:
> I can help with MRI cost estimates! To get the most accurate price for a lower abdomen MRI, could you tell me your ZIP code? This helps me look up local pricing in your area.
> You:
> 22206
> Momentary:
> **LOCAL COST ESTIMATE**
> ZIP area 22206
> **MRI abdomen without contrast**
> Professional (Radiologist)
> LOW
> $24
> TYPICAL
> $161
> HIGH
> $1,163
> CPT 74181
> Legacy negotiated-rate cost engine
> This is an informational estimate, not a guarantee of coverage, a bill, or your out-of-pocket cost.
> Estimated Cost for MRI of Lower Abdomen (Without Contrast)
> Location: 22206
> **What's Included:**
> Radiologist interpretation of the MRI scan
> Report sent to ordering provider
> **What May Be Billed Separately:**
> MRI facility/facility fees (the table above covers the radiologist’s reading fee only)
> Contrast agent (if ordered)
> Follow-up appointments or additional scans
> 💡 **Tip:** Using a freestanding imaging center (not a hospital) often results in lower total costs.
>
> **What would you like to do next?**
> 🏥 **See providers** with the lowest rates
>
> 🔍 **Find in-network providers** (I'll need your insurance info)
>
> If it would help, you can also ask me why this scan is ordered, how to prepare, what contrast involves, or how results are typically interpreted.
>
> You:
> How much at GW hospital
> Momentary:
> **LOCAL COST ESTIMATE**
> ZIP area 22206
> **MRI lower abdomen (facility fee)**
> Facility (Hospital/ASC)
> LOW
> $43
> TYPICAL
> $529
> HIGH
> $632
> CPT 74181
> Legacy negotiated-rate cost engine
> This is an informational estimate, not a guarantee of coverage, a bill, or your out-of-pocket cost.
> Estimated Cost for MRI of Lower Abdomen (Without Contrast) at Hospital Facilities
> Location: 22206 (Washington, DC area, includes GW Hospital and similar facilities)
> These amounts reflect the **facility fee**(charged by hospitals like GW). The facility fee often covers the use of the MRI machine, staff, supplies, and general hospital overhead.
> This table does **not** include the professional fee (radiologist reading the scan), which is billed separately and typically ranges from $50–$200.
> **What's Included:**
> Operating and equipment costs at hospital or hospital-affiliated imaging centers
> **What May Be Billed Separately:**
> Radiologist (professional) interpretation fee
> Contrast agent (if ordered)
> 💡 **Tip:** Hospital MRI fees can be significantly higher than freestanding imaging centers. For potential savings, compare facilities if possible.
>
> **What would you like to do next?**
> 🏥 **See providers** with the lowest rates
> 🔍 **Find in-network providers** (I'll need your insurance info)
> You:
> See providers
> Momentary:
> I can't pull up a ranked list of providers or their rates in this chat, and I don't want to guess at names or prices. Here's how you can compare options near 22206:
> **Get the exact order details.** Ask your clinician for the exact exam name and billing (CPT) code, and whether it's with or without contrast. Prices vary a lot by code.
> **Call freestanding imaging centers.** Ask for the total price for the scan, including both the facility fee and the radiologist's reading fee. Ask about self-pay discounts if you'll pay cash.
> **Compare with GW Hospital.** Ask for the same total price from the hospital, since hospital facility fees are often higher.
> **If you have insurance,** check your insurer's in-network search tool or call the number on your card. Ask whether the scan needs prior authorization.
> **Ask your ordering clinician** whether they can send the order to a different facility.
> Will you be using insurance, or paying out of pocket? I can suggest questions to ask based on that.

---

> **moktor**（1 分） · 2026-10-22T23:42:01+08:00　
> Very cool! I've always thought this would be a good problem to tackle. The lengths the hospitals go through to obscure this information or make it as useless as possible is astounding. The charge master is pretty much its own weird form of archaic language.

---

> **reosanchiz**（1 分） · 2026-10-23T00:30:55+08:00　
> Wow bro nice!! I love developing Health care related solutions.
> If you need a helping hand ever count me in

---

> **Early-Foot7307**（1 分） · 2026-10-23T01:59:04+08:00　
> TIC files are notoriously full of ghost rates and gaps. How are you filtering out providers who don't actually perform a procedure, and how you validate that your estimates match what patients really pay. Transparency tools have struggled to get a footing (Castlight has moved away towards care nav). And generally employers thay have these add ons like Valenz Healthcare Bluebook, Turquoise are expensive solutions.  Not saying it is not worthwhile, but the data is voluminous and messy.

---

> **oyiyo**（15 分） · 2026-10-23T02:37:51+08:00　
> Scrap the chat. Do a plain lookup of procedure * zip code+distance first, as the data is the valuable piece. A maps of places that offer a given procedure would do wonders to visualize price disparity, and would even go viral vs a chat that hides everything.
>
> The chat itself is annoying as it snaps to the bottom as the Agent replies, instead of letting you maintain your scroll up
>
> Great work otherwise! I really hope you find an iteration that speaks to users!

---

> **oyiyo**（3 分） · 2026-10-23T02:41:59+08:00　
> Also the AI returned a very low price for MRI ($5), I asked it which hospital it was, and they replied by saying $5 is not possible. At this point I can't be sure if the number is hallucinated or if it's a data pipeline issue, but it does point at the former, meaning the AI is not trustworthy with its numbers, which makes me no longer trust the app

---

> **nooffense789**（1 分） · 2026-10-23T15:40:18+08:00　
> How can it be 100 TB??

---

> **SnooCauliflowers4570**（1 分） · 2026-10-24T02:02:00+08:00　
> Pretty cool. There were a few bugs and wrong info, but directionally useful.

---

> **root617**（1 分） · 2026-10-24T02:59:26+08:00　
> Can’t emphasize this point enough. @OP exposing the data (and providing some assurance it’s up to date or at least when it was last updated) would massively improve this tool

---

> **papuzek**（1 分） · 2026-10-24T19:38:24+08:00　
> I'd love to solve such a problems but I live in Europe :(

## 导航

- 项目页：[[10-项目/momentarylab.com_588a277a]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
