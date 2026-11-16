---
type: "project"
title: "Show HN: Totpvault - a universal desktop app for your TOTPs"
project_url: "https://github.com/spapas/totpvault"
first_seen: "2026-11-11T13:37:17+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_spapas82
  - story_50444590
  - show_hn
lang: "en"
---

# Show HN: Totpvault - a universal desktop app for your TOTPs

> [!info] 一句话导读
> License: MIT License

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/spapas/totpvault>
> 首次收录：2026-11-11T13:37:17+08:00
> 来源渠道：HN Show HN
> 标签：author_spapas82, story_50444590, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-11T13:37:17+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-11-11/e3a172c4fc186fda_Show-HN-Totpvault-a-universal-desktop-app-for-your]] |

## 摘要正文

# spapas/totpvault  - Stars: 0 - Forks: 0 - Watchers: 0 - Open issues: 0 - License: MIT License - Default branch: master - Created: 2026-10-08T06:06:03Z  ## Languages  - Go - Python - Rust  ## Top Contributors  - spapas (35 contributions) - Copilot (3 contributions)  ---  ## README  # TOTP Vault  A small offline authenticator for Windows, Linux and macOS, written in Rust with `egui`.  ## Screenshots  Main window with account cards, live codes and countdown rings Unlock screen with master password prompt  ## Features  - Create and unlock an encrypted vault with a master password. - Add, edit, delete and search TOTP accounts (list sorted alphabetically; search shows `showing X of Y`). - Duplicate protection: same name+issuer or same secret with identical settings is rejected. - Import `otpauth://totp/...` provisioning URIs. - Export a selected account as a provisioning URI for import in another app. - Paste a QR screenshot from the clipboard (`Paste QR`): the image is decoded  offline and the enclosed provisioning URI is imported (PNG/JPEG, ≤5 MiB). - SHA-1, SHA-256 and SHA-512; 6 or 8 digits; configurable period (default 30 seconds). - Live codes and countdown rings (red under 6 sec…
