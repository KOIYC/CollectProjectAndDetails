---
type: "project"
title: "Show HN: Chuks v0.2.0-RC.1, we're asking people to try to break it"
project_url: "https://chuks.org/blog/chuks-v020-rc1-the-release-candidate"
first_seen: "2026-09-20T09:48:16+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_princeLex
  - story_49764179
  - show_hn
lang: "en"
---

# Show HN: Chuks v0.2.0-RC.1, we're asking people to try to break it

> [!info] 一句话导读
> Published: 2026-09-18

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://chuks.org/blog/chuks-v020-rc1-the-release-candidate>
> 首次收录：2026-09-20T09:48:16+08:00
> 来源渠道：HN Show HN
> 标签：author_princeLex, story_49764179, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T02:35:34+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/2b4521243f9bf52b_Show-HN-Chuks-v0.2.0-RC.1,-we're-asking-people-to]] |
| 2026-09-20T02:46:51+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/2b4521243f9bf52b_Show-HN-Chuks-v0.2.0-RC.1,-we're-asking-people-to]] |
| 2026-09-20T02:55:58+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/2b4521243f9bf52b_Show-HN-Chuks-v0.2.0-RC.1,-we're-asking-people-to]] |
| 2026-09-20T03:04:29+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/2b4521243f9bf52b_Show-HN-Chuks-v0.2.0-RC.1,-we're-asking-people-to]] |
| 2026-09-20T03:16:53+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/2b4521243f9bf52b_Show-HN-Chuks-v0.2.0-RC.1,-we're-asking-people-to]] |
| 2026-09-20T03:29:12+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/2b4521243f9bf52b_Show-HN-Chuks-v0.2.0-RC.1,-we're-asking-people-to]] |
| 2026-09-20T03:38:50+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/2b4521243f9bf52b_Show-HN-Chuks-v0.2.0-RC.1,-we're-asking-people-to]] |
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/2b4521243f9bf52b_Show-HN-Chuks-v0.2.0-RC.1,-we're-asking-people-to]] |
| 2026-09-20T09:48:16+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/2b4521243f9bf52b_Show-HN-Chuks-v0.2.0-RC.1,-we're-asking-people-to]] |

## 摘要正文

Published: 2026-09-18 Author: Chuks Team   Language Design & Engineering  Chuks v0.2.0-rc.1: The Release Candidate | Chuks Programming Language  # Chuks v0.2.0-rc.1: The Release Candidate   Sep 18, 2026  v0.2.0-rc.1 is a release candidate, not the stable release. Opt in:  Terminal window  # Already have Chuks installed  chuks upgrade --prerelease  # First-time install  curl -fsSL https://chuks.org/install.sh | bash && chuks upgrade --prerelease  A plain `chuks upgrade` stays on v0.1.2 until v0.2.0 ships. On an rc build it says so rather than moving you back.  Chuks v0.2.0-rc.1 is the build we believe is 0.2.0. Everything in it went through the same gate as a release: the golden suite on both backends, the fuzzed differential between the bytecode VM and the native binary, twenty-four differential suites, cross-compilation for five targets, and two consumer test suites that must print byte-identical output both ways. What that gate cannot supply is a program it has never seen. Most of what is fixed below was found not by a test but by building real programs in Chuks; the rest of the way to 0.2.0 is other people’s programs, which is what a release candidate is for.  `chuks --version` …
