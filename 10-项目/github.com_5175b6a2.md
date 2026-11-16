---
type: "project"
title: "Show HN: Get your coding agent off ~2019 JavaScript, onto modern web primitives"
project_url: "https://github.com/GoogleChrome/modern-web-guidance"
first_seen: "2026-11-11T13:37:17+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_paulirish
  - story_50443812
  - show_hn
  - front_page
lang: "en"
---

# Show HN: Get your coding agent off ~2019 JavaScript, onto modern web primitives

> [!info] 一句话导读
> Browsers natively handle a lot of what used to take 50 lines of JS (or a dependency): `CSS.highlights` for text range highlighting without <span>s everywhere, `…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/GoogleChrome/modern-web-guidance>
> 首次收录：2026-11-11T13:37:17+08:00
> 来源渠道：HN Show HN
> 标签：author_paulirish, story_50443812, show_hn, front_page
> 最新指标：点赞=321 · 评论=98 · engagement_velocity=321

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-11T13:37:17+08:00 | HN Show HN | 点赞=321 · 评论=98 · engagement_velocity=321 | [[20-语料/posts/hn_show/2026-11-11/aa8e9ffb2c83fea6_Show-HN-Get-your-coding-agent-off-~2019-JavaScript]] |

## 摘要正文

Browsers natively handle a lot of what used to take 50 lines of JS (or a dependency): `CSS.highlights` for text range highlighting without s everywhere, `<dialog>` and showModal() give you backdrops and ideal focus management, `field-sizing` to auto-grow textareas as the user types.. (Something yesterday's ftrain post touched on [0])Models know about some of these by name, but consistently won't default to using the platform-native solution and instead prefer the incumbent +JS based pattern. We started an effort in Chrome to supplement coding agents with this key domain knowledge and we're shipping our 1.0 today, in collaboration with Firefox, MDN, and Edge.200+ guides (~1.7MB) of curated, hand-crafted implementation best-practices from web experts, updated as the web evolves. (Open source, obv, so.. we'll welcome your bikeshedding ;) Readable versions here: [1]I've spent the last 9 months obsessing over how to ship this as an agent skill + (Agentic RAG) CLI without blowing up your context window. (Or cedeing activation mechanics to MCP dynamic tool search). The skill description is minmaxed for activating on relevant frontend tasks. The RAG work I'm pretty proud of… originally a 5…
