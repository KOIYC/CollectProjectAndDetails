---
type: "project"
title: "Show HN: Stable Audio 3 – one-shot sample generator (110gb download)"
project_url: "https://github.com/shiehn/sas-sample-generator"
first_seen: "2026-09-21T21:59:54+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_stevehiehn
  - story_48345377
  - show_hn
lang: "en"
---

# Show HN: Stable Audio 3 – one-shot sample generator (110gb download)

> [!info] 一句话导读
> shiehn/sas-sample-generator

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/shiehn/sas-sample-generator>
> 首次收录：2026-09-21T21:59:54+08:00
> 来源渠道：HN Show HN
> 标签：author_stevehiehn, story_48345377, show_hn
> 最新指标：点赞=10 · 评论=5 · engagement_velocity=10

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:27:24+08:00 | HN Show HN | 点赞=10 · 评论=5 · engagement_velocity=10 | [[20-语料/posts/hn_show/2026-09-21/fdd309c576f9b7a9_Show-HN-Stable-Audio-3-–-one-shot-sample-generator]] |
| 2026-09-21T01:42:43+08:00 | HN Show HN | 点赞=10 · 评论=5 · engagement_velocity=10 | [[20-语料/posts/hn_show/2026-09-21/fdd309c576f9b7a9_Show-HN-Stable-Audio-3-–-one-shot-sample-generator]] |
| 2026-09-21T02:52:45+08:00 | HN Show HN | 点赞=10 · 评论=5 · engagement_velocity=10 | [[20-语料/posts/hn_show/2026-09-21/fdd309c576f9b7a9_Show-HN-Stable-Audio-3-–-one-shot-sample-generator]] |
| 2026-09-21T03:11:00+08:00 | HN Show HN | 点赞=10 · 评论=5 · engagement_velocity=10 | [[20-语料/posts/hn_show/2026-09-21/fdd309c576f9b7a9_Show-HN-Stable-Audio-3-–-one-shot-sample-generator]] |
| 2026-09-21T03:16:05+08:00 | HN Show HN | 点赞=10 · 评论=5 · engagement_velocity=10 | [[20-语料/posts/hn_show/2026-09-21/fdd309c576f9b7a9_Show-HN-Stable-Audio-3-–-one-shot-sample-generator]] |
| 2026-09-21T03:17:41+08:00 | HN Show HN | 点赞=10 · 评论=5 · engagement_velocity=10 | [[20-语料/posts/hn_show/2026-09-21/fdd309c576f9b7a9_Show-HN-Stable-Audio-3-–-one-shot-sample-generator]] |
| 2026-09-21T09:54:58+08:00 | HN Show HN | 点赞=10 · 评论=5 · engagement_velocity=10 | [[20-语料/posts/hn_show/2026-09-21/fdd309c576f9b7a9_Show-HN-Stable-Audio-3-–-one-shot-sample-generator]] |
| 2026-09-21T21:59:54+08:00 | HN Show HN | 点赞=10 · 评论=5 · engagement_velocity=10 | [[20-语料/posts/hn_show/2026-09-21/fdd309c576f9b7a9_Show-HN-Stable-Audio-3-–-one-shot-sample-generator]] |

## 摘要正文

# shiehn/sas-sample-generator  One shot sample generation for the SignalsAndSorcery.com platform  - Stars: 13 - Forks: 0 - Watchers: 13 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2026-05-17T20:07:40Z  ## Languages  - Dockerfile - Python - Shell  ## Top Contributors  - shiehn (51 contributions)  ---  ## README  # sas-sample-generator  ## ⬇️ Download the pre-built sample packs  The latest **v3** libraries are hosted publicly on GCP (no auth required). The Signals & Sorcery app installs these automatically, but you can grab them directly here:  | Pack | Contents | Download | |------|----------|----------| | **Drums** (v3 large) | 24 roles · 10,359 one-shots (+ prompt sidecars) · ~1.4 GB | sas-drum-pack-v3-large.zip | | **Instruments** (v3 large) | 28 categories · 5,475 multi-zone instruments · ~26.6 GB | sas-instrument-pack-v3-large.zip |  > Each zip contains a `_pack-version.json` marker plus the payload tree > (drums: ` /*.wav`; instruments: ` / /manifest.json` + `zones/`). > The instrument pack is zones-only (the 24-bit generation `sources/` are omitted — > they aren't used at playback).  ---  Generate large batches of audio samples with Stable Audio …
