---
type: "corpus"
item_id: "3286b5ffb0ad7ab4"
title: "Tomato Ritual (番茄仪式) v1.3.0：专为 Mac 雕琢的原生番茄钟，新增 52 周专注热力图、离线柴火溪流声与护眼幕布（楼内送码）"
source: "v2ex"
source_name: "V2EX"
url: "https://www.v2ex.com/t/1252143"
project_url: "https://apps.apple.com/app/apple-store/id6811364084?pt=119695882&ct=v2ex_v130&mt=8"
author: "jasun"
published_at: "2026-10-27T02:28:37"
captured_at: "2026-10-27T23:56:38+08:00"
lang: "zh"
kind: "post"
topic: "开发者工具"
shard: "2026-10-27"
pub_day: "2026-10-27"
tags:
  - 语料
  - v2ex
  - 17
metrics: {"replies": 0}
comments_count: 0
comments_total: 0
discovered_via: "v2ex:独立开发"
---

# Tomato Ritual (番茄仪式) v1.3.0：专为 Mac 雕琢的原生番茄钟，新增 52 周专注热力图、离线柴火溪流声与护眼幕布（楼内送码）

> [!info] 一句话导读
> 大家好，我是 Tomato Ritual （番茄仪式）的独立开发者。

> [!meta]- 语料信息（点开展开）
> 来源：V2EX（post）
> 原帖：<https://www.v2ex.com/t/1252143>
> 指标：回复=0
> 作者：jasun　|　发布：2026-10-27T02:28:37
> 项目链接：<https://apps.apple.com/app/apple-store/id6811364084?pt=119695882&ct=v2ex_v130&mt=8>
> 采集：2026-10-27T23:56:38+08:00　|　id：`3286b5ffb0ad7ab4`

## 正文

大家好，我是 Tomato Ritual （番茄仪式）的独立开发者。

一个月前，我在 V 站分享了这款完全基于原生 Swift / SwiftUI 打造的 macOS 番茄钟。收到很多 V 友的中肯建议，大家对「多屏全屏毛玻璃休息幕布」和「离岗不跑秒的智能接力」反响热烈。

经过这个月的深度迭代，**Tomato Ritual v1.3.0 已经在 Mac App Store 正式发布**！这次版本几乎重构了视觉统计与声音管线，带来了几个我个人非常喜欢、也极其适合程序员深度工作的新特性：

---

### 🌟 v1.3.0 核心更新亮点

#### 1. 🔥 全年 52 周专注热力图与连击成就 (52-Week Heatmap & Streaks)
作为习惯了 GitHub 绿格子的开发者，总希望自己的专注时间也能被优雅地可视化记录：
- **完整年报 vs 近期卡片**：支持在「近 6 周」卡片与「全年 52 周」年报视图之间一键丝滑切换；
- **横向弹性滚动**：52 周网格支持触控板横向弹性滚动，并自动智能对齐至当前周；
- **全周期数据联动**：热力图与上方的劳逸汇总卡、下方的任务分解直方图完全联动，彻底消除了统计脱节；
- **成就胶囊条**：实时展示当前连续打卡天数 (Current Streak)、历史最长连击 (Longest Streak)、单日最高完成记录等。

#### 2. 🎧 纯算法实时合成自然氛围音 (6 Procedural Soundscapes)
许多番茄钟要么外挂庞大的 MP3 音频包，要么需要联网加载。我们在原有白噪音/雨声基础上，新增了 3 款大自然氛围音：
- **温暖柴火 (Warm Campfire)**：低频温暖共鸣 + 算法偶发木柴爆裂微脉冲 (Organic Pops & Crackles)；
- **山涧溪流 (Forest Stream)**：立体声相位差水流带通滤波，仿佛置身林间溪畔；
- **潮汐海浪 (Ocean Waves)**：3 秒平滑周期潮涌包络，与深呼吸自然同频；
- **100% 纯本地离线**：运行时由 `AVAudioEngine` 纯数学滤波器实时生成，应用体积依然极其轻巧（不到 10MB ），零外部音频依赖，零网络请求。

#### 3. 🌿 4 种护眼全屏幕布主题与正念引言 (Mindful Rest Ritual)
休息是番茄工作法的另一半灵魂：
- **4 款专属护眼氛围色**：经典暗黑毛玻璃 (Classic Frost)、暖琥珀护眼 (Amber Warmth ，夜间码字首选)、沉静森林绿 (Forest Sage)、深邃暗夜 (Deep Midnight)；
- **正念引言轮播**：中英双语提示，带你实践 20-20-20 眺望远方护眼法则、腹式呼吸与肩颈放松指引；
- **依然是无感退出**：任何紧急情况，按下 `Esc` 键瞬间即可收起幕布，绝不死锁屏幕。

#### 4. ⚡️ 继续坚守原生体验与零隐私索取
- **原生 Shortcuts & AppIntents 联动**：支持系统快捷指令，可联动系统「专注模式 (Focus Filter)」，一键联动 Raycast / Alfred ；
- **极简画中画 & 菜单栏进度**：菜单栏微环动效，或 230×132 置顶迷你小窗；
- **100% 本地沙盒**：严格遵循 Apple App Sandbox ，零联网权限（应用沙盒内不包含任何出站网络 entitlement ），零第三方 SDK ，所有数据只存你自己的 Mac 。

---

### 🎁 V 友福利：楼内留言赠送 App Store 兑换码（ Promo Code ）

Tomato Ritual 采用**一次性买断制（¥28 / $3.99 ）**，无任何订阅，包含所有后续大版本免费升级。

为了感谢 V2EX 社区在早期提供的宝贵建议，新版本在 App Store 生成了一批官方促销码：
- **参与方式**：大家只要在**本帖留言**（谈谈你平时习惯的番茄钟节奏、或者写代码时最喜欢的背景白噪音/功能期待）；
- **发码方式**：我会在今天下午和晚上分批通过**回帖附带 Base64 兑换码**或邮件发送（如果希望私密收码，留言时可附上邮箱或 Base64 邮箱），送出 **20 枚全新 1.3.0 终生买断兑换码**！

---

### 🔗 产品链接
- **官方网站**：[https://mactomato.com]( https://mactomato.com)（已更新 1.3.0 完整多语言与演示）
- **Mac App Store**：[https://apps.apple.com/app/apple-store/id6811364084?pt=119695882&ct=v2ex_v130&mt=8]( https://apps.apple.com/app/apple-store/id6811364084?pt=119695882&ct=v2ex_v130&mt=8)
- **适配要求**：macOS 13.0 (Ventura) 及以上，原生支持 Apple Silicon (M1/M2/M3/M4) 与 Intel Mac

欢迎大家体验与拍砖，每一条回复我都会认真查看和回复！

## 关联链接

- https://mactomato.com

## 导航

- 项目页：[[10-项目/apps.apple.com_1e8c138a]]
- 渠道页：[[50-渠道/v2ex]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
