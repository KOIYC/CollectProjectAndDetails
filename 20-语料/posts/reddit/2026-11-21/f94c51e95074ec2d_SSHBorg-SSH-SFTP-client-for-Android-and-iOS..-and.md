---
type: "corpus"
item_id: "f94c51e95074ec2d"
title: "SSHBorg: SSH/SFTP client for Android and iOS.. and now speaks mosh. GPL-3.0, no account, no telemetry"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1xt240p/sshborg_sshsftp_client_for_android_and_ios_and/"
project_url: "https://github.com/payne1982/sshborg"
author: "sshborg"
published_at: "2026-11-11T07:28:14+08:00"
captured_at: "2026-11-21T14:46:47+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-21"
pub_day: "2026-11-11"
tags:
  - 语料
  - reddit
  - r/selfhosted
  - Wednesday Exceptions
metrics: {"score": 11, "comments": 17, "upvote_ratio": 0.7037037037037037}
comments_count: 17
comments_total: 17
discovered_via: "reddit:14d+settle10"
---

# SSHBorg: SSH/SFTP client for Android and iOS.. and now speaks mosh. GPL-3.0, no account, no telemetry

> [!info] 一句话导读
> Disclosure: I wrote this. It is GPL-3.0 and free everywhere it is published, and I am not selling anything.

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/selfhosted/comments/1xt240p/sshborg_sshsftp_client_for_android_and_ios_and/>
> 指标：得分=11 · 评论=17 · 赞踩比=0.7037037037037037
> 作者：sshborg　|　发布：2026-11-11T07:28:14+08:00
> 项目链接：<https://github.com/payne1982/sshborg>
> 采集：2026-11-21T14:46:47+08:00　|　id：`f94c51e95074ec2d`

## 正文

Disclosure: I wrote this. It is GPL-3.0 and free everywhere it is published, and I am not selling anything.

SSHBorg is an SSH and SFTP client for Android and iOS. It is not self-hosted software: it is the thing you hold in your hand while you fix the machine that is. No account, no cloud of mine, no telemetry, no ads: it talks to your servers and to nothing else. Keys stay on the device, encrypted by the Android Keystore or the iOS Keychain when you turn that on, and a backup is a plain JSON file that you keep.

The new release adds mosh, which is the part worth your time here. An SSH session is tied to the connection that opened it, so a phone that moves from Wi-Fi to mobile data, or sleeps in a pocket, loses the shell. With mosh the session survives all of it: you come back and the shell is where you left it, with whatever was running still running.

How it behaves in practice:

* Off by default, enabled per host: it is still experimental after all.
* The server needs mosh-server and a UTF-8 locale, nothing else — no daemon of mine, no agent. The usual mosh firewall requirement applies: a UDP port range you want.
* The SSH login stays open alongside the mosh session, so SFTP, port forwarding and agent forwarding keep working on the same host.
* Behind a bastion it works the other way round from what you would expect: mosh to the bastion, then one ssh line inwards, so the half of the terminal that lives on the network that keeps changing is the half that can take it.

Source and issues: https://github.com/payne1982/sshborg (GPL-3.0). It is on F-Droid, Google Play, the App Store and AppGallery; docs are at https://sshborg.com

Bug reports and ideas are genuinely welcome: most of what is in the app came from people opening issues.

## 评论（17/17）

> **asimovs-auditor**（1 分） · 2026-11-11T07:28:49+08:00　
> Expand the replies to this comment to learn how AI was used in this post/project.

---

> **sshborg**（-6 分） · 2026-11-11T07:35:47+08:00　
> Happy to clarify.
>
> Post: I wrote the content and the facts, but drafted the text with an LLM to tighten it up — English isn't my first language.
>
> Project: the code was written with Claude Code. I designed it, decided the architecture and the feature set, reviewed every change, and tested everything on real hardware against real servers. Nothing ships without me having run it.
>
> Worth being specific about the security-critical parts, since this is an SSH client: I did not write my own crypto and neither did the model. The SSH protocol, key exchange and ciphers come from JSch (mwiede fork), a maintained library. Key storage uses the Android Keystore. The app has no AI features, no LLM calls at runtime, no network access beyond the SSH connections you configure, and no telemetry.
>
> It's GPL-3.0 and the full source is public, so anyone who wants to judge the code quality for themselves can:
>
> [https://github.com/payne1982/sshborg](https://github.com/payne1982/sshborg)

---

> **No_Cryptographer_802**（1 分） · 2026-11-11T07:41:14+08:00　
> After releasing my own SSH client like 6 months ago, im starting to realize just how saturated the market is lmao, no hate to you at all in any way
> But damn, SaaS is going to be completely dead in a few years

---

> **QuestionAggravating9**（1 分） · 2026-11-11T07:48:01+08:00　
> How is this different from termius?

---

> **sshborg**（0 分） · 2026-11-11T07:48:04+08:00　
> Hello, mine is actually 8 months old! 😝 what is your SSH client name?

---

> **sshborg**（2 分） · 2026-11-11T07:51:52+08:00　
> Termius is not open source and it has paywalled features. Also it has different colors! 😆 Termius is a very good app in my opinion. I used for some time before I could build my own.

---

> **No_Cryptographer_802**（1 分） · 2026-11-11T07:54:52+08:00　
> ZestSSH, probably made mine for similar reasons as you, I found Termius, hated the subscription idea so made my own lol
>
> Originally made mine for a college project then just kept building

---

> **No_Cryptographer_802**（1 分） · 2026-11-11T07:56:29+08:00　
> I also just realized, I made mine 8 months ago too, back in March, damn didn't realise its been that long already

---

> **sshborg**（1 分） · 2026-11-11T08:04:04+08:00　
> Very nice site! 😊

---

> **No_Cryptographer_802**（-1 分） · 2026-11-11T08:36:42+08:00　
> Thank you :)
> Good luck on your adventures!

---

> **danielholm**（-1 分） · 2026-11-11T14:18:11+08:00　
> Thank you for creating and sharing. I've been looking for an open source replacement.

---

> **oneguysomewhere**（1 分） · 2026-11-12T05:27:28+08:00　
> I have a rather complex ssh config. Is there anyway to import one?

---

> **sshborg**（1 分） · 2026-11-12T07:24:38+08:00　
> Hello! The backup import/export system has an open format. You can find the specifics here https://sshborg.com/docs.html#backup
> If any connection parameter you need is missing, you can try posting in the issues tab on github

---

> **sshborg**（0 分） · 2026-11-12T07:26:43+08:00　
> Thank you! Let me know how it goes! ☺️

---

> **oneguysomewhere**（1 分） · 2026-11-12T07:49:35+08:00　
> I'll see if claude can convert my config to your json format. Thanks!

---

> **danielholm**（0 分） · 2026-11-13T05:02:30+08:00　
> It is now my default app and replaced Termius. Was an easy switch and I'm happy with it. Thanks again!

---

> **jebotecarobnjak**（1 分） · 2026-11-14T20:52:34+08:00　
> looks and works great, but i get disconnected if my screen goes off. is this normal or did i miss setting something up?

## 关联链接

- https://sshborg.com

## 导航

- 项目页：[[10-项目/github.com_5c3bd0e6]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
