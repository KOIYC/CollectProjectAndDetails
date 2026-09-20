---
type: "project"
title: "Consistent Hashing Proofs"
project_url: "https://ch.terabyteoff.com/"
first_seen: "2026-09-20T09:20:20+08:00"
sources:
  - lobsters
tags:
  - 项目
  - lobsters
  - compsci
  - math
lang: "en"
stale: true
---

# Consistent Hashing Proofs

- **项目链接**：https://ch.terabyteoff.com/
- **首次收录**：2026-09-20T09:20:20+08:00
- **来源渠道**：Lobsters
- **标签**：compsci, math
- **最新指标**：得分=5 · 评论=0

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T02:36:26+08:00 | Lobsters | 得分=4 · 评论=0 | [[80-归档/posts/lobsters/2026-09-20/e713a5a3db414a4c_Consistent-Hashing-Proofs]] |
| 2026-09-20T02:48:08+08:00 | Lobsters | 得分=4 · 评论=0 | [[80-归档/posts/lobsters/2026-09-20/e713a5a3db414a4c_Consistent-Hashing-Proofs]] |
| 2026-09-20T02:57:31+08:00 | Lobsters | 得分=4 · 评论=0 | [[80-归档/posts/lobsters/2026-09-20/e713a5a3db414a4c_Consistent-Hashing-Proofs]] |
| 2026-09-20T03:06:43+08:00 | Lobsters | 得分=4 · 评论=0 | [[80-归档/posts/lobsters/2026-09-20/e713a5a3db414a4c_Consistent-Hashing-Proofs]] |
| 2026-09-20T03:31:09+08:00 | Lobsters | 得分=5 · 评论=0 | [[80-归档/posts/lobsters/2026-09-20/e713a5a3db414a4c_Consistent-Hashing-Proofs]] |
| 2026-09-20T09:20:20+08:00 | Lobsters | 得分=5 · 评论=0 | [[80-归档/posts/lobsters/2026-09-20/e713a5a3db414a4c_Consistent-Hashing-Proofs]] |

## 摘要正文

Consistent Hashing Proofs  # Consistent hashing math #  And more than you wanted to know about it   Kevin Guthrie  This is a derivation of the formulas that describe the distribution of work in systems using consistent hashing to share work. It is part technical paper, part demo and part blog post, so there is a lot of math, some web assembly, but also some jokes. My hope is that it will be complete and compelling but also approachable (and interesting?) for any reader regardless of background.  This is a companion piece to this blog post I wrote for Cloudflare, so check it out if you want to hear the complete story and how we used the math here to safely reclaim 100+ TB of RAM on the edge. It also has a basic primer on what consistent hashing even is.  ## Motivation #  The main reason I'm writing this is to help out anyone in the future who is interested in this subject. When I first started researching the subject of consistent hashing and how its accuracy changes based on the number of hashes, I was frustrated by the resources that came up when googling. The results ranged from detailed (but utterly opaque to me) technical papers on the subject or understandable but incomplete d…
