---
type: "corpus"
item_id: "83d9a567bdb19f0f"
title: "Show HN: Bot scans DDoS your Django app? Hurricane 2.0 (now Rust-powered)"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50393896"
project_url: "https://django-hurricane.io/"
author: "schille"
published_at: "2026-11-06T15:52:31Z"
captured_at: "2026-11-07T09:43:25+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-11-07"
pub_day: "2026-11-06"
tags:
  - 语料
  - hn_show
  - author_schille
  - story_50393896
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Bot scans DDoS your Django app? Hurricane 2.0 (now Rust-powered)

> [!info] 一句话导读
> 🚀 Version 2.0.0 is live! Explore the release & PyPI package ↓

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50393896>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：schille　|　发布：2026-11-06T15:52:31Z
> 项目链接：<https://django-hurricane.io/>
> 采集：2026-11-07T09:43:25+08:00　|　id：`83d9a567bdb19f0f`

## 正文

Search ⌘ K ...
🚀 Version 2.0.0 is live! Explore the release & PyPI package ↓
 The Django-Native Application Server
 High-performance, battle-tested, and built specifically for Django. Zero-config WSGI & ASGI, built-in edge defense, native static serving, and deep health observability—ready for Docker, Kubernetes, and Cloud.
 Get Started View on GitHub
Bash
$ uv add django-hurricane
 Click to copy
Latest Release
 LATEST RELEASE v2.0.0 November 2026
 GitHub Release View on PyPI
Django Hurricane 2.0.0
 A major evolution of Django Hurricane featuring an async Rust-powered HTTP engine, instant bot defense, and shared-memory observability designed for high-concurrency cloud deployments.
 ⚡
 Rust HTTP Engine ( Granian ) High-throughput HTTP runtime replacing Tornado with native ASGI & WSGI handling.
🛡️
 Fast-404 Security Defense Drops automated vulnerability scans (.php, .env) in microseconds before hitting Django.
⏱️
 Token-Bucket Rate Limiter Per-IP volumetric throttling with zero log-flooding overhead to prevent log DoS.
📊
 Shared-Memory Metrics Lock-free atomic POSIX shared memory buffers aggregating cross-worker Prometheus state.
Quick Install: uv pip
uv add django-hurricane==2.0.0 Copy
Built for Production Excellence
 Engine
 High-Performance Granian Core
 Fast HTTP parsing powered by Hyper & Tokio. Delivers zero-copy networking, async socket dispatch, and 2x higher throughput than Gunicorn or Tornado.
Static & Media
 Nginx-Grade Asset Serving
 Native Rust file streaming with kernel sendfile and HTTP 304 caching. Includes zero-setup dynamic finders fallback for development and automated collectstatic workflows.
Edge Shield
 Fast-404 Security Defense
 Instantly drops automated scanners (probing for .php , /.env , /wp-admin/ ) at the gateway in <0.35 microseconds. Shields Django middleware, sessions, and database connection pools.
DoS Defense
 Token-Bucket Rate Limiter
 Gateway rate limiting with client IP resolution via X-Forwarded-For for load balancers and Ingress. Silently drops volumetric floods with zero log spam.
Observability
 Deep Health & Prometheus
 Built-in /alive , /ready , /startup , and /metrics endpoints. Compatible out-of-the-box with AWS ALBs, Docker healthchecks, Prometheus, and Kubernetes probes.
Zero Config
 WSGI & ASGI Auto-Detection
 Run any project with python manage.py serve . Seamlessly auto-detects WSGI_APPLICATION or ASGI_APPLICATION from your settings with zero extra config files.
The Django-Native Advantage
 Django was developed with a batteries-included philosophy and gracefully handles complex web application challenges. But in production—whether running on a single Docker container, an AWS/Fly.io PaaS, or an autoscaling Kubernetes cluster—Django needs more than generic server wrappers like Gunicorn.
 It's Not Just About Running a Container
 Generic servers like Gunicorn, Uvicorn, and Nginx know nothing about Django settings, URL patterns, or database lifecycles. Hurricane brings Django-native intelligence to the application server layer:
 Zero-Nginx Architecture: Serve static and media files natively with kernel sendfile speed, or develop with live dynamic finders without running collectstatic .
 Edge Attack Immunity: Automated bot vulnerability scans ( wp-login.php , .env ) are dropped at Tier 2 without ever touching Django middlewares or database connections.
 Migration & Health Synchronization: Preflight database migrations ( --check-migrations-apply ) prevent traffic routing until the database is ready.
 Traffic Shedding & Deadlock Detection: Real queue depth metrics signal load balancers and orchestrators when worker queues saturate, diverting traffic before requests time out.
 Hurricane solves these architectural friction points directly at the server layer, giving your Django applications the reliability and resilience required in modern cloud platforms.
 Proven Track Record
 Developed and maintained by Blueshoe and open-source contributors:
 Battle-tested in Production: Running critical Django workloads across enterprise Kubernetes clusters since 2020.
 Thorough Test Coverage: Comprehensive test suite with automated Kubernetes end-to-end (k3d) validation and cross-process telemetry tests.
 Independently Benchmarked: 2x throughput increase and 100% elimination of false probe flaps verified in the django-hurricane-bench suite.
 Cloud-Native Standards: Fully compliant with CNCF standards, OpenMetrics, and 12-factor application guidelines.
 Quickstart
 1. Install Hurricane
 Astral uv uv add django-hurricane
 Copy to clipboard
 pip pip install django-hurricane
 Copy to clipboard
 2. Add to INSTALLED_APPS
 settings.py INSTALLED_APPS = [
 # Standard Django apps...
 "django.contrib.admin" ,
 "django.contrib.auth" ,
 # ...
 # Add Hurricane:
 "hurricane" ,
 ]
 Copy to clipboard
 3. Launch Your Server
 python manage.py serve
 Copy to clipboard
 2026-10-21 12:00:00 INFO hurricane.server.general Django Hurricane web server active.
 2026-10-21 12:00:00 INFO hurricane.server.fast_404 Fast-404 active in prefix mode (9 prefixes, 31 signatures)
 2026-10-21 12:00:00 INFO hurricane.server.limiter Rate limiter active: 10.0 req/s (burst: 30) [IP Header: X-Forwarded-For]
 2026-10-21 12:00:00 INFO hurricane.server.general Starting probe application running on port 8001 (/startup, /alive, /ready, /metrics)
 2026-10-21 12:00:00 INFO hurricane.server.general Starting HTTP Server on port 8000
 2026-10-21 12:00:00 INFO hurricane.server.general Startup time is 0.114 seconds
 Copy to clipboard
 Read the Getting Started Guide Explore the Product Roadmap → Community & Support
 Have questions, architectural ideas, or need help optimizing your deployment? Join the community:
 Chat with the team on Discord
 Follow and connect on LinkedIn
 Star the project and contribute on GitHub
The Django Hurricane Community & Blueshoe
Discord LinkedIn Legal Notice Privacy Policy

## 导航

- 项目页：[[10-项目/django-hurricane.io_bf1b5f16]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
