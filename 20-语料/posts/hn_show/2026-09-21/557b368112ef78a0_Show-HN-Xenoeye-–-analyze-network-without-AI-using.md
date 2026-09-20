---
type: "corpus"
item_id: "557b368112ef78a0"
title: "Show HN: Xenoeye – analyze network without AI using netflow, PostgreSQL, Grafana"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48725156"
project_url: "https://github.com/vmxdev/xenoeye"
author: "vmxdev"
published_at: "2026-06-29T21:00:01Z"
captured_at: "2026-09-21T03:11:03+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-06-29"
tags:
  - 语料
  - hn_show
  - author_vmxdev
  - story_48725156
  - show_hn
metrics: {"points": 5, "comments": 0, "engagement_velocity": 5}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:113d"
---

# Show HN: Xenoeye – analyze network without AI using netflow, PostgreSQL, Grafana

> [!info] 一句话导读
> Lightweight Netflow/IPFIX/sFlow collector and analyzer

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48725156>
> 指标：点赞=5 · 评论=0 · engagement_velocity=5
> 作者：vmxdev　|　发布：2026-06-29T21:00:01Z
> 项目链接：<https://github.com/vmxdev/xenoeye>
> 采集：2026-09-21T03:11:03+08:00　|　id：`557b368112ef78a0`

## 正文

# vmxdev/xenoeye

Lightweight Netflow/IPFIX/sFlow collector and analyzer

- Stars: 136
- Forks: 4
- Watchers: 136
- Open issues: 6
- License: ISC License
- Default branch: master
- Created: 2018-12-04T18:14:22Z

## Languages

- C
- C++
- Dockerfile
- M4
- Makefile
- Python
- Shell

## Topics

- clickhouse
- grafana
- ipfix
- netflow
- netflow-analyzer
- netflow-collector
- postgresql
- sflow

## Top Contributors

- vmxdev (342 contributions)
- nerosketch (7 contributions)

---

## README

# xenoeye
Lightweight Netflow/IPFIX/sFlow collector and analyzer

`README.ru.md` - документация на русском

The documentation is mostly translated automatically using Google translator, so if you see something weird - feel free to let us know.

With this collector you can

 * Monitor traffic of IP networks, individual IP addresses or services
 * React quickly to traffic spikes or traffic drops below thresholds
 * Monitor traffic patterns and distribution of network packets using data from Netflow/IPFIX/sFlow

## Key Features

 * The collector was developed for medium and large networks, with different user groups that need different reports. For this purpose, "monitoring objects" are used. A monitoring object can be a network, a set of networks, an autonomous system, a geo-object or arbitrary network traffic that can be extracted from Netflow/IPFIX/sFlow.
 * Using the collector, you can generate various reports, build charts, dashboards in Grafana, perform some actions when the traffic speed exceeds thresholds or falls below thresholds.
 * We use the collector to monitor our networks. We are using Netflow v9 and IPFIX, so the collector supports them.
 * Netflow v5 and sFlow are also supported.
 * The documentation contains examples of building simple reports. To build more complex ones, you need at least basic knowledge of SQL.
 * The collector uses text configuration files. This allows you to write simple configs manually, and for complex configurations with a large number of objects, you can generate configs using scripts.
 * The collector processes data in two ways: it aggregates it over periods (fixed-size time windows to produce reports and graphs), and it uses moving averages to quickly react to spikes.
 * Both methods can be used individually or together. For example, if a moving average detects a threshold being exceeded, you can run a custom script and immediately enable extended statistics collection.
 * We use moving averages to detect volumetric DoS/DDoS attacks. When thresholds are reached, BGP announcements are created (FlowSpec filtering, rate-limit, redirection to cleaning servers or Blackhole) and users receive a notification in the messenger.
 * Collector is not very demanding on resources. It can process data and build reports even on Orange Pi (analogous to Raspberry Pi) with 4 GB of memory. On small networks it can run in a VM with one CPU and 1GB of RAM.
 * The collector has only been tested under 64-bit Linux (x64, AArch64 and Elbrus).
 * We use PostgreSQL as a storage for time series data. Aggregated data by selected Netflow fields is exported there. The collector can export **not all** data to the DBMS, it can aggregate and export only top-N entities, and aggregate the rest into one row. This is a useful feature for large monitoring objects - you can regulate the amount of data that is written to the DBMS and use cheaper, slower disks.
 * In addition to PostgreSQL, the collector has experimental support for storing data in ClickHouse
 * A basic set of Netflow/IPFIX fields are supported out of the box, but you can add almost any field you need.
 * The project has a very liberal ISC license. We have no plans to make commercial or semi-commercial versions. This means that we cannot make any predictions about the future of the project. But on the other hand:
 * There are no hidden or artificial restrictions

## Performance

Users are usually interested in at least a rough performance estimate, so we made several tests: we recorded real Netflow traffic from different routers in pcap files and played them on the loopback interface using tcpreplay at different speeds.

Tests were run on i3-2120 CPU @ 3.30GHz.

Very roughly, you can rely on following numbers:

In debug mode, when the contents of each flow are printed to a file, it turned out about 100K flow per second per one CPU.

In a slightly closer to production mode, with two monitoring objects, two sliding windows - about 700K fps per single CPU.

These numbers are best read in a pessimistic mood:
 1. if you load the collector with many monitoring objects with a bunch of reports and debug printing, it can choke on 100K fps/CPU or less
 2. most likely 700K fps and more cannot be processed on one CPU

Scaling to multiple cores is described below in the documentation

## LXC container

The v25.02 release comes with an LXC container image xe2502.tar.xz. This is a **privileged** container and is configured to use the **host network**, use this configuration with extreme caution. The container contains a collector with several pre-configured monitoring objects, PostgreSQL and Grafana.

Brief usage instructions:
``` sh
# install lxc
$ sudo apt install lxc

# unpack the container image
$ sudo tar Jxf xe2502.tar.xz -C /var/lib/lxc

# run container
$ sudo lxc-start --name xe2502

# run container shell
$ sudo lxc-attach --name xe2502
```

Inside the container, edit the file `/etc/xenoeye/xenoeye.conf`

If you are capturing `*flow` with pcap, add capabilities:
``` sh
# setcap "cap_net_admin,cap_net_raw,cap_dac_read_search,cap_sys_ptrace+pe" /usr/local/bin/xenoeye
```

Edit the file `/var/lib/xenoeye/iplists/mynet`, write your networks there (IPv4 and IPv6), and delete unnecessary ones.

Restart the service
``` sh
# service xenoeye restart
```

Navigate your browser to `http://server-address:3000`, Grafana should open. Login/password admin/admin.

Grafana comes with several pre-configured dashboards (Overview, AS/GeoIP, Routers, DoS/DDoS) separately for IPv4 and IPv6 addresses. The documentation below describes how to add other reports and configure moving averages.

## Proxmox-template

A template for Proxmox is also available: proxmox-xe2502.tar.xz

## Documentation

 * Step-by-step instructions for installing and configuring the collector
 * Build and install
 * Checking Netflow packets receiving
 * Load-balancing across multiple CPUs
 * Sampling rate
 * Monitoring objects
 * IP lists
 * Configure what data should be exported to the DBMS
 * Export to DBMS
 * Simple Reporting by IP Addresses
 * Detect spam-bots and ssh-scanners
 * Plotting with gnuplot
 * Plots with Python Matplotlib
 * Traffic visualization with Grafana
 * Moving Averages
 * Configure and set thresholds
 * Scripts and their options
 * Extended stats
 * Anomaly alerts using Telegram-bot

 * Additional features
 * GeoIP
 * Autonomous systems
 * Updating databases without restarting the collector
 * xegeoq utility
 * Visualizing GeoIP data and AS names with Grafana
 * Traffic classification
 * sFlow
 * Additional data analysis using sFlow: DNS and SNI
 * Nested/Hierarchical Monitoring Objects
 * Interfaces classification
 * Traffic drops below threshold
 * Changing moving average thresholds without restarting the collector
 * Exporting data to ClickHouse

 * Full description of configuration files
 * Main configuration file `xenoeye.conf`
 * Device configuration (sampling rate and interface classification) `devices.conf`
 * Description of the monitoring object `mo.conf`
 * Files with thresholds
 * IP Lists

 * Internals
 * General remarks
 * Worker and auxiliary threads
 * Monitoring objects and filters
 * How to add a new Netflow field to the collector
 * Time source
 * Fixed time windows
 * Moving averages
 * IP lists
 * GeoIP and AS databases

## Plans for the future

Right now we don't plan to add new features. We look at stability, work results, try to fix bugs and make the code simpler and more understandable.

## 关联链接

- http://server-address:3000`,

## 导航

- 项目页：[[10-项目/github.com_ea18a831]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
