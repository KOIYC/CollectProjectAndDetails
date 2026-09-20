---
type: "project"
title: "Show HN: A Prometheus exporter for Sagemcom F3896 cable modems"
project_url: "https://github.com/colinedwardwood/sagemcom-docsis-exporter"
first_seen: "2026-09-20T09:36:37+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_b1shp
  - story_49757048
  - show_hn
lang: "en"
---

# Show HN: A Prometheus exporter for Sagemcom F3896 cable modems

> [!info] 一句话导读
> colinedwardwood/sagemcom-docsis-exporter

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/colinedwardwood/sagemcom-docsis-exporter>
> 首次收录：2026-09-20T09:36:37+08:00
> 来源渠道：HN Show HN
> 标签：author_b1shp, story_49757048, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/461fd1f6c02cfe14_Show-HN-A-Prometheus-exporter-for-Sagemcom-F3896-c]] |
| 2026-09-20T09:36:37+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/461fd1f6c02cfe14_Show-HN-A-Prometheus-exporter-for-Sagemcom-F3896-c]] |

## 摘要正文

# colinedwardwood/sagemcom-docsis-exporter  Prometheus exporter for Sagemcom F3896/FAST3896S DOCSIS cable gateways (Cogeco, Breezeline, and likely other ISPs)  - Stars: 0 - Forks: 0 - Watchers: 0 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2026-07-22T18:01:06Z  ## Languages  - Dockerfile - Makefile - Python - Shell  ## Topics  - cable-modem - docsis - grafana - homelab - prometheus - prometheus-exporter - sagemcom - self-hosted  ## Top Contributors  - colinedwardwood (6 contributions)  ---  ## README  # Sagemcom DOCSIS cable modem exporter  Prometheus exporter for Sagemcom F3896/FAST3896S cable gateways (tested on Cogeco's F3896 in bridge mode). It scrapes the modem's authenticated JSON-RPC management API and exposes DOCSIS, Ethernet, and system telemetry on `:9488/metrics`.  This firmware redirects the documented F3896 REST URLs back to the GUI. This exporter talks to the same `/cgi/json-req` endpoint the web UI uses instead.  It never calls reboot, reset, configuration, or other write methods.  ## Should this work on your modem/ISP?  Probably, if you have a Sagemcom **F3896** or **FAST3896S** cable gateway — this is Sagemcom's general DOCSIS 3.1 cabl…
