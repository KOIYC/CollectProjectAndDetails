---
type: "project"
title: "Show HN: Has Anthropic been nerfing their models without disclosure"
project_url: "https://github.com/ninjahawk/livenerf"
first_seen: "2026-09-28T09:47:28+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_ninjahawk1
  - story_49871819
  - show_hn
lang: "en"
---

# Show HN: Has Anthropic been nerfing their models without disclosure

> [!info] 一句话导读
> Benchmark for tracking model capability after release.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/ninjahawk/livenerf>
> 首次收录：2026-09-28T09:47:28+08:00
> 来源渠道：HN Show HN
> 标签：author_ninjahawk1, story_49871819, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-28T09:47:28+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-28/7b3b282196d1fb7d_Show-HN-Has-Anthropic-been-nerfing-their-models-wi]] |

## 摘要正文

# ninjahawk/livenerf  Benchmark for tracking model capability after release.  - Stars: 76 - Forks: 4 - Watchers: 76 - Open issues: 0 - Default branch: main - Created: 2026-09-22T21:59:26Z  ## Languages  - PowerShell - Python - Shell  ## Top Contributors  - ninjahawk (37 contributions)  ---  ## README  # livenerf  *A long-running, deterministic-as-possible benchmark for detecting whether a frontier model gets quietly worse after launch.*  Python Model Framework Harness Baseline Status  **📋 The plan** · **📊 Results** · **🔬 How it works** · **🧪 Pre-registration**  ---  livenerf is a small, boring, append-only benchmark for one question: does a model get worse after it ships? For months there have been reports that Anthropic "nerfs" models some days or weeks after release. That could mean quantization, a smaller model behind the same name, lower effort, or routing changes. It could also mean nothing happened and people are pattern-matching on noise. Nobody has had a clean day-0 baseline to check against, so every argument ends up as vibes versus vibes. Claude Opus 5.5 came out on 2026-09-22, so this is a chance to start the clock on launch day and keep it running. Right now v0 runs on …
