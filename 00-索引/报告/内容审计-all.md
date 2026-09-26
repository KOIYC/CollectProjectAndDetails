---
type: "report"
title: "内容质量审计 all"
updated: "2026-09-26T10:02:49+08:00"
tags:
  - 索引
  - 审计
  - 内容质量
---

# 语料内容质量审计

> 生成 2026-09-26T10:02:49+08:00 · 审计器 `tools/kb_content_audit.py`

- 唯一条目 **2068** · 可用（无致命缺陷、且相关）**1828** (88%)
- 不可用于深度分析（空/过短/摘要残文）**99** (5%)
- 相关性可疑（无项目信号/资源清单/泛媒体/大厂）**166** (8%)
- 正文长度 中位 **1820.5** · 均值 4673 · 空正文 43 · <200 字符 109
- 历史深度（**内容发布时间轴**，趋势分析看这个）：近 90 天 **1594 条**，更早 382 条，无发布时间 92 条（最早 ['2014-04-04']）
- 采集时间轴：`captured_at` 覆盖 6 天 (2026-09-20, 2026-09-21, 2026-09-22, 2026-09-24, 2026-09-25, 2026-09-26)
- 语种：en=1954, zh=114
- kind：post=1870, project=178, method=17, person=3

## 问题标签汇总

| 问题 | 条数 | 占比 |
|---|---|---|
| 无指标 | 355 | 17% |
| 无项目链接 | 336 | 16% |
| 缺作者 | 196 | 9% |
| HTML未清理 | 196 | 9% |
| 无项目信号 | 131 | 6% |
| 视频无正文 | 109 | 5% |
| 缺发布时间 | 92 | 4% |
| 正文过短(<200) | 66 | 3% |
| 空正文 | 43 | 2% |
| 资源清单/名录 | 34 | 2% |
| Exa截断 | 29 | 1% |
| RSS摘要/残文 | 25 | 1% |
| 大厂产品 | 6 | 0% |
| 发布时间未规范化 | 5 | 0% |
| 泛媒体主题 | 3 | 0% |

## 渠道质量矩阵

| 渠道 | 角色 | 条目 | 可用 | 不可用 | 相关性可疑 | 资源清单 | 大厂 | 摘要残文 | Exa截断 | HTML残留 | 无时间 | 无作者 | 无指标 | 正文中位 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hn_show | 原文=项目发布帖 | 1200 | 1131 | 69 | 0 | 0 | 0 | 19 | 25 | 21 | 0 | 0 | 0 | 3945 |
| reddit | 项目讨论 | 338 | 204 | 28 | 131 | 9 | 5 | 4 | 0 | 0 | 0 | 0 | 0 | 936 |
| producthunt | 项目发布 | 156 | 155 | 0 | 1 | 0 | 1 | 0 | 0 | 156 | 0 | 0 | 156 | 328 |
| betalist | 预发布项目 | 96 | 96 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 96 | 96 | 1652 |
| indiehackers | 项目库 | 78 | 77 | 1 | 0 | 0 | 0 | 1 | 4 | 0 | 78 | 78 | 78 | 2657 |
| github_new | 项目仓库 | 64 | 48 | 1 | 15 | 11 | 0 | 1 | 0 | 19 | 0 | 0 | 0 | 5370 |
| v2ex | 中文讨论 | 52 | 40 | 0 | 12 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 997 |
| bilibili | 中文视频（仅元数据） | 49 | 47 | 0 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 132 |
| exa_discovery | 全网语义发现 | 17 | 12 | 0 | 5 | 5 | 0 | 0 | 0 | 0 | 5 | 17 | 17 | 2931 |
| devto | 项目复盘文 | 10 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10108 |
| c1c7 | 中文名录（含资源/人物） | 7 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 4 | 7 | 216 |
| xiaohongshu | 中文社媒 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 497 |

## 跨渠道重复（同 project_url 出现在多渠道，语料层未合并）

- hn_show, indiehackers, reddit → play.google.com/store/apps/details

## 元数据完整性

- `published_at` 缺失 **92** · 格式未规范化 **5**
- `author` 缺失 **196** · `metrics` 全空 **355**
- `body_format`：markdown=1251, text=817


## 问题样例（人工复核用）

### 无指标（355 条）
- `betalist` Gb7 Meetup
- `betalist` Zapters
- `betalist` 1Presence
- `betalist` Campaignstack

### 无项目链接（336 条）
- `bilibili` 个人独立游戏作品
- `bilibili` 为什么很多程序员都不去做独立开发者？
- `bilibili` 独立开发者一年可以赚多少钱？
- `bilibili` 16岁高一学生正在尝试独立开发galgame（插画和脚本独立完成）但需要BGM支持，有没有会音编的朋友（本人只懂一些钢琴纯音

### 缺作者（196 条）
- `betalist` Gb7 Meetup
- `betalist` Zapters
- `betalist` 1Presence
- `betalist` Campaignstack

### HTML未清理（196 条）
- `github_new` Edge0-AI/Edge0
- `github_new` s87343472/backlink-pilot
- `github_new` Gingiris/gingiris-launch
- `github_new` joshwcomeau/Tello

### 无项目信号（131 条）
- `c1c7` Patrick McKenzie (@patio11)
- `c1c7` Pieter Levels (@levelsio)
- `github_new` tamaratran/fast-jev-compaction
- `github_new` Edge0-AI/Edge0

### 视频无正文（109 条）
- `bilibili` 独立开发两种赚钱方式！99%的人没想明白！
- `bilibili` 个人独立游戏作品
- `bilibili` 为什么很多程序员都不去做独立开发者？
- `bilibili` 独立开发赚了500W后，我想给你这些建议！

### 缺发布时间（92 条）
- `betalist` Flowmate
- `betalist` Dividend Stacker
- `betalist` Halv
- `betalist` Matthew Kellogg

### 正文过短(<200)（66 条）
- `bilibili` 独立开发两种赚钱方式！99%的人没想明白！
- `bilibili` 个人独立游戏作品
- `bilibili` 为什么很多程序员都不去做独立开发者？
- `bilibili` 独立开发赚了500W后，我想给你这些建议！

### 空正文（43 条）
- `bilibili` 【亲身经历】30+程序员折腾的11年，第二章：独立开发！
- `bilibili` 程序员辞职做独立开发者，靠谱吗？
- `bilibili` 一个老板八个AI虾兵，AI催生一人公司热潮，睿见
- `bilibili` 为什么说接下来会诞生很多“一人公司”？

### 资源清单/名录（34 条）
- `bilibili` 独立开发者省钱之穷鬼套餐，从零开始完整实战，不花一分钱上线完整应用
- `bilibili` S1E9｜2026年普通人还能做一人公司吗？｜油管大神DanKoe｜三小时教程拆解
- `exa_discovery` Tony Dinh: $45K/mo Indie Hacker Journey
- `exa_discovery` 做了个 AI 视频生成工具出海，分享一些踩坑经验 · w2solo - 独立开发者社区

### Exa截断（29 条）
- `hn_show` Show HN: LingBot-World 2.0 (1.3B) running at 16 FPS on one RTX 5090
- `hn_show` Show HN: Omabib, a Zotero alternative for Omarchy with agent support
- `hn_show` Show HN: Talos – A personal agent whose kernel gates every tool call
- `hn_show` Show HN: Proxy-benchmark – is it the proxy, the browser, or your machine?

### RSS摘要/残文（25 条）
- `github_new` huaminghuangtw/Strava-Tool
- `hn_show` Show HN: Koi Editor Alpha
- `hn_show` Show HN: Concat: the open-source CapCut replacement.
- `hn_show` Show HN: Knecht, a tool for building software factories for agencies

### 大厂产品（6 条）
- `producthunt` Google Flow for iOS & Android
- `reddit` Google isn't ranking our website despite following basic SEO best practices - wh
- `reddit` Ranked on Google, ChatGPT within 30 days of launch 💪
- `reddit` 120K+ Daily views on TikTok with a Phone Farm

### 发布时间未规范化（5 条）
- `exa_discovery` Building a $10K MRR testimonial tool by building in public
- `exa_discovery` 一年上线超 10 款产品，AI 时代如何做独立开发 - InfoQ
- `exa_discovery` 《独立开发者的出海之道》
- `exa_discovery` 独立开发者做APP出海,最缺的其实不是代码-夜雨聆风

### 泛媒体主题（3 条）
- `reddit` Started this viking survival game at 15, I'm 24 now
- `reddit` Hardware advise request
- `v2ex` RED 实战：用 AI 把一个想法做成能用的 DSH 插件
