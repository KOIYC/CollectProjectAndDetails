---
type: "corpus"
item_id: "3f687dc563dc336f"
title: "How do you fight the urge to build first instead If doing marketing/product validation?"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/microsaas/comments/1wg2te2/how_do_you_fight_the_urge_to_build_first_instead/"
author: "ibr-o"
published_at: "2026-09-14T21:01:58+08:00"
captured_at: "2026-09-24T23:59:01+08:00"
lang: "en"
kind: "post"
topic: AI 工具/Agent
shard: "2026-09-24"
pub_day: "2026-09-14"
tags:
  - 语料
  - reddit
  - r/microsaas
metrics: {"score": 8, "comments": 13, "upvote_ratio": 1}
comments_count: 13
comments_total: 13
discovered_via: "reddit:14d+settle10"
---

# How do you fight the urge to build first instead If doing marketing/product validation?

> [!info] 一句话导读
> As a software engineer, I have this dopamine rush about building features for a new product despite knowing well the right thing to do is gather potential payin…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/microsaas/comments/1wg2te2/how_do_you_fight_the_urge_to_build_first_instead/>
> 指标：得分=8 · 评论=13 · 赞踩比=1
> 作者：ibr-o　|　发布：2026-09-14T21:01:58+08:00
> 项目链接：—
> 采集：2026-09-24T23:59:01+08:00　|　id：`3f687dc563dc336f`

## 正文

As a software engineer, I have this dopamine rush about building features for a new product despite knowing well the right thing to do is gather potential paying customers first then build the product. always think I've done enough market research and then proceed to build a set of features. Then surprise surprise, I can't sell the product and I'm here pretending to be shocked.. always fall on this trap thinking if I build enough features, people will eventually come but it never worked, need better discipline to stop building at all.

Started doing the same again recently but then scraped everything and for the first time, I tried to build a waiting list first, then wait to see if people are interested before making something that works.

If there is a single soul interested about the product I'm trying to build right now, I had a vision of the product end to end but scrapped everything and want to have proper validation from someone willing to pay for it. Basically what it does, it will scan your codebase locally and generate a manifest or via GitHub actions then the manifest will track the different APIS, SDK, Al model in your code and compare it to a database of provider notice about deprecations (deprecations are scattered everywhere, not easy to find) so that you can see exactly what will fail in your product before it's too late.

I'm happy to get feedbacks.

## 评论（13/13）

> **Glass-Interaction972**（2 分） · 2026-09-14T21:09:21+08:00　
> Stop writing code until 5 tech managers agree to talk to you. Focus on AI teams whose tools break often when companies make updates. Ask bosses if they will pay to avoid these bugs, and only build the tool if they promise to buy it.

---

> **tom-mart**（1 分） · 2026-09-14T21:23:44+08:00　
> Build what? How can I build something that i haven't discussed and agreed with the client? I don't start building anything until I have detailed contract signed with the client.

---

> **ThomasBuildLab**（1 分） · 2026-09-14T21:32:03+08:00　
> I think the discipline is not “don’t build anything.” It’s “don’t build the product before you’ve tested the outcome.”
>
> A waiting list is useful, but it mostly validates curiosity.
>
> For your idea, I’d take 5 real repos, manually or semi-automatically scan them, and send each owner a short report: “These are the APIs/SDKs/models in your codebase that have upcoming deprecations or migration risk.”
>
> Then watch what happens.
>
> If people ask you to keep monitoring it, send alerts, or pay for continuous coverage, that’s much stronger validation than signups.
>
> Build the smallest version of the result, not the smallest version of the SaaS.

---

> **ibr-o**（1 分） · 2026-09-14T21:38:12+08:00　
> I really like this idea, thank you, will try it!

---

> **mazeway**（1 分） · 2026-09-14T22:44:56+08:00　
> Build a marketing/product validator first?

---

> **Next-Relation9939**（1 分） · 2026-09-14T23:24:50+08:00　
> agree, though id say even 3 solid convos where they describe the pain unprompted is enough to know youre onto something

---

> **ioilmio**（1 分） · 2026-09-15T04:41:44+08:00　
> You don't fight the build urge, you redirect it. Code gives feedback instantly; the market replies in weeks. So feed the urge something that gets judged in a day (a manifest of your own repo, a landing page, a demo gif).
> Building isn't the disease.
> Building things nobody can judge is.
> On the idea — disclosure, I've built adjacent dependency-risk tooling, so discount accordingly:
> scanning a codebase for APIs/SDKs is a commodity. Dependabot does it, SBOM tools do it, a Saturday-afternoon script does it. The hard part is the deprecation-notice database, because providers announce deaths in changelogs, emails, and docs nobody reads. If that's your edge, the scanner is the hook and the notice DB is the moat. Validate the moat.
>  Cheapest test: skip the waitlist. Publish "every deprecation that will hit a typical repo in the next 6 months" where platform engineers live. If they say "where do I pay," build it. If they say "cool," you just saved a quarter.

---

> **ioilmio**（1 分） · 2026-09-15T04:42:11+08:00　
> Disclosure2: I just built FXF — an exchange where founders who don't owe you anything tear into exactly this kind of idea before you burn a month building it. Ask and I'll drop the link.

---

> **geekyneha**（1 分） · 2026-09-15T04:51:23+08:00　
> Sell before you build.

---

> **Apprehensive_Use7047**（1 分） · 2026-09-15T06:27:17+08:00　
> It's psychology, it's the build trap. I teach how to avoid it with a few simple steps. It starts with awareness of your own biases...

---

> **InstanceKey6343**（1 分） · 2026-09-15T20:27:29+08:00　
> This shit happens with everything, i think it's mostly coping from the truth, building things nowadays is like a playground with ai, the real shit happens when u dedicate at least 1-2 hours a day of pure work on the marketing side and product validation, it's really just the truth, and you already know it

---

> **mathayles**（1 分） · 2026-09-16T02:11:01+08:00　
> Easy. Don’t be technical 😊

---

> **devhisaria**（1 分） · 2026-09-16T14:46:40+08:00　
> Waiting lists validate curiosity, not wallets. For your deprecation scanner, manually scan 5 real repos and DM the owners the actual failing APIs you found, then ask for $20/mo.

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
