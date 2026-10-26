---
type: "corpus"
item_id: "a2596aa2925a33de"
title: "ScreenTinker v3.0 - open-source digital signage, now with a guided setup, content requests and screen share"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1x6viet/screentinker_v30_opensource_digital_signage_now/"
project_url: "https://github.com/screentinker/screentinker"
author: "dw5304"
published_at: "2026-10-16T03:43:55+08:00"
captured_at: "2026-10-26T09:43:54+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-26"
pub_day: "2026-10-16"
tags:
  - 语料
  - reddit
  - r/selfhosted
  - Release (AI)
metrics: {"score": 17, "comments": 10, "upvote_ratio": 0.7073170731707317}
comments_count: 10
comments_total: 10
discovered_via: "reddit:14d+settle10"
---

# ScreenTinker v3.0 - open-source digital signage, now with a guided setup, content requests and screen share

> [!info] 一句话导读
> Dev here. ScreenTinker is a self-hostable signage CMS (Node/Express/SQLite, MIT, Docker image on ghcr). v3.0 is out:

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/selfhosted/comments/1x6viet/screentinker_v30_opensource_digital_signage_now/>
> 指标：得分=17 · 评论=10 · 赞踩比=0.7073170731707317
> 作者：dw5304　|　发布：2026-10-16T03:43:55+08:00
> 项目链接：<https://github.com/screentinker/screentinker>
> 采集：2026-10-26T09:43:54+08:00　|　id：`a2596aa2925a33de`

## 正文

Dev here. ScreenTinker is a self-hostable signage CMS (Node/Express/SQLite, MIT, Docker image on ghcr). v3.0 is out:

  - Guided first run + Simple view for new users; import from Xibo, Yodeck, ScreenCloud and others.
  - Content requests - an approval-gated link so people without an account can send content for the screens.
  - Screen share (peer-to-peer WebRTC, TURN supported with short-lived credentials) to several screens at once.
  - Blank/frozen screen detection, stale-content and accessibility checks, captions via a local Whisper server.
  - Private A.I. - point it at your own Ollama/OpenAI-compatible box; a Data & privacy page lists exactly what leaves the server.
  - Passkeys, SCIM, full data export, and moving an org to another server by import.
  - Every install now ships its player packages: upgrade.sh fetches the signed APK etc. (checksum-verified), and the Docker image builds the native Pi player.

  Upgrade notes: Node 22.14+ is now enforced, and the first start snapshots the DB. From a 2.6 git install, run 3.0's upgrade script (the command is in the release notes) - we hit an apt needrestart race on our own prod upgrade, so the notes include the
  fix.

  Thanks to gainskills and arminfauland for PRs.

  **How A.I. is used:** most of the code is written with Claude Code, and I'm not going to pretend otherwise.
 I've been doing IT/telecom/security for 20+ years (network architecture, firmware RE, hardware hacking), so my job on this is the stuff AI is bad at: architecture, threat modelling, reviewing what it writes, and testing on real hardware (Fire TV, Android, Tizen,
  webOS, Pi, BrightSign, Roku). Nothing reaches production without my sign-off, and community bug reports from people running real screens drive a lot of the fixes. This post was drafted with Claude and edited by me.

  The A.I. features in the product (sign suggestions, translations, captions) are optional and off unless you configure a provider. Point them at your own hardware and nothing leaves your network.

  MIT licensed, all the code is public - judge it on that.

https://github.com/screentinker/screentinker

## 评论（10/10）

> **asimovs-auditor**（1 分） · 2026-10-16T03:44:05+08:00　
> Expand the replies to this comment to learn how AI was used in this post/project.

---

> **dw5304**（-5 分） · 2026-10-16T03:45:07+08:00　
> was allready in the post... that said.
> **How A.I. is used:** most of the code is written with Claude Code, and I'm not going to pretend otherwise. I've been doing IT/telecom/security for 20+ years (network architecture, firmware RE, hardware hacking), so my job on this is the stuff AI is bad at: architecture, threat modelling, reviewing what it writes, and testing on real hardware (Fire TV, Android, Tizen, webOS, Pi, BrightSign, Roku). Nothing reaches production without my sign-off, and community bug reports from people running real screens drive a lot of the fixes. This post was drafted with Claude and edited by me.

---

> **derical_cap_musical**（0 分） · 2026-10-16T04:22:14+08:00　
> respect for being upfront about using claude. definitely gonna spin this up on an old pi this weekend.

---

> **dw5304**（-2 分） · 2026-10-16T04:28:48+08:00　
> Why hide the A.I. side of the house? It's a tool, just like IDEs and IntelliSense. Heads up: a Pi 4 Model B is the oldest I've tested on my side. The native player needs Raspberry Pi OS 13 (Trixie); on anything older, the setup script's browser player is the safer bet. Would love feedback on whatever you try it on :)

---

> **fernandops**（1 分） · 2026-10-16T06:19:27+08:00　
> Can a content request include an end date that the approver has to confirm? A poster for Friday's event can be perfectly valid when approved and wrong by Saturday. Expiring it automatically would save the screen owner from having to remember every removal.

---

> **dw5304**（2 分） · 2026-10-16T06:21:26+08:00　
> Oh that's a good suggestion on auto expire I haven't tested that yet. But their is an end date allready. I'll reply once I get a chance to review it.

---

> **selfhosted-ModTeam**（1 分） · 2026-10-16T07:16:56+08:00　
> Thanks for posting to /r/selfhosted.
>
> Your post was removed as it violated our rule 2.
>
> > Do not spam or promote your own projects too much. We expect you to follow this [Reddit self-promotion guideline](https://www.reddit.com/r/reddit.com/wiki/selfpromotion). Promoted apps must be production ready and have docs. No direct ads for web hosting or VPS. Only mention your service in comments if it’s relevant and adds value.
>
> When promoting an app or service:
>
> - App must be self-hostable
> - App must be released and available for users to download / try
> - App must have some minimal form of documentation explaining how to install or use your app.
> - Services must be related to self-hosting
> - Posts must include a description of what your app or service does
> - Posts must include a brief list of features that your app or service includes
> - Posts must explain how your app or service is beneficial for users who may try it
>
> ---
>
> ### Moderator Comments
>
> None
>
> ---
>
> ^(Questions or Disagree? Contact [/r/selfhosted Mod Team](https://reddit.com/message/compose?to=r/selfhosted))

---

> **Joncallim**（1 分） · 2026-10-16T15:23:35+08:00　
> Curious how the frozen-screen check works with a static poster. How does it tell that apart from a player that’s stopped responding?

---

> **dw5304**（1 分） · 2026-10-16T21:42:14+08:00　
> Good question - a static poster can’t trip it by design. The check isn’t “screen hasn’t changed,” it’s “screen hasn’t changed when it should have.”
>
> Every screenshot is perceptually hashed and tagged with the item the player reports is on screen at that moment. A freeze only gets flagged when:
>
> 1. Captures tagged with different playlist items all show the same picture (player thinks it advanced, the panel didn’t), or
> 2. A multi-item loop sits on one image well past its longest item duration and the player reports starting nothing new, or
> 3. A single video shows one frame for 2x its runtime.
>
> A single still item is expected to look the same forever, so it’s never flagged. Same for triggers/overrides it can’t time.
>
> A player that stops responding entirely is a different path - that’s heartbeat/socket liveness, which marks the screen offline. The frozen check covers the nastier case: player is alive and reporting fine, but the display output is stuck.

---

> **Joncallim**（1 分） · 2026-10-16T22:13:38+08:00　
> Ohh that makes sense. Thanks for the detailed explanation!

## 导航

- 项目页：[[10-项目/github.com_7635bac7]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
