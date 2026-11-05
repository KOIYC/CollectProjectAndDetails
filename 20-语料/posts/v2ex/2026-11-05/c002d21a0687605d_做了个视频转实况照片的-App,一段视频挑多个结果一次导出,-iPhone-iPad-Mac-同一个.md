---
type: "corpus"
item_id: "c002d21a0687605d"
title: "做了个视频转实况照片的 App，一段视频挑多个结果一次导出， iPhone / iPad / Mac 同一个"
source: "v2ex"
source_name: "V2EX"
url: "https://www.v2ex.com/t/1254562"
project_url: "https://apps.apple.com/cn/app/id6826636404?ct=social-v2ex"
author: "lson"
published_at: "2026-11-04T15:37:45"
captured_at: "2026-11-05T11:26:05+08:00"
lang: "zh"
kind: "post"
topic: "开发者工具"
shard: "2026-11-05"
pub_day: "2026-11-04"
tags:
  - 语料
  - v2ex
  - 17
metrics: {"replies": 0}
comments_count: 0
comments_total: 0
discovered_via: "v2ex:独立开发"
---

# 做了个视频转实况照片的 App，一段视频挑多个结果一次导出， iPhone / iPad / Mac 同一个

> [!info] 一句话导读
> Beavery 做的事：演唱会、旅行只管录视频，回来在同一段视频里把想要的瞬间一个个挑出来，这段做实况照片、那段做 GIF 、再截一帧原画质照片，加进「待导出」，一次全部导出到相册。时间轴慢慢拖会放大到逐帧，封面任选一帧。

> [!meta]- 语料信息（点开展开）
> 来源：V2EX（post）
> 原帖：<https://www.v2ex.com/t/1254562>
> 指标：回复=0
> 作者：lson　|　发布：2026-11-04T15:37:45
> 项目链接：<https://apps.apple.com/cn/app/id6826636404?ct=social-v2ex>
> 采集：2026-11-05T11:26:05+08:00　|　id：`c002d21a0687605d`

## 正文

独立开发，上周刚过审上架，来分享一下。

Beavery 做的事：演唱会、旅行只管录视频，回来在同一段视频里把想要的瞬间一个个挑出来，这段做实况照片、那段做 GIF 、再截一帧原画质照片，加进「待导出」，一次全部导出到相册。时间轴慢慢拖会放大到逐帧，封面任选一帧。

几个技术上的点：

- 实况照片的配对（图片里的 MakerApple 17 、视频里的 content identifier 、still-image-time 元数据轨）用 AVFoundation + ImageIO 自己写，视频样本直接从源文件拷贝不重编码，所以 HDR 、声音、拍摄时间地点都原样保留，画质和源视频一致。
- 实况不限时长，拖多长就多长；新选区默认长度和相机拍的实况差不多，因为不少地方只播实况的前几秒。
- Mac 版是原生 Mac App ，和 iPhone 共用 SwiftUI 代码，不是 Catalyst 也不是「专为 iPad 设计」。拖文件进窗口、方向键逐帧、⌘E 打开待导出。
- 照片和视频在你的设备上处理，不上传，不用注册。

收费：免费下载，一次导出一个结果免费，第一次批量导出也免费；之后一次导出多个要 Pro ，终身 ¥38 或年订阅 ¥22 ，iPhone / iPad / Mac 买一次通用。

App Store： https://apps.apple.com/cn/app/id6826636404?ct=social-v2ex
官网： https://beavery.savetimefor.fun
30 秒演示： https://youtu.be/AGBc4EetiHU

欢迎提意见，尤其是拖时间轴的手感。

## 关联链接

- https://beavery.savetimefor.fun
- https://youtu.be/AGBc4EetiHU

## 导航

- 项目页：[[10-项目/apps.apple.com_806303d6]]
- 渠道页：[[50-渠道/v2ex]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
