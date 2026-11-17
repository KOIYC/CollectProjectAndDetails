---
type: "project"
title: "Show HN: CutCraft – an MIT library for making and editing videos in TSX"
project_url: "https://github.com/prefix-tree/cutcraft"
first_seen: "2026-11-17T11:09:12+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_bsnisar
  - story_50521717
  - show_hn
lang: "en"
---

# Show HN: CutCraft – an MIT library for making and editing videos in TSX

> [!info] 一句话导读
> prefix-tree/cutcraft

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/prefix-tree/cutcraft>
> 首次收录：2026-11-17T11:09:12+08:00
> 来源渠道：HN Show HN
> 标签：author_bsnisar, story_50521717, show_hn
> 最新指标：点赞=4 · 评论=0 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-17T11:09:12+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-11-17/6ef1ff353b4648d8_Show-HN-CutCraft-–-an-MIT-library-for-making-and-e]] |

## 摘要正文

# prefix-tree/cutcraft  Video editor as code: LLMs write code well and math badly, so a model writes a TSX file of words and shots, and CutCraft does the arithmetic, plays it in the browser, edits it and exports it.  - Stars: 0 - Forks: 0 - Watchers: 0 - Open issues: 0 - License: MIT License - Homepage: https://cutcraft.prefixtree.xyz/ - Default branch: main - Created: 2026-10-25T15:18:35Z  ## Languages  - CSS - HTML - JavaScript - TypeScript  ## Topics  - ai-agents - dsl - llm - react - timeline - typescript - video - video-editing - video-rendering - webcodecs  ## Top Contributors  - bsnisar (152 contributions) - claude (45 contributions) - dependabot[bot] (3 contributions)  ---  ## README   CutCraft   Video editor as code.  LLMs write code well and math badly, so a model writes a TSX file of words and shots, and CutCraft does the  arithmetic, plays it in the browser, edits it and exports it.   Documentation ·  Examples ·  Guide ·  Reference ·  Changelog  ---  ```tsx export const schema = z.object({ product: z.string(), accent: z.string() }); export const defaults = { product: "Shed", accent: "#ff5a1f" };  export default function Video({ product, accent }: z.infer<typeof schema>)…
