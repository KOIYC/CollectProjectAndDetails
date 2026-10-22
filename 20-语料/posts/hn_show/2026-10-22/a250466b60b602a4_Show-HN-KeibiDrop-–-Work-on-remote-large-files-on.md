---
type: "corpus"
item_id: "a250466b60b602a4"
title: "Show HN: KeibiDrop – Work on remote large files on-demand (no upload/download)"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50180280"
project_url: "https://github.com/KeibiSoft/KeibiDrop"
author: "coldstartops"
published_at: "2026-10-21T13:06:09Z"
captured_at: "2026-10-22T09:46:18+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-22"
pub_day: "2026-10-21"
tags:
  - 语料
  - hn_show
  - author_coldstartops
  - story_50180280
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: KeibiDrop – Work on remote large files on-demand (no upload/download)

> [!info] 一句话导读
> We have built KeibiDrop because me and the people close to me were tired of cloud storages, and to copy data fully across our devices in order to use it.Now wit…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50180280>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：coldstartops　|　发布：2026-10-21T13:06:09Z
> 项目链接：<https://github.com/KeibiSoft/KeibiDrop>
> 采集：2026-10-22T09:46:18+08:00　|　id：`a250466b60b602a4`

## 正文

We have built KeibiDrop because me and the people close to me were tired of cloud storages, and to copy data fully across our devices in order to use it.Now with KeibiDrop you can mount and stream folders between your computers (and web browser) access and edit data on-demand as if it was local.You can try it instantly in the browser https://web.keibidrop.com/ (you need two devices) or by building from source/ downloading from the github releases. (there are also demo recordings in the Readme on github).We also got a marketing website for it here: https://keibidrop.comThe desktop app, engine and CLI are FOSS AGPL-v3 and in terms of architecture and stack the following holds:- It uses a full-duplex P2P IPv6 connection between peers with a fallback to a data forwarding relay.- We got a dual networking stack QUIC + TCP using protocol buffers (WebRTC to be added), and we use ML-KEM-1024 + X25519 for the handshake and either aes-gcm-256 or chacha20-poly1305 for the session, and we do a latency hiding re-key inspired by Signal's SPQR.- it relies on FUSE, macFUSE, and WinFsp as filesystem drivers and the whole gist of it is to "hide the latency" of remote filesystems and to just give the feeling of teleporting files.- we use golang for the engine, and rust + slint.dev for the GUIOur goal was to have a lightweight, cross platform filesystem that does not use many resources, has the RAM usage bounded and gives the feeling as if working on a local filesystem.Currently the filesystem respects POSIX semantics, (except for symlinks and hardlinks, I have them disabled), and we tested it on intercontinental links (between Romania and Singapore), on both relayed connections and direct connections.You can use git, pijul, Premiere Pro, DaVinci Resolve or any tools you would normally use on your local computer, or use our docker image on your NAS storage and instantly access the data you need while you are travelling.

## 关联链接

- https://keibidrop.comThe
- https://web.keibidrop.com/

## 导航

- 项目页：[[10-项目/github.com_96e9d5cc]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
