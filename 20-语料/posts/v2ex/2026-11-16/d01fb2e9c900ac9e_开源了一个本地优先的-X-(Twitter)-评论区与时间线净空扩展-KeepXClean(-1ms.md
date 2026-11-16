---
type: "corpus"
item_id: "d01fb2e9c900ac9e"
title: "开源了一个本地优先的 X (Twitter) 评论区与时间线净空扩展 KeepXClean（< 1ms、零登录、不轮询接口）"
source: "v2ex"
source_name: "V2EX"
url: "https://www.v2ex.com/t/1256499"
project_url: "https://chromewebstore.google.com/detail/keepxclean/plngcinmibjmkjjpfjemhfabjfjjkhhd"
author: "linheitu"
published_at: "2026-11-12T07:54:02"
captured_at: "2026-11-16T10:06:32+08:00"
lang: "zh"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-16"
pub_day: "2026-11-12"
tags:
  - 语料
  - v2ex
  - 17
metrics: {"replies": 0}
comments_count: 0
comments_total: 0
discovered_via: "v2ex:独立开发"
---

# 开源了一个本地优先的 X (Twitter) 评论区与时间线净空扩展 KeepXClean（< 1ms、零登录、不轮询接口）

> [!info] 一句话导读
> 现在刷 X （ Twitter ）体验越来越差：点开一条热门推文的评论区，前排经常全是蓝标复读机水军、冒充原推主的高仿钓鱼号、评论扣数字领资料的引流帖、币圈土狗合约刷屏和穿插的推广广告，真正有价值的讨论全被淹没在下面。

> [!meta]- 语料信息（点开展开）
> 来源：V2EX（post）
> 原帖：<https://www.v2ex.com/t/1256499>
> 指标：回复=0
> 作者：linheitu　|　发布：2026-11-12T07:54:02
> 项目链接：<https://chromewebstore.google.com/detail/keepxclean/plngcinmibjmkjjpfjemhfabjfjjkhhd>
> 采集：2026-11-16T10:06:32+08:00　|　id：`d01fb2e9c900ac9e`

## 正文

现在刷 X （ Twitter ）体验越来越差：点开一条热门推文的评论区，前排经常全是蓝标复读机水军、冒充原推主的高仿钓鱼号、评论扣数字领资料的引流帖、币圈土狗合约刷屏和穿插的推广广告，真正有价值的讨论全被淹没在下面。

之前试过几款过滤脚本和插件，痛点主要有两个：一是靠后台高频轮询 X 接口拉资料，容易撞速率限制甚至触发账号风控；二是把时间线文本发往远端大模型判断，既有延迟又有隐私顾虑。

其实浏览器在渲染页面前，已经通过 X 自身的 GraphQL 数据流拿到了完整的推文与作者元数据。于是我做并开源了 **KeepXClean** —— 直接在浏览器本地内存里对既有 GraphQL 响应做同步确定性过滤，单条判定 **< 1 ms**，零账号登录、零额外接口轮询，刷推保持丝滑不卡顿。

### 主要功能与设计细节

- **专治评论区与时间线重灾区**：支持识别原推主高仿钓鱼号（句柄/昵称相似度 + 粉丝量级悬殊对比）、蓝标极短无意义水评与 AI 套话、低粉简介外链导流、口令抽奖互动引流、日均/爆发高频刷屏、`#hashtag` / `$cashtag` 堆砌，以及无痕移除原生 `Promoted` 推广广告。
- **内置 24 条公共词库包 + 自定义规则**：按 5 大噪音分类整理了 24 条开箱即用的词库规则（支持逐条独立开关，也可一键复制为自定义正则），同时支持多作用范围自定义规则与语种黑白名单。
- **单行折叠可查证据 / 无痕移除 + 转引穿透**：可选择把拦截内容折叠为单行提示条，随时点击展开核查命中的具体规则与证据；当已关注的博主转发/引用垃圾推文时，快捷净空按钮会精准穿透指向源头垃圾号，避免误伤关注对象。
- **4.5 秒撤销窗口 + 匿名去重社区防线**：点击一键净空后本地立即生效，并留出 **4.5 秒倒计时撤销窗口**；窗口结束后再按偏好执行 X 原生拉黑与可选的社区匿名投票。社区黑名单采用单向加盐 `SHA-256` 哈希去重（严格 `1 账号 = 1 票`，投票号需注册满 30 天，且对 ≥ 5 万粉创作者设 `5×` 门槛保护防恶意抱团）。
- **隐私与开源**：扩展不读取任何密码、Cookie 、登录 Token 或私信，无任何第三方遥测 SDK ；基于 WXT (Manifest V3) + Shadow DOM 开发，MIT 协议完全开源，内置简中、繁中、英、日、韩等 10 种界面语言。

### 界面预览

![](  )

![](  )

### 在线体验与安装

- **官方网站**（首屏内置免安装的 X 评论区交互沙盒 + 30 秒演示视频）： https://keepxclean.com/?lang=zh-CN
- **Chrome 应用商店**（兼容 Chrome / Edge / Brave / Arc 等 Chromium 浏览器）： https://chromewebstore.google.com/detail/keepxclean/plngcinmibjmkjjpfjemhfabjfjjkhhd
- **GitHub 开源仓库（ MIT ）**： https://github.com/KeepXClean/keepxclean

刚发第一个正式版本，规则细节还在持续迭代中。欢迎常刷 X 的 V 友体验拍砖，遇到漏网的新型水军套路、误判样本或者有任何建议，欢迎直接回帖交流或提 Issue ！

## 关联链接

- https://github.com/KeepXClean/keepxclean
- https://keepxclean.com/?lang=zh-CN

## 导航

- 项目页：[[10-项目/chromewebstore.google.com_31a5ec95]]
- 渠道页：[[50-渠道/v2ex]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
