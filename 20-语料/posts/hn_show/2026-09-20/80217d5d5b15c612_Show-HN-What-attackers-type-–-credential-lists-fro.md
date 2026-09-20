---
type: "corpus"
item_id: "80217d5d5b15c612"
title: "Show HN: What attackers type – credential lists from our honeypots"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49713079"
project_url: "https://github.com/lurescope/top-attack-lists"
author: "lurescope"
published_at: "2026-09-15T14:27:15Z"
captured_at: "2026-09-20T09:37:14+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-20"
pub_day: "2026-09-15"
tags:
  - 语料
  - hn_show
  - author_lurescope
  - story_49713079
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: What attackers type – credential lists from our honeypots

> [!info] 一句话导读
> lurescope/top-attack-lists

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49713079>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：lurescope　|　发布：2026-09-15T14:27:15Z
> 项目链接：<https://github.com/lurescope/top-attack-lists>
> 采集：2026-09-20T09:37:14+08:00　|　id：`80217d5d5b15c612`

## 正文

# lurescope/top-attack-lists

Live brute-force telemetry from our own honeypot sensors — top usernames, passwords & empty-password probes with real attempt counts. Updated weekly.

- Stars: 2
- Forks: 0
- Watchers: 2
- Open issues: 0
- License: Other
- Default branch: main
- Created: 2026-08-09T11:02:49Z

## Topics

- brute-force
- cybersecurity
- honeypot
- ioc
- security-research
- ssh
- threat-intelligence
- wordlist

## Top Contributors

- lurescope (10 contributions)

---

## README

# Top Attack Lists — Live Data From Our Own Honeypots

**What attackers actually type when they knock on your door.** These lists are generated from LureScope's own passive sensor network — real brute-force telemetry, not recycled wordlists, not crowdsourced reports.

> **857,835 attack events · 15,697 unique IPs · 159 countries** — and counting. Observation window opened 2026-07-28.

> **Live free tools:** Have attackers tried it? · Daily blocklist · Network stats · Threat reports

## What's here

| File | Contents |
|---|---|
| `data/top-usernames.txt` | Top 47 most-probed usernames (with attempt counts) |
| `data/top-passwords.txt` | Top 50 most-probed passwords (with attempt counts) |
| `data/empty-password-probes.txt` | Usernames probed with an **empty** password — a targeted misconfiguration sweep |

## Why these lists are different

- **First-party data.** Every line comes from unsolicited inbound connections to our own sensors. We never scan anyone, and we don't resell third-party feeds.
- **Counts included.** Most public wordlists are unranked. These carry real attempt volumes, so you can weight your detections.
- **It moves.** `wallet` was nowhere in our top 10 on August 5. By August 8 it was #2 overall — 3,253 attempts, **every single one with an empty password**. Crypto-themed usernames (`wallet`, `binance`, `blockchain`, `crypto`, `bitcoin`) now account for 3,646 attempts and form the clearest targeting wave we've observed. See Report #3.
- **Beyond SSH.** In August 2026 we added industrial protocol decoys to the network. First ~60 hours: 172 probes from 151 IPs across 7 ICS protocols — FTP leading at 38%, 88% one-shot visitors, nearly all from rented cloud infrastructure. See Report #5 — Who's Scanning the Industrial Internet?.

## How to use

- **Detection:** flag SSH/auth attempts against these username+password pairs, especially any `wallet` login attempt with an empty password.
- **Hardening audits:** if any account on your systems matches a row in `top-usernames.txt` with a password from `top-passwords.txt`, that combination is being actively probed *right now*.
- **Honeypot research:** compare with your own telemetry — we'd love to hear how it overlaps.

## Methodology & ethics

- Passive decoy sensors only (SSH, Windows-service, and industrial protocol emulation). We never initiate connections or interact with attacking systems.
- Attacker IPs are **never** published here. These files contain only attempted credentials — which attackers already know, since they supplied them.
- Hex-encoded artifacts (e.g. `\x726f6f74` = `root` from MSSQL-layer probes) are filtered out of the lists.
- Geolocation of sources reflects hosting infrastructure, not attacker nationality.

## Updates

Weekly, alongside our threat reports. Machine-readable, scored, per-IP indicators with HASSH tooling clusters are available through the LureScope API — free early access, 100 queries/month.

## License

CC BY 4.0 — use it, remix it, ship it in your product. Attribution: link to `lurescope.com`.

---

*Data: LureScope global sensor network · Questions: support@lurescope.com*

## 导航

- 项目页：[[10-项目/github.com_a6749037]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
