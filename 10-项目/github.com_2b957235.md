---
type: "project"
title: "Show HN: Pi-hosts – Give the Pi coding agent access to your servers"
project_url: "https://github.com/hunvreus/pi-hosts"
first_seen: "2026-09-21T02:52:41+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_hunvreus
  - story_47943466
  - show_hn
lang: "en"
---

# Show HN: Pi-hosts – Give the Pi coding agent access to your servers

> [!info] 一句话导读
> Give the Pi coding agent access to your servers.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/hunvreus/pi-hosts>
> 首次收录：2026-09-21T02:52:41+08:00
> 来源渠道：HN Show HN
> 标签：author_hunvreus, story_47943466, show_hn
> 最新指标：点赞=23 · 评论=0 · engagement_velocity=23

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:09:14+08:00 | HN Show HN | 点赞=23 · 评论=0 · engagement_velocity=23 | [[20-语料/posts/hn_show/2026-09-21/f28219fa4b53936a_Show-HN-Pi-hosts-–-Give-the-Pi-coding-agent-access]] |
| 2026-09-21T01:13:42+08:00 | HN Show HN | 点赞=23 · 评论=0 · engagement_velocity=23 | [[20-语料/posts/hn_show/2026-09-21/f28219fa4b53936a_Show-HN-Pi-hosts-–-Give-the-Pi-coding-agent-access]] |
| 2026-09-21T02:52:41+08:00 | HN Show HN | 点赞=23 · 评论=0 · engagement_velocity=23 | [[20-语料/posts/hn_show/2026-09-21/f28219fa4b53936a_Show-HN-Pi-hosts-–-Give-the-Pi-coding-agent-access]] |

## 摘要正文

# hunvreus/pi-hosts  Give the Pi coding agent access to your servers.  - Stars: 45 - Forks: 7 - Watchers: 45 - Open issues: 1 - License: MIT License - Default branch: main - Created: 2026-04-28T05:25:34Z  ## Languages  - JavaScript - TypeScript  ## Top Contributors  - hunvreus (7 contributions)  ---  ## README  # pi-hosts  Give the Pi coding agent access to your servers.  `pi-hosts` gives Pi named SSH targets, host facts, connection reuse, command risk checks, and an audit trail.  ```text check docker version on web-1 is api-1 healthy? compare disk usage on web-1 and web-2 check all database servers update nginx config on web-1 and restart it install htop on db-1 vacuum the database on app-1 ```  ## Why This Exists  Pi can often infer `ssh web-1 'command'` by itself. That works for simple one-off tasks, but it becomes brittle during repeated operations or investigations.  With `pi-hosts`, Pi gets:  - predictable target resolution from host names, aliases, and tags - cached host facts such as OS, distro, package manager, service manager, Docker, and sudo - guarded execution with risk classification before remote commands run - lower token burn on repeated workflows because Pi calls …
