---
type: "corpus"
item_id: "95547e10417f23e2"
title: "How do you tell a self-hosted customer “that’s your infra”"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/SaaS/comments/1x9ti3k/how_do_you_tell_a_selfhosted_customer_thats_your/"
author: "navigatethefirewall"
published_at: "2026-10-19T18:43:06+08:00"
captured_at: "2026-10-29T20:44:32+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-10-29"
pub_day: "2026-10-19"
tags:
  - 语料
  - reddit
  - r/SaaS
metrics: {"score": 24, "comments": 28, "upvote_ratio": 1}
comments_count: 27
comments_total: 28
discovered_via: "reddit:14d+settle10"
---

# How do you tell a self-hosted customer “that’s your infra”

> [!info] 一句话导读
> Say a paying customer’s app stops working. They host it themselves, and the problem turns out to be something they changed in their setup.

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/SaaS/comments/1x9ti3k/how_do_you_tell_a_selfhosted_customer_thats_your/>
> 指标：得分=24 · 评论=28 · 赞踩比=1
> 作者：navigatethefirewall　|　发布：2026-10-19T18:43:06+08:00
> 项目链接：—
> 采集：2026-10-29T20:44:32+08:00　|　id：`95547e10417f23e2`

## 正文

Say a paying customer’s app stops working. They host it themselves, and the problem turns out to be something they changed in their setup.

From their side, they paid for your product and it isn’t working. I can understand why they’d come to you.

What I’d struggle with is knowing when to stop helping. You might need to spend hours investigating before you can even explain why it’s their setup. By then, you’ve already done a fair amount of the work.

I wouldn’t want to leave them stuck, but I also wouldn’t want every ticket to become our engineering team fixing someone else’s environment.

If you offer self-hosting options, how do you navigate this conversation?

## 评论（27/28）

> **TheSinfulBasin**（14 分） · 2026-10-19T18:52:34+08:00　
> Scope of support has to be real clear from the jump, otherwise you end up debugging their mess for free.

---

> **Ok-Count-3366**（0 分） · 2026-10-19T18:54:38+08:00　
> I would do it like this:
> you probably have multiple customers so I assume your app is a multitenant application.
>
> When a ticket comes in, the first thing you check is:
> DO ALL CLIENTS HAVE THAT ISSUE?
> or you check it on your test server.
> IF YES that means it's your software, if no that means it's mostly their infrastructure.
> If not every client have that issue you need to explain to the customer:
>
> I will investigate this: if this is related to a bug in my software that is so circumstantial that only occurs on your setup, then fine. But if it IS a problem with your setup, then you pay me for my time. Simple as that.

---

> **Business448**（1 分） · 2026-10-19T19:08:54+08:00　
> Simple rule for self-hosted: We are responsible for the software, not your server.
>
> We will show you where the problem is, but fixing your server is not part of our support.

---

> **Spare-Ad-1429**（43 分） · 2026-10-19T19:20:43+08:00　
> you make the self hosted plan expensive enough so that you properly support them

---

> **NegottionOk**（7 分） · 2026-10-19T19:43:32+08:00　
> you gotta build diagnostic scripts that they have to run before opening a ticket so they end up finding their own broken config files

---

> **maiznieks**（7 分） · 2026-10-19T20:47:54+08:00　
> Sell consulting.

---

> **NagibCazau-52**（10 分） · 2026-10-19T21:07:00+08:00　
> pricing alone wont fix the boundary issue, a $5k/mo customer whos environment is broken will feel even more entitled to your eng time

---

> **leon_pylo**（1 分） · 2026-10-19T21:35:17+08:00　
> You need to establish boundaries and where the scope of your support ends as early as possible and you should probably adjust the pricing for your self-hosted version.
>
> Self-hosted solutions may have some advantages, but the issue always stays that you either have to invest time to investigate in someone else's infrastructure or you cannot guarantee the same great user experience as you can when you own the infra.

---

> **GDur**（6 分） · 2026-10-19T22:13:55+08:00　
> Wowowow.. You guys have customers? :D
> (as in I don't even have customers)

---

> **IssueRemote8759**（4 分） · 2026-10-20T01:09:46+08:00　
> this. also keep a clean install around. if it works there with their config, just show them the diff, way easier than arguing

---

> **emcell**（1 分） · 2026-10-20T01:58:15+08:00　
> i usually charge a high amount per hour to fix. If it turns out that it's my fault, the support is free. I'm always honest and most customers are really happy with this solution

---

> **spiggle_64236**（3 分） · 2026-10-20T03:13:11+08:00　
> What helped me was deciding the line before the ticket shows up, so it's a policy and not a judgment call at 11pm.
>
> Ship a small health-check command (versions, env, DB connection, queue, disk, file permissions) and ask for its output in the very first reply. Half the time they find the problem themselves.
>
> Timebox: "We'll spend up to 30 minutes confirming whether it's our software or your environment." If it's theirs, you tell them where it is, you don't fix it.
>
> Tag those tickets "customer infra." After a month you'll know which setup mistakes keep coming back. Those become docs, or checks inside the health command.
>
> Anything past the timebox is paid setup help, priced per hour or as a pack.
>
> Saying "it's your server" lands much better when you can show the exact failing check instead of just telling them.

---

> **Old-Confection-5129**（0 分） · 2026-10-20T05:47:26+08:00　
> Are you providing a dockerized solution?

---

> **Fire_Lake**（9 分） · 2026-10-20T09:17:18+08:00　
> I think that was their point, charge them enough that it covers your support time

---

> **NotA_A**（1 分） · 2026-10-20T12:38:34+08:00　
> Interesting. Same problem in Corporate vs SaaS, but different players.
> Corporate: What did infra change that now is blaming the Dev's code that hasn't changed?
> SaaS: What did the customer change who now wants the provider to fix?
>
> I like the answer I've seen here (what I understand as) about a diagnostic script that may show their deviation from your deployed baseline. Therefore it's their infra-change.

---

> **Dekkars**（2 分） · 2026-10-20T20:59:47+08:00　
> We had this issue with self hosted enterprise.
>
> The easiest way was to require a log file to open a ticket. That log file’s main job was to make it very clear if it was us or if it was them.
>
> We had automated parsing when the file came in that posted an internal comment on the ticket letting support know.
>
> That said - this was highly available multi tenant cluster type stuff. Our stuff was usually always up to pull the log files on at least one of the nodes

---

> **mmcnama4**（1 分） · 2026-10-22T00:47:01+08:00　
> That and you know they're likely big enough to have the correct resources internally as well

---

> **Ash_ArceusLegal**（1 分） · 2026-10-22T04:40:06+08:00　
> Have a very clear support contract related to what diagnostic time costs. You might offer the first 30 minutes free and then a high hourly rate.
>
> Anything past that 30 minutes, if it turns out to be their infra, you get reimbursed for your time. But if it’s a problem with your app, you waive the hourly fee.
>
> It’s not a bad idea to have an attorney review the agreement.

---

> **Main_Cheesecake4059**（1 分） · 2026-10-24T10:43:19+08:00　
> That was my fault. I made a dns change. I appreciate the help though.

---

> **EmergencyPrize8567**（1 分） · 2026-10-24T13:39:07+08:00　
> I've seen where the clients employees assumes its problems are our stuff . And bypasses it to try and fix the system . Then wants us to put it all back together again ,  and figure out the problem . So while we are there on site . The employees by- passed these systems we put back together again , Before we have even completed all of them . And had a chance to understand where the main problem was ? This was back in the days with a very large Casino / Hotel . Turns out ,the problem was with their stuff !

---

> **Davx-Forever**（1 分） · 2026-10-24T18:39:15+08:00　
> I ran a company that supported IP CCTV systems. Generally we are using their network or their servers sometimes. There were a lot of occations where the customer changed something or a switch went down and we get a call to investigate. We would always do as much as we could but it did waste a lot of time.
>
> Nowadays I would build custom scripts with AI to run tests and flag who was at fault.

---

> **Xyz3r**（1 分） · 2026-10-24T22:52:38+08:00　
> Yeah if you sell on premise it’s priced in a way yyou can hire someone to support them full time.
>
> They’ll pay up if it’s important to them. Otherwise it’s doomed to not work out anyway numbers wise

---

> **peasantking**（1 分） · 2026-10-25T14:51:30+08:00　
> Brilliant idea

---

> **ImpressiveFee6007**（1 分） · 2026-10-26T07:42:15+08:00　
> As a customer who runs self-hosted enterprise software, I really appreciate the vendors that have a clean install, and are willing to reproduce things on their end. I’ve had multiple times where I’m very certain it is a bug in the software but it takes going back and forth with the vendor for weeks on end to “prove” its a bug and not something we screwed up in our environment. When I have clear, reproducible steps for the bug, it saves so much time for the vendor to just reproduce it instead of doing many rounds of troubleshooting and back and forth.

---

> **ILikeToHaveCookies**（1 分） · 2026-10-26T13:11:03+08:00　
> Make it 10k month and hire someone to support them, if he has time left over that's a bonus

---

> **fatalglory**（1 分） · 2026-10-26T15:44:03+08:00　
> You could charge them for tech support on a pay-as-you-go basis. If they opt to self host then need your engineering team to bail out their admins, you bill them for the time it took to sort out.
>
> Maybe give them a basic amount of free support hours per month (say 3 hours) if they are a premium customer, but charge them for anything beyond that.
>
> If you don’t make the terms absolutely explicit, then there are some SaaS customers who will just keep pushing you for more and more free custom work. Ask me how I know 😅

---

> **fatalglory**（1 分） · 2026-10-26T15:47:34+08:00　
> It’s like the old joke about the doctor and the lawyer at a party. The doctor asks the lawyer “Hey, how do you stop people trying to get free advice from you at parties? Sometimes I want to just relax and not answer medical questions.”
>
> The lawyer answers “I start billing them for advice I give them at parties. That stops it real quick.”
>
> The next morning, the doctor opens his mailbox to find an invoice from the lawyer that says “Consult at party last night: $1,000.”

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
