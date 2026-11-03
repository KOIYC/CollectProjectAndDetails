---
type: "corpus"
item_id: "44f7226760056655"
title: "做了一个少切 App 的两步验证器 Cue， iOS 开放 TestFlight，求导入和填码体验反馈"
source: "v2ex"
source_name: "V2EX"
url: "https://www.v2ex.com/t/1253794"
project_url: "https://cueapp.net/"
author: "kaneki"
published_at: "2026-11-02T06:15:56"
captured_at: "2026-11-03T09:45:49+08:00"
lang: "zh"
kind: "post"
topic: "开发者工具"
shard: "2026-11-03"
pub_day: "2026-11-02"
tags:
  - 语料
  - v2ex
  - 17
metrics: {"replies": 0}
comments_count: 0
comments_total: 0
discovered_via: "v2ex:独立开发"
---

# 做了一个少切 App 的两步验证器 Cue， iOS 开放 TestFlight，求导入和填码体验反馈

> [!info] 一句话导读
> 我是 Cue 的开发者，iPhone 版刚开放 TestFlight ，想请经常使用 2FA 的朋友试一下。

> [!meta]- 语料信息（点开展开）
> 来源：V2EX（post）
> 原帖：<https://www.v2ex.com/t/1253794>
> 指标：回复=0
> 作者：kaneki　|　发布：2026-11-02T06:15:56
> 项目链接：<https://cueapp.net/>
> 采集：2026-11-03T09:45:49+08:00　|　id：`44f7226760056655`

## 正文

我是 Cue 的开发者，iPhone 版刚开放 TestFlight ，想请经常使用 2FA 的朋友试一下。

Cue 关注的是“最后一步怎么填”：验证码生成之后，怎样少做一次切 App 、找账号、复制、切回来。iOS 版做了系统验证码自动填充，也做了一个 Cue 键盘，可以在允许第三方键盘的输入框里点选账号填码。

两种入口各有边界：自动填充需要条目的网站信息和输入框配合； iOS 第三方键盘不能识别当前宿主 App ，部分 App 也会禁用第三方键盘。因此 Cue 键盘是手动选条目，不宣称能在所有 App 里自动匹配。

其他已有功能：

- 从 Google 身份验证器迁移二维码、Aegis 、2FAS 、Bitwarden 等备份导入。
- 分组、搜索、Face ID 、备份和导出；设置密码后数据库用 AES-256-GCM 加密。
- 可选 iCloud 同步，加密数据库保存在用户自己的 iCloud 私有数据库。
- 不需要注册 Cue 账号。Android 版基于 Aegis 开源； iOS 是独立的 Swift 实现，未开源，两端读写兼容的数据库格式。

公测链接： https://testflight.apple.com/join/t8CGfyCF

要求 iPhone / iOS 18+，先安装 TestFlight 。官网： https://cueapp.net/

基础功能免费，正式版 Cue Pro ¥18 买断，包含自动填充、Cue 键盘、小组件、图标包和 iCloud 同步。TestFlight 内购是测试交易，不实际扣费，也不转为正式版购买权益。

希望重点收集：导入兼容性、具体 App/网站里的填码体验，以及 Face ID 和键盘切换是否顺畅。欢迎回帖或通过 TestFlight 反馈，附系统版本和复现步骤即可，不要发真实密钥。建议先用测试账号并保留原验证器、备份。

也想听听大家：你现在最常用哪种方式填两步验证码，哪一步最打断登录？

## 关联链接

- https://testflight.apple.com/join/t8CGfyCF

## 导航

- 项目页：[[10-项目/cueapp.net_2af7d229]]
- 渠道页：[[50-渠道/v2ex]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
