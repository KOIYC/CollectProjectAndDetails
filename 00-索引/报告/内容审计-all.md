---
type: "report"
title: "内容质量审计 all"
updated: "2026-09-20T15:27:39+08:00"
tags:
  - 索引
  - 审计
  - 内容质量
---

# 语料内容质量审计

> 生成 2026-09-20T15:27:39+08:00 · 审计器 `tools/kb_content_audit.py`

- 唯一条目 **713** · 可用（无致命缺陷、且相关）**622** (87%)
- 不可用于深度分析（空/过短/摘要残文）**46** (6%)
- 相关性可疑（无项目信号/资源清单/泛媒体/大厂）**56** (8%)
- 正文长度 中位 **1845** · 均值 4744 · 空正文 20 · <200 字符 52
- 历史深度（**内容发布时间轴**，趋势分析看这个）：近 90 天 **597 条**，更早 63 条，无发布时间 53 条（最早 ['2014-04-04']）
- 采集时间轴：`captured_at` 覆盖 1 天 (2026-09-20)
- 语种：en=663, zh=50
- kind：post=651, project=50, method=9, person=3

## 问题标签汇总

| 问题 | 条数 | 占比 |
|---|---|---|
| 无指标 | 111 | 16% |
| 无项目链接 | 106 | 15% |
| HTML未清理 | 69 | 10% |
| 缺作者 | 59 | 8% |
| 缺发布时间 | 53 | 7% |
| 无项目信号 | 41 | 6% |
| 视频无正文 | 39 | 5% |
| 正文过短(<200) | 32 | 4% |
| 空正文 | 20 | 3% |
| 资源清单/名录 | 18 | 3% |
| Exa截断 | 14 | 2% |
| RSS摘要/残文 | 9 | 1% |
| 泛媒体主题 | 2 | 0% |
| 大厂产品 | 1 | 0% |

## 渠道质量矩阵

| 渠道 | 角色 | 条目 | 可用 | 不可用 | 相关性可疑 | 资源清单 | 大厂 | 摘要残文 | Exa截断 | HTML残留 | 无时间 | 无作者 | 无指标 | 正文中位 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hn_show | 原文=项目发布帖 | 400 | 372 | 28 | 0 | 0 | 0 | 3 | 12 | 2 | 0 | 0 | 0 | 3967 |
| reddit | 项目讨论 | 94 | 60 | 9 | 31 | 3 | 1 | 2 | 0 | 0 | 0 | 0 | 0 | 879 |
| github_new | 项目仓库 | 60 | 40 | 9 | 16 | 9 | 0 | 4 | 0 | 18 | 0 | 0 | 0 | 4598 |
| producthunt | 项目发布 | 49 | 49 | 0 | 0 | 0 | 0 | 0 | 0 | 49 | 0 | 0 | 49 | 329 |
| v2ex | 中文讨论 | 24 | 20 | 0 | 4 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1137 |
| betalist | 预发布项目 | 23 | 23 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 23 | 23 | 23 | 706 |
| indiehackers | 项目库 | 23 | 23 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 23 | 23 | 23 | 1696 |
| bilibili | 中文视频（仅元数据） | 19 | 18 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 89 |
| exa_discovery | 全网语义发现 | 9 | 8 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 9 | 9 | 2998 |
| c1c7 | 中文名录（含资源/人物） | 7 | 6 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 7 | 4 | 7 | 265 |
| devto | 项目复盘文 | 5 | 3 | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6574 |

## 元数据完整性

- `published_at` 缺失 **53** · 格式未规范化 **0**
- `author` 缺失 **59** · `metrics` 全空 **111**
- `body_format`：markdown=469, text=244


## 问题样例（人工复核用）

### 无指标（111 条）
- `betalist` Gb7 Meetup
- `betalist` Zapters
- `betalist` 1Presence
- `betalist` Campaignstack

### 无项目链接（106 条）
- `bilibili` 个人独立游戏作品
- `bilibili` 为什么很多程序员都不去做独立开发者？
- `bilibili` 独立开发者一年可以赚多少钱？
- `bilibili` 16岁高一学生正在尝试独立开发galgame（插画和脚本独立完成）但需要BGM支持，有没有会音编的朋友（本人只懂一些钢琴纯音

### HTML未清理（69 条）
- `github_new` eternity4719/HowToLiveBetter
- `github_new` Edge0-AI/Edge0
- `github_new` s87343472/backlink-pilot
- `github_new` Gingiris/gingiris-launch

### 缺作者（59 条）
- `betalist` Gb7 Meetup
- `betalist` Zapters
- `betalist` 1Presence
- `betalist` Campaignstack

### 缺发布时间（53 条）
- `betalist` Gb7 Meetup
- `betalist` Zapters
- `betalist` 1Presence
- `betalist` Campaignstack

### 无项目信号（41 条）
- `c1c7` v2ex 论坛 - 分享创造板块
- `c1c7` Patrick McKenzie (@patio11)
- `c1c7` Pieter Levels (@levelsio)
- `devto` Show Me the Article You're Most Proud Of And I'll Read Every Single One of Them

### 视频无正文（39 条）
- `bilibili` 独立开发两种赚钱方式！99%的人没想明白！
- `bilibili` 个人独立游戏作品
- `bilibili` 为什么很多程序员都不去做独立开发者？
- `bilibili` 独立开发赚了500W后，我想给你这些建议！

### 正文过短(<200)（32 条）
- `bilibili` 独立开发两种赚钱方式！99%的人没想明白！
- `bilibili` 个人独立游戏作品
- `bilibili` 为什么很多程序员都不去做独立开发者？
- `bilibili` 独立开发赚了500W后，我想给你这些建议！

### 空正文（20 条）
- `bilibili` 【亲身经历】30+程序员折腾的11年，第二章：独立开发！
- `bilibili` 程序员辞职做独立开发者，靠谱吗？
- `c1c7` Patrick McKenzie (@patio11)
- `hn_show` Show HN: Keydris, Sudo for AI Agents

### 资源清单/名录（18 条）
- `bilibili` 独立开发者省钱之穷鬼套餐，从零开始完整实战，不花一分钱上线完整应用
- `devto` The Internship That Taught Me to Read Between the Lines of a Job Offer
- `exa_discovery` Tony Dinh: $45K/mo Indie Hacker Journey
- `github_new` eternity4719/HowToLiveBetter

### Exa截断（14 条）
- `hn_show` Show HN: LingBot-World 2.0 (1.3B) running at 16 FPS on one RTX 5090
- `hn_show` Show HN: Koi Editor Alpha
- `hn_show` Show HN: Omabib, a Zotero alternative for Omarchy with agent support
- `hn_show` Show HN: Talos – A personal agent whose kernel gates every tool call

### RSS摘要/残文（9 条）
- `github_new` eternity4719/HowToLiveBetter
- `github_new` TowhidKashem/snapchat-clone
- `github_new` yynxxxxx/gpt_sub_analysis
- `github_new` huaminghuangtw/Strava-Tool

### 泛媒体主题（2 条）
- `reddit` Started this viking survival game at 15, I'm 24 now
- `v2ex` RED 实战：用 AI 把一个想法做成能用的 DSH 插件

### 大厂产品（1 条）
- `reddit` Google isn't ranking our website despite following basic SEO best practices - wh
