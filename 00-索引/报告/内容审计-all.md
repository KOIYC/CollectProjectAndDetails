---
type: "report"
title: "内容质量审计 all"
updated: "2026-11-19T09:59:15+08:00"
tags:
  - 索引
  - 审计
  - 内容质量
---

# 语料内容质量审计

> 生成 2026-11-19T09:59:15+08:00 · 审计器 `tools/kb_content_audit.py`

- 唯一条目 **5158** · 可用（无致命缺陷、且相关）**4558** (88%)
- 不可用于深度分析（空/过短/摘要残文）**190** (4%)
- 相关性可疑（无项目信号/资源清单/泛媒体/大厂）**459** (9%)
- 正文长度 中位 **1388.5** · 均值 3864 · 空正文 67 · <200 字符 205
- 历史深度（**内容发布时间轴**，趋势分析看这个）：近 90 天 **4221 条**，更早 730 条，无发布时间 207 条（最早 ['2014-04-04']）
- 采集时间轴：`captured_at` 覆盖 34 天 (2026-09-20, 2026-09-21, 2026-09-22, 2026-09-24, 2026-09-25, 2026-09-26, 2026-09-28, 2026-09-29, 2026-09-30, 2026-10-01, 2026-10-10, 2026-10-11, 2026-10-16, 2026-10-17, 2026-10-22, 2026-10-25, 2026-10-26, 2026-10-27, 2026-10-28, 2026-10-29, 2026-10-30, 2026-11-01, 2026-11-02, 2026-11-03, 2026-11-04, 2026-11-05, 2026-11-07, 2026-11-08, 2026-11-09, 2026-11-10, 2026-11-11, 2026-11-16, 2026-11-17, 2026-11-19)
- 语种：en=4722, zh=436
- kind：post=4544, project=557, method=54, person=3

## 问题标签汇总

| 问题 | 条数 | 占比 |
|---|---|---|
| 无指标 | 1428 | 28% |
| HTML未清理 | 911 | 18% |
| 无项目链接 | 867 | 17% |
| 缺作者 | 612 | 12% |
| 无项目信号 | 317 | 6% |
| 视频无正文 | 242 | 5% |
| 缺发布时间 | 207 | 4% |
| 正文过短(<200) | 138 | 3% |
| 资源清单/名录 | 126 | 2% |
| 空正文 | 67 | 1% |
| Exa截断 | 48 | 1% |
| RSS摘要/残文 | 47 | 1% |
| 大厂产品 | 32 | 1% |
| 泛媒体主题 | 19 | 0% |
| 发布时间未规范化 | 5 | 0% |

## 渠道质量矩阵

| 渠道 | 角色 | 条目 | 可用 | 不可用 | 相关性可疑 | 资源清单 | 大厂 | 摘要残文 | Exa截断 | HTML残留 | 无时间 | 无作者 | 无指标 | 正文中位 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hn_show | 原文=项目发布帖 | 2307 | 2192 | 115 | 0 | 0 | 0 | 37 | 42 | 44 | 0 | 0 | 0 | 3246 |
| reddit | 项目讨论 | 863 | 540 | 70 | 302 | 26 | 14 | 5 | 0 | 0 | 0 | 0 | 0 | 828 |
| producthunt | 项目发布 | 813 | 806 | 0 | 7 | 0 | 7 | 0 | 0 | 813 | 0 | 0 | 813 | 327 |
| betalist | 预发布项目 | 358 | 357 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 4 | 358 | 358 | 2127 |
| v2ex | 中文讨论 | 332 | 237 | 0 | 95 | 65 | 9 | 0 | 0 | 5 | 0 | 0 | 0 | 1234 |
| indiehackers | 项目库 | 195 | 193 | 2 | 0 | 0 | 0 | 2 | 5 | 0 | 195 | 195 | 195 | 2931 |
| github_new | 项目仓库 | 105 | 74 | 3 | 28 | 18 | 1 | 3 | 0 | 46 | 0 | 0 | 0 | 8550 |
| bilibili | 中文视频（仅元数据） | 89 | 82 | 0 | 7 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 137 |
| exa_discovery | 全网语义发现 | 54 | 45 | 0 | 9 | 9 | 0 | 0 | 0 | 0 | 5 | 54 | 54 | 2560 |
| devto | 项目复盘文 | 34 | 27 | 0 | 7 | 3 | 0 | 0 | 1 | 3 | 0 | 0 | 0 | 9845 |
| c1c7 | 中文名录（含资源/人物） | 7 | 5 | 0 | 2 | 2 | 0 | 0 | 0 | 0 | 7 | 4 | 7 | 218 |
| xiaohongshu | 中文社媒 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 496 |

## 跨渠道重复（同 project_url 出现在多渠道，语料层未合并）

- hn_show, indiehackers, reddit, v2ex → play.google.com/store/apps/details
- hn_show, reddit → github.com/sshah03/recalc

## 元数据完整性

- `published_at` 缺失 **207** · 格式未规范化 **5**
- `author` 缺失 **612** · `metrics` 全空 **1428**
- `body_format`：text=2783, markdown=2375


## 问题样例（人工复核用）

### 无指标（1428 条）
- `betalist` Gb7 Meetup
- `betalist` Zapters
- `betalist` 1Presence
- `betalist` Campaignstack

### HTML未清理（911 条）
- `devto` I Built a Better Codex Pet Than OpenAI Did
- `devto` Why you still need a Website Portfolio, even though everyone can Vibe Code it.
- `devto` I Turned My GitHub Profile Into a Cyberpunk Console With a City Built From My Co
- `github_new` Edge0-AI/Edge0

### 无项目链接（867 条）
- `bilibili` 个人独立游戏作品
- `bilibili` 为什么很多程序员都不去做独立开发者？
- `bilibili` 独立开发者一年可以赚多少钱？
- `bilibili` 16岁高一学生正在尝试独立开发galgame（插画和脚本独立完成）但需要BGM支持，有没有会音编的朋友（本人只懂一些钢琴纯音

### 缺作者（612 条）
- `betalist` Gb7 Meetup
- `betalist` Zapters
- `betalist` 1Presence
- `betalist` Campaignstack

### 无项目信号（317 条）
- `bilibili` 【Lee哥】做了10年Unity后，他说AI已经超过很多程序员了 | 游戏开发 | 案例分析
- `bilibili` 游戏开发者如何造出诺奖 AI
- `bilibili` 耗时7天，我用K3.1攻克了3D游戏开发最深的无人区【B站AI创造公开赛】
- `bilibili` 27岁失业，参加了政府组织的游戏开发培训

### 视频无正文（242 条）
- `bilibili` 独立开发两种赚钱方式！99%的人没想明白！
- `bilibili` 个人独立游戏作品
- `bilibili` 为什么很多程序员都不去做独立开发者？
- `bilibili` 独立开发赚了500W后，我想给你这些建议！

### 缺发布时间（207 条）
- `betalist` Flowmate
- `betalist` Matthew Kellogg
- `betalist` Beteam
- `betalist` Budgetpixel

### 正文过短(<200)（138 条）
- `bilibili` 独立开发两种赚钱方式！99%的人没想明白！
- `bilibili` 个人独立游戏作品
- `bilibili` 为什么很多程序员都不去做独立开发者？
- `bilibili` 独立开发赚了500W后，我想给你这些建议！

### 资源清单/名录（126 条）
- `bilibili` 独立开发者省钱之穷鬼套餐，从零开始完整实战，不花一分钱上线完整应用
- `bilibili` S1E9｜2026年普通人还能做一人公司吗？｜油管大神DanKoe｜三小时教程拆解
- `bilibili` 【视频播客】裁员潮下，互联网人该不该做独立开发？
- `c1c7` Sideidea

### 空正文（67 条）
- `bilibili` 【亲身经历】30+程序员折腾的11年，第二章：独立开发！
- `bilibili` 程序员辞职做独立开发者，靠谱吗？
- `bilibili` 一个老板八个AI虾兵，AI催生一人公司热潮，睿见
- `bilibili` 为什么说接下来会诞生很多“一人公司”？

### Exa截断（48 条）
- `devto` Promise Delivered: Welcome to the DEV Hall of Fame (65 Authors, 65 Masterpieces)
- `hn_show` Show HN: LingBot-World 2.0 (1.3B) running at 16 FPS on one RTX 5090
- `hn_show` Show HN: Omabib, a Zotero alternative for Omarchy with agent support
- `hn_show` Show HN: Talos – A personal agent whose kernel gates every tool call

### RSS摘要/残文（47 条）
- `github_new` huaminghuangtw/Strava-Tool
- `github_new` huamidev/GestaltX
- `github_new` huami1314/GestaltX
- `hn_show` Show HN: Koi Editor Alpha

### 大厂产品（32 条）
- `betalist` Convert Pdf To Google Sheets
- `github_new` openai/math
- `producthunt` Playground by Google Labs
- `producthunt` Microsoft Copilot

### 泛媒体主题（19 条）
- `github_new` Zagitta/gpu-unlock
- `reddit` Started this viking survival game at 15, I'm 24 now
- `reddit` Hardware advise request
- `reddit` Jellyfin Remote Access with Whitelisted Dynamic IPs

### 发布时间未规范化（5 条）
- `exa_discovery` 一年上线超 10 款产品，AI 时代如何做独立开发 - InfoQ
- `exa_discovery` 《独立开发者的出海之道》
- `exa_discovery` 独立开发者做APP出海,最缺的其实不是代码-夜雨聆风
- `exa_discovery` TelAve News - Solo Indie Developer Launches Not Pink, a Couples App Built Around
