---
type: "project"
title: "My experience of implementing GGPO-style rollback netcode for my 3D melee arena fighter"
project_url: "https://v.redd.it/y1894v72lfah1"
first_seen: "2026-09-21T01:30:35+08:00"
sources:
  - reddit
tags:
  - 项目
  - reddit
  - r/indiedev
  - Discussion
lang: "en"
---

# My experience of implementing GGPO-style rollback netcode for my 3D melee arena fighter

> [!info] 一句话导读
> Over the past few months, I’ve been working on the netcode for my 3D melee arena fighter Rasen and I’d like to share my experience.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://v.redd.it/y1894v72lfah1>
> 首次收录：2026-09-21T01:30:35+08:00
> 来源渠道：Reddit 独立开发版块
> 标签：r/indiedev, Discussion
> 最新指标：得分=3 · 评论=0 · 赞踩比=0.71

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:30:35+08:00 | Reddit 独立开发版块 | 得分=3 · 评论=0 · 赞踩比=0.71 | [[20-语料/posts/reddit/2026-09-21/2df32d848d6e68d5_My-experience-of-implementing-GGPO-style-rollback]] |

## 摘要正文

**Hi everyone,**  Over the past few months, I’ve been working on the netcode for my 3D melee arena fighter Rasen and I’d like to share my experience.  **Unreal Engine systems**  Although I knew about GGPO netcode from the beginning, I was so intimidated by the amount of work involved. Instead, I started with delay-based networking, then experimented with Unreal's Character Movement Component, tried the Unreal Mover, and even built some custom networking solutions on top of the CMC.  Unfortunately, none of these were a good enough fit for this kind of fast-paced, parry-based, knockback-heavy combat.  Even with low ping, either the latency felt very high or there were visible corrections and out-of-sync animations. Also, my custom animation syncing was conflicting with the CMC's built-in root motion syncing and knockbacks were especially really bad.  **GGPO rollback netcode**  While experimenting with all these systems, I learnt more and more about GGPO solutions. With no other option, I finally decided to implement my own GGPO rollback architecture in Unreal Engine, along with the custom deterministic physics and movement required for it to all work.  Fortunately, the game had alrea…
