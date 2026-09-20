---
type: "corpus"
item_id: "7acbc0db4a3a402c"
title: "开源分享： FlowLens - 终端环境下的流量分析工具"
source: "v2ex"
source_name: "V2EX"
url: "https://www.v2ex.com/t/1242993"
project_url: "https://github.com/power4j/flowlens"
author: "cppc"
published_at: "2026-09-18T07:11:01"
captured_at: "2026-09-20T09:52:10+08:00"
lang: "zh"
kind: "post"
topic: "开发者工具"
shard: "2026-09-20"
pub_day: "2026-09-18"
tags:
  - 语料
  - v2ex
  - 17
metrics: {"replies": 0}
comments_count: 0
comments_total: 0
discovered_via: "v2ex:独立开发"
---

# 开源分享： FlowLens - 终端环境下的流量分析工具

> [!info] 一句话导读
> 起因是我的 VPS 流量消耗异常，找了一圈也没有合适的工具，为了抓贼，只好自己动手。一开始做了一个非常简单的，解决问题后觉得能用，就继续开发了一下。目前我是在 Windows 和 Linux 使用，MacOS 理论上也行，但是没有测试环境，所以没测。

> [!meta]- 语料信息（点开展开）
> 来源：V2EX（post）
> 原帖：<https://www.v2ex.com/t/1242993>
> 指标：回复=0
> 作者：cppc　|　发布：2026-09-18T07:11:01
> 项目链接：<https://github.com/power4j/flowlens>
> 采集：2026-09-20T09:52:10+08:00　|　id：`7acbc0db4a3a402c`

## 正文

起因是我的 VPS 流量消耗异常，找了一圈也没有合适的工具，为了抓贼，只好自己动手。一开始做了一个非常简单的，解决问题后觉得能用，就继续开发了一下。目前我是在 Windows 和 Linux 使用，MacOS 理论上也行，但是没有测试环境，所以没测。

项目地址：[https://github.com/power4j/flowlens]( https://github.com/power4j/flowlens)

下面是简介

---

FlowLens 是面向资源受限 Linux 和 Windows 主机的命令行网络流量分析工具，用于查看网卡流量，并以尽力而为的方式提供进程、IP 和出站域名归属信息。项目同时提供实验性 macOS 构建。

![FlowLens 流量总览](  )

## 功能亮点
- 一屏总览。 同时查看网卡流量总量、流量最高的进程、远端 IP 和出站域名。
- 可解释的进程归属。 区分独占、共享、系统和未归属流量，并提供流量守恒摘要。
- 进程详情。 查看 PID 、可执行文件路径、最后活跃时间、归属构成，以及按流量排序的双向 TCP/UDP 端点流。
- 可配置排行窗口。 在累计总量与 5 秒、10 秒、30 秒、60 秒或 5 分钟平均吞吐量之间切换；有限窗口会显示预热覆盖率。
- 出站域名识别。 从本机发起的 TCP 连接中提取 TLS ClientHello SNI 和明文 HTTP/1.x Host 头。
- 交互式网卡选择。 在 TUI 中切换抓包网卡，并查看网卡的 IPv4 和 IPv6 地址。
- 多种输出方式。 支持交互式 TUI 、纯文本快照、JSON Lines 流、格式化 JSON 文件和独立的 JSONL 诊断日志。
- 跨平台与主题支持。 支持 Linux 和 Windows 发布版本，提供 x86_64 、aarch64 实验性 macOS 构建，并内建四种主题和自定义 JSON 主题。

## 导航

- 项目页：[[10-项目/github.com_dca0468f]]
- 渠道页：[[50-渠道/v2ex]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
