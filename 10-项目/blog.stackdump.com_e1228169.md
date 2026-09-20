---
type: "project"
title: "Show HN: A browser music sequencer: every note is a Petri-net transition firing"
project_url: "https://blog.stackdump.com/posts/petri-net-runtime"
first_seen: "2026-09-21T02:52:23+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_orksliver
  - story_47963271
  - show_hn
lang: "en"
---

# Show HN: A browser music sequencer: every note is a Petri-net transition firing

> [!info] 一句话导读
> A browser music sequencer where every note is a Petri-net transition firing

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://blog.stackdump.com/posts/petri-net-runtime>
> 首次收录：2026-09-21T02:52:23+08:00
> 来源渠道：HN Show HN
> 标签：author_orksliver, story_47963271, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:09:14+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-21/12f1b053d59676af_Show-HN-A-browser-music-sequencer-every-note-is-a]] |
| 2026-09-21T01:13:42+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-21/12f1b053d59676af_Show-HN-A-browser-music-sequencer-every-note-is-a]] |
| 2026-09-21T02:52:23+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-21/12f1b053d59676af_Show-HN-A-browser-music-sequencer-every-note-is-a]] |

## 摘要正文

← Home petri-nets  music  beats-bitwrap A browser music sequencer where every note is a Petri-net transition firing Live at beats.bitwrap.io . Source: github.com/stackdump/beats-bitwrap-io . That picture is the runtime, not a render of it. Each cluster on the ring is a sub-net (kick, snare, hihat, bass, melody, plus four hit slots) with its A/B/C variants beside it; the spokes meeting at the centre are the connector places that compose the song. The audio engine is reading exactly this state to fire transitions — at any moment you're hearing one variant per slot, chosen from the denser structure on screen. The thing I wanted to share isn't that we built a beat generator — there are plenty. It's the implementation choice underneath it: the sequencer is a Petri net executor . There is no separate timeline data structure, no event list, no "schedule note at tick N." A drum pattern is a ring of places with one token circulating; each transition fire is a note. Polyrhythm is two rings of different length sharing a tempo. Song structure is a control net that fires mute-track / unmute-track / activate-slot actions at section boundaries. Macros are short linear-chain control nets injected …
