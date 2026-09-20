---
type: "project"
title: "2026 iPhone 侧载保姆级教程： AltStore PAL + LiveContainer/SideStore 双方案"
project_url: "https://altstore.io/"
first_seen: "2026-09-20T09:52:10+08:00"
sources:
  - v2ex
tags:
  - 项目
  - v2ex
  - 8
lang: "zh"
---

# 2026 iPhone 侧载保姆级教程： AltStore PAL + LiveContainer/SideStore 双方案

> [!info] 一句话导读
> 最近折腾了一圈 iPhone 侧载，把 AltStore PAL 、SideStore 、LiveContainer 基本弄明白了。

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://altstore.io/>
> 首次收录：2026-09-20T09:52:10+08:00
> 来源渠道：V2EX
> 标签：8
> 最新指标：回复=0

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T02:37:40+08:00 | V2EX | 回复=0 | [[20-语料/posts/v2ex/2026-09-20/157b40dcb4ee0332_2026-iPhone-侧载保姆级教程-AltStore-PAL-+-LiveContainer-S]] |
| 2026-09-20T03:00:51+08:00 | V2EX | 回复=0 | [[20-语料/posts/v2ex/2026-09-20/157b40dcb4ee0332_2026-iPhone-侧载保姆级教程-AltStore-PAL-+-LiveContainer-S]] |
| 2026-09-20T03:09:29+08:00 | V2EX | 回复=0 | [[20-语料/posts/v2ex/2026-09-20/157b40dcb4ee0332_2026-iPhone-侧载保姆级教程-AltStore-PAL-+-LiveContainer-S]] |
| 2026-09-20T03:22:56+08:00 | V2EX | 回复=0 | [[20-语料/posts/v2ex/2026-09-20/157b40dcb4ee0332_2026-iPhone-侧载保姆级教程-AltStore-PAL-+-LiveContainer-S]] |
| 2026-09-20T03:34:26+08:00 | V2EX | 回复=0 | [[20-语料/posts/v2ex/2026-09-20/157b40dcb4ee0332_2026-iPhone-侧载保姆级教程-AltStore-PAL-+-LiveContainer-S]] |
| 2026-09-20T03:43:04+08:00 | V2EX | 回复=0 | [[20-语料/posts/v2ex/2026-09-20/157b40dcb4ee0332_2026-iPhone-侧载保姆级教程-AltStore-PAL-+-LiveContainer-S]] |
| 2026-09-20T09:52:10+08:00 | V2EX | 回复=0 | [[20-语料/posts/v2ex/2026-09-20/157b40dcb4ee0332_2026-iPhone-侧载保姆级教程-AltStore-PAL-+-LiveContainer-S]] |

## 摘要正文

最近折腾了一圈 iPhone 侧载，把 AltStore PAL 、SideStore 、LiveContainer 基本弄明白了。  网上最大的问题是很多教程把这几个东西混在一起讲。  实际上目前比较值得折腾的是两套完全不同的方案：  **方案 A：AltStore PAL**  优点：Apple 官方第三方 Marketplace 机制、不用 7 天续签、没有免费开发者账号传统 3 App 限制。  缺点：**不能拿任意 `.ipa` 直接安装。**  **方案 B：LiveContainer + SideStore 一体版**  优点：自己下载的 IPA 可以导入 LiveContainer 运行，非常适合开源 App 、阅读器、漫画 App 、小众工具、模拟器等。  缺点：宿主仍然使用开发者签名，需要定期刷新，而且不是所有 IPA 都兼容。  我的建议不是二选一，而是：  **App Store + AltStore PAL + LiveContainer/SideStore 共存。**  下面从零开始。  ---  # 一、先搞清楚最终能实现什么  安装完成以后，你的 iPhone 可以变成：  iPhone  ├── App Store   │　├── 微信   │　├── B 站   │　└── 正常 App   │   ├── AltStore PAL   │　└── Apple Alternative Marketplace 应用   │   └── LiveContainer + SideStore   　　├── VReader   　　├── Aidoku   　　├── 各种开源 App   　　├── 模拟器   　　├── 自己的测试 IPA   　　└── 其他兼容 IPA  简单理解：  **App Store = 苹果官方商店**  **AltStore PAL = Apple 允许的第三方商店**  **SideStore = 开发者签名/刷新工具**  **LiveContainer = IPA 容器**  真正实现：  “我手里有一个 IPA ，我想自己运行”  主要靠最后两个。  ---  # 二、方案 A：安装 AltStore PAL  ## 需要什么？  目前 AltStore PAL 官方要求：  1. iPhone/iPad 2. iOS/iPadOS 18+ 3. 实际位于欧盟、日本或巴西 4. App Store 登录对应地区 Apple Account 5. Safari 、Chrome 或 Vivaldi  AltStore PAL：  h…
