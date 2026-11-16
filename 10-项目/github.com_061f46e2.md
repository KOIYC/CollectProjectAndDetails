---
type: "project"
title: "Show HN: Skillset: Easily curate and install agent skills collection"
project_url: "https://github.com/itsmeyaw/skillset"
first_seen: "2026-11-16T10:00:05+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_itsmeyaw
  - story_50511761
  - show_hn
lang: "en"
---

# Show HN: Skillset: Easily curate and install agent skills collection

> [!info] 一句话导读
> Hi everyone!Installing skills globally in ~/.agents or ~/.claude consumes too much context, yet manually installing specific skills for every project is tedious…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/itsmeyaw/skillset>
> 首次收录：2026-11-16T10:00:05+08:00
> 来源渠道：HN Show HN
> 标签：author_itsmeyaw, story_50511761, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-16T10:00:05+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-11-16/035e8d287112eba8_Show-HN-Skillset-Easily-curate-and-install-agent-s]] |

## 摘要正文

Hi everyone!Installing skills globally in ~/.agents or ~/.claude consumes too much context, yet manually installing specific skills for every project is tedious. Wouldn't it be better to group skills for programming, backend architecture, or graphic design into collections, and install them with a single command only when needed?To solve this, I built Skillset. It acts as a wrapper around the Vercel Skill CLI that batch-installs sets of skills from multiple sources using a single JSON file, essentially npm for skills!While similar tools exist, most are written from scratch, which makes me concerned about their compatibility. Because Vercel’s Skill CLI is already the de facto standard (imo!), Skillset uses it directly as an underlying library. So it guarantees seamless compatibility across teams, regardless of whether they use Skillset or the standard Vercel CLI.
