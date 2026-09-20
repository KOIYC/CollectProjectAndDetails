---
type: "project"
title: "Show HN: Snaketron – Competitive multiplayer Snake. Back after 14 years"
project_url: "https://snaketron.io/"
first_seen: "2026-09-21T02:57:17+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_lopatin
  - story_49499499
  - show_hn
lang: "en"
---

# Show HN: Snaketron – Competitive multiplayer Snake. Back after 14 years

> [!info] 一句话导读
> Hi HN, I just completed a rewrite of Snaketron, a competitive multiplayer Snake game. (Yes, yes, in Rust)A quick funny story about this game's history:Back in 2…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://snaketron.io/>
> 首次收录：2026-09-21T02:57:17+08:00
> 来源渠道：HN Show HN
> 标签：author_lopatin, story_49499499, show_hn
> 最新指标：点赞=5 · 评论=1 · engagement_velocity=5

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:33:52+08:00 | HN Show HN | 点赞=5 · 评论=1 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-09-21/ca86904929879a8d_Show-HN-Snaketron-–-Competitive-multiplayer-Snake]] |
| 2026-09-21T02:57:17+08:00 | HN Show HN | 点赞=5 · 评论=1 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-09-21/ca86904929879a8d_Show-HN-Snaketron-–-Competitive-multiplayer-Snake]] |

## 摘要正文

Hi HN, I just completed a rewrite of Snaketron, a competitive multiplayer Snake game. (Yes, yes, in Rust)A quick funny story about this game's history:Back in 2012 I had (poorly) implemented the first version of Snaketron. The issue with it was that I was keeping game state on the client, and while I did realize that it was insecure, I also had no idea what to do about it without increasing latency to unplayable levels. I was still in school, never worked on games, and haven't even heard of the term "netcode" before. The excitement of releasing my first pet project got the better of me, and I placed this security concern in the "theoretical issues" bucket, and shipped it.No one would even notice, and if they did, they wouldn't take the time to break into my little Snake game project, right?WRONG! Hacker News absolutely lived up to its name. While I was busy with my first experience of handling a traffic surge, scaling up my database and fixing bugs, several players found the security holes and were beginning their Snake rampage. Reports were coming in of unkillable snakes so I decided to start up a game to see if I could catch it.I loaded a 1v1 and my opponent was ... space invader…
