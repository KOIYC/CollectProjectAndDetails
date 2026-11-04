---
type: "corpus"
item_id: "7628ccf72dbfc173"
title: "Show HN: Backuparr – Backups for the *ARR Stack and Plex/Jellyfin/Emby"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50355512"
project_url: "https://github.com/rsaturns/backuparr"
author: "rsaturns"
published_at: "2026-11-03T17:55:49Z"
captured_at: "2026-11-04T09:51:43+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-11-04"
pub_day: "2026-11-03"
tags:
  - 语料
  - hn_show
  - author_rsaturns
  - story_50355512
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Backuparr – Backups for the *ARR Stack and Plex/Jellyfin/Emby

> [!info] 一句话导读
> I run the *arr stack on my NAS and like the lazy bad admin I was, didn't backup the configuration files / databases etc. and proceeded to have to set this all u…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50355512>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：rsaturns　|　发布：2026-11-03T17:55:49Z
> 项目链接：<https://github.com/rsaturns/backuparr>
> 采集：2026-11-04T09:51:43+08:00　|　id：`7628ccf72dbfc173`

## 正文

I run the *arr stack on my NAS and like the lazy bad admin I was, didn't backup the configuration files / databases etc. and proceeded to have to set this all up again when my NAS died. Needless to say this sucked. So I got started on a project to ensure I didn't have to go through this again and make it as hands off as possible. I wanted something that would collect backups on a schedule and put them somewhere else, ready in the event the worst strikes again. Doing some scouring I couldn't find anything that addressed this in the manner and scope I was looking for.Backuparr is a single Docker container with a web UI. You give it each app's URL and API key, choose where the backups go (a local folder, Google Drive, OneDrive or Dropbox, all through rclone), and set a schedule and how long to keep them. It currently supports Radarr, Sonarr, Lidarr, Whisparr, Prowlarr, Profilarr, Bazarr, Tdarr, SABnzbd, NZBGet, Tautulli, Jellyfin, Emby, Plex, Seerr, and LazyLibrarian.If an app has a backup API, Backuparr uses it. Emby, Plex and Seerr don't have one, so it takes a SQLite online backup of their databases from a mounted folder. All of them except Profilarr can be restored from Backuparr itself, once the service container is re-deployed.The closest existing tool I found was servarr-backup, which covers Radarr, Sonarr and Prowlarr and sends backups to S3. I wanted more apps and the destinations I actually use.Limitations: the backup archives themselves aren't encrypted. Only Backuparr's own config (API keys and passwords) and rclone credentials are. Jellyfin, Emby, Plex and Seerr need their folders mounted into the container.I built this with my coding companion du jour claude-code, along with full review, a lot of self testing, debugging, full lab synthetic tests and running it against my own stack. I’ve been using it for two months now and would love some additional feedback.Docs: https://rsaturns.github.io/backuparr/
License: AGPLv3

## 关联链接

- https://rsaturns.github.io/backuparr/

## 导航

- 项目页：[[10-项目/github.com_17ec2448]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
