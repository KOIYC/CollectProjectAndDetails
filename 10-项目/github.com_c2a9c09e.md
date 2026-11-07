---
type: "project"
title: "Show HN: CloneGuard – Scan a repo for credential-stealing tricks before it runs"
project_url: "https://github.com/tharun208/cloneguard"
first_seen: "2026-11-07T09:43:25+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_tharun208
  - story_50397435
  - show_hn
lang: "en"
---

# Show HN: CloneGuard – Scan a repo for credential-stealing tricks before it runs

> [!info] 一句话导读
> tharun208/cloneguard

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/tharun208/cloneguard>
> 首次收录：2026-11-07T09:43:25+08:00
> 来源渠道：HN Show HN
> 标签：author_tharun208, story_50397435, show_hn
> 最新指标：点赞=28 · 评论=7 · engagement_velocity=28

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-07T09:43:25+08:00 | HN Show HN | 点赞=28 · 评论=7 · engagement_velocity=28 | [[20-语料/posts/hn_show/2026-11-07/dcb7edf0c93fe6cb_Show-HN-CloneGuard-–-Scan-a-repo-for-credential-st]] |

## 摘要正文

# tharun208/cloneguard  Scan a repo for malware tricks before you run it. Catches credential theft, hidden network calls, obfuscated code and auto-run hooks. Read-only, with no dependencies.  - Stars: 0 - Forks: 0 - Watchers: 0 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2026-11-03T22:19:55Z  ## Languages  - Go  ## Top Contributors  - tharun208 (3 contributions)  ---  ## README  # CloneGuard  Scan a project for malware tricks **before** you run it. Built after a fake-recruiter "demo app" tried to steal SSH and AWS keys.  cloneguard is a small, dependency-free Go command-line tool. It only reads files. It never runs, installs, or imports anything from the project it scans.  ## Why this exists  A common attack goes like this: someone posing as a recruiter sends you a "take-home assignment" or "demo app". You clone it, run `npm install` or open it in your editor, and it quietly uploads your SSH keys, cloud credentials, browser passwords or crypto wallets. Often the trigger isn't the app itself but an install hook or an editor task that runs the moment you open the folder.  cloneguard is a quick first look that catches the usual tricks, so you can decide w…
