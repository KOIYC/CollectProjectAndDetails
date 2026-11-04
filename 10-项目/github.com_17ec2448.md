---
type: "project"
title: "Show HN: Backuparr – Backups for the *ARR Stack and Plex/Jellyfin/Emby"
project_url: "https://github.com/rsaturns/backuparr"
first_seen: "2026-11-04T09:51:43+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_rsaturns
  - story_50355512
  - show_hn
lang: "en"
---

# Show HN: Backuparr – Backups for the *ARR Stack and Plex/Jellyfin/Emby

> [!info] 一句话导读
> I run the *arr stack on my NAS and like the lazy bad admin I was, didn't backup the configuration files / databases etc. and proceeded to have to set this all u…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/rsaturns/backuparr>
> 首次收录：2026-11-04T09:51:43+08:00
> 来源渠道：HN Show HN
> 标签：author_rsaturns, story_50355512, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-04T09:51:43+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-11-04/7628ccf72dbfc173_Show-HN-Backuparr-–-Backups-for-the-ARR-Stack-and]] |

## 摘要正文

I run the *arr stack on my NAS and like the lazy bad admin I was, didn't backup the configuration files / databases etc. and proceeded to have to set this all up again when my NAS died. Needless to say this sucked. So I got started on a project to ensure I didn't have to go through this again and make it as hands off as possible. I wanted something that would collect backups on a schedule and put them somewhere else, ready in the event the worst strikes again. Doing some scouring I couldn't find anything that addressed this in the manner and scope I was looking for.Backuparr is a single Docker container with a web UI. You give it each app's URL and API key, choose where the backups go (a local folder, Google Drive, OneDrive or Dropbox, all through rclone), and set a schedule and how long to keep them. It currently supports Radarr, Sonarr, Lidarr, Whisparr, Prowlarr, Profilarr, Bazarr, Tdarr, SABnzbd, NZBGet, Tautulli, Jellyfin, Emby, Plex, Seerr, and LazyLibrarian.If an app has a backup API, Backuparr uses it. Emby, Plex and Seerr don't have one, so it takes a SQLite online backup of their databases from a mounted folder. All of them except Profilarr can be restored from Backuparr …
