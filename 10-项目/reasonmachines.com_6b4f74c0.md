---
type: "project"
title: "Show HN: R/place for Git – Open-source Git server sustaining 567 pushes/s"
project_url: "https://reasonmachines.com/blog/aspen"
first_seen: "2026-11-07T09:43:25+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_svemyh
  - story_50393394
  - show_hn
lang: "en"
---

# Show HN: R/place for Git – Open-source Git server sustaining 567 pushes/s

> [!info] 一句话导读
> hey hn, sven from Reason Machines (YC F26).we've been experimenting with how fast we can push our ci/cd and code storage systems when swarms of coding agents ar…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://reasonmachines.com/blog/aspen>
> 首次收录：2026-11-07T09:43:25+08:00
> 来源渠道：HN Show HN
> 标签：author_svemyh, story_50393394, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-07T09:43:25+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-11-07/b016ca10164c0065_Show-HN-R-place-for-Git-–-Open-source-Git-server-s]] |

## 摘要正文

hey hn, sven from Reason Machines (YC F26).we've been experimenting with how fast we can push our ci/cd and code storage systems when swarms of coding agents are all pushing at once. turns out giving 100 agents git push basically ddos'es normal git servers.so we wrote aspen: an open-source git server (apache 2.0) that hits 567 pushes/sec on a single 8-core box with stock git clients.to stress test it live, we put up a shared canvas where every pixel is a real git push: https://place.reasonmachines.comcode & how it works: - blog: https://reasonmachines.com/blog/aspen - github: https://github.com/reason-machines/aspen
