---
type: "project"
title: "Show HN: A Zoomable Equal-Area Map Projection that interpolates to Mercator"
project_url: "https://benjoffe.com/map"
first_seen: "2026-09-20T09:37:30+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_benjoffe
  - story_49710096
  - show_hn
lang: "en"
---

# Show HN: A Zoomable Equal-Area Map Projection that interpolates to Mercator

> [!info] 一句话导读
> A New Equal-Area Map for Interactive Computer Use

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://benjoffe.com/map>
> 首次收录：2026-09-20T09:37:30+08:00
> 来源渠道：HN Show HN
> 标签：author_benjoffe, story_49710096, show_hn
> 最新指标：点赞=4 · 评论=0 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-20/6783143a074df08c_Show-HN-A-Zoomable-Equal-Area-Map-Projection-that]] |
| 2026-09-20T09:37:30+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-20/6783143a074df08c_Show-HN-A-Zoomable-Equal-Area-Map-Projection-that]] |

## 摘要正文

Author: Ben Joffe  A New Equal-Area Map for Interactive Computer Use  ## Seamlessly transitioning to Mercator upon zoom (and some new compromise cylindrical maps)  15 September 2026  Recently the UN passed the non-binding "Correct the Map" resolution which encourages the use of the Equal Earth projection in place of Mercator (which represents country-sizes disproportionately).  The Mercator projection is well suited to zoomable/navigation maps due to being "conformal", meaning it represents directions accurately. At a global scale Equal Earth may look pretty good, but it's not what web and mobile based apps typically require.  I present an alternative. The map below is equal-area at a global scale, and upon zoom, it transitions seamlessly to the Mercator projection. It is defined by an unusually simple math formula. The hybrid nature of the map is baked into the very design.  Note: the transition states are compromise map projections. It is equal area only at the global scale, and conformal only once zoomed in.  In my view most countries improve in appearance in the zoomed-out mode compared to Equal Earth. An obvious exception is Northern Europe when centred, however I encourage yo…
