---
type: "report"
title: "内容质量审计 all"
updated: "2026-10-26T09:57:33+08:00"
tags:
  - 索引
  - 审计
  - 内容质量
---

# 语料内容质量审计

> 生成 2026-10-26T09:57:33+08:00 · 审计器 `tools/kb_content_audit.py`

- 唯一条目 **3279** · 可用（无致命缺陷、且相关）**2904** (89%)
- 不可用于深度分析（空/过短/摘要残文）**135** (4%)
- 相关性可疑（无项目信号/资源清单/泛媒体/大厂）**274** (8%)
- 正文长度 中位 **1674** · 均值 4239 · 空正文 54 · <200 字符 147
- 历史深度（**内容发布时间轴**，趋势分析看这个）：近 90 天 **2543 条**，更早 569 条，无发布时间 167 条（最早 ['2014-04-04']）
- 采集时间轴：`captured_at` 覆盖 17 天 (2026-09-20, 2026-09-21, 2026-09-22, 2026-09-24, 2026-09-25, 2026-09-26, 2026-09-28, 2026-09-29, 2026-09-30, 2026-10-01, 2026-10-10, 2026-10-11, 2026-10-16, 2026-10-17, 2026-10-22, 2026-10-25, 2026-10-26)
- 语种：en=3048, zh=231
- kind：post=2866, project=371, method=39, person=3

## 问题标签汇总

| 问题 | 条数 | 占比 |
|---|---|---|
| 无指标 | 835 | 25% |
| 无项目链接 | 507 | 15% |
| HTML未清理 | 490 | 15% |
| 缺作者 | 411 | 13% |
| 无项目信号 | 190 | 6% |
| 缺发布时间 | 167 | 5% |
| 视频无正文 | 163 | 5% |
| 正文过短(<200) | 93 | 3% |
| 资源清单/名录 | 74 | 2% |
| 空正文 | 54 | 2% |
| Exa截断 | 41 | 1% |
| RSS摘要/残文 | 35 | 1% |
| 大厂产品 | 16 | 0% |
| 泛媒体主题 | 8 | 0% |
| 发布时间未规范化 | 5 | 0% |

## 渠道质量矩阵

| 渠道 | 角色 | 条目 | 可用 | 不可用 | 相关性可疑 | 资源清单 | 大厂 | 摘要残文 | Exa截断 | HTML残留 | 无时间 | 无作者 | 无指标 | 正文中位 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hn_show | 原文=项目发布帖 | 1627 | 1542 | 85 | 0 | 0 | 0 | 26 | 36 | 28 | 0 | 0 | 0 | 3498 |
| reddit | 项目讨论 | 492 | 297 | 45 | 184 | 14 | 7 | 4 | 0 | 0 | 0 | 0 | 0 | 835 |
| producthunt | 项目发布 | 421 | 415 | 0 | 6 | 0 | 6 | 0 | 0 | 421 | 0 | 0 | 421 | 328 |
| betalist | 预发布项目 | 212 | 212 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 212 | 212 | 1887 |
| indiehackers | 项目库 | 155 | 151 | 4 | 0 | 0 | 0 | 4 | 4 | 0 | 155 | 155 | 155 | 2852 |
| v2ex | 中文讨论 | 148 | 107 | 0 | 41 | 31 | 2 | 0 | 0 | 1 | 0 | 0 | 0 | 1213 |
| github_new | 项目仓库 | 86 | 62 | 1 | 23 | 16 | 1 | 1 | 0 | 37 | 0 | 0 | 0 | 7324 |
| bilibili | 中文视频（仅元数据） | 69 | 65 | 0 | 4 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 137 |
| exa_discovery | 全网语义发现 | 39 | 31 | 0 | 8 | 8 | 0 | 0 | 0 | 0 | 5 | 39 | 39 | 2560 |
| devto | 项目复盘文 | 22 | 17 | 0 | 5 | 2 | 0 | 0 | 1 | 3 | 0 | 0 | 0 | 10035 |
| c1c7 | 中文名录（含资源/人物） | 7 | 5 | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 7 | 4 | 7 | 216 |
| xiaohongshu | 中文社媒 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 489 |

## 跨渠道重复（同 project_url 出现在多渠道，语料层未合并）

- hn_show, indiehackers, reddit → play.google.com/store/apps/details

## 元数据完整性

- `published_at` 缺失 **167** · 格式未规范化 **5**
- `author` 缺失 **411** · `metrics` 全空 **835**
- `body_format`：markdown=1730, text=1549


## 问题样例（人工复核用）

### 无指标（835 条）
- `betalist` Gb7 Meetup
- `betalist` Zapters
- `betalist` 1Presence
- `betalist` Campaignstack

### 无项目链接（507 条）
- `bilibili` 个人独立游戏作品
- `bilibili` 为什么很多程序员都不去做独立开发者？
- `bilibili` 独立开发者一年可以赚多少钱？
- `bilibili` 16岁高一学生正在尝试独立开发galgame（插画和脚本独立完成）但需要BGM支持，有没有会音编的朋友（本人只懂一些钢琴纯音

### HTML未清理（490 条）
- `devto` I Built a Better Codex Pet Than OpenAI Did
- `devto` Why you still need a Website Portfolio, even though everyone can Vibe Code it.
- `devto` I Turned My GitHub Profile Into a Cyberpunk Console With a City Built From My Co
- `github_new` Edge0-AI/Edge0

### 缺作者（411 条）
- `betalist` Gb7 Meetup
- `betalist` Zapters
- `betalist` 1Presence
- `betalist` Campaignstack

### 无项目信号（190 条）
- `bilibili` 【Lee哥】做了10年Unity后，他说AI已经超过很多程序员了 | 游戏开发 | 案例分析
- `bilibili` 游戏开发者如何造出诺奖 AI
- `c1c7` Master of Scale
- `c1c7` Patrick McKenzie (@patio11)

### 缺发布时间（167 条）
- `betalist` Flowmate
- `betalist` Matthew Kellogg
- `betalist` Beteam
- `betalist` Budgetpixel

### 视频无正文（163 条）
- `bilibili` 独立开发两种赚钱方式！99%的人没想明白！
- `bilibili` 个人独立游戏作品
- `bilibili` 为什么很多程序员都不去做独立开发者？
- `bilibili` 独立开发赚了500W后，我想给你这些建议！

### 正文过短(<200)（93 条）
- `bilibili` 独立开发两种赚钱方式！99%的人没想明白！
- `bilibili` 个人独立游戏作品
- `bilibili` 为什么很多程序员都不去做独立开发者？
- `bilibili` 独立开发赚了500W后，我想给你这些建议！

### 资源清单/名录（74 条）
- `bilibili` 独立开发者省钱之穷鬼套餐，从零开始完整实战，不花一分钱上线完整应用
- `bilibili` S1E9｜2026年普通人还能做一人公司吗？｜油管大神DanKoe｜三小时教程拆解
- `c1c7` Sideidea
- `devto` Why you still need a Website Portfolio, even though everyone can Vibe Code it.

### 空正文（54 条）
- `bilibili` 【亲身经历】30+程序员折腾的11年，第二章：独立开发！
- `bilibili` 程序员辞职做独立开发者，靠谱吗？
- `bilibili` 一个老板八个AI虾兵，AI催生一人公司热潮，睿见
- `bilibili` 为什么说接下来会诞生很多“一人公司”？

### Exa截断（41 条）
- `devto` Promise Delivered: Welcome to the DEV Hall of Fame (65 Authors, 65 Masterpieces)
- `hn_show` Show HN: LingBot-World 2.0 (1.3B) running at 16 FPS on one RTX 5090
- `hn_show` Show HN: Omabib, a Zotero alternative for Omarchy with agent support
- `hn_show` Show HN: Talos – A personal agent whose kernel gates every tool call

### RSS摘要/残文（35 条）
- `github_new` huaminghuangtw/Strava-Tool
- `hn_show` Show HN: Koi Editor Alpha
- `hn_show` Show HN: Concat: the open-source CapCut replacement.
- `hn_show` Show HN: Knecht, a tool for building software factories for agencies

### 大厂产品（16 条）
- `github_new` openai/math
- `producthunt` Gemini Agent for Google Cloud
- `producthunt` Playground by Google Labs
- `producthunt` Microsoft Copilot

### 泛媒体主题（8 条）
- `github_new` Zagitta/gpu-unlock
- `reddit` Started this viking survival game at 15, I'm 24 now
- `reddit` Hardware advise request
- `reddit` Jellyfin Remote Access with Whitelisted Dynamic IPs

### 发布时间未规范化（5 条）
- `exa_discovery` 一年上线超 10 款产品，AI 时代如何做独立开发 - InfoQ
- `exa_discovery` 《独立开发者的出海之道》
- `exa_discovery` 独立开发者做APP出海,最缺的其实不是代码-夜雨聆风
- `exa_discovery` TelAve News - Solo Indie Developer Launches Not Pink, a Couples App Built Around
