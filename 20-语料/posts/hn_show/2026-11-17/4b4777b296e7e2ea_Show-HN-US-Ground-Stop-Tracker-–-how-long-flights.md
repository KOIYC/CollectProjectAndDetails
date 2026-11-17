---
type: "corpus"
item_id: "4b4777b296e7e2ea"
title: "Show HN: US Ground Stop Tracker – how long flights take to recover"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50521699"
project_url: "https://data.beetl.io/flights"
author: "rykam"
published_at: "2026-11-16T19:16:49Z"
captured_at: "2026-11-17T11:09:12+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-17"
pub_day: "2026-11-16"
tags:
  - 语料
  - hn_show
  - author_rykam
  - story_50521699
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: US Ground Stop Tracker – how long flights take to recover

> [!info] 一句话导读
> US Ground Stop Tracker

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50521699>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：rykam　|　发布：2026-11-16T19:16:49Z
> 项目链接：<https://data.beetl.io/flights>
> 采集：2026-11-17T11:09:12+08:00　|　id：`4b4777b296e7e2ea`

## 正文

US Ground Stop Tracker
Where the FAA is holding flights right now, what each ground stop did to departures and how flights recovered, and how this year compares with every year since 2000. Read the story of the 13 November nationwide stop →
`${s.name}: ${s.records.toLocaleString(" en-us")}="" records`).join("="" ·="" ")}"=""> million records from public sources · page built ET
What a ground stop does to flights
Every major ground stop (2 hours or more at one of the 30 busiest airports) by the share of departures it cost during the stop, against the same hours a week earlier. Drag across the strip below the chart, or pick a year, to zoom in. Open one to see that day hour by hour, the airlines hit and how departures recovered.
Every FAA ground stop of the last 7 days, one row per airport, the airports with the most hours stopped first. Eastern time.
Source: FAA ATCSCC advisory archive. Extensions, revisions and cancellations are merged, so a stop counts once. "Volume, runway, other" also takes in emergencies, security and stops with no stated cause. Nationwide stops: shaded band.
This year against every year
Hours of FAA ground stops so far this year, week by week, against every year since .
Which airlines cancel when a ground stop hits
Share of departures canceled at the 30 busiest airports on days with a ground stop of 2 hours or more (bars), and on other days (black tick), to .
Source: Bureau of Transportation Statistics on-time data, departures at the 30 busiest airports; ground stops from FAA ATCSCC advisories. BTS names the marketing airline, so regional flights count under their brand (American includes American Eagle). Airlines with at least 1,000 departures on stop days. BTS publishes about 2 months after the month ends.
Airlines on
Airline departures at the 30 busiest airports on the latest complete day, against the same weekday a week earlier (grey).
Source: ADS-B positions from ADSB.lol (ODbL 1.0), takeoffs by airline callsign (operating airline, so regional partners appear under their own name). A sample from volunteer receivers: compare with the week before, not as flight counts. Updated each morning.
What should this tracker show next?
We read every message and use them to decide what to build next.
About this data
US air traffic control disruptions, as of 9:00 pm ET on November 16, 2026
In the FAA's NAS status snapshot of 9:00 pm ET on November 16, 2026, 0 airports were under a ground stop, 2 ground delay programs were and 0 airspace flow programs were in effect. FAA facilities attributed 4,471 delays to equipment in 2025: 18.3 per 100,000 commercial operations, against 6.8 in 2016. In 2026 (Jan–Sep) the rate was 19.9. Airlines attributed 21.6% of all arrival delay minutes to the National Aviation System in 2025, and 20.2% from January to August 2026 (Bureau of Transportation Statistics). The FAA advisory archive lists 61 ground stops at US airports in the 7 days before this build.
Towers with the most equipment delays per 1,000 operations, 2025
Tower Equipment delays Operations Per 1,000 operations
 Teterboro (TEB) 232 175,217 1.32
 Newark Liberty Intl (EWR) 511 397,535 1.28
 Philadelphia Intl (PHL) 185 322,099 0.57
 Dallas Love Fld (DAL) 129 245,484 0.53
 Laguardia (LGA) 180 359,780 0.50
 Dallas-Fort Worth Intl (DFW) 172 741,286 0.23
 Miami Intl (MIA) 103 501,529 0.20
 Chicago O'Hare Intl (ORD) 156 857,392 0.18
 Bozeman Yellowstone Intl (BZN) 16 114,239 0.14
 San Francisco Intl (SFO) 56 416,527 0.13
En-route centers with the most equipment delays, 2025
Center Equipment delays
 New York Center (ZNY) 663
 Miami Center (ZMA) 492
 Washington Center (ZDC) 172
 Boston Center (ZBW) 90
 Jacksonville Center (ZJX) 72
Sources: FAA NAS status (live programs, read every 10 minutes); FAA ATCSCC advisory archive (ground stops from 2016; a stop is the chain of advisories for one airport and airline, counted as one event); FAA OPSNET delays by cause, attributed to the System Impact facility that caused them, and OPSNET operations counts (2016 to September 2026); FAA controller workforce plan (staffing as of 2025-09-20); FAA NASR (airports and the facilities that control them, cycle 2026-10-29); Bureau of Transportation Statistics, Airline On-Time Statistics and Delay Causes. "Equipment" includes non-FAA equipment such as leased telecom lines. TRACON boundaries: VATSIM SimAware TRACON Project, CC BY-SA 4.0, approximate. US states: Census Bureau via us-atlas. FAA and BTS data are public domain. 1,136,251 records processed on Beetl . Built 2026-11-17. Background: How fragile is US air traffic control?
Sources and method
Live programs : FAA NAS status feed, read every 10 minutes into Beetl. "Now" is the latest snapshot; the time at the top says how old it is.
Ground stops : FAA ATCSCC advisory archive from February 2000 (the year-to-date chart) and January 2016 (the stop overview, with flight data). A stop is the chain of advisories for one airport and airline, merged, so each stop counts once however many advisories it took. Causes are the FAA's stated cause; "volume, runway, other" also takes in emergencies, security and stops with no stated cause.
Recovery : for each stop, the first hour after the lift with departures back within 10% of the same hour a week earlier, and the next day's departures (and, from BTS, cancellations) against the same weekday a week before. Flight data: BTS on-time records through the latest month BTS has published, ADS-B positions from ADSB.lol (ODbL) since September 2026.
Equipment delays : FAA OPSNET, delays of 15 minutes or more to flights on instrument flight plans, attributed to the System Impact facility: the facility that caused them, often not the airport where the flight waited. "Equipment" includes non-FAA equipment such as leased telecom lines. No claims here about why equipment fails.
Facility rates : equipment delays per 1,000 of OPSNET's own traffic count for the same months: airport operations for towers, TRACON operations for TRACONs, aircraft handled for en-route centers. Facilities under 50,000 a year (annualized for partial years) are grey and not ranked. Combined tower and approach facilities (PHL, YNG) report under the tower.
Operations and staffing : OPSNET Airport Operations; FAA controller workforce plan (certified controllers, as of September 20, 2025).
Airline delay causes : Bureau of Transportation Statistics, Airline On-Time Statistics and Delay Causes.
Maps : US states from the Census Bureau via us-atlas; en-route centers and airports from FAA Aeronautical Information Services and NASR. TRACON boundaries: VATSIM SimAware TRACON Project, CC BY-SA 4.0, approximate. Newark: SimAware still draws Newark inside New York TRACON (N90); the FAA has assigned Newark's approach control to Philadelphia (PHL) since 2024, which the highlights follow.
Partial periods are labeled: the current year runs to the latest month published.
FAA and BTS data are US government works in the public domain.
How this stays live. Connectors on Beetl read the FAA NAS status feed every 10 minutes and collect the FAA advisory archive, OPSNET and BTS delay causes; pipelines merge advisories into ground stops and snapshots into events. The page rebuilds every hour with the latest snapshot. The story behind it: The FAA's 4-hour ground stop was still canceling flights the next day
Data: FAA (NAS status, ATCSCC advisories, OPSNET, NASR, controller workforce plan), US Bureau of Transportation Statistics, VATSIM SimAware, Census Bureau. Processed on

## 导航

- 项目页：[[10-项目/data.beetl.io_55e6b088]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
