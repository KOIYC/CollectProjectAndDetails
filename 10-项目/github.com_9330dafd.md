---
type: "project"
title: "Show HN: Elemental – simple front ends in plain JavaScript"
project_url: "https://github.com/fynyky/elemental"
first_seen: "2026-09-21T02:53:00+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_fynyky
  - story_48324378
  - show_hn
lang: "en"
---

# Show HN: Elemental – simple front ends in plain JavaScript

> [!info] 一句话导读
> Simple reactive front-end library

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/fynyky/elemental>
> 首次收录：2026-09-21T02:53:00+08:00
> 来源渠道：HN Show HN
> 标签：author_fynyky, story_48324378, show_hn
> 最新指标：点赞=6 · 评论=3 · engagement_velocity=6

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:27:24+08:00 | HN Show HN | 点赞=6 · 评论=3 · engagement_velocity=6 | [[20-语料/posts/hn_show/2026-09-21/bb6d61231da76bef_Show-HN-Elemental-–-simple-front-ends-in-plain-Jav]] |
| 2026-09-21T01:44:14+08:00 | HN Show HN | 点赞=6 · 评论=3 · engagement_velocity=6 | [[20-语料/posts/hn_show/2026-09-21/bb6d61231da76bef_Show-HN-Elemental-–-simple-front-ends-in-plain-Jav]] |
| 2026-09-21T02:53:00+08:00 | HN Show HN | 点赞=6 · 评论=3 · engagement_velocity=6 | [[20-语料/posts/hn_show/2026-09-21/bb6d61231da76bef_Show-HN-Elemental-–-simple-front-ends-in-plain-Jav]] |

## 摘要正文

# fynyky/elemental  Simple reactive front-end library  - Stars: 32 - Forks: 1 - Watchers: 32 - Open issues: 2 - License: MIT License - Default branch: master - Created: 2023-08-03T21:26:27Z  ## Languages  - JavaScript  ## Topics  - declarative - dom - frontend - javascript - reactive - reactive-ui - ui - vanilla-js - web-components  ## Top Contributors  - fynyky (148 contributions) - github-actions[bot] (1 contributions)  ---  ## README  Elemental ==========  Elemental is a simple front-end library that lets you build reactive UIs declaratively using plain JavaScript. No special syntax to learn or complex frameworks to build around, just normal nested functions.  Here's a quick example of what Elemental does: ```javascript import { Reactor, ob, el } from '@fynyky/elemental'  const rx = new Reactor({ name: 'Anakin' })  el(document.body,   el('main',     el('h1', 'Hello World!'),     el('h2', (x) => { x.id = 'foo' }, () => 'returned text'),     el('div.note', ['this', 'is', 'an', 'array']),     el('p.greeting', ob(() => ('My name is ' + rx.name)))   ) ) // <main> //   <h1>Hello World!</h1> //   <h2 id="foo">returned text</h2> //   <div class="note">thisisanarray</div> //   <p class="…
