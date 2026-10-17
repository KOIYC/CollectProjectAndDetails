---
type: "report"
title: "内容质量审计 all"
updated: "2026-10-16T09:56:36+08:00"
tags:
  - 索引
  - 审计
  - 内容质量
---

# 语料内容质量审计

> 生成 2026-10-16T09:56:36+08:00 · 审计器 `tools/kb_content_audit.py`

- 唯一条目 **2809** · 可用（无致命缺陷、且相关）**2493** (89%)
- 不可用于深度分析（空/过短/摘要残文）**124** (4%)
- 相关性可疑（无项目信号/资源清单/泛媒体/大厂）**223** (8%)
- 正文长度 中位 **1734** · 均值 4405 · 空正文 51 · <200 字符 133
- 历史深度（**内容发布时间轴**，趋势分析看这个）：近 90 天 **2128 条**，更早 541 条，无发布时间 140 条（最早 ['2014-04-04']）
- 采集时间轴：`captured_at` 覆盖 13 天 (2026-09-20, 2026-09-21, 2026-09-22, 2026-09-24, 2026-09-25, 2026-09-26, 2026-09-28, 2026-09-29, 2026-09-30, 2026-10-01, 2026-10-10, 2026-10-11, 2026-10-16)
- 语种：en=2628, zh=181
- kind：post=2479, project=302, method=25, person=3

## 问题标签汇总

| 问题 | 条数 | 占比 |
|---|---|---|
| 无指标 | 659 | 23% |
| 无项目链接 | 420 | 15% |
| HTML未清理 | 388 | 14% |
| 缺作者 | 328 | 12% |
| 无项目信号 | 157 | 6% |
| 缺发布时间 | 140 | 5% |
| 视频无正文 | 140 | 5% |
| 正文过短(<200) | 82 | 3% |
| 资源清单/名录 | 58 | 2% |
| 空正文 | 51 | 2% |
| Exa截断 | 36 | 1% |
| RSS摘要/残文 | 34 | 1% |
| 大厂产品 | 14 | 0% |
| 发布时间未规范化 | 5 | 0% |
| 泛媒体主题 | 4 | 0% |

## 渠道质量矩阵

| 渠道 | 角色 | 条目 | 可用 | 不可用 | 相关性可疑 | 资源清单 | 大厂 | 摘要残文 | Exa截断 | HTML残留 | 无时间 | 无作者 | 无指标 | 正文中位 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hn_show | 原文=项目发布帖 | 1479 | 1396 | 83 | 0 | 0 | 0 | 26 | 32 | 27 | 0 | 0 | 0 | 3725 |
| reddit | 项目讨论 | 409 | 248 | 37 | 155 | 10 | 5 | 4 | 0 | 0 | 0 | 0 | 0 | 877 |
| producthunt | 项目发布 | 328 | 322 | 0 | 6 | 0 | 6 | 0 | 0 | 328 | 0 | 0 | 328 | 327 |
| betalist | 预发布项目 | 170 | 170 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 170 | 170 | 1859 |
| indiehackers | 项目库 | 128 | 125 | 3 | 0 | 0 | 0 | 3 | 4 | 0 | 128 | 128 | 128 | 2680 |
| v2ex | 中文讨论 | 106 | 75 | 0 | 31 | 23 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 1213 |
| github_new | 项目仓库 | 78 | 58 | 1 | 19 | 14 | 1 | 1 | 0 | 30 | 0 | 0 | 0 | 6321 |
| bilibili | 中文视频（仅元数据） | 62 | 59 | 0 | 3 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 137 |
| exa_discovery | 全网语义发现 | 25 | 19 | 0 | 6 | 6 | 0 | 0 | 0 | 0 | 5 | 25 | 25 | 2913 |
| devto | 项目复盘文 | 16 | 14 | 0 | 2 | 2 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 10344 |
| c1c7 | 中文名录（含资源/人物） | 7 | 6 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 7 | 4 | 7 | 216 |
| xiaohongshu | 中文社媒 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 499 |

## 跨渠道重复（同 project_url 出现在多渠道，语料层未合并）

- hn_show, indiehackers, reddit → play.google.com/store/apps/details

## 元数据完整性

- `published_at` 缺失 **140** · 格式未规范化 **5**
- `author` 缺失 **328** · `metrics` 全空 **659**
- `body_format`：markdown=1564, text=1245


## 问题样例（人工复核用）

### 无指标（659 条）
- `betalist` Gb7 Meetup
- `betalist` Zapters
- `betalist` 1Presence
- `betalist` Campaignstack

### 无项目链接（420 条）
- `bilibili` 个人独立游戏作品
- `bilibili` 为什么很多程序员都不去做独立开发者？
- `bilibili` 独立开发者一年可以赚多少钱？
- `bilibili` 16岁高一学生正在尝试独立开发galgame（插画和脚本独立完成）但需要BGM支持，有没有会音编的朋友（本人只懂一些钢琴纯音

### HTML未清理（388 条）
- `devto` I Built a Better Codex Pet Than OpenAI Did
- `devto` Why you still need a Website Portfolio, even though everyone can Vibe Code it.
- `devto` I Turned My GitHub Profile Into a Cyberpunk Console With a City Built From My Co
- `github_new` Edge0-AI/Edge0

### 缺作者（328 条）
- `betalist` Gb7 Meetup
- `betalist` Zapters
- `betalist` 1Presence
- `betalist` Campaignstack

### 无项目信号（157 条）
- `bilibili` 【Lee哥】做了10年Unity后，他说AI已经超过很多程序员了 | 游戏开发 | 案例分析
- `c1c7` Patrick McKenzie (@patio11)
- `c1c7` Pieter Levels (@levelsio)
- `github_new` tamaratran/fast-jev-compaction

### 缺发布时间（140 条）
- `betalist` Flowmate
- `betalist` Matthew Kellogg
- `betalist` Beteam
- `betalist` Budgetpixel

### 视频无正文（140 条）
- `bilibili` 独立开发两种赚钱方式！99%的人没想明白！
- `bilibili` 个人独立游戏作品
- `bilibili` 为什么很多程序员都不去做独立开发者？
- `bilibili` 独立开发赚了500W后，我想给你这些建议！

### 正文过短(<200)（82 条）
- `bilibili` 独立开发两种赚钱方式！99%的人没想明白！
- `bilibili` 个人独立游戏作品
- `bilibili` 为什么很多程序员都不去做独立开发者？
- `bilibili` 独立开发赚了500W后，我想给你这些建议！

### 资源清单/名录（58 条）
- `bilibili` 独立开发者省钱之穷鬼套餐，从零开始完整实战，不花一分钱上线完整应用
- `bilibili` S1E9｜2026年普通人还能做一人公司吗？｜油管大神DanKoe｜三小时教程拆解
- `c1c7` Sideidea
- `devto` Why you still need a Website Portfolio, even though everyone can Vibe Code it.

### 空正文（51 条）
- `bilibili` 【亲身经历】30+程序员折腾的11年，第二章：独立开发！
- `bilibili` 程序员辞职做独立开发者，靠谱吗？
- `bilibili` 一个老板八个AI虾兵，AI催生一人公司热潮，睿见
- `bilibili` 为什么说接下来会诞生很多“一人公司”？

### Exa截断（36 条）
- `hn_show` Show HN: LingBot-World 2.0 (1.3B) running at 16 FPS on one RTX 5090
- `hn_show` Show HN: Omabib, a Zotero alternative for Omarchy with agent support
- `hn_show` Show HN: Talos – A personal agent whose kernel gates every tool call
- `hn_show` Show HN: Proxy-benchmark – is it the proxy, the browser, or your machine?

### RSS摘要/残文（34 条）
- `github_new` huaminghuangtw/Strava-Tool
- `hn_show` Show HN: Koi Editor Alpha
- `hn_show` Show HN: Concat: the open-source CapCut replacement.
- `hn_show` Show HN: Knecht, a tool for building software factories for agencies

### 大厂产品（14 条）
- `github_new` openai/math
- `producthunt` Gemini Agent for Google Cloud
- `producthunt` Playground by Google Labs
- `producthunt` Microsoft Copilot

### 发布时间未规范化（5 条）
- `exa_discovery` Building a $10K MRR testimonial tool by building in public
- `exa_discovery` 一年上线超 10 款产品，AI 时代如何做独立开发 - InfoQ
- `exa_discovery` 《独立开发者的出海之道》
- `exa_discovery` 独立开发者做APP出海,最缺的其实不是代码-夜雨聆风

### 泛媒体主题（4 条）
- `reddit` Started this viking survival game at 15, I'm 24 now
- `reddit` Hardware advise request
- `reddit` Jellyfin Remote Access with Whitelisted Dynamic IPs
- `v2ex` RED 实战：用 AI 把一个想法做成能用的 DSH 插件
