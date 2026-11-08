---
type: "corpus"
item_id: "9643314401487c96"
title: "Show HN: FoilGateway–Linux firewall gateway with telemetry blocking (2×Ethernet)"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50406146"
project_url: "https://github.com/iBgeek/FoilGateway-Network"
author: "Codemonkey2k5"
published_at: "2026-11-07T17:10:25Z"
captured_at: "2026-11-08T12:50:31+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-11-08"
pub_day: "2026-11-07"
tags:
  - 语料
  - hn_show
  - author_Codemonkey2k5
  - story_50406146
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: FoilGateway–Linux firewall gateway with telemetry blocking (2×Ethernet)

> [!info] 一句话导读
> iBgeek/FoilGateway-Network

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50406146>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：Codemonkey2k5　|　发布：2026-11-07T17:10:25Z
> 项目链接：<https://github.com/iBgeek/FoilGateway-Network>
> 采集：2026-11-08T12:50:31+08:00　|　id：`9643314401487c96`

## 正文

# iBgeek/FoilGateway-Network

Firewall gateway for home and office networks - Simple to install, simple to use. Powerful enough for sensitive networks.

- Stars: 1
- Forks: 0
- Watchers: 1
- Open issues: 0
- License: Other
- Homepage: https://ibgeek.github.io/FoilGateway-Network/
- Default branch: main
- Created: 2026-11-06T01:43:08Z

## Languages

- CSS
- HTML
- JavaScript
- Python
- Rust
- Shell

## Topics

- firewall
- gateway
- homelab
- linux
- network-analysis
- network-monitoring
- network-security
- rust
- security
- security-tools
- telemetry-blocker

---

## README

# FoilGateway Network

Firewall gateway for home and office networks.

Dashboard with live connection map

FoilGateway connects between your router and your network. Your router, DHCP and DNS* keep working as they do now, with no changes to their settings. FoilGateway watches, logs and blocks the traffic that passes through it.

Everything downstream of the LAN port is protected. Anything upstream of the WAN port is not.

## Features

- **Protection Mode** - Normal, Audit, Local Network Only, Block Everything
- **Protection Level** - Normal, FortNox, Custom (Hardening settings under each)
- **Hardening** - Threat Lists, Block All Telemetry, Block Encrypted DNS (port 853), Strict Outbound, Block VPN Ports, Block IPv6, Whitelist Expiry, Stronger Device Identity, Deeper Detection, Remote Desktop controls
- **Geo-Blocking**, **Whitelist**, and **Blacklist**
- **Devices** - per-device policy, Troubleshooter, Connections Now
- **Capture Log** - searchable history of blocks, alerts, audit rows, and settings changes
- **Safety** - always-allowed hosts for settings pages and SSH; both require sign-in
- **Updates** - Settings → Updates checks GitHub Releases and installs only when you ask

## Requirements

- A Linux box with two network ports (WAN and LAN)
- Architecture: x86_64 or riscv64
- systemd

## Install

```sh
curl -fsSL https://github.com/iBgeek/FoilGateway-Network/releases/latest/download/install.sh | sudo sh
```

The installer:

- Detects the architecture and downloads the matching binary, web package, and checksums
- Verifies `SHA256SUMS`
- Installs the service (or upgrades in place if FoilGateway is already there)
- Leaves existing settings untouched on a re-run

Then open `https://:8443` and finish setup in the browser.

Release assets (also attached to each GitHub Release): `foilgw-riscv64`, `foilgw-x86_64`, `foilgw-web.tar.gz`, `install.sh`, `SHA256SUMS`, `FoilGateway-Manual.html`.

## Update

**Settings → Updates**

- **Check Now** - asks GitHub for the latest release. A daily check also runs in the background.
- **Install Update** - downloads the matching binary and web package, checks `SHA256SUMS`, installs, and restarts. Shown only when a newer release is available. Updates never install by themselves.
- **Roll Back To Previous Version** - restores the version kept from the last update.

If the settings page does not come back after Install Update, FoilGateway restores the previous version within the undo timer.

Running the install command again also upgrades in place and keeps your settings.

## Manual

FoilGateway-Manual.html (also on each release)

Help inside the product matches the manual. Use Download Manual on Help or About for a local copy.

## Screenshots

Dummy data for illustration.

| Page | |
| --- | --- |
| Firewall → Status | Firewall Status |
| Protection Mode | Protection Mode |
| Devices | Devices |
| Capture Log | Capture Log |
| Settings → Updates | Updates |
| Settings → About | About |
| Protection change preview | Protection preview |

## Support

Contact Support

* Block Encrypted DNS stops DNS over TLS on port 853. It is Off by default and in the Normal protection level, and On in FortNox. While it is On, devices set to require DNS over TLS cannot look up names. Change it under Firewall → Hardening.

## Software License

Copyright (C) 2026 iBGeek

Permission is granted to anyone to use, copy, modify, and share this software and its source, free of charge, for personal, educational, or other non-commercial purposes, subject to the conditions in LICENSE.

You may not sell this software, offer it as a paid product or paid hosted service, or use it as part of a commercial product or service, without a separate commercial license from iBGeek.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND. See LICENSE for the full text.

# Video-Rebirth/hyperflow-h3-flash

## 关联链接

- https://:8443`
- https://github.com/iBgeek/FoilGateway-Network/releases/latest/download/install.sh
- https://ibgeek.github.io/FoilGateway-Network/

## 导航

- 项目页：[[10-项目/github.com_1a73dfe6]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
