---
type: "project"
title: "Show HN: Wanim – Manim in the browser, but 1/20 smaller"
project_url: "https://github.com/Acfboy/Wanim"
first_seen: "2026-10-30T09:46:09+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_Acfboy
  - story_50291932
  - show_hn
lang: "en"
---

# Show HN: Wanim – Manim in the browser, but 1/20 smaller

> [!info] 一句话导读
> Hi HN, I really like Manim, but when I tried to use it to make interactive small demos on the web, I found that no project can simultaneously satisfy running or…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/Acfboy/Wanim>
> 首次收录：2026-10-30T09:46:09+08:00
> 来源渠道：HN Show HN
> 标签：author_Acfboy, story_50291932, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-30T09:46:09+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-10-30/0f9497907d07c339_Show-HN-Wanim-–-Manim-in-the-browser,-but-1-20-sma]] |

## 摘要正文

Hi HN, I really like Manim, but when I tried to use it to make interactive small demos on the web, I found that no project can simultaneously satisfy running original manim python code without carrying the bulky pyodide which makes it impossible to embed. So I made one. My idea is to rewrite a js library that is almost completely identical to manim, and then patch rapydscript-ng to translate the original code to js, and support numpy syntax. It looks surprisingly good, supports the vast majority of syntax, and the size is only about 1M (1/20 of pyodide)! You can try it at https://wanim.org/playground, and there is an interactive courseware example at https://wanim.org/blog.
