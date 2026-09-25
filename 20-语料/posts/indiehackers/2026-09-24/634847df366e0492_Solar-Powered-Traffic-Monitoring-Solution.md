---
type: "corpus"
item_id: "634847df366e0492"
title: "Solar Powered Traffic Monitoring Solution"
source: "indiehackers"
source_name: "Indie Hackers 产品库"
url: "https://www.indiehackers.com/product/solar-powered-traffic-monitoring-solution"
captured_at: "2026-09-25T13:45:40+08:00"
lang: "en"
kind: "project"
topic: "AI 工具/Agent"
shard: "2026-09-24"
tags:
  - 语料
  - indiehackers
metrics: {}
comments_count: 0
comments_total: 0
discovered_via: "ih:products"
---

# Solar Powered Traffic Monitoring Solution

> [!info] 一句话导读
> Home Starting Up Case Studies DB Products Ideas DB Vibe Coding Tools Subscribe to IH+

> [!meta]- 语料信息（点开展开）
> 来源：Indie Hackers 产品库（project）
> 原帖：<https://www.indiehackers.com/product/solar-powered-traffic-monitoring-solution>
> 指标：—
> 作者：—　|　发布：—
> 项目链接：—
> 采集：2026-09-25T13:45:40+08:00　|　id：`634847df366e0492`

## 正文

Home Starting Up Case Studies DB Products Ideas DB Vibe Coding Tools Subscribe to IH+
Starting Up Case Studies
 Ideas DB Products DB Sign in Join
Solar Powered Traffic Monitoring Solution
 Counts the number of passing cars and finds their direction.
Visit Website
Solar Powered Traffic Monitoring Solution Counts the number of passing cars and finds their direction.
 Post 1
 Revenue $0 / mo
 Website
September 23, 2026
 Solar Powered Traffic Monitoring Solution
This was my final-year thesis project for my Computer Engineering degree. The goal was a solar-powered, camera-based device to count vehicles by direction at a specific point on a road, without needing to tap into road infrastructure.
 Runs on a Raspberry Pi 5 4GB (although 2GB should work fine too) with a basic 720p USB webcam. Detection is based on the YOLOv8 Nano, then a Kalman filter + greedy IoU tracker maintains vehicle IDs across frames and classifies direction of travel.
 On my test footage it hit 96.6% detection/classification accuracy. It also works at night if there is street lighting.
 Powering it is a 100W solar panel + 600Wh lead-acid battery, sized using PVGIS irradiance data and modeled to survive at least 3 winter days worst-case. Measured draw is 5.6W average (power optimization details on the website).
 Privacy was a real design constraint. All inference happens on-device, frames only ever exist in RAM, and the only thing that leaves the device is an anonymized, aggregated vehicle count per time period.
 Full writeup and thesis report on my website.
Marios Christoforou
4 Likes
3 Comments
Say something nice…
Post Comment
1
Have you tested the system with a specific potential buyer, such as municipalities or private road operators, and what evidence would make them pay for deployment?
Aryan Sinh
·
2 days ago
 ·
Reply
1
I have tested the system in collaboration with the University of Cyprus. It was not meant to be a commercial solution at this point, which is why the project is open source. As stated in the full report, this system can provide valuable information about the traffic patterns on the road and could even allow for a prediction model to be trained off of its data.
Marios Christoforou
·
a day ago
 ·
Reply
1
That gap between a working system and a buyer case is interesting. Could be useful to dig into that transition by email sometime, if you’re open to it.
Aryan Sinh
·
a day ago
 ·
Reply
About
 This was my final-year thesis project for my Computer Engineering degree. The goal was a self-powered, camera-based device to count vehicles by direction at a specific point on a road, and upload the data to an online DB
 People
 Marios Christoforou Founder
Stay informed as an indie hacker.
 Market insights that help you start and grow your business.
Subscribe
Follow @IndieHackers on X for stories and insights about founders building profitable online businesses, and to connect with others in the Indie Hackers community.
 © Indie Hackers, Inc. · FAQ · Terms · Privacy · Cookie Settings / Policy ·
Community
 Top Today Top This Week Top This Month Join
Products
 All Products Highest Revenue Add Yours
Databases
 Ideas Products Stories

## 导航

- 项目页：[[10-项目/Solar-Powered-Traffic-Monitoring-Solution_634847df]]
- 渠道页：[[50-渠道/indiehackers]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
