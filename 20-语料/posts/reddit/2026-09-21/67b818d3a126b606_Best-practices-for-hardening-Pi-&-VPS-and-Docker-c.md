---
type: "corpus"
item_id: "67b818d3a126b606"
title: "Best practices for hardening Pi & VPS and Docker containers"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1w3crhr/best_practices_for_hardening_pi_vps_and_docker/"
author: "locanse"
published_at: "2026-08-31T20:46:15+08:00"
captured_at: "2026-09-21T13:04:37+08:00"
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
comments_count: 12
comments_total: 17
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
> 采集：2026-09-21T13:04:37+08:00　|　id：`67b818d3a126b606`

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

## 评论（12/17）

> **asimovs-auditor**（1 分） · 2026-08-31T20:46:25+08:00　
> Expand the replies to this comment to learn how AI was used in this post/project.

---

> **locanse**（0 分） · 2026-08-31T20:47:20+08:00　
> I did not use AI to write this post at all I wrote it with my own two hands and ten fingers. I do discuss using AI for my project but not for this post

---

> **Bloated_Plaid**（1 分） · 2026-08-31T20:58:49+08:00　
> Tailscale will solve a lot of problems here.

---

> **ChubbyWabbit**（2 分） · 2026-08-31T21:06:06+08:00　
> If you're the only user, I'd just use an overlay VPN like Netbird or Tailscale & forgo the VPS.

---

> **GolemancerVekk**（2 分） · 2026-08-31T22:01:04+08:00　
> > Most of my containers are running as root. [...] Should I downgrade them to lesser user permissions?
>
> You can try but some of them will not play nice.
>
> Here's the main 4 compose settings that are needed for a minimum downgrade:
>
>     user: "1000:1000" # or whatever non-root user you wanna use
>     security_opt:
>       - no-new-privileges
>     cap_drop:
>       - ALL
>     read_only: true
>
> I would try them one by one from the top and see how it goes. Some apps accept all of them without fuss but for many of them you will have to use workarounds.
>
> * You can work around the UID:GID with bind mounts owned by that user, `tmpfs:`mount points like `/dev/shm:mode=770,uid=1000,gid=1000,size=256m`, `group_add:` for making that user a member of groups that own certain devices, and/or `device_cgroup_rules:` for access to special devices.
> * You can work around the caps by using `cap_add:` with [specific capabilities](https://www.man7.org/linux/man-pages/man7/capabilities.7.html), but figuring out which capabilities for which errors can be very time consuming.
> * Same for read only, in theory the workarounds are the same as for the user but figuring out the paths that need to be made a bind mount or tmpfs can be very time consuming. Sometimes an app will not even tell you enough to figure out which path is the problem, or they have stupid settings that make it impossible to map out entire folders, like when they want to create their temporary files in with the app files.
>
> Some apps are so badly made that it's pointless to even try. For example if you come across something that uses s6 and bundles multiple apps in the same docker image, just save yourself the grief and don't bother. Frigate is one such example, the app itself is nice to use but the docker image is horrifying and almost impossible to secure properly.

---

> **pelazas1**（2 分） · 2026-08-31T22:37:02+08:00　
> downgrading them is fine until watchtower updates something that already wrote files as root. then it just can't open its own files.

---

> **FanClubof5**（3 分） · 2026-09-01T00:10:01+08:00　
> This is my distilled list of security hardening guidelines.
>
> **Identity & privileges**
>
> * cap_drop: [ALL] on every service. Only add back what you explicitly need.
>
> * security_opt: ["no-new-privileges:true"] — blocks setuid escalation.
>
> * Run as non-root: explicit user: "1000:1000", or PUID/PGID for LSIO images.
>
> **Resource limits**
>
> * mem_limit + memswap_limit
>
> * pids_limit set
>
> * cpu_shares
>
> **Image hygiene**
>
> * No :latest. Use SHA pinning for best security.
>
> **Networking**
>
> * Separate networks unless containers need to talk to each other. A db might be on a stack specific network while a webui might have access to a shared traefik network.
>
> **Secrets**
>
> * Nothing in compose/env files. Pull from secrets manager for easy rotation if compromised.

---

> **Fickle-Owl666**（1 分） · 2026-09-01T00:28:44+08:00　
> "AI has been very helpful in making me hard"
>
> 😂😂😂😂

---

> **TechnicianGreedy7998**（1 分） · 2026-09-01T08:25:24+08:00　
> agreed with everything except pinning versions

---

> **Anonimoste**（1 分） · 2026-09-01T13:32:23+08:00　
> I am a huge fan of using cloudflare reverse tunnel. This allows devices to be secured with 2FA and all ports can be closed. I’m not sure if it’s appropriate for you since you are using it for home devices, but you mentioned access via VPS, etc so I figured I’d throw it out there.

---

> **RyuuPendragon**（1 分） · 2026-09-13T02:56:33+08:00　
> Why? You want to use latest and update without checking breaking updates?

---

> **TechnicianGreedy7998**（1 分） · 2026-09-13T03:43:04+08:00　
> If you’re on top of your homelab you can do that, but if you keep containers sitting without security updates that’s a vulnerability

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
