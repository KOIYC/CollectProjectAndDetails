---
type: "corpus"
item_id: "9e0d91d863fc05ee"
title: "Redundant DC power supply for rack"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1xp0uym/redundant_dc_power_supply_for_rack/"
author: "pugglewugglez"
published_at: "2026-11-06T09:58:56+08:00"
captured_at: "2026-11-16T10:02:00+08:00"
lang: "en"
kind: "post"
topic: AI 工具/Agent
shard: "2026-11-16"
pub_day: "2026-11-06"
tags:
  - 语料
  - reddit
  - r/selfhosted
  - Need Help
metrics: {"score": 4, "comments": 5, "upvote_ratio": 1}
comments_count: 5
comments_total: 5
discovered_via: "reddit:14d+settle10"
---

# Redundant DC power supply for rack

> [!info] 一句话导读
> I am looking or buy (or make) a redundant power supply for my rack, with 2x AC inputs to make a redundant 12V DC supply to power a number of SBCs and directly p…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/selfhosted/comments/1xp0uym/redundant_dc_power_supply_for_rack/>
> 指标：得分=4 · 评论=5 · 赞踩比=1
> 作者：pugglewugglez　|　发布：2026-11-06T09:58:56+08:00
> 项目链接：—
> 采集：2026-11-16T10:02:00+08:00　|　id：`9e0d91d863fc05ee`

## 正文

I am looking or buy (or make) a redundant power supply for my rack, with 2x AC inputs to make a redundant 12V DC supply to power a number of SBCs and directly power several HDD/SSD backplanes through the connectors that usually come from an ATX power supply. I have seen a number of “mining rig” breakout power boards that take two or more CRPS power supplies and break out the power to various connectors. However, none of them state if they are actually redundant - they seem to be mostly for getting additional power as they are explicit about the load needing to be populated symmetrically to the physical connectors. My purpose is to split power, yes, but to achieve redundancy if one power supply loses power.

Requirements:
\- \~750W max load, but almost always \~100W. I want to extra max load to be able to absorb spikes such as HDDs spinning up and things turning on/off
\- Two separate AC to DC power supplies powering the shared single 12V supply
\- Redundant - 12V DC is not interrupted if one of the power supplies fails or loses power
\- Power supplies DO NOT need to be ATX compatible - I just need stable, quality, clean DC power as would normally be output by a quality ATX power supply
12V DC output only - no need for any of the other ATX voltages or connectors
\- At minimum, 5x 8-pin 12V ATX Type 4 connectors. More is better
\- At minimum, 8x 6-pin/8-pin 12V ATX PCIE style connectors. More is better
\-Fit into a cheap stock or custom 1U or 2U rack enclosure. I can make any parts needed
\- Would be nice but doesn’t matter: a means to monitor voltage and amps (and watts)
\- Desired: 80 Plus Platinum efficiency rating (Gold is OK too)
\- Trying to keep cost as minimal as is reasonable
If there is no other option I can make a custom PCB - but there has to be something out there, right?

## 评论（5/5）

> **asimovs-auditor**（1 分） · 2026-11-06T09:59:05+08:00　
> Expand the replies to this comment to learn how AI was used in this post/project.

---

> **pugglewugglez**（1 分） · 2026-11-06T10:00:12+08:00　
> No AI

---

> **agowa338**（2 分） · 2026-11-06T16:26:55+08:00　
> Just buy some server PSUs + the power distribution thingy. For supermicro servers you'll find some that have regular connectors then.
>
> Basically you slide two of the server PSUs into the power distribution thingy and it'll convert the proprietary connector into a regular one. (You may need to build your own adapter cables though).

---

> **pugglewugglez**（2 分） · 2026-11-06T16:37:29+08:00　
> Link to the “power distribution thingy”? :)

---

> **agowa338**（2 分） · 2026-11-06T16:40:01+08:00　
> Had to double check the name, but it is really called "Power Distribution Box" or "PDB". Initially thought that was wrong, but that's actually the name. You need the one that fits to your PSUs though.
>
> Here a link to their page in the Supermicro store: https://store.supermicro.com/server-accessories/power-distributor.html

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
