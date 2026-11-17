---
type: "corpus"
item_id: "443741d504af95d4"
title: "Show HN: Play last week's Outlook outage as the on-call responder"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50525717"
project_url: "https://app.midflight.dev/drills/microsoft-365-outlook-outage"
author: "__warlord__"
published_at: "2026-11-17T00:28:23Z"
captured_at: "2026-11-17T11:09:12+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-17"
pub_day: "2026-11-17"
tags:
  - 语料
  - hn_show
  - author___warlord__
  - story_50525717
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Play last week's Outlook outage as the on-call responder

> [!info] 一句话导读
> Back Back to Midflight Use light theme Use dark theme

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50525717>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：__warlord__　|　发布：2026-11-17T00:28:23Z
> 项目链接：<https://app.midflight.dev/drills/microsoft-365-outlook-outage>
> 采集：2026-11-17T11:09:12+08:00　|　id：`443741d504af95d4`

## 正文

Back Back to Midflight Use light theme Use dark theme
 Outlook mail stops
 Outlook access fails across regions. Act as the service responder: restore capacity, test servers under traffic, and recover delayed mail. Based only on Microsoft's incident updates. The system, logs, and measurements are simulated.
Start drill Enter starts
 10 min Time limit
 3 Incident stages
 Time not documented Responders on the day
Free to play. No account or credit card needed.
 Each stage brings a new problem. Solve it while keeping earlier fixes working.
 This practice result is not saved or shared with a team. Pause stops the clock. If you leave, continue in this browser within 24 hours.
 Use Contain incident to limit damage before you identify the cause.
Outlook clients Incoming traffic Health checks Server capacity Connection handling Exchange mailboxes Delayed mail Exchange dependencies DNS resolution
 The system before the incident.
 What happened on 12–14 Nov 2026 Gives the answer away Microsoft: unavailable servers increased load on the remaining capacity; traffic had not surged.
 Microsoft paused deployments and shifted traffic away from affected infrastructure.
 Microsoft tested an alternative health check and returned a subset of servers to service.
 Microsoft found restarted servers could become unresponsive again when traffic returned.
 Microsoft isolated servers, restarted components, and tested stability as traffic returned.
 Microsoft extended the email timeout to 48 hours to help preserve delayed mail.
 Microsoft expanded recovery gradually and monitored email queues and remaining regional impact.
 Microsoft linked the issue to an earlier network capacity upgrade and a later network change.
 Microsoft described a technical failure unrelated to cyberattacks or AI agents.
 Microsoft later confirmed restoration for the remaining affected customers and regions.
 Loss of available servers can overload the remaining capacity without a traffic spike. Validate health checks, then test restarted servers under traffic. Restore traffic gradually and verify stability at each stage. Preserve delayed mail and check delivery separately from mailbox access. Confirm recovery across affected regions and features. The root-cause explanation remains preliminary.
 More outages to play
 Three services disappear from the internet 4 Oct 2021
 A brief network gap disrupts database writes 21-22 Oct 2018
 Slack fails as people return to work 4 Jan 2021
 Workday returns, but can tenants safely resume? 13–14 Nov 2026
 Hosted Prometheus rejects customer metric writes 19 Jul 2019

## 导航

- 项目页：[[10-项目/app.midflight.dev_88274261]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
