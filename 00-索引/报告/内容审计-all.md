---
type: "report"
title: "内容质量审计 all"
updated: "2026-10-29T21:06:14+08:00"
tags:
  - 索引
  - 审计
  - 内容质量
---

# 语料内容质量审计

> 生成 2026-10-29T21:06:14+08:00 · 审计器 `tools/kb_content_audit.py`

- 唯一条目 **3608** · 可用（无致命缺陷、且相关）**3193** (88%)
- 不可用于深度分析（空/过短/摘要残文）**153** (4%)
- 相关性可疑（无项目信号/资源清单/泛媒体/大厂）**301** (8%)
- 正文长度 中位 **1595.0** · 均值 4136 · 空正文 58 · <200 字符 163
- 历史深度（**内容发布时间轴**，趋势分析看这个）：近 90 天 **2796 条**，更早 639 条，无发布时间 173 条（最早 ['2014-04-04']）
- 采集时间轴：`captured_at` 覆盖 20 天 (2026-09-20, 2026-09-21, 2026-09-22, 2026-09-24, 2026-09-25, 2026-09-26, 2026-09-28, 2026-09-29, 2026-09-30, 2026-10-01, 2026-10-10, 2026-10-11, 2026-10-16, 2026-10-17, 2026-10-22, 2026-10-25, 2026-10-26, 2026-10-27, 2026-10-28, 2026-10-29)
- 语种：en=3336, zh=272
- kind：post=3156, project=410, method=39, person=3

## 问题标签汇总

| 问题 | 条数 | 占比 |
|---|---|---|
| 无指标 | 937 | 26% |
| 无项目链接 | 566 | 16% |
| HTML未清理 | 560 | 16% |
| 缺作者 | 450 | 12% |
| 无项目信号 | 209 | 6% |
| 视频无正文 | 178 | 5% |
| 缺发布时间 | 173 | 5% |
| 正文过短(<200) | 105 | 3% |
| 资源清单/名录 | 81 | 2% |
| 空正文 | 58 | 2% |
| Exa截断 | 41 | 1% |
| RSS摘要/残文 | 39 | 1% |
| 大厂产品 | 18 | 0% |
| 泛媒体主题 | 10 | 0% |
| 发布时间未规范化 | 5 | 0% |

## 渠道质量矩阵

| 渠道 | 角色 | 条目 | 可用 | 不可用 | 相关性可疑 | 资源清单 | 大厂 | 摘要残文 | Exa截断 | HTML残留 | 无时间 | 无作者 | 无指标 | 正文中位 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hn_show | 原文=项目发布帖 | 1747 | 1652 | 95 | 0 | 0 | 0 | 30 | 36 | 33 | 0 | 0 | 0 | 3459 |
| reddit | 项目讨论 | 556 | 345 | 53 | 197 | 14 | 8 | 4 | 0 | 0 | 0 | 0 | 0 | 835 |
| producthunt | 项目发布 | 484 | 479 | 0 | 5 | 0 | 5 | 0 | 0 | 484 | 0 | 0 | 484 | 327 |
| betalist | 预发布项目 | 245 | 244 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 4 | 245 | 245 | 1914 |
| v2ex | 中文讨论 | 185 | 131 | 0 | 54 | 38 | 3 | 0 | 0 | 3 | 0 | 0 | 0 | 1251 |
| indiehackers | 项目库 | 161 | 157 | 4 | 0 | 0 | 0 | 4 | 4 | 0 | 161 | 161 | 161 | 2915 |
| github_new | 项目仓库 | 86 | 62 | 1 | 23 | 16 | 1 | 1 | 0 | 37 | 0 | 0 | 0 | 7324 |
| bilibili | 中文视频（仅元数据） | 73 | 69 | 0 | 4 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 139 |
| exa_discovery | 全网语义发现 | 39 | 31 | 0 | 8 | 8 | 0 | 0 | 0 | 0 | 5 | 39 | 39 | 2560 |
| devto | 项目复盘文 | 24 | 18 | 0 | 6 | 2 | 0 | 0 | 1 | 3 | 0 | 0 | 0 | 9845 |
| c1c7 | 中文名录（含资源/人物） | 7 | 4 | 0 | 3 | 1 | 0 | 0 | 0 | 0 | 7 | 4 | 7 | 216 |
| xiaohongshu | 中文社媒 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 502 |

## 跨渠道重复（同 project_url 出现在多渠道，语料层未合并）

- hn_show, indiehackers, reddit → play.google.com/store/apps/details

## 元数据完整性

- `published_at` 缺失 **173** · 格式未规范化 **5**
- `author` 缺失 **450** · `metrics` 全空 **937**
- `body_format`：markdown=1849, text=1759


## 问题样例（人工复核用）

### 无指标（937 条）
- `betalist` Gb7 Meetup
- `betalist` Zapters
- `betalist` 1Presence
- `betalist` Campaignstack

### 无项目链接（566 条）
- `bilibili` 个人独立游戏作品
- `bilibili` 为什么很多程序员都不去做独立开发者？
- `bilibili` 独立开发者一年可以赚多少钱？
- `bilibili` 16岁高一学生正在尝试独立开发galgame（插画和脚本独立完成）但需要BGM支持，有没有会音编的朋友（本人只懂一些钢琴纯音

### HTML未清理（560 条）
- `devto` I Built a Better Codex Pet Than OpenAI Did
- `devto` Why you still need a Website Portfolio, even though everyone can Vibe Code it.
- `devto` I Turned My GitHub Profile Into a Cyberpunk Console With a City Built From My Co
- `github_new` Edge0-AI/Edge0

### 缺作者（450 条）
- `betalist` Gb7 Meetup
- `betalist` Zapters
- `betalist` 1Presence
- `betalist` Campaignstack

### 无项目信号（209 条）
- `bilibili` 【Lee哥】做了10年Unity后，他说AI已经超过很多程序员了 | 游戏开发 | 案例分析
- `bilibili` 游戏开发者如何造出诺奖 AI
- `c1c7` Master of Scale
- `c1c7` v2ex 论坛 - 分享创造板块

### 视频无正文（178 条）
- `bilibili` 独立开发两种赚钱方式！99%的人没想明白！
- `bilibili` 个人独立游戏作品
- `bilibili` 为什么很多程序员都不去做独立开发者？
- `bilibili` 独立开发赚了500W后，我想给你这些建议！

### 缺发布时间（173 条）
- `betalist` Flowmate
- `betalist` Matthew Kellogg
- `betalist` Beteam
- `betalist` Budgetpixel

### 正文过短(<200)（105 条）
- `bilibili` 独立开发两种赚钱方式！99%的人没想明白！
- `bilibili` 个人独立游戏作品
- `bilibili` 为什么很多程序员都不去做独立开发者？
- `bilibili` 独立开发赚了500W后，我想给你这些建议！

### 资源清单/名录（81 条）
- `bilibili` 独立开发者省钱之穷鬼套餐，从零开始完整实战，不花一分钱上线完整应用
- `bilibili` S1E9｜2026年普通人还能做一人公司吗？｜油管大神DanKoe｜三小时教程拆解
- `c1c7` Sideidea
- `devto` Why you still need a Website Portfolio, even though everyone can Vibe Code it.

### 空正文（58 条）
- `bilibili` 【亲身经历】30+程序员折腾的11年，第二章：独立开发！
- `bilibili` 程序员辞职做独立开发者，靠谱吗？
- `bilibili` 一个老板八个AI虾兵，AI催生一人公司热潮，睿见
- `bilibili` 为什么说接下来会诞生很多“一人公司”？

### Exa截断（41 条）
- `devto` Promise Delivered: Welcome to the DEV Hall of Fame (65 Authors, 65 Masterpieces)
- `hn_show` Show HN: LingBot-World 2.0 (1.3B) running at 16 FPS on one RTX 5090
- `hn_show` Show HN: Omabib, a Zotero alternative for Omarchy with agent support
- `hn_show` Show HN: Talos – A personal agent whose kernel gates every tool call

### RSS摘要/残文（39 条）
- `github_new` huaminghuangtw/Strava-Tool
- `hn_show` Show HN: Koi Editor Alpha
- `hn_show` Show HN: Concat: the open-source CapCut replacement.
- `hn_show` Show HN: Knecht, a tool for building software factories for agencies

### 大厂产品（18 条）
- `betalist` Convert Pdf To Google Sheets
- `github_new` openai/math
- `producthunt` Gemini Agent for Google Cloud
- `producthunt` Playground by Google Labs

### 泛媒体主题（10 条）
- `github_new` Zagitta/gpu-unlock
- `reddit` Started this viking survival game at 15, I'm 24 now
- `reddit` Hardware advise request
- `reddit` Jellyfin Remote Access with Whitelisted Dynamic IPs

### 发布时间未规范化（5 条）
- `exa_discovery` 一年上线超 10 款产品，AI 时代如何做独立开发 - InfoQ
- `exa_discovery` 《独立开发者的出海之道》
- `exa_discovery` 独立开发者做APP出海,最缺的其实不是代码-夜雨聆风
- `exa_discovery` TelAve News - Solo Indie Developer Launches Not Pink, a Couples App Built Around
