---
type: "project"
title: "Show HN: An online shop where your friends can hurry the courier"
project_url: "https://dopaminechic.com/"
first_seen: "2026-11-08T12:50:31+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_AmsterErdo
  - story_50403954
  - show_hn
lang: "en"
---

# Show HN: An online shop where your friends can hurry the courier

> [!info] 一句话导读
> I built an emulator of a flash-sale fashion outlet with no registration and fake checkout that never takes money. You can browse items that are on sale, watch i…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://dopaminechic.com/>
> 首次收录：2026-11-08T12:50:31+08:00
> 来源渠道：HN Show HN
> 标签：author_AmsterErdo, story_50403954, show_hn
> 最新指标：点赞=6 · 评论=2 · engagement_velocity=6

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-08T12:50:31+08:00 | HN Show HN | 点赞=6 · 评论=2 · engagement_velocity=6 | [[20-语料/posts/hn_show/2026-11-08/6d0155fb86e84206_Show-HN-An-online-shop-where-your-friends-can-hurr]] |

## 摘要正文

I built an emulator of a flash-sale fashion outlet with no registration and fake checkout that never takes money. You can browse items that are on sale, watch in real time as they go out of stock one by one, and get notified when they are back on sale (possibly with different prices).Every order placed on the website gets “tracking” which fails on the delivery day with one of 50 available reasons (for example, “a raccoon in the Newark depot has claimed your parcel; animal control reports that it seems happy there”). But you can also share the tracking with your friends, and they can hurry the courier; the more hurries, the more spectacularly it fails, until your parcel lands in the Svalbard seed vault, the North Pole, the International Space Station or some such place.The complete shop contents (campaigns, prices, item availability and stock levels) are computed from the current time with a fixed seed (FNV-1a for hashing, mulberry32 as the PRNG). I wrote the mechanism first in JS and then ported to PHP (for the website) and Flutter (for the mobile app); a test ran over several thousand random time points to verify they are identical. The Flutter app uses its own generator because i…
