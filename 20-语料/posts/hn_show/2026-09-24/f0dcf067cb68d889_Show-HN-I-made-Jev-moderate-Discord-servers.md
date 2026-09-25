---
type: "corpus"
item_id: "f0dcf067cb68d889"
title: "Show HN: I made Jev moderate Discord servers"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49825787"
project_url: "https://soter.frolleks.site/"
author: "frolleks"
published_at: "2026-09-24T03:14:51Z"
captured_at: "2026-09-24T23:57:22+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-24"
pub_day: "2026-09-24"
tags:
  - 语料
  - hn_show
  - author_frolleks
  - story_49825787
  - show_hn
metrics: {"points": 2, "comments": 2, "engagement_velocity": 2}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:3d"
---

# Show HN: I made Jev moderate Discord servers

> [!info] 一句话导读
> Soter — Discord moderation that watches so you don't have to

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49825787>
> 指标：点赞=2 · 评论=2 · engagement_velocity=2
> 作者：frolleks　|　发布：2026-09-24T03:14:51Z
> 项目链接：<https://soter.frolleks.site/>
> 采集：2026-09-24T23:57:22+08:00　|　id：`f0dcf067cb68d889`

## 正文

Soter — Discord moderation that watches so you don't have to

Early development — not yet 24/7

# Moderation that watches so you don't have to

Soter moderates mostly on its own: every message is scanned for hate speech and spam, and repeat violators are timed out automatically.

Example: a member posts hate speech, Soter deletes it, and the member gets a DM explaining why.

general

M

maya

gg everyone, same time tomorrow?

A

anon_7713 Jev · hate speech 0.97

message hidden for this demo

Deleted by Soter · hate speech

Soter APP DM to anon_7713

Your message was removed because it was flagged as hate speech.

## Built for decisions, not conversation

Jev is a model by TypeSafe AI made specifically for quick, structured decisions. Instead of generating text, it returns typed answers with probabilities.

Soter asks it two things about every message — is it hate speech, and does it look like spam — then acts on the answers: clear cases are removed, borderline ones go to your mods.

Example: Jev judges a spam message and Soter removes it.

new_user_4821 joined 2 minutes ago

@everyone free nitro for the first 50 people, dm me to claim

Jev

is_hate_speech

0.01

spam_level

high_spam · 0.96

Removed and logged to #mod-log

## Hands-off moderation

Set it up once, then let Soter handle the day-to-day.

Hate speech detection

Every message is scanned automatically and flagged the moment it crosses the line.

Spam filtering

Repeated and low-effort spam gets caught before it floods your channels.

Automatic timeouts

Repeat violators are timed out on their own — no mod has to be watching.

Channel exemptions

Exempt specific channels from moderation with a simple settings command.

Configurable thresholds

Tune violation thresholds and timeout duration to fit how strict you want to be.

Mod action logging

Every automated action is logged to a channel you choose, so nothing happens silently.

## Built in the open

Soter is open source, written in TypeScript on Bun, with Jev (via OpenRouter) doing the message analysis. MIT licensed.

# Unspin: Spot Fake News

## 评论（2/2）

> **verdverm** · 2026-09-24T03:54:06.000Z　
> related, Discord is a founding partner for https://roost.tools/ (open source tools for online moderation)

---

> **frolleks** · 2026-09-24T04:45:46.000Z　
> That seems very interesting, thanks for the referral!

## 导航

- 项目页：[[10-项目/soter.frolleks.site_c4356c0d]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
