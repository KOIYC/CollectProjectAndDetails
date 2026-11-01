---
type: "corpus"
item_id: "aca65872d59dbde5"
title: "不想再为了改一句英文切去 ChatGPT 了，我做了个在任何输入框里一键搞定的 Mac 工具"
source: "v2ex"
source_name: "V2EX"
url: "https://www.v2ex.com/t/1253333"
project_url: "https://getinklet.app/zh"
author: "tomwan"
published_at: "2026-10-30T22:34:05"
captured_at: "2026-11-01T09:43:04+08:00"
lang: "zh"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-01"
pub_day: "2026-10-30"
tags:
  - 语料
  - v2ex
  - 17
metrics: {"replies": 0}
comments_count: 0
comments_total: 0
discovered_via: "v2ex:独立开发"
---

# 不想再为了改一句英文切去 ChatGPT 了，我做了个在任何输入框里一键搞定的 Mac 工具

> [!info] 一句话导读
> 在外企打工，每天都是是脑子里想的是中文，手上还得敲英文。Slack、邮件写完总要读两遍，感觉怪怪的，又不知道怎么改。

> [!meta]- 语料信息（点开展开）
> 来源：V2EX（post）
> 原帖：<https://www.v2ex.com/t/1253333>
> 指标：回复=0
> 作者：tomwan　|　发布：2026-10-30T22:34:05
> 项目链接：<https://getinklet.app/zh>
> 采集：2026-11-01T09:43:04+08:00　|　id：`aca65872d59dbde5`

## 正文

在外企打工，每天都是是脑子里想的是中文，手上还得敲英文。Slack、邮件写完总要读两遍，感觉怪怪的，又不知道怎么改。

之前一直用 Raycast 的 AI 改英文，但输入框太小，prompt 改起来也不太顺手。干脆自己搓了一个，叫 Inklet，常驻 Mac 菜单栏，专门干这件事。

用起来很简单：

在任何输入框按 `⌥ Space`（可以随意设置），中文英文随便写，回车生成自然的英文，再回车直接填回原来的输入框。不用切窗口，也不用复制粘贴。

![Inklet](  )

另外还加了几个自己常用的功能：

- **免费开源**，MIT 协议
- **不用 API Key**，M 系列 Mac 可以直接跑本地模型，断网也能用
- 也支持 DeepSeek、Claude、OpenAI、Gemini 等云端模型
- 按住右 Option 直接说话，本地语音识别，中英混说也行
- 选中文字就能翻译、朗读
- Prompt 随便改，比如「礼貌一点但别太客套」
- 不用注册，没有埋点。用本地模型的话，数据不出电脑

支持 macOS 14+，安装包也做了苹果签名和公证。

官网： https://getinklet.app/zh

GitHub： https://github.com/wanming/Inklet

目前还在自己慢慢迭代，欢迎试用，有什么不好用的直接吐槽。如果觉得还行，也求个 Star，给独立开发者一点动力哈哈。

## 关联链接

- https://github.com/wanming/Inklet

## 导航

- 项目页：[[10-项目/getinklet.app_d3ba34b4]]
- 渠道页：[[50-渠道/v2ex]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
