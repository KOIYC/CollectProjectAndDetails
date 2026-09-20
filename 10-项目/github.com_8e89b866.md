---
type: "project"
title: "Show HN: Microsoft Office running with Wine on Linux with no virtualization"
project_url: "https://github.com/Tombert/office365_flake"
first_seen: "2026-09-20T09:37:54+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_tombert
  - story_49746401
  - show_hn
lang: "en"
---

# Show HN: Microsoft Office running with Wine on Linux with no virtualization

> [!info] 一句话导读
> Tombert/office365_flake

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/Tombert/office365_flake>
> 首次收录：2026-09-20T09:37:54+08:00
> 来源渠道：HN Show HN
> 标签：author_tombert, story_49746401, show_hn
> 最新指标：点赞=90 · 评论=87 · engagement_velocity=90

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=90 · 评论=87 · engagement_velocity=90 | [[20-语料/posts/hn_show/2026-09-20/bd7c9407627ef94c_Show-HN-Microsoft-Office-running-with-Wine-on-Linu]] |
| 2026-09-20T09:36:45+08:00 | HN Show HN | 点赞=90 · 评论=87 · engagement_velocity=90 | [[20-语料/posts/hn_show/2026-09-20/bd7c9407627ef94c_Show-HN-Microsoft-Office-running-with-Wine-on-Linu]] |
| 2026-09-20T09:37:54+08:00 | HN Show HN | 点赞=90 · 评论=87 · engagement_velocity=90 | [[20-语料/posts/hn_show/2026-09-20/bd7c9407627ef94c_Show-HN-Microsoft-Office-running-with-Wine-on-Linu]] |

## 摘要正文

# Tombert/office365_flake  A set of Nix Flakes and scripts to get Office 365 working on Linux without virtualization.  - Stars: 39 - Forks: 0 - Watchers: 39 - Open issues: 0 - Default branch: main - Created: 2026-09-16T22:44:01Z  ## Languages  - C - Nix - Python - Shell  ## Top Contributors  - Tombert (51 contributions)  ---  ## README  # Microsoft 365 on Linux via umu + GE-Proton (Nix flake)  Microsoft 365 (click-to-run Office) famously does not work on stock Wine. This flake is a best-effort attempt to run it through **umu-launcher** with **GE-Proton** (the Wine build that Valve/GloriousEggroll ship for games) instead, with the Bottles project's **ProtoSoda** Wine core available as a second runner. It packages nothing from Microsoft: the Office Deployment Tool and Office itself are downloaded at install time by the `ms365` script. You need a Microsoft 365 licence to sign in.  ## Where the recipe comes from  * A February 2026 report in the Bottles tracker of Office 365 x64 running on Wine 10.20 with  `corefonts msxml6 riched20 gdiplus`, the Office Deployment Tool and a couple of DLL copies. * The classic ruados / eylenburg Office-on-Wine notes (Direct2D registry tweak, copying the…
