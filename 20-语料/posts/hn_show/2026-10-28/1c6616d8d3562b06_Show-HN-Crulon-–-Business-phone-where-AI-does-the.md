---
type: "corpus"
item_id: "1c6616d8d3562b06"
title: "Show HN: Crulon – Business phone where AI does the work, humans make the calls"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50261381"
project_url: "https://crulon.ai/"
author: "rayn11"
published_at: "2026-10-27T16:10:26Z"
captured_at: "2026-10-28T09:39:16+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-28"
pub_day: "2026-10-27"
tags:
  - 语料
  - hn_show
  - author_rayn11
  - story_50261381
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Crulon – Business phone where AI does the work, humans make the calls

> [!info] 一句话导读
> Hi HN, I’m Rayhan. Crulon is a business phone system where an AI agent answers the line and your team works alongside it. You can talk with our demo agent right…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50261381>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：rayn11　|　发布：2026-10-27T16:10:26Z
> 项目链接：<https://crulon.ai/>
> 采集：2026-10-28T09:39:16+08:00　|　id：`1c6616d8d3562b06`

## 正文

Hi HN, I’m Rayhan. Crulon is a business phone system where an AI agent answers the line and your team works alongside it. You can talk with our demo agent right in your browser, no sign-up: https://crulon.ai/#talkWhy I built it: I’ve spent eight years as a software and network engineer, mostly building tools for internet providers, and kept watching small support teams lose customers in the seams. Calls missed after hours. Calls passed from a bot to a person who had to start over. Most voice AI products are a bot sitting on someone else’s phone line, so a handoff means forwarding to another number and losing the context. We built the phone system and the agent as one thing.What that gets you:The handoff happens inside the same system. When something isn’t the AI’s job, it asks the caller, then rings your team (in the browser or on a desk phone) with a note on why they’re calling.
Live calls: anyone with permission can listen to an AI call (no one on the call can hear them) and take it over. It’s the same call, with no transfer and no hold music; the AI just leaves.
Tools: the agent can call any API you define in an Action builder (look up the caller, open a ticket), and it checks with the caller before changing anything.
Outbound campaigns: the agent works through a call list for reminders, renewals and follow-ups, and puts interested people through to your team.
SIP desk phones, and bring-your-own-carrier so you can keep your numbers.
If you run out of AI minutes, calls follow your fallback route (ring the team, voicemail) instead of dropping, and the refused call isn’t billed.How it’s built, briefly: calls come in over SIP into Call Flows (menus, queues, schedules), and your team answers in the browser or on SIP desk phones. Each agent runs on one of two engines. Classic transcribes, thinks, then speaks, so you get exact wording and English, Spanish and French. Live is a full-duplex speech model that listens while it talks and hands tool work to a second model. One fun problem with that split was teaching the agent when to hang up, which I wrote up here: https://crulon.ai/blog/teaching-a-voice-agent-to-hang-upIt isn’t a CRM; it works alongside yours. Built-in Apps connect it to systems like billing and network tools, and anything with a web API plugs in through the Action builder.Pricing is per seat ($24, $49 or $89 a month) with a pool of AI minutes; human calls are included. If you sign up this month, HN30 takes 30% off the first 3 months.I’ll be here all day. Try the agent, try to trip it up, and tell me what you’d want from a phone system like this.

## 关联链接

- https://crulon.ai/#talkWhy
- https://crulon.ai/blog/teaching-a-voice-agent-to-hang-upIt

## 导航

- 项目页：[[10-项目/crulon.ai_e5700a3e]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
