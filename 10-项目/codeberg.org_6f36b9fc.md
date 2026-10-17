---
type: "project"
title: "What I run - Oct 2026"
project_url: "https://codeberg.org/forgejo/forgejo"
first_seen: "2026-10-17T13:37:02+08:00"
sources:
  - reddit
tags:
  - 项目
  - reddit
  - r/selfhosted
  - Wednesday Exceptions
lang: "en"
---

# What I run - Oct 2026

> [!info] 一句话导读
> I just want to introduce myself and tell you all about my homelab. It's all pretty high-level, feel free to ask me about anything here.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://codeberg.org/forgejo/forgejo>
> 首次收录：2026-10-17T13:37:02+08:00
> 来源渠道：Reddit 独立开发版块
> 标签：r/selfhosted, Wednesday Exceptions
> 最新指标：得分=312 · 评论=66 · 赞踩比=0.93

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-17T13:37:02+08:00 | Reddit 独立开发版块 | 得分=312 · 评论=66 · 赞踩比=0.93 | [[20-语料/posts/reddit/2026-10-17/7a4f2d437b67a769_What-I-run-Oct-2026]] |

## 摘要正文

Helllooo everyone!  I just want to introduce myself and tell you all about my homelab. It's all pretty high-level, feel free to ask me about anything here.  # About me  I’m just someone that absolutely loves technology. Software and systems are mostly where my heart lies, I’ve been working in IT for about 19 years. I have been homelabbing and self-hosting since about 2005. It started with game servers then learning how to become a sys admin, then wanting control over my data, and now I just want to explore different technology stacks and new software.  My homelab is a bit of a mix of running services for my family and a testing ground for learning new technology.  # Quick and dirty  My entire homelab is Proxmox as the hypervisor, debian VMs to run Docker and Komodo. Forgejo  deploys my containers on Komodo. Docker labels control Traefik and exposure.  6 hosts (3 “production” and 3 test lab) and \~147 containers.  |Hostname|CPU|RAM|Storage|Used For| |:-|:-|:-|:-|:-| |Jupiter|i7-9800X|128GB|122TB|App + Storage| |Saturn|i9-13900K|64GB|3TB|Home Assistant + Dev + DNS (Secondary)| |Mars|N150|16GB|500GB|Router + DNS (Primary)| |Neptune|2x Xeon Silver 4214R|1.5TB|24TB|Testing + DR| |Uranus…
