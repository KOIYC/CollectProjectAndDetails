---
type: "corpus"
item_id: "372b7e89584144df"
title: "做了一个纯浏览器端的 GPS 轨迹文件转换工具： FIT / GPX / TCX / KML 互转，文件不上传服务器"
source: "v2ex"
source_name: "V2EX"
url: "https://www.v2ex.com/t/1256001"
project_url: "https://gpxconverter.com/"
author: "Selenium39"
published_at: "2026-11-10T16:51:45"
captured_at: "2026-11-11T13:41:31+08:00"
lang: "zh"
kind: "post"
topic: "未分类"
shard: "2026-11-11"
pub_day: "2026-11-10"
tags:
  - 语料
  - v2ex
  - 17
metrics: {"replies": 0}
comments_count: 0
comments_total: 0
discovered_via: "v2ex:独立开发"
---

# 做了一个纯浏览器端的 GPS 轨迹文件转换工具： FIT / GPX / TCX / KML 互转，文件不上传服务器

> [!info] 一句话导读
> 跑步骑行几年，手里的轨迹文件越来越多，经常遇到这种小麻烦：Garmin 导出的 FIT 想传到别的平台不认、两个活动想合并、FIT 文件损坏打不开……在线工具大多要把文件上传到陌生服务器，轨迹里可是完整的出行记录，想想还是不踏实。

> [!meta]- 语料信息（点开展开）
> 来源：V2EX（post）
> 原帖：<https://www.v2ex.com/t/1256001>
> 指标：回复=0
> 作者：Selenium39　|　发布：2026-11-10T16:51:45
> 项目链接：<https://gpxconverter.com/>
> 采集：2026-11-11T13:41:31+08:00　|　id：`372b7e89584144df`

## 正文

跑步骑行几年，手里的轨迹文件越来越多，经常遇到这种小麻烦：Garmin 导出的 FIT 想传到别的平台不认、两个活动想合并、FIT 文件损坏打不开……在线工具大多要把文件上传到陌生服务器，轨迹里可是完整的出行记录，想想还是不踏实。

所以做了这个：**GPX Converter** —— https://gpxconverter.com

![](  )

所有解析和转换都在浏览器本地用 JS 完成，没有上传这一步（断网也能用），免费、无需注册、无次数限制。

**现在能做的：**

- 格式互转：FIT ↔ GPX ↔ TCX ，以及 KML / KMZ / GeoJSON 之间的转换矩阵，心率、踏频、功率数据都会保留
- Google 时间线（ Timeline ） JSON 导出转 GPX
- 合并 / 拆分 FIT 和 GPX ；修复损坏的 FIT 文件（文件头、CRC 、截断这类常见问题）
- 在线预览轨迹：地图、距离、爬升、配速
- 轨迹海报生成、GPS 热力图

站点是纯静态的，转换逻辑就在浏览器里跑，所以速度基本取决于你自己的电脑。最近刚补了全站中文版和十几篇使用教程（ Garmin / Strava 之间迁移数据、修 FIT 之类的）。

独立开发维护，欢迎试用，更欢迎挑毛病：哪个格式转出来有问题、缺哪个工具，直接回帖告诉我就行。

## 关联链接

- https://gpxconverter.com

## 导航

- 项目页：[[10-项目/gpxconverter.com_7f571ce6]]
- 渠道页：[[50-渠道/v2ex]]
- 赛道：`未分类`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
