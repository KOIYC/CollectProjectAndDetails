---
type: "report"
title: "内容质量审计 all"
updated: "2026-09-29T09:51:47+08:00"
tags:
  - 索引
  - 审计
  - 内容质量
---

# 语料内容质量审计

> 生成 2026-09-29T09:51:47+08:00 · 审计器 `tools/kb_content_audit.py`

- 唯一条目 **2254** · 可用（无致命缺陷、且相关）**1996** (89%)
- 不可用于深度分析（空/过短/摘要残文）**106** (5%)
- 相关性可疑（无项目信号/资源清单/泛媒体/大厂）**179** (8%)
- 正文长度 中位 **1795.0** · 均值 4565 · 空正文 45 · <200 字符 117
- 历史深度（**内容发布时间轴**，趋势分析看这个）：近 90 天 **1627 条**，更早 529 条，无发布时间 98 条（最早 ['2014-04-04']）
- 采集时间轴：`captured_at` 覆盖 8 天 (2026-09-20, 2026-09-21, 2026-09-22, 2026-09-24, 2026-09-25, 2026-09-26, 2026-09-28, 2026-09-29)
- 语种：en=2131, zh=123
- kind：post=2019, project=207, method=25, person=3

## 问题标签汇总

| 问题 | 条数 | 占比 |
|---|---|---|
| 无指标 | 441 | 20% |
| 无项目链接 | 355 | 16% |
| HTML未清理 | 249 | 11% |
| 缺作者 | 233 | 10% |
| 无项目信号 | 139 | 6% |
| 视频无正文 | 114 | 5% |
| 缺发布时间 | 98 | 4% |
| 正文过短(<200) | 72 | 3% |
| 空正文 | 45 | 2% |
| 资源清单/名录 | 38 | 2% |
| Exa截断 | 32 | 1% |
| RSS摘要/残文 | 26 | 1% |
| 大厂产品 | 7 | 0% |
| 发布时间未规范化 | 5 | 0% |
| 泛媒体主题 | 4 | 0% |

## 渠道质量矩阵

| 渠道 | 角色 | 条目 | 可用 | 不可用 | 相关性可疑 | 资源清单 | 大厂 | 摘要残文 | Exa截断 | HTML残留 | 无时间 | 无作者 | 无指标 | 正文中位 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hn_show | 原文=项目发布帖 | 1280 | 1207 | 73 | 0 | 0 | 0 | 20 | 28 | 24 | 0 | 0 | 0 | 3818 |
| reddit | 项目讨论 | 348 | 208 | 31 | 136 | 9 | 5 | 4 | 0 | 0 | 0 | 0 | 0 | 926 |
| producthunt | 项目发布 | 205 | 203 | 0 | 2 | 0 | 2 | 0 | 0 | 205 | 0 | 0 | 205 | 328 |
| betalist | 预发布项目 | 117 | 117 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 117 | 117 | 1796 |
| indiehackers | 项目库 | 86 | 85 | 1 | 0 | 0 | 0 | 1 | 4 | 0 | 86 | 86 | 86 | 2945 |
| github_new | 项目仓库 | 64 | 48 | 1 | 15 | 11 | 0 | 1 | 0 | 19 | 0 | 0 | 0 | 5370 |
| v2ex | 中文讨论 | 58 | 43 | 0 | 15 | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 997 |
| bilibili | 中文视频（仅元数据） | 52 | 50 | 0 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 137 |
| exa_discovery | 全网语义发现 | 25 | 19 | 0 | 6 | 6 | 0 | 0 | 0 | 0 | 5 | 25 | 25 | 2913 |
| devto | 项目复盘文 | 11 | 11 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 10035 |
| c1c7 | 中文名录（含资源/人物） | 7 | 5 | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 7 | 4 | 7 | 216 |
| xiaohongshu | 中文社媒 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 501 |

## 跨渠道重复（同 project_url 出现在多渠道，语料层未合并）

- hn_show, indiehackers, reddit → play.google.com/store/apps/details

## 元数据完整性

- `published_at` 缺失 **98** · 格式未规范化 **5**
- `author` 缺失 **233** · `metrics` 全空 **441**
- `body_format`：markdown=1326, text=928


## 问题样例（人工复核用）

### 无指标（441 条）
- `betalist` Gb7 Meetup
- `betalist` Zapters
- `betalist` 1Presence
- `betalist` Campaignstack

### 无项目链接（355 条）
- `bilibili` 个人独立游戏作品
- `bilibili` 为什么很多程序员都不去做独立开发者？
- `bilibili` 独立开发者一年可以赚多少钱？
- `bilibili` 16岁高一学生正在尝试独立开发galgame（插画和脚本独立完成）但需要BGM支持，有没有会音编的朋友（本人只懂一些钢琴纯音

### HTML未清理（249 条）
- `devto` I Built a Better Codex Pet Than OpenAI Did
- `github_new` Edge0-AI/Edge0
- `github_new` s87343472/backlink-pilot
- `github_new` Gingiris/gingiris-launch

### 缺作者（233 条）
- `betalist` Gb7 Meetup
- `betalist` Zapters
- `betalist` 1Presence
- `betalist` Campaignstack

### 无项目信号（139 条）
- `c1c7` Master of Scale
- `c1c7` Patrick McKenzie (@patio11)
- `c1c7` Pieter Levels (@levelsio)
- `github_new` tamaratran/fast-jev-compaction

### 视频无正文（114 条）
- `bilibili` 独立开发两种赚钱方式！99%的人没想明白！
- `bilibili` 个人独立游戏作品
- `bilibili` 为什么很多程序员都不去做独立开发者？
- `bilibili` 独立开发赚了500W后，我想给你这些建议！

### 缺发布时间（98 条）
- `betalist` Flowmate
- `betalist` Matthew Kellogg
- `betalist` Beteam
- `betalist` Budgetpixel

### 正文过短(<200)（72 条）
- `bilibili` 独立开发两种赚钱方式！99%的人没想明白！
- `bilibili` 个人独立游戏作品
- `bilibili` 为什么很多程序员都不去做独立开发者？
- `bilibili` 独立开发赚了500W后，我想给你这些建议！

### 空正文（45 条）
- `bilibili` 【亲身经历】30+程序员折腾的11年，第二章：独立开发！
- `bilibili` 程序员辞职做独立开发者，靠谱吗？
- `bilibili` 一个老板八个AI虾兵，AI催生一人公司热潮，睿见
- `bilibili` 为什么说接下来会诞生很多“一人公司”？

### 资源清单/名录（38 条）
- `bilibili` 独立开发者省钱之穷鬼套餐，从零开始完整实战，不花一分钱上线完整应用
- `bilibili` S1E9｜2026年普通人还能做一人公司吗？｜油管大神DanKoe｜三小时教程拆解
- `c1c7` Sideidea
- `exa_discovery` Tony Dinh: $45K/mo Indie Hacker Journey

### Exa截断（32 条）
- `hn_show` Show HN: LingBot-World 2.0 (1.3B) running at 16 FPS on one RTX 5090
- `hn_show` Show HN: Omabib, a Zotero alternative for Omarchy with agent support
- `hn_show` Show HN: Talos – A personal agent whose kernel gates every tool call
- `hn_show` Show HN: Proxy-benchmark – is it the proxy, the browser, or your machine?

### RSS摘要/残文（26 条）
- `github_new` huaminghuangtw/Strava-Tool
- `hn_show` Show HN: Koi Editor Alpha
- `hn_show` Show HN: Concat: the open-source CapCut replacement.
- `hn_show` Show HN: Knecht, a tool for building software factories for agencies

### 大厂产品（7 条）
- `producthunt` Google Flow for iOS & Android
- `producthunt` Microsoft Copilot
- `reddit` Google isn't ranking our website despite following basic SEO best practices - wh
- `reddit` Ranked on Google, ChatGPT within 30 days of launch 💪

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
