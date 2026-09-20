---
type: "project"
title: "Show HN: PortButler – send files from macOS to a device with no way to receive"
project_url: "https://portbutler.sshlab.dev/"
first_seen: "2026-09-20T09:36:44+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_swq115
  - story_49749079
  - show_hn
lang: "en"
---

# Show HN: PortButler – send files from macOS to a device with no way to receive

> [!info] 一句话导读
> PortButler — Native SSH, SFTP and serial for macOS

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://portbutler.sshlab.dev/>
> 首次收录：2026-09-20T09:36:44+08:00
> 来源渠道：HN Show HN
> 标签：author_swq115, story_49749079, show_hn
> 最新指标：点赞=4 · 评论=0 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-20/b3fe5bb70550ca35_Show-HN-PortButler-–-send-files-from-macOS-to-a-de]] |
| 2026-09-20T09:36:44+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-20/b3fe5bb70550ca35_Show-HN-PortButler-–-send-files-from-macOS-to-a-de]] |

## 摘要正文

PortButler — Native SSH, SFTP and serial for macOS  # Three of them. One window.  A terminal, a file manager and a serial monitor — three apps for one machine. Here a host is a tab, its files are the pane beside it, and the board on your desk sits in the same list as the servers.  No account, no card, nothing to enter · macOS 13+ · Apple silicon and Intel · Notarized by Apple  One window. Hosts on the left, their files in the middle, a shell on the right — and the serial adapter sits in the same list as the servers.  ## It tells you why it failed.  `connection failed` is not an error message. These five look identical on most clients and each needs a completely different fix.  | What happened | What PortButler tells you | | --- | --- | | The port refused it | The machine is up. Check the port — many devices use 2222 | | Nothing answered | Powered off, or a firewall dropping packets silently | | The name will not resolve | Check spelling, or whether it only exists on a VPN | | Connected, no SSH greeting | That port is not SSH, or `sshd` is stuck | | Something answered, not SSH | A web server may be sitting on that port |  ## The board on your desk is in the same list.  A USB-serial …
