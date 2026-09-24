---
type: "project"
title: "Show HN: Breathe CLI – Paced resonance breathing in the macOS terminal"
project_url: "https://github.com/marekkowalczyk/breathe-cli"
first_seen: "2026-09-22T13:13:19+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_marekkowalczyk
  - story_48340315
  - show_hn
lang: "en"
---

# Show HN: Breathe CLI – Paced resonance breathing in the macOS terminal

> [!info] 一句话导读
> I built a terminal app that paces slow breathing at 6 breaths per minute for vagal tone training. It's a single Python file, stdlib only, no dependencies — just…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/marekkowalczyk/breathe-cli>
> 首次收录：2026-09-22T13:13:19+08:00
> 来源渠道：HN Show HN
> 标签：author_marekkowalczyk, story_48340315, show_hn
> 最新指标：点赞=132 · 评论=55 · engagement_velocity=132

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:27:24+08:00 | HN Show HN | 点赞=132 · 评论=55 · engagement_velocity=132 | [[20-语料/posts/hn_show/2026-09-21/a19edfb034532d17_Show-HN-Breathe-CLI-–-Paced-resonance-breathing-in]] |
| 2026-09-21T01:43:16+08:00 | HN Show HN | 点赞=132 · 评论=55 · engagement_velocity=132 | [[20-语料/posts/hn_show/2026-09-21/a19edfb034532d17_Show-HN-Breathe-CLI-–-Paced-resonance-breathing-in]] |
| 2026-09-21T02:54:24+08:00 | HN Show HN | 点赞=132 · 评论=55 · engagement_velocity=132 | [[20-语料/posts/hn_show/2026-09-21/a19edfb034532d17_Show-HN-Breathe-CLI-–-Paced-resonance-breathing-in]] |
| 2026-09-21T03:11:56+08:00 | HN Show HN | 点赞=132 · 评论=55 · engagement_velocity=132 | [[20-语料/posts/hn_show/2026-09-21/a19edfb034532d17_Show-HN-Breathe-CLI-–-Paced-resonance-breathing-in]] |
| 2026-09-21T03:18:01+08:00 | HN Show HN | 点赞=132 · 评论=55 · engagement_velocity=132 | [[20-语料/posts/hn_show/2026-09-21/a19edfb034532d17_Show-HN-Breathe-CLI-–-Paced-resonance-breathing-in]] |
| 2026-09-21T09:55:22+08:00 | HN Show HN | 点赞=132 · 评论=55 · engagement_velocity=132 | [[20-语料/posts/hn_show/2026-09-21/a19edfb034532d17_Show-HN-Breathe-CLI-–-Paced-resonance-breathing-in]] |
| 2026-09-21T12:59:40+08:00 | HN Show HN | 点赞=132 · 评论=55 · engagement_velocity=132 | [[20-语料/posts/hn_show/2026-09-21/a19edfb034532d17_Show-HN-Breathe-CLI-–-Paced-resonance-breathing-in]] |
| 2026-09-21T13:02:45+08:00 | HN Show HN | 点赞=132 · 评论=55 · engagement_velocity=132 | [[20-语料/posts/hn_show/2026-09-21/a19edfb034532d17_Show-HN-Breathe-CLI-–-Paced-resonance-breathing-in]] |
| 2026-09-21T22:00:46+08:00 | HN Show HN | 点赞=132 · 评论=55 · engagement_velocity=132 | [[20-语料/posts/hn_show/2026-09-21/a19edfb034532d17_Show-HN-Breathe-CLI-–-Paced-resonance-breathing-in]] |
| 2026-09-22T13:13:19+08:00 | HN Show HN | 点赞=132 · 评论=55 · engagement_velocity=132 | [[20-语料/posts/hn_show/2026-09-21/a19edfb034532d17_Show-HN-Breathe-CLI-–-Paced-resonance-breathing-in]] |

## 摘要正文

I built a terminal app that paces slow breathing at 6 breaths per minute for vagal tone training. It's a single Python file, stdlib only, no dependencies — just run breathe and follow the bar.I'm a cardiology patient (HFrEF). Slow breathing at resonance frequency is one of the few non-pharmacological interventions shown to improve cardiac vagal tone and baroreflex sensitivity (Bernardi et al., Circulation 2002; Lancet 1998). I wanted a frictionless daily habit tool — no app store, no account, no subscription, just open terminal and go.Design constraints, all grounded in the clinical literature:- No breath retention — Valsalva risk in cardiac patients- No rapid breathing — minimum 8-second cycles- Exhale ≤ 2x inhale — no evidence for extreme ratios- Immediate exit, always — q or Ctrl+C restores the terminal even on crashThe README includes a resonance frequency measurement protocol for anyone with a chest-strap HRV monitor who wants to find their individual optimum instead of using the 6 bpm default.macOS only (uses afplay for audio cues). MIT licensed.pip install breathe-cliorbrew tap marekkowalczyk/breathe && brew install breathe.
