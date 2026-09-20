---
type: "project"
title: "Screening login attempts for containerized applications"
project_url: "https://www.reddit.com/r/selfhosted/comments/1whh7zz/screening_login_attempts_for_containerized/"
first_seen: "2026-09-20T09:24:44+08:00"
sources:
  - reddit
tags:
  - 项目
  - reddit
  - r/selfhosted
  - Need Help
lang: "en"
stale: true
---

# Screening login attempts for containerized applications

- **项目链接**：https://www.reddit.com/r/selfhosted/comments/1whh7zz/screening_login_attempts_for_containerized/
- **首次收录**：2026-09-20T09:24:44+08:00
- **来源渠道**：Reddit 独立开发版块
- **标签**：r/selfhosted, Need Help
- **最新指标**：得分=4 · 评论=8 · 赞踩比=0.7

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:24:44+08:00 | Reddit 独立开发版块 | 得分=4 · 评论=8 · 赞踩比=0.7 | [[20-语料/posts/reddit/2026-09-20/20691509a7c2cc30_Screening-login-attempts-for-containerized-applica]] |

## 摘要正文

Hello everyone,  Forgive me for what may be a newby question, but I have a web application - in this case Jellyfin, that I host for myself and some family and friends. I currently have Jellyfin running in a Docker container, and Nginx running on the host machine serving it.  I've done a decent job hardening the configuration for both, but I'd still like to use fail2ban to autoban IPs that fail logins. The issue I'm having here is that Jellyfin's logs only show internal Docker network IPs, and so all activity reported in the logs only shows as some address in the 172.16.0.0/12 subnet. Nginx doesn't have any of its own user authentication set up, so sniffing the Nginx logs yields no results, and thus no bans.   So my question is:  Is there a way to have jellyfin detect source IPs from behind NAT so that I can actually create a fail2ban filter that works, or is this a larger misconfiguration problem that would require me to restructure how I've built this server?  I'm fairly new to hosting and would greatly appreciate some guidance here. Thanks :)
