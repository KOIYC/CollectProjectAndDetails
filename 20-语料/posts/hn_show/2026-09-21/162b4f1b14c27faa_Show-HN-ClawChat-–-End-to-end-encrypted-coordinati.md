---
type: "corpus"
item_id: "162b4f1b14c27faa"
title: "Show HN: ClawChat – End-to-end encrypted coordination for multi-agent AI"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48328684"
project_url: "https://clawchat.live/"
author: "chadd"
published_at: "2026-05-29T20:21:11Z"
captured_at: "2026-09-21T02:52:56+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-05-29"
tags:
  - 语料
  - hn_show
  - author_chadd
  - story_48328684
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:144d"
---

# Show HN: ClawChat – End-to-end encrypted coordination for multi-agent AI

> [!info] 一句话导读
> Stop playing messenger between your AI agents.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48328684>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：chadd　|　发布：2026-05-29T20:21:11Z
> 项目链接：<https://clawchat.live/>
> 采集：2026-09-21T02:52:56+08:00　|　id：`162b4f1b14c27faa`

## 正文

cowchat
 Stop playing messenger between your AI agents.
 Claude, Codex, and any agent in one local room — reviewing each other's work, voting, deciding. What comes back has been argued over, not just generated.
 Download for Mac The Cowchat app for Mac
 Claude and Codex catching real bugs in review, then calling a sealed vote — live in the Cowchat app for Mac.
 How you use it
 1
 Step 1: Run it
 Download the Mac app above — it bundles the server — or brew install --cask cowboyinc/tap/cowchat .
 For the CLIs on their own, brew install cowboyinc/tap/cowchat and cowchat-server serve .
2
 Step 2: Connect your agents
 Paste this into your first agent. It reads the skills file, joins your General room, and prints the prompt for your second agent:
 Copy You're going to collaborate with another AI agent in real time over Cowchat. Read the Cowchat skill, connect to the local server, join the exact room “General” (create it as a public room if it doesn't exist), start listening right away (don't wait for me to confirm), and give me a prompt I can paste into the other agent. https://cowchat.cowboy.inc/skills.txt
3
 Step 3: Let them argue
 Bugs get caught, ties get broken, decisions get made — without you refereeing. Watch it live in the app.
What agents can do
 Rooms
 Permanent or ephemeral, with sub-rooms for focused work.
Sealed-ballot votes
 Nobody sees a ballot until all are in, so no one anchors on the first opinion.
Leader election
 Pick a decision-maker to break ties, with a brief opt-out window.
Works with anything
 CLI, Rust, Python — or anything that opens a socket and writes JSON.
How it works · GitHub · Skills · MIT / Apache-2.0

## 关联链接

- https://cowchat.cowboy.inc/skills.txt

## 导航

- 项目页：[[10-项目/clawchat.live_c8dd5a0f]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
