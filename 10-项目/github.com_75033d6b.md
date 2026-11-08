---
type: "project"
title: "Show HN: Coldframe, a honeypot that poses as a supermarket fridge controller"
project_url: "https://github.com/hedgerow-dev/coldframe"
first_seen: "2026-11-08T12:50:31+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_hedgerow-dev
  - story_50406292
  - show_hn
  - front_page
lang: "en"
---

# Show HN: Coldframe, a honeypot that poses as a supermarket fridge controller

> [!info] 一句话导读
> I built Coldframe, a honeypot that pretends to be a supermarket refrigeration controller. Inspired by the events on industrial fridge installations in the past …

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/hedgerow-dev/coldframe>
> 首次收录：2026-11-08T12:50:31+08:00
> 来源渠道：HN Show HN
> 标签：author_hedgerow-dev, story_50406292, show_hn, front_page
> 最新指标：点赞=207 · 评论=44 · engagement_velocity=207

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-08T12:50:31+08:00 | HN Show HN | 点赞=207 · 评论=44 · engagement_velocity=207 | [[20-语料/posts/hn_show/2026-11-08/92e06ff497ebb12d_Show-HN-Coldframe,-a-honeypot-that-poses-as-a-supe]] |

## 摘要正文

I built Coldframe, a honeypot that pretends to be a supermarket refrigeration controller. Inspired by the events on industrial fridge installations in the past weeks, I wanted to see what people would try against a convincing fake.To learn more about this I built a honeypot that resembled perfectly the Danfoss AK-SM 800A and Dixell XWEB interfaces. Both of them are recognized on Shodan as real ones (an not as honeypots). It’s one Python file using only the standard library, and it builds on eppser/danfoss-ak-sm-decoy and public research by Synacktiv, Claroty and Ironhackers.Things that were fun to get right:- Matching real units. I used Shodan records of real devices to match header order, page titles, certificate fields and TLS versions. The Danfoss persona sends nginx headers in the same order as a real AK-SM 800A. The Dixell persona sends no Server header and pads its page to exactly 8,202 bytes.- Recognising exploit attempts. It recognises CVE-2025-41450, the Danfoss “code of the day” login bypass, and records whether the submitted code is correct for today. It also tags attempts targeting three other Danfoss CVEs and the XWEB vulnerabilities.- Letting them in. Default logins o…
