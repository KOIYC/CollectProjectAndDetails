---
type: "project"
title: "Show HN: KeibiDrop – Work on remote large files on-demand (no upload/download)"
project_url: "https://github.com/KeibiSoft/KeibiDrop"
first_seen: "2026-10-22T09:46:18+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_coldstartops
  - story_50180280
  - show_hn
lang: "en"
---

# Show HN: KeibiDrop – Work on remote large files on-demand (no upload/download)

> [!info] 一句话导读
> We have built KeibiDrop because me and the people close to me were tired of cloud storages, and to copy data fully across our devices in order to use it.Now wit…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/KeibiSoft/KeibiDrop>
> 首次收录：2026-10-22T09:46:18+08:00
> 来源渠道：HN Show HN
> 标签：author_coldstartops, story_50180280, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-22T09:46:18+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-10-22/a250466b60b602a4_Show-HN-KeibiDrop-–-Work-on-remote-large-files-on]] |

## 摘要正文

We have built KeibiDrop because me and the people close to me were tired of cloud storages, and to copy data fully across our devices in order to use it.Now with KeibiDrop you can mount and stream folders between your computers (and web browser) access and edit data on-demand as if it was local.You can try it instantly in the browser https://web.keibidrop.com/ (you need two devices) or by building from source/ downloading from the github releases. (there are also demo recordings in the Readme on github).We also got a marketing website for it here: https://keibidrop.comThe desktop app, engine and CLI are FOSS AGPL-v3 and in terms of architecture and stack the following holds:- It uses a full-duplex P2P IPv6 connection between peers with a fallback to a data forwarding relay.- We got a dual networking stack QUIC + TCP using protocol buffers (WebRTC to be added), and we use ML-KEM-1024 + X25519 for the handshake and either aes-gcm-256 or chacha20-poly1305 for the session, and we do a latency hiding re-key inspired by Signal's SPQR.- it relies on FUSE, macFUSE, and WinFsp as filesystem drivers and the whole gist of it is to "hide the latency" of remote filesystems and to just give the …
