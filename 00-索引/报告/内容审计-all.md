---
type: "report"
title: "内容质量审计 all"
updated: "2026-09-25T00:31:32+08:00"
tags:
  - 索引
  - 审计
  - 内容质量
---

# 语料内容质量审计

> 生成 2026-09-25T00:31:32+08:00 · 审计器 `tools/kb_content_audit.py`

- 唯一条目 **1886** · 可用（无致命缺陷、且相关）**1662** (88%)
- 不可用于深度分析（空/过短/摘要残文）**104** (6%)
- 相关性可疑（无项目信号/资源清单/泛媒体/大厂）**147** (8%)
- 正文长度 中位 **1905.5** · 均值 4794 · 空正文 43 · <200 字符 115
- 历史深度（**内容发布时间轴**，趋势分析看这个）：近 90 天 **1421 条**，更早 382 条，无发布时间 83 条（最早 ['2014-04-04']）
- 采集时间轴：`captured_at` 覆盖 5 天 (2026-09-20, 2026-09-21, 2026-09-22, 2026-09-24, 2026-09-25)
- 语种：en=1774, zh=112
- kind：post=1709, project=157, method=17, person=3

## 问题标签汇总

| 问题 | 条数 | 占比 |
|---|---|---|
| 无项目链接 | 308 | 16% |
| 无指标 | 299 | 16% |
| 缺作者 | 175 | 9% |
| HTML未清理 | 158 | 8% |
| 无项目信号 | 114 | 6% |
| 视频无正文 | 101 | 5% |
| 缺发布时间 | 83 | 4% |
| 正文过短(<200) | 72 | 4% |
| 空正文 | 43 | 2% |
| 资源清单/名录 | 34 | 2% |
| Exa截断 | 28 | 1% |
| RSS摘要/残文 | 24 | 1% |
| 发布时间未规范化 | 5 | 0% |
| 大厂产品 | 4 | 0% |
| 泛媒体主题 | 3 | 0% |

## 渠道质量矩阵

| 渠道 | 角色 | 条目 | 可用 | 不可用 | 相关性可疑 | 资源清单 | 大厂 | 摘要残文 | Exa截断 | HTML残留 | 无时间 | 无作者 | 无指标 | 正文中位 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hn_show | 原文=项目发布帖 | 1120 | 1052 | 68 | 0 | 0 | 0 | 17 | 24 | 18 | 0 | 0 | 0 | 4025 |
| reddit | 项目讨论 | 296 | 182 | 32 | 109 | 8 | 3 | 4 | 0 | 0 | 0 | 0 | 0 | 873 |
| producthunt | 项目发布 | 121 | 120 | 0 | 1 | 0 | 1 | 0 | 0 | 121 | 0 | 0 | 121 | 329 |
| betalist | 预发布项目 | 78 | 78 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 78 | 78 | 1839 |
| indiehackers | 项目库 | 75 | 74 | 1 | 0 | 0 | 0 | 1 | 4 | 0 | 75 | 75 | 75 | 2945 |
| github_new | 项目仓库 | 64 | 47 | 2 | 15 | 11 | 0 | 2 | 0 | 19 | 0 | 0 | 0 | 5370 |
| v2ex | 中文讨论 | 51 | 38 | 1 | 12 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 968 |
| bilibili | 中文视频（仅元数据） | 48 | 46 | 0 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 132 |
| exa_discovery | 全网语义发现 | 17 | 12 | 0 | 5 | 5 | 0 | 0 | 0 | 0 | 5 | 17 | 17 | 2931 |
| devto | 项目复盘文 | 8 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10344 |
| c1c7 | 中文名录（含资源/人物） | 7 | 4 | 0 | 3 | 1 | 0 | 0 | 0 | 0 | 7 | 4 | 7 | 216 |
| xiaohongshu | 中文社媒 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 497 |

## 跨渠道重复（同 project_url 出现在多渠道，语料层未合并）

- hn_show, indiehackers, reddit → play.google.com/store/apps/details

## 元数据完整性

- `published_at` 缺失 **83** · 格式未规范化 **5**
- `author` 缺失 **175** · `metrics` 全空 **299**
- `body_format`：markdown=1163, text=723


## 问题样例（人工复核用）

### 无项目链接（308 条）
- `bilibili` 个人独立游戏作品
- `bilibili` 为什么很多程序员都不去做独立开发者？
- `bilibili` 独立开发者一年可以赚多少钱？
- `bilibili` 16岁高一学生正在尝试独立开发galgame（插画和脚本独立完成）但需要BGM支持，有没有会音编的朋友（本人只懂一些钢琴纯音

### 无指标（299 条）
- `betalist` Gb7 Meetup
- `betalist` Zapters
- `betalist` 1Presence
- `betalist` Campaignstack

### 缺作者（175 条）
- `betalist` Gb7 Meetup
- `betalist` Zapters
- `betalist` 1Presence
- `betalist` Campaignstack

### HTML未清理（158 条）
- `github_new` Edge0-AI/Edge0
- `github_new` s87343472/backlink-pilot
- `github_new` Gingiris/gingiris-launch
- `github_new` joshwcomeau/Tello

### 无项目信号（114 条）
- `c1c7` Master of Scale
- `c1c7` v2ex 论坛 - 分享创造板块
- `c1c7` Patrick McKenzie (@patio11)
- `c1c7` Pieter Levels (@levelsio)

### 视频无正文（101 条）
- `bilibili` 独立开发两种赚钱方式！99%的人没想明白！
- `bilibili` 个人独立游戏作品
- `bilibili` 为什么很多程序员都不去做独立开发者？
- `bilibili` 独立开发赚了500W后，我想给你这些建议！

### 缺发布时间（83 条）
- `c1c7` Master of Scale
- `c1c7` Sideidea
- `c1c7` PriceTag 的独立开发者采访（公众号 PriceTagApp）
- `c1c7` v2ex 论坛 - 分享创造板块

### 正文过短(<200)（72 条）
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
- `c1c7` Sideidea
- `exa_discovery` Tony Dinh: $45K/mo Indie Hacker Journey

### Exa截断（28 条）
- `hn_show` Show HN: LingBot-World 2.0 (1.3B) running at 16 FPS on one RTX 5090
- `hn_show` Show HN: Omabib, a Zotero alternative for Omarchy with agent support
- `hn_show` Show HN: Talos – A personal agent whose kernel gates every tool call
- `hn_show` Show HN: Proxy-benchmark – is it the proxy, the browser, or your machine?

### RSS摘要/残文（24 条）
- `github_new` huaminghuangtw/Strava-Tool
- `github_new` NandhaKishorM/laya
- `hn_show` Show HN: Koi Editor Alpha
- `hn_show` Show HN: Concat: the open-source CapCut replacement.

### 发布时间未规范化（5 条）
- `exa_discovery` Building a $10K MRR testimonial tool by building in public
- `exa_discovery` 一年上线超 10 款产品，AI 时代如何做独立开发 - InfoQ
- `exa_discovery` 《独立开发者的出海之道》
- `exa_discovery` 独立开发者做APP出海,最缺的其实不是代码-夜雨聆风

### 大厂产品（4 条）
- `producthunt` Google Flow for iOS & Android
- `reddit` Google isn't ranking our website despite following basic SEO best practices - wh
- `reddit` Ranked on Google, ChatGPT within 30 days of launch 💪
- `reddit` 120K+ Daily views on TikTok with a Phone Farm

### 泛媒体主题（3 条）
- `reddit` Started this viking survival game at 15, I'm 24 now
- `reddit` Hardware advise request
- `v2ex` RED 实战：用 AI 把一个想法做成能用的 DSH 插件
