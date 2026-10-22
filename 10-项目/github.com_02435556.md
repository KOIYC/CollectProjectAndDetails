---
type: "project"
title: "Show HN: TUI to manage firewall and HTTP server, in Rust"
project_url: "https://github.com/ivankovic/stop-bots"
first_seen: "2026-10-22T09:46:18+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_FabCH
  - story_50180355
  - show_hn
lang: "en"
---

# Show HN: TUI to manage firewall and HTTP server, in Rust

> [!info] 一句话导读
> I have been self-hosting for 10 years, and "family hosting" for 2.The number of attacks my servers get has increased by 3x since May of this year. Now personall…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/ivankovic/stop-bots>
> 首次收录：2026-10-22T09:46:18+08:00
> 来源渠道：HN Show HN
> 标签：author_FabCH, story_50180355, show_hn
> 最新指标：点赞=2 · 评论=4 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-22T09:46:18+08:00 | HN Show HN | 点赞=2 · 评论=4 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-10-22/ec41854318990e0c_Show-HN-TUI-to-manage-firewall-and-HTTP-server,-in]] |

## 摘要正文

I have been self-hosting for 10 years, and "family hosting" for 2.The number of attacks my servers get has increased by 3x since May of this year. Now personally, I don't like hiding behind Cloudflare because I don't want them to be a SPOF, but it was becoming a bit too scary to just be open to the web. Because it is a family cloud, it can't hide behind a VPN, it has to support devices like TV sticks that can't connect properly over VPN. It has to support HTTPS.So I put together a Rust/Ratatui TUI+cron/CLI that manages my second line of defense: firewall and HTTP server. I run a reverse Nginx proxy in front of apps like Nextcloud, and a nftables firewall with SSH as my admin tunnel. It does several things:1) It allows me to block entire segments, countries, datacenter IP ranges, TOR exit nodes etc...2) It allows me to block specific bots: search bots, AI bots, security scanners3) It does dynamic blocking too, looking at the logs to spot bad behavior and block it. I used to run fail2ban for SSH for example, but a centralized UI for both SSH and HTTP(S) is nicer IMHO.So if this is useful to anyone else, feel free. It's AGPL v3.In my experience, geoblocking is the biggest win, reducin…
