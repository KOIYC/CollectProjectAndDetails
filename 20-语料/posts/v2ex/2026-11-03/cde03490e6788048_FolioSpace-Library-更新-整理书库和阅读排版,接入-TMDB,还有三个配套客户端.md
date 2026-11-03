---
type: "corpus"
item_id: "cde03490e6788048"
title: "FolioSpace Library 更新：整理书库和阅读排版，接入 TMDB，还有三个配套客户端"
source: "v2ex"
source_name: "V2EX"
url: "https://www.v2ex.com/t/1253758"
project_url: "https://foliolume.app/"
author: "deadseafu"
published_at: "2026-11-02T04:35:37"
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

# FolioSpace Library 更新：整理书库和阅读排版，接入 TMDB，还有三个配套客户端

> [!info] 一句话导读
> 之前在 V 站分享过 FolioSpace Library ，最近继续做了一轮更新，来汇报一下进展。

> [!meta]- 语料信息（点开展开）
> 来源：V2EX（post）
> 原帖：<https://www.v2ex.com/t/1253758>
> 指标：回复=0
> 作者：deadseafu　|　发布：2026-11-02T04:35:37
> 项目链接：<https://foliolume.app/>
> 采集：2026-11-03T09:45:49+08:00　|　id：`cde03490e6788048`

## 正文

之前在 V 站分享过 FolioSpace Library ，最近继续做了一轮更新，来汇报一下进展。

我做它的起因很简单：NAS 里的书、漫画、游戏和电影越来越多，但存进去之后，真正打开它们的次数并不多。我希望有一个统一入口，让这些收藏更容易被找到、阅读和播放。

Library 通过 Docker 部署，负责整理自己的文件，也自带 Web 界面。项目开源：[GitHub 和部署说明]( https://github.com/funland/foliospace-Library)。

这轮主要改善了两件事。

**书库和阅读排版**：电子书、漫画可以分别浏览，EPUB 、PDF 支持筛选，漫画目录层级也重新整理了。已有 Calibre 书库可以读取书名、作者和封面。EPUB 改善了双栏宽度、阅读位置恢复、键盘翻页和脚注跳转。

内置的 Web 阅读器我也花了不少功夫：不装客户端，直接用浏览器就能读电子书、PDF 和漫画；手机和平板上的阅读布局、翻页与条漫浏览也做了适配。

![浏览器中的双页阅读](  )

![浏览器中的条漫阅读](  )

**影视库接入 TMDB**：可以搜索并确认影片、剧集信息，补充海报和季集目录。需要自行配置 TMDB 读取令牌，按需匹配；也可以继续使用本地 NFO 、图片和手动填写的信息。

![影视库海报墙](  )

另外，我也在持续开发三个配套客户端：

- [FolioSpace Reader]( https://reader.foliospace.app/)：在 iPhone 、iPad 、Vision Pro 上阅读电子书、PDF 、漫画和条漫。最近也加入了 iPhone Duo 支持，连接 Library 后，可以方便地从自己的书库加载书籍和漫画。
- [FolioLume Player]( https://foliolume.app/)：观看自己的影片收藏，支持多种本地和网络来源，以及兼容的蓝光原盘播放、菜单和字幕功能。
- [SpatialEMU]( https://spatialemu.com/)：浏览 Library 中的游戏收藏，在支持的设备上运行兼容游戏。

三个客户端都可以独立使用，也都已在 App Store 上架。其中 FolioLume Player 暂未在中国区上架，需要使用已上架地区的 Apple 账户下载。

![游戏库](  )

顺便提一句，绿联官网也写过一篇 [FolioSpace Library 部署教程]( https://www.ugnas.com/play-detail/id-154.html)，有安装步骤和使用截图，初次接触可以参考。教程使用的是早期版本，当前配置以项目文档为准。

欢迎有类似收藏习惯的朋友试试，也想听听大家实际使用时，最希望先改善的是哪一部分。

如果你也在做阅读器、播放器或其他客户端，也欢迎通过 [Client API]( https://github.com/funland/foliospace-Library/blob/main/docs/api/client-v1.md) 接入自己的 FolioSpace 资料库。接口和文档还会继续完善，也欢迎交流需求。

## 关联链接

- https://github.com/funland/foliospace-Library
- https://github.com/funland/foliospace-Library/blob/main/docs/api/client-v1.md
- https://reader.foliospace.app/
- https://spatialemu.com/
- https://www.ugnas.com/play-detail/id-154.html

## 导航

- 项目页：[[10-项目/foliolume.app_439c753c]]
- 渠道页：[[50-渠道/v2ex]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
