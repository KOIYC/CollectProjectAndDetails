---
type: "corpus"
item_id: "3dfa61072ce87d36"
title: "Show HN: Aircheck shows every post your agents queued today on one screen"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50413906"
project_url: "https://aircheck.dev/"
author: "kyisaiah47"
published_at: "2026-11-08T15:04:09Z"
captured_at: "2026-11-09T09:39:29+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-09"
pub_day: "2026-11-08"
tags:
  - 语料
  - hn_show
  - author_kyisaiah47
  - story_50413906
  - show_hn
metrics: {"points": 3, "comments": 2, "engagement_velocity": 3}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:3d"
---

# Show HN: Aircheck shows every post your agents queued today on one screen

> [!info] 一句话导读
> Aircheck Today Fix a post Wire your jobs Questions Docs

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50413906>
> 指标：点赞=3 · 评论=2 · engagement_velocity=3
> 作者：kyisaiah47　|　发布：2026-11-08T15:04:09Z
> 项目链接：<https://aircheck.dev/>
> 采集：2026-11-09T09:39:29+08:00　|　id：`3dfa61072ce87d36`

## 正文

Aircheck Today Fix a post Wire your jobs Questions Docs
 Connect Aircheck
Aircheck shows every post your agents queued today on one screen.
 Connect Aircheck See how a post is fixed
 Claude Code Codex
Aircheck reads the posts that your Claude Code, Codex, cron, Airflow and launchd jobs queued for the day and the ad creative that your ad pipeline builds. It shows each item with all of its media and whether it is ready to go out.
Review the whole day before posts go out.
 Aircheck offers a send-time strip, a thumbnail sheet grouped by hour, and a list. Each lane shows a ring until all of its posts are sent.
 The send-time strip places every post at its send time and colors it by platform.
 The sheet shows the first image of each post, grouped by hour, with a slide count.
 The list shows one row per post with its lane, format, send time, and file count.
Aircheck provides three ways to work on a post.
 Each action runs the post's own pipeline again with a headless agent and shows the result beside the original.
 Example Shown only
 Aircheck runs the post's pipeline again and shows a fresh version. It changes nothing.
Feedback Shown only
 Write what should change. Aircheck shows the revised version beside the original and changes nothing.
Repair Can replace
 Aircheck rebuilds the post through its pipeline. When you approve the new version, it replaces the queued post. Undo restores the old one.
Repair is off for sent posts and locks during the last minutes before a send.
Aircheck works with the jobs you already run.
 Each job writes one JSON file per post into a queue folder. The MCP server writes those files, and your agent reports what it queued.
 The MCP server for Claude Code and Codex reads your setup, suggests the wiring, and applies it only after you approve it. You can also read the docs and write the files yourself.
 // queue/2026-11-06/blockdex-hero.json
{
 "lane" : "brand-x" ,
 "at" : "2026-11-06T15:30:00Z" ,
 "kind" : "carousel" ,
 "text" : "Post copy as it will go out" ,
 "media" : [ "slide-1.png" , "slide-2.png" ] ,
 "status" : "queued" ,
 "postUrl" : null
 } Read the full format in the docs
Social posts and ad creative in one review.
 Social and Ads use the same screen. The screen shows the same day and media and provides Example, Feedback and Repair. Only the work changes.
 Social shows posts queued for your lanes, grouped by send hour.
 Ads shows the creative built by your ad pipeline, grouped by the ad account it was cut for.
 Repair replaces a queued post. Repair replaces an ad creative only while it is still a draft.
Aircheck runs the agent on your machine, and a preview cannot post.
 Aircheck starts headless Codex or Claude as a local process. The agent can read your pipelines but writes only in its own run folder, and it has no network.
 Aircheck stores the JSON that describes your posts. It never stores your media.
 Each run keeps the prompt it was given, its log, and its output.
 Runs survive an Aircheck restart.
Questions
 Does Aircheck post for me? No. Your jobs post. Aircheck shows what they queued and can replace a queued post only when you approve a repair.
Which agents does it run? Aircheck runs headless Codex or Claude on your own subscription and your own machine.
Can a preview go out by mistake? No. A preview runs with no network and can write only in its run folder. The prompt also forbids posting.
Can a repair make the problem worse? Press Undo. Aircheck backs up the old copy and files in the run folder.
Which platforms? Any platform your jobs post to. Aircheck reads the queue folder and does not connect to the platforms.
Review tomorrow's posts tonight.
 Install Aircheck and point it at your queue folder.
 Connect Aircheck
 Today Fix a post Wire your jobs Questions Docs Docs Privacy Terms Contact
 Aircheck
 Built by Compound Labs Aircheck is made by Compound Labs, an independent product R&D lab.

## 评论（2/2）

> **loveTech** · 2026-11-08T15:23:07.000Z　
> Congrats for the launch! Create a demo video to help people understand what it is and how it works at Fluxcut(fluxcut.dev): https://www.youtube.com/watch?v=JVBTCoruJ8o

---

> **loveTech** · 2026-11-08T15:24:54.000Z　
> The UI is so beautiful! How did you design? Any skills or plugins you used?

## 导航

- 项目页：[[10-项目/aircheck.dev_90ce6e44]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
