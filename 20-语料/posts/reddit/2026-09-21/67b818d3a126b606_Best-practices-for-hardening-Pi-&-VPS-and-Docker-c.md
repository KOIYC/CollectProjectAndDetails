---
type: "corpus"
item_id: "67b818d3a126b606"
title: "Best practices for hardening Pi & VPS and Docker containers"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1w3crhr/best_practices_for_hardening_pi_vps_and_docker/"
author: "locanse"
published_at: "2026-08-31T20:46:15+08:00"
captured_at: "2026-09-21T01:34:41+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-08-31"
tags:
  - 语料
  - reddit
  - r/selfhosted
  - Docker Management
metrics: {"score": 8, "comments": 17, "upvote_ratio": 0.83}
comments_count: 0
comments_total: 0
discovered_via: "reddit:52d+settle3"
---

# Best practices for hardening Pi & VPS and Docker containers

> [!info] 一句话导读
> I am new to self-hosting but have been at it for about 3 weeks now. I am currently hosting about two dozen services mostly for self-use on a Raspberry Pi at hom…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/selfhosted/comments/1w3crhr/best_practices_for_hardening_pi_vps_and_docker/>
> 指标：得分=8 · 评论=17 · 赞踩比=0.83
> 作者：locanse　|　发布：2026-08-31T20:46:15+08:00
> 项目链接：—
> 采集：2026-09-21T01:34:41+08:00　|　id：`67b818d3a126b606`

## 正文

Hello,,

I am new to self-hosting but have been at it for about 3 weeks now. I am currently hosting about two dozen services mostly for self-use on a Raspberry Pi at home. I access it remotely via a VPS running Pangolin, Traefik, and Gerbil.

I have tried to harden system in every way possible but I am new to selfhosting so appreciating the help of the community. AI has been very helpful in making me hard faster but I am still not sure I am doing everything right. I list what so far I have done:

**Pi and VPS:**

   1. On both Pi and VPS: automatic security upgrades for Ubuntu, restrict open ports to only those necessary for VPN tunnel to function and SSH.
* SSH to Pi is restricted on home LAN to only my laptop's IP. Remote SSH to Pi only via using VPS as a jump box, requires both keys which are PW protected.
* SSH access for both is key only and access is via non-root user. Fail2ban on both systems though this seems to be more important for the VPS.
* CrowdSec has been a pain to get working so I have not set this up but it also seems somewhat like overkill for a harden VPS with few open ports? Appreciate you thoughts

**Self-hosted services:**

* All of my self-hosted services are Docker containers setup via Compose files
* Watchtower for regular updates
* Everything that can be run on loop back, i.e. 127.0.0.1:port:port is setup that way so all traffic is routed to them only from the VPN tunnel between Newt and Gerbil
* Most of my containers are running as root. The AI says this is no good so I should change it. It wasn't something I thought about when I set it up. **Should I downgrade them to lesser user permissions?**

This is all I can think of so far, I may also have done a few other tweaks via AI recs but I am still fairly new to linux so I lose track of the changes I've made.

I aprpeciate your advice on how hard you are

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
