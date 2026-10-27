---
type: "project"
title: "Show HN: Dinemic – self-hosted ingress across multiple providers (DNS, LB, TLS)"
project_url: "https://dinemic.com/"
first_seen: "2026-10-27T23:46:32+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_didijo
  - story_50260093
  - show_hn
lang: "en"
---

# Show HN: Dinemic – self-hosted ingress across multiple providers (DNS, LB, TLS)

> [!info] 一句话导读
> I recently published a project for running self hosted, highly available ingress for your infrastructure: authoritative DNS for your own domain, load balancers …

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://dinemic.com/>
> 首次收录：2026-10-27T23:46:32+08:00
> 来源渠道：HN Show HN
> 标签：author_didijo, story_50260093, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-27T23:46:32+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-10-27/df45ea930cfe7ba8_Show-HN-Dinemic-–-self-hosted-ingress-across-multi]] |

## 摘要正文

Hey HN, I recently published a project for running self hosted, highly available ingress for your infrastructure: authoritative DNS for your own domain, load balancers and network mesh, to expose your web apps. It started over a year ago as side project to handle several websites for clients and other side projects, and finished as the replacement cert-manager, external-dns and ingress that works without k8s, and is independent from single cloud/vps provider.It ended up as the HA platform, able to manage dozens of load balancers with TLS termination (and Let's Encrypt integration), DNS servers and full redundant mesh. The design goal from the beginning was to prepare a tool with minimized risk of single point of failure and independent from single hosting.It is running all my home lab, nextcloud, gitlab and production websites for clients for the few last months.Quick links for those who want to test: https://dinemic.com - project page https://console.dinemic.com - hosted control plane, if you want to test it with your own vps and domain, without setting up whole stack https://gitlab.cloudover.io/dinemic/docs - project documentationIn high availability section of documentation you …
