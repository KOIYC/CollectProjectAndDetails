---
type: "project"
title: "Show HN: A malleable and formally verified Web engine"
project_url: "https://github.com/gterzian/formal-webIntro"
first_seen: "2026-10-29T20:41:52+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_polyglotfacto
  - story_50285197
  - show_hn
lang: "en"
---

# Show HN: A malleable and formally verified Web engine

> [!info] 一句话导读
> Hello HN,I've been working on a new Web engine, build around two ideas:- use formal methods from day one.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/gterzian/formal-webIntro>
> 首次收录：2026-10-29T20:41:52+08:00
> 来源渠道：HN Show HN
> 标签：author_polyglotfacto, story_50285197, show_hn
> 最新指标：点赞=6 · 评论=0 · engagement_velocity=6

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-29T20:41:52+08:00 | HN Show HN | 点赞=6 · 评论=0 · engagement_velocity=6 | [[20-语料/posts/hn_show/2026-10-29/9dca8c5af5e1017f_Show-HN-A-malleable-and-formally-verified-Web-engi]] |

## 摘要正文

Hello HN,I've been working on a new Web engine, build around two ideas:- use formal methods from day one. - make it modular.The modularity is orientated towards the following goals:- enabling shipping anywhere, including on IOS in the EU as per Apple’s guidelines. - only write code for stuff the OS or application platform cannot do for you: keep binary size to a minimum and achieve native performance. - developer choice: bring what you want, and only build what you need.For example you can choose a JS engine like v8 or Boa, or just bring your own. The entire graphics pipeline consists of components whose implementation can be swapped-out, with currently a relatively fast path on Mac integrating with Core Animation and a slower cross platform path.Project is at https://github.com/gterzian/formal-webIntro essay at: https://medium.com/@polyglot_factotum/how-i-am-building-a-we...Please let me know what you think.
