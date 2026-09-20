---
type: "project"
title: "Best practices for hardening Pi & VPS and Docker containers"
project_url: "https://www.reddit.com/r/selfhosted/comments/1w3crhr/best_practices_for_hardening_pi_vps_and_docker/"
first_seen: "2026-09-21T03:20:20+08:00"
sources:
  - reddit
tags:
  - 项目
  - reddit
  - r/selfhosted
  - Docker Management
lang: "en"
stale: true
---

# Best practices for hardening Pi & VPS and Docker containers

> [!info] 一句话导读
> I am new to self-hosting but have been at it for about 3 weeks now. I am currently hosting about two dozen services mostly for self-use on a Raspberry Pi at hom…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://www.reddit.com/r/selfhosted/comments/1w3crhr/best_practices_for_hardening_pi_vps_and_docker/>
> 首次收录：2026-09-21T03:20:20+08:00
> 来源渠道：Reddit 独立开发版块
> 标签：r/selfhosted, Docker Management
> 最新指标：得分=8 · 评论=17 · 赞踩比=0.83

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T03:05:10+08:00 | Reddit 独立开发版块 | 得分=8 · 评论=17 · 赞踩比=0.83 | [[20-语料/posts/reddit/2026-09-21/67b818d3a126b606_Best-practices-for-hardening-Pi-&-VPS-and-Docker-c]] |
| 2026-09-21T03:14:03+08:00 | Reddit 独立开发版块 | 得分=8 · 评论=17 · 赞踩比=0.83 | [[20-语料/posts/reddit/2026-09-21/67b818d3a126b606_Best-practices-for-hardening-Pi-&-VPS-and-Docker-c]] |
| 2026-09-21T03:20:20+08:00 | Reddit 独立开发版块 | 得分=8 · 评论=17 · 赞踩比=0.83 | [[20-语料/posts/reddit/2026-09-21/67b818d3a126b606_Best-practices-for-hardening-Pi-&-VPS-and-Docker-c]] |

## 摘要正文

Hello,,  I am new to self-hosting but have been at it for about 3 weeks now. I am currently hosting about two dozen services mostly for self-use on a Raspberry Pi at home. I access it remotely via a VPS running Pangolin, Traefik, and Gerbil.  I have tried to harden system in every way possible but I am new to selfhosting so appreciating the help of the community. AI has been very helpful in making me hard faster but I am still not sure I am doing everything right. I list what so far I have done:  **Pi and VPS:**     1. On both Pi and VPS: automatic security upgrades for Ubuntu, restrict open ports to only those necessary for VPN tunnel to function and SSH. * SSH to Pi is restricted on home LAN to only my laptop's IP. Remote SSH to Pi only via using VPS as a jump box, requires both keys which are PW protected. * SSH access for both is key only and access is via non-root user. Fail2ban on both systems though this seems to be more important for the VPS. * CrowdSec has been a pain to get working so I have not set this up but it also seems somewhat like overkill for a harden VPS with few open ports? Appreciate you thoughts  **Self-hosted services:**  * All of my self-hosted services are…
