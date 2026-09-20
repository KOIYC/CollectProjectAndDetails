---
type: "corpus"
item_id: "cfdca86928fedbbb"
title: "Separate Log & Management Server - what do you use?"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1w3azet/separate_log_management_server_what_do_you_use/"
author: "TheKrakenRoyale"
published_at: "2026-08-31T19:27:22+08:00"
captured_at: "2026-09-21T03:05:12+08:00"
lang: "en"
kind: "post"
topic: AI 工具/Agent
shard: "2026-09-21"
pub_day: "2026-08-31"
tags:
  - 语料
  - reddit
  - r/selfhosted
  - Monitoring Tools
metrics: {"score": 8, "comments": 15, "upvote_ratio": 0.79}
comments_count: 18
comments_total: 18
discovered_via: "reddit:52d+settle3"
---

# Separate Log & Management Server - what do you use?

> [!info] 一句话导读
> Does anyone host their own syslog server/system separate from other services? I'm thinking about moving my n8n services to a stand alone server and adding a sys…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/selfhosted/comments/1w3azet/separate_log_management_server_what_do_you_use/>
> 指标：得分=8 · 评论=15 · 赞踩比=0.79
> 作者：TheKrakenRoyale　|　发布：2026-08-31T19:27:22+08:00
> 项目链接：—
> 采集：2026-09-21T03:05:12+08:00　|　id：`cfdca86928fedbbb`

## 正文

Does anyone host their own syslog server/system separate from other services? I'm thinking about moving my n8n services to a stand alone server and adding a syslog system.

I don't collect logs centrally now, my setup isn't large enough to justify the work, but now I'm just curious enough to learn it.

What does everyone use for log collection and analytics?

## 评论（18/18）

> **asimovs-auditor**（1 分） · 2026-08-31T19:27:42+08:00　
> Expand the replies to this comment to learn how AI was used in this post/project.

---

> **TheKrakenRoyale**（1 分） · 2026-08-31T19:30:12+08:00　
> No AI was used in this post, it's just a question for my own education..

---

> **NinthTurtle1034**（2 分） · 2026-08-31T19:36:49+08:00　
> I do use a dedicated log and metrics system, bit it still runs on my pve cluster and not on a dedicated server.
>
> I run Grafana as the frontend and Alloy as the collector. I then run VictoriaMetrics and VictoriaLogs as the actual databases.
>
> I also have a Wazuh instance running but that's more for experimenting for work, as we run Wazuh at work, and not for anything particularly meaningful for home infra.
>
> I'm not actually doing anything particularly useful with all this data yet as I've not got a notifications system setup yet, although its on the list.

---

> **neatly_flat_metre**（5 分） · 2026-08-31T19:38:00+08:00　
> I just spun up a tiny vm with graylog for exactly this, mostly to get nagios alerts into one place without digging through emails. It's overkill for my 4 containers but the dashboards are fun to stare at when I'm avoiding actual work

---

> **WordCommercial7932**（1 分） · 2026-08-31T19:56:02+08:00　
> Grafana has alerting built in if you want to avoid standing up a separate tool for it, you can wire alert rules straight off the VictoriaMetrics/VictoriaLogs data you already have. It won't be as polished as something purpose built, but it saves you from bolting on yet another service just to get pinged when something's wrong.

---

> **NinthTurtle1034**（2 分） · 2026-08-31T19:59:05+08:00　
> I'm aware Grafana has an alerting system natively, but you still need something to point it at, don't you? Something like Discord/Slsck via webhook or ntfy/apprise/gotify. I thought Grafanas own "On Call" notification app was only accessible on their paid plans.

---

> **TheKrakenRoyale**（1 分） · 2026-08-31T20:31:29+08:00　
> Thanks, I'll have to look into these. I've looked at grafana, but not deployed it, and the others are now to me!

---

> **TheKrakenRoyale**（1 分） · 2026-08-31T20:32:04+08:00　
> Awesome, thanks, will add to the list to check into!

---

> **jeyrb**（2 分） · 2026-08-31T21:44:42+08:00　
> Tried them all, settled on OpenObserve, with Vector as a pipeline for what OO can’t handle directly. Log OTel where possible, syslog otherwise

---

> **ttlequals0**（3 分） · 2026-08-31T22:07:57+08:00　
> Alloy agent on hosts sent to Loki with grafana frontend.

---

> **NinthTurtle1034**（3 分） · 2026-08-31T22:52:10+08:00　
> Yesh most ppl who go with Grafana use Loki and Prometheus as thier backends.
>
> The reason I went with victoria is Victoriametrics support influxdb (which I needed for proxmox) natively, snd Victorialogs can support syslog natively.
>
> Whereas with the others you'd need something in front if Loki snd Prometheus to conver the data. Alloy csn do that, and that's actually how I'm doing it so I do some fiwld mapping (to prvent duplicate netrics and whatnot), but having the option to use them directly is a bonus.

---

> **Charming_Skin_8549**（1 分） · 2026-09-01T07:22:39+08:00　
> VictoriaLogs should work great for centralized log collection and analytics, because it accepts logs over syslog protocol, and provides a built-in web UI for analysing the ingested logs. It is very easy to install and operate - it
>  works great with default Configs, and it consists of a single executable, which stores the ingested logs into a local folder, and splits the logs into per-day directories (partitions), which are easy to manage.

---

> **TheKrakenRoyale**（1 分） · 2026-09-01T07:25:40+08:00　
> Thanks!

---

> **terryfilch**（1 分） · 2026-09-01T21:53:29+08:00　
> \> which I needed for proxmox
>
> As an option, you can send OpenTelemetry data from Proxmox to the OTEL collector and connect VictoriaMetrics and VictoriaLogs as receivers.

---

> **NinthTurtle1034**（2 分） · 2026-09-01T21:57:29+08:00　
> That's what I ended up doing, more so I can do fiwld mapping in Alloy so I don't end up with duplicateed metrics from the octel collectir vs the native collection, as I need alloy on the hosts to collect logs. I'm baffled why pve doesn't have a syslog configuration option in the gui as it does have a log viewer that calls itself syslog.

---

> **WordCommercial7932**（1 分） · 2026-09-05T09:14:11+08:00　
> Yeah, you're right, the alerting rule is only half of it. For actual delivery I'd go with something like ntfy or apprise sitting behind the Grafana alert, apprise especially since it fans out to a ton of services from one config instead of you maintaining separate webhook setups per channel.

---

> **One-Draft-3134**（2 分） · 2026-09-05T17:42:42+08:00　
> I keep logs on a separate box too. Graylog worked, but it felt heavy for a small homelab. If you just want syslog plus search, Loki or OpenObserve might be simpler.

---

> **Smooth_Buy6230**（1 分） · 2026-09-15T02:09:07+08:00　
> I ran rsyslog to a folder for years because my setup didn't seem big enough to bother, what tipped it was wanting to search across boxes and Graylog felt heavy at that size like someone said above. I put Logmanager on a small VM on the free tier and had the firewall and n8n logs searchable the same evening. Mostly I use it to prove the thing I'm blaming isn't what broke.

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
