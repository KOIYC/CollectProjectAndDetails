---
type: "project"
title: "ScreenTinker v3.0 - open-source digital signage, now with a guided setup, content requests and screen share"
project_url: "https://github.com/screentinker/screentinker"
first_seen: "2026-10-26T09:43:54+08:00"
sources:
  - reddit
tags:
  - 项目
  - reddit
  - r/selfhosted
  - Release (AI)
lang: "en"
---

# ScreenTinker v3.0 - open-source digital signage, now with a guided setup, content requests and screen share

> [!info] 一句话导读
> Dev here. ScreenTinker is a self-hostable signage CMS (Node/Express/SQLite, MIT, Docker image on ghcr). v3.0 is out:

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/screentinker/screentinker>
> 首次收录：2026-10-26T09:43:54+08:00
> 来源渠道：Reddit 独立开发版块
> 标签：r/selfhosted, Release (AI)
> 最新指标：得分=17 · 评论=10 · 赞踩比=0.7073170731707317

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-26T09:43:54+08:00 | Reddit 独立开发版块 | 得分=17 · 评论=10 · 赞踩比=0.7073170731707317 | [[20-语料/posts/reddit/2026-10-26/a2596aa2925a33de_ScreenTinker-v3.0-open-source-digital-signage,-now]] |

## 摘要正文

Dev here. ScreenTinker is a self-hostable signage CMS (Node/Express/SQLite, MIT, Docker image on ghcr). v3.0 is out:    - Guided first run + Simple view for new users; import from Xibo, Yodeck, ScreenCloud and others.   - Content requests - an approval-gated link so people without an account can send content for the screens.   - Screen share (peer-to-peer WebRTC, TURN supported with short-lived credentials) to several screens at once.   - Blank/frozen screen detection, stale-content and accessibility checks, captions via a local Whisper server.   - Private A.I. - point it at your own Ollama/OpenAI-compatible box; a Data & privacy page lists exactly what leaves the server.   - Passkeys, SCIM, full data export, and moving an org to another server by import.   - Every install now ships its player packages: upgrade.sh fetches the signed APK etc. (checksum-verified), and the Docker image builds the native Pi player.    Upgrade notes: Node 22.14+ is now enforced, and the first start snapshots the DB. From a 2.6 git install, run 3.0's upgrade script (the command is in the release notes) - we hit an apt needrestart race on our own prod upgrade, so the notes include the   fix.    Thanks to …
