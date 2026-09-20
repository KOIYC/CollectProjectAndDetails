---
type: "project"
title: "Show HN: Train 300M/32-Layer Model in 1.5GB RAM on Base M1 Mac"
project_url: "https://news.ycombinator.com/item?id=49497451"
first_seen: "2026-09-21T03:11:32+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_vlad_kalinkin
  - story_49497451
  - show_hn
lang: "en"
---

# Show HN: Train 300M/32-Layer Model in 1.5GB RAM on Base M1 Mac

> [!info] 一句话导读
> Show HN: Train 300M/32-Layer Model in 1.5GB RAM on Base M1 Mac

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://news.ycombinator.com/item?id=49497451>
> 首次收录：2026-09-21T03:11:32+08:00
> 来源渠道：HN Show HN
> 标签：author_vlad_kalinkin, story_49497451, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:33:52+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-21/68a4dc7c7367c734_Show-HN-Train-300M-32-Layer-Model-in-1.5GB-RAM-on]] |
| 2026-09-21T03:11:32+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-21/68a4dc7c7367c734_Show-HN-Train-300M-32-Layer-Model-in-1.5GB-RAM-on]] |

## 摘要正文

Show HN: Train 300M/32-Layer Model in 1.5GB RAM on Base M1 Mac | Hacker News  | https://news.ycombinator.com/vote?id=49497451&how=up&goto=item%3Fid%3D49497451 | Show HN: Train 300M/32-Layer Model in 1.5GB RAM on Base M1 Mac | | --- | --- | | | 2 points by vlad_kalinkin 2 days ago| hide| past| favorite| discuss | | | Hello again! Since my last post about Ullis, the project has gone through several changes as I was searching for the right architecture. As it turned out, KAN and Hyena were quite resource-heavy, and I couldn't get anything viable out of them. Then I tried RWKV, specifically the latest RWKV-8 Heron version with 1-bit ROSA activation. This ultimately proved to be the most viable architecture of all. As an example: on my 2020 MacBook Pro M1 with 8GB RAM and a 68GB/s memory bandwidth, I managed to start training a model with ~272 million parameters, a 2048 context length, and 32 layers—all within a 1.5GB memory footprint. On my specific hardware, this is still a highly taxing task. Due to the low bandwidth, the total latency per step is around half a minute, and the throughput drops to about 70 tokens per second. To be clear right away: I had to keep ROSA SAM on the CPU be…
