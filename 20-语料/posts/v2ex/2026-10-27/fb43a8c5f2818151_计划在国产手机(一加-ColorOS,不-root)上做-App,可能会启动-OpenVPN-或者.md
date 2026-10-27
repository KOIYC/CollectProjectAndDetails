---
type: "corpus"
item_id: "fb43a8c5f2818151"
title: "计划在国产手机(一加 ColorOS，不 root)上做 App，可能会启动 OpenVPN 或者 frp 去连接业务，会被找麻烦吗？"
source: "v2ex"
source_name: "V2EX"
url: "https://www.v2ex.com/t/1252331"
author: "qazwsxkevin"
published_at: "2026-10-27T10:56:25"
captured_at: "2026-10-27T23:56:38+08:00"
lang: "zh"
kind: "post"
topic: "开发者工具"
shard: "2026-10-27"
pub_day: "2026-10-27"
tags:
  - 语料
  - v2ex
  - 300
metrics: {"replies": 0}
comments_count: 0
comments_total: 0
discovered_via: "v2ex:独立开发"
---

# 计划在国产手机(一加 ColorOS，不 root)上做 App，可能会启动 OpenVPN 或者 frp 去连接业务，会被找麻烦吗？

> [!info] 一句话导读
> 非商业，纯小圈子内使用，不涉及到爬 T 外联外区数据.

> [!meta]- 语料信息（点开展开）
> 来源：V2EX（post）
> 原帖：<https://www.v2ex.com/t/1252331>
> 指标：回复=0
> 作者：qazwsxkevin　|　发布：2026-10-27T10:56:25
> 项目链接：—
> 采集：2026-10-27T23:56:38+08:00　|　id：`fb43a8c5f2818151`

## 正文

- 非商业，纯小圈子内使用，不涉及到爬 T 外联外区数据.
- openvpn 的方案是连接到中心点(已经有现成的设施环境存在)，获取到部分网段的路由转发，从而使 App 获得一些自部署 IP 端口业务的数据的获取和写入.（这是首先考虑的方案）
- 如果 openvpn 的方案会有麻烦，就打算启用 frp ，在公网上找个服务器转发自部署网内的 IP 端口，使用本地密钥加密两端.
- 以上提及的两种工具，不打算在手机上独立存在，内嵌方式在 App 启动和在驻时维护连接.
- 以前没有搞过 Android 开发，因为有 vibe code ，还是第一次做这种，这种 App 能在未 root 的情况下，连接可以启动？
- 会被内置的反炸通道误判惹麻烦吗？

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/v2ex]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
