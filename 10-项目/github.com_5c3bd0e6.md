---
type: "project"
title: "SSHBorg: SSH/SFTP client for Android and iOS.. and now speaks mosh. GPL-3.0, no account, no telemetry"
project_url: "https://github.com/payne1982/sshborg"
first_seen: "2026-11-21T14:46:47+08:00"
sources:
  - reddit
tags:
  - 项目
  - reddit
  - r/selfhosted
  - Wednesday Exceptions
lang: "en"
---

# SSHBorg: SSH/SFTP client for Android and iOS.. and now speaks mosh. GPL-3.0, no account, no telemetry

> [!info] 一句话导读
> Disclosure: I wrote this. It is GPL-3.0 and free everywhere it is published, and I am not selling anything.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/payne1982/sshborg>
> 首次收录：2026-11-21T14:46:47+08:00
> 来源渠道：Reddit 独立开发版块
> 标签：r/selfhosted, Wednesday Exceptions
> 最新指标：得分=11 · 评论=17 · 赞踩比=0.7037037037037037

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-21T14:46:47+08:00 | Reddit 独立开发版块 | 得分=11 · 评论=17 · 赞踩比=0.7037037037037037 | [[20-语料/posts/reddit/2026-11-21/f94c51e95074ec2d_SSHBorg-SSH-SFTP-client-for-Android-and-iOS..-and]] |

## 摘要正文

Disclosure: I wrote this. It is GPL-3.0 and free everywhere it is published, and I am not selling anything.  SSHBorg is an SSH and SFTP client for Android and iOS. It is not self-hosted software: it is the thing you hold in your hand while you fix the machine that is. No account, no cloud of mine, no telemetry, no ads: it talks to your servers and to nothing else. Keys stay on the device, encrypted by the Android Keystore or the iOS Keychain when you turn that on, and a backup is a plain JSON file that you keep.  The new release adds mosh, which is the part worth your time here. An SSH session is tied to the connection that opened it, so a phone that moves from Wi-Fi to mobile data, or sleeps in a pocket, loses the shell. With mosh the session survives all of it: you come back and the shell is where you left it, with whatever was running still running.  How it behaves in practice:  * Off by default, enabled per host: it is still experimental after all. * The server needs mosh-server and a UTF-8 locale, nothing else — no daemon of mine, no agent. The usual mosh firewall requirement applies: a UDP port range you want. * The SSH login stays open alongside the mosh session, so SFTP, po…
