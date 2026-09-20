---
type: "corpus"
item_id: "5a5abb9570dc6bb4"
title: "Show HN: Give your AI agents access to WhatsApp"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49728159"
project_url: "https://chat-man.net/"
author: "fabian_shipamax"
published_at: "2026-09-16T15:04:08Z"
captured_at: "2026-09-20T09:41:43+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-16"
tags:
  - 语料
  - hn_show
  - author_fabian_shipamax
  - story_49728159
  - show_hn
metrics: {"points": 14, "comments": 31, "engagement_velocity": 14}
comments_count: 31
comments_total: 31
discovered_via: "hn:show_hn:90d"
---

# Show HN: Give your AI agents access to WhatsApp

> [!info] 一句话导读
> Show HN: Free WhatsApp MCP (+UI) – Give Your AI Agents Access to WhatsApp

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49728159>
> 指标：点赞=14 · 评论=31 · engagement_velocity=14
> 作者：fabian_shipamax　|　发布：2026-09-16T15:04:08Z
> 项目链接：<https://chat-man.net/>
> 采集：2026-09-20T09:41:43+08:00　|　id：`5a5abb9570dc6bb4`

## 正文

Show HN: Free WhatsApp MCP (+UI) – Give Your AI Agents Access to WhatsApp | Hacker News

Show HN: Free WhatsApp MCP (+UI) – Give Your AI Agents Access to WhatsApp

8 points by fabian_shipamax 32 minutes ago | hide | past | favorite | 10 comments

Hi,

I built Chat-Man because I wanted a cheap way to give my agents access to WhatsApp without integrating a WhatsApp library separately in every project.

You get WhatsApp MCP server, so you can connect WhatsApp to an agent and programmatically read, search, extract and send messages - but also have a web UI for non-techies.

You can also receive webhooks for incoming messages for starred conversations.

What you can do with the MCP? -Read WhatsApp messages and turn them into CRM records -Summarise conversations or groups -Extract structured information from messages -Find messages, participants or other WhatsApp data -Send messages -Manage group memberships

Of course.. you always need to follow data protection regulation.

The web UI: -Edit group details -See who joined or left -See who is most active -Export group members -Match members against a CSV (e.g. from a CRM) -Bulk message members -Bulk kick members -Create invite links For individual contacts, you can send messages directly from the UI.

Why I built it for myself? I needed WhatsApp access for several projects (hermo.ai, florahaus.co.uk, …) and didn't want to pay for a WhatsApp integration for each project.

Link: https://chat-man.net

I’d love to get some feedback, especially from people building agents that need access to WhatsApp. Fabian

LawrenceKerr 14 minutes ago | next [–]

Does this require a Meta / WhatsApp business account?

If not, is this a solution using WhatsApp Web in the backend (like Baileys does)? If this is the case, how does your solution avoid getting blocked or banned? I used Baileys once in an MVP with only 7 users, and my agent got blocked really quickly after just a few days of using it. So I guess the official path is the only way to go?

fabian_shipamax 12 minutes ago | parent | next [–]

No it doesn’t.

fabian_shipamax 10 minutes ago | root | parent | next [–]

If you use it for personal and not excessively you won’t get banned is my experience. You if you start messaging new contacts on a large scale you probably will.

TZubiri 3 minutes ago | prev | next [–]

Breaks ToS

Will be used to spam

kreidema 14 minutes ago | prev | next [–]

Do I understand correctly that your service works as a registered device into my whatsapp account with full "admin" like access? This seems a bit harsh for the sensitive data that peoples wahatsapp contain? Or am I missing a usecase here where that is unproblematic? Business accounts maybe?

fabian_shipamax 9 minutes ago | parent | next [–]

Not quite sure what you mean with admin access. There no such concept. But you can basically do anything a user can do - but via MCP.

asteroidburger 11 minutes ago | parent | prev | next [–]

Businesses should be using WhatsApp business accounts. They cost money per message sent and don’t support groups, but it’s the officially sanctioned way to do it.

fabian_shipamax 9 minutes ago | root | parent | next [–]

Businesses can use the official API which is costly and takes time to set up. Correct.

lordgrenville 9 minutes ago | prev [–]

Am I correct in guessing that this is a ToS violation and could lead to getting blocked?

fabian_shipamax 5 minutes ago | parent [–]

You are right that this is a consideration and risk. But it can make your life much easier. The reality is that these tool are available now. This is in fact not the first one like this. It can make the work of small businesses or clubs more more efficient.

## 评论（31/31）

> **kreidema** · 2026-09-16T15:22:09.000Z　
> Do I understand correctly that your service works as a registered device into my whatsapp account with full "admin" like access? This seems a bit harsh for the sensitive data that peoples wahatsapp contain? Or am I missing a usecase here where that is unproblematic? Business accounts maybe?

---

> **LawrenceKerr** · 2026-09-16T15:22:20.000Z　
> Does this require a Meta / WhatsApp business account?If not, is this a solution using WhatsApp Web in the backend (like Baileys does)? If this is the case, how does your solution avoid getting blocked or banned? I used Baileys once in an MVP with only 7 users, and my agent got blocked really quickly after just a few days of using it. So I guess the official path is the only way to go?

---

> **lordgrenville** · 2026-09-16T15:27:30.000Z　
> Am I correct in guessing that this is a ToS violation and could lead to getting blocked?

---

> **TZubiri** · 2026-09-16T15:33:45.000Z　
> Breaks ToSWill be used to spam

---

> **lbrito** · 2026-09-16T15:40:54.000Z　
> Are people really this nonchalant about giving away their private whatsapp conversations to the likes of Anthropic and Openai?

---

> **monononon34** · 2026-09-16T15:54:38.000Z　
> it looks like a dangerous. i can't trust the LLM

---

> **cute_boi** · 2026-09-16T15:55:52.000Z　
> how is this different than https://github.com/WhiskeySockets/Baileys which seems more reliable?

---

> **yablak** · 2026-09-16T15:59:56.000Z　
> Looked into this a while back. WhatsApp MCP servers attach as a second device to WhatsApp and pull down your message history.Most of the ones I've seen on github do not store the messages encrypted locally.When evaluating these tools, check to see what they store unencrypted on disk. A quick search shows that only one seems to check the boxes:https://github.com/adelaidasofia/whatsapp-mcpHowever I haven't tested it. And it does phone home, you may want to disable that before running it.

---

> **KellyCriterion** · 2026-09-16T16:11:14.000Z　
> Take a look at www.superchat.com, they are doing something similar for B2B

---

> **nom** · 2026-09-16T16:15:29.000Z　
> Using this will get your WhatsApp account banned sooner or later.

---

> **lucenacloud** · 2026-09-16T17:31:04.000Z　
> nice! i will try it out! amazing!

---

> **asteroidburger** · 2026-09-16T15:24:47.000Z　
> Businesses should be using WhatsApp business accounts. They cost money per message sent and don’t support groups, but it’s the officially sanctioned way to do it.

---

> **fabian_shipamax** · 2026-09-16T15:27:42.000Z　
> Not quite sure what you mean with admin access. There no such concept. But you can basically do anything a user can do - but via MCP.

---

> **fabian_shipamax** · 2026-09-16T15:24:19.000Z　
> No it doesn’t.

---

> **fabian_shipamax** · 2026-09-16T15:31:16.000Z　
> You are right that this is a consideration and risk. But it can make your life much easier. The reality is that these tool are available now. This is in fact not the first one like this. It can make the work of small businesses or clubs more more efficient.

---

> **gcgbarbosa** · 2026-09-16T15:54:58.000Z　
> This is ToS violation for sure. OP will soon receive a letter from Zuck's lawyers

---

> **liotier** · 2026-09-16T15:42:34.000Z　
> Any opening of proprietary chat to useful tools will be used for spam too. It is a curse.

---

> **dpoloncsak** · 2026-09-16T15:42:42.000Z　
> This can be used locally, no?

---

> **robertclaus** · 2026-09-16T15:52:07.000Z　
> I'm much more concerned about the odds that this tool is vibe coded and will leak the conversations everywhere other than the LLM agent I've already vetted.

---

> **addag** · 2026-09-16T15:57:53.000Z　
> Oh gosh, if only it was just the whatsapp chats...

---

> **monononon34** · 2026-09-16T15:56:27.000Z　
> does it have any security system?

---

> **fabian_shipamax** · 2026-09-16T15:26:50.000Z　
> Businesses can use the official API which is costly and takes time to set up. Correct.

---

> **blueplanet200** · 2026-09-16T15:56:17.000Z　
> Exactly. OP meant that it has permission to do anything, hence "admin".

---

> **fabian_shipamax** · 2026-09-16T15:26:07.000Z　
> If you use it for personal and not excessively you won’t get banned is my experience. You if you start messaging new contacts on a large scale you probably will.

---

> **dpoloncsak** · 2026-09-16T15:47:31.000Z　
> ...with the risk of getting banned, you can't reasonably use this for anything 'important'.In order to make my life easier, it probably needs to be doing important stuff.You can't hide behind 'other apps are doing it too', if my 'important business account' or whatever gets banned from using your tool, I'd be upset at you.How do you guarantee your uptime SLA if my account may get banned any second?

---

> **TZubiri** · 2026-09-16T17:30:32.000Z　
> might be orthogonal to whether it's proprietary or Free Software in theory (although correlated in practice), couldn't a communication software be Open Source and free licensed BUT ask that users only use the software in a manual fashion and never automated?A harder version of the clause, that only a specific interface be used, might be contrary to Free Software howeer, as it would infringe in the right to modify (the interface), but not the right to study the software.

---

> **testycool** · 2026-09-16T15:44:27.000Z　
> And you typically use them for business, not on private accounts.

---

> **fabian_shipamax** · 2026-09-16T15:46:40.000Z　
> It’s a cloud product

---

> **thomasjeff1** · 2026-09-16T15:55:20.000Z　
> That is normal when you lose your contacts and do an external backup. WhatsApp thinks I am texting large number of strangers whereas I already know those contacts. Happened to me. Lost access to WhatsApp.

---

> **lbrito** · 2026-09-16T15:59:14.000Z　
> Most of the use cases in the page are personal, like Family Group, Sports Group and so on."Pick members and send them a personal direct message".

---

> **dpoloncsak** · 2026-09-16T15:56:49.000Z　
> Sorry, I may has misphrased what I meant. Can I use this with a local model? Or is it locked to Claude

## 关联链接

- https://chat-man.net

## 导航

- 项目页：[[10-项目/chat-man.net_e816be7b]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
