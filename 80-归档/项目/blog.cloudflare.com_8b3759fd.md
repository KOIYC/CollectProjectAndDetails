---
type: "project"
title: "Saving another 100TB of RAM with math (and Rust)"
project_url: "https://blog.cloudflare.com/saving-100-tb-of-ram-with-math"
first_seen: "2026-09-20T09:20:20+08:00"
sources:
  - lobsters
tags:
  - 项目
  - lobsters
  - performance
  - rust
lang: "en"
stale: true
---

# Saving another 100TB of RAM with math (and Rust)

- **项目链接**：https://blog.cloudflare.com/saving-100-tb-of-ram-with-math
- **首次收录**：2026-09-20T09:20:20+08:00
- **来源渠道**：Lobsters
- **标签**：performance, rust
- **最新指标**：得分=29 · 评论=0

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T02:36:26+08:00 | Lobsters | 得分=27 · 评论=0 | [[80-归档/posts/lobsters/2026-09-20/b38a231007f303c3_Saving-another-100TB-of-RAM-with-math-(and-Rust)]] |
| 2026-09-20T02:48:08+08:00 | Lobsters | 得分=27 · 评论=0 | [[80-归档/posts/lobsters/2026-09-20/b38a231007f303c3_Saving-another-100TB-of-RAM-with-math-(and-Rust)]] |
| 2026-09-20T02:57:31+08:00 | Lobsters | 得分=27 · 评论=0 | [[80-归档/posts/lobsters/2026-09-20/b38a231007f303c3_Saving-another-100TB-of-RAM-with-math-(and-Rust)]] |
| 2026-09-20T03:06:43+08:00 | Lobsters | 得分=27 · 评论=0 | [[80-归档/posts/lobsters/2026-09-20/b38a231007f303c3_Saving-another-100TB-of-RAM-with-math-(and-Rust)]] |
| 2026-09-20T03:07:32+08:00 | HN 首页（非 Show HN） | 点赞=437 · 评论=97 · engagement_velocity=437 | [[80-归档/重复副本/20260921T004922/posts/hn_front/2026-09-20/be69d1c920579bcd_Saving-another-100TB-of-RAM]] |
| 2026-09-20T03:16:36+08:00 | HN 首页（非 Show HN） | 点赞=437 · 评论=97 · engagement_velocity=437 | [[80-归档/重复副本/20260921T004922/posts/hn_front/2026-09-20/be69d1c920579bcd_Saving-another-100TB-of-RAM]] |
| 2026-09-20T03:19:19+08:00 | Lobsters | 得分=28 · 评论=0 | [[80-归档/posts/lobsters/2026-09-20/b38a231007f303c3_Saving-another-100TB-of-RAM-with-math-(and-Rust)]] |
| 2026-09-20T03:21:04+08:00 | HN 首页（非 Show HN） | 点赞=438 · 评论=97 · engagement_velocity=438 | [[80-归档/重复副本/20260921T004922/posts/hn_front/2026-09-20/be69d1c920579bcd_Saving-another-100TB-of-RAM]] |
| 2026-09-20T03:28:01+08:00 | HN 首页（非 Show HN） | 点赞=438 · 评论=97 · engagement_velocity=438 | [[80-归档/重复副本/20260921T004922/posts/hn_front/2026-09-20/be69d1c920579bcd_Saving-another-100TB-of-RAM]] |
| 2026-09-20T03:31:09+08:00 | Lobsters | 得分=29 · 评论=0 | [[80-归档/posts/lobsters/2026-09-20/b38a231007f303c3_Saving-another-100TB-of-RAM-with-math-(and-Rust)]] |
| 2026-09-20T03:32:45+08:00 | HN 首页（非 Show HN） | 点赞=439 · 评论=97 · engagement_velocity=439 | [[80-归档/重复副本/20260921T004922/posts/hn_front/2026-09-20/be69d1c920579bcd_Saving-another-100TB-of-RAM]] |
| 2026-09-20T03:41:55+08:00 | HN 首页（非 Show HN） | 点赞=439 · 评论=98 · engagement_velocity=439 | [[80-归档/重复副本/20260921T004922/posts/hn_front/2026-09-20/be69d1c920579bcd_Saving-another-100TB-of-RAM]] |
| 2026-09-20T09:20:19+08:00 | HN 首页（非 Show HN） | 点赞=439 · 评论=98 · engagement_velocity=439 | [[80-归档/重复副本/20260921T004922/posts/hn_front/2026-09-20/be69d1c920579bcd_Saving-another-100TB-of-RAM]] |
| 2026-09-20T09:20:20+08:00 | Lobsters | 得分=29 · 评论=0 | [[80-归档/posts/lobsters/2026-09-20/b38a231007f303c3_Saving-another-100TB-of-RAM-with-math-(and-Rust)]] |

## 摘要正文

Published: 2026-09-18  Saving another 100TB of RAM with math (and Rust) | Cloudflare Blog  September 18, 2026  # Saving another 100TB of RAM with math (and Rust)  Kevin Guthrie  Mariia Iurchenko  Zaidoon Abd Al Hadi   and   Ivan Babrou  Cloudflare operates at a scale so big that even after working here for years, it doesn’t seem real. We have thousands of servers all over the world with petabytes of RAM and millions of CPU cores, and all of it is pushed to the max. As vast as those resources feel, they are still finite, and when you need every service to run on every node, it doesn’t leave room for wasted space.  At this scale, small improvements are greatly magnified, so even 1%-at-a-time improvements are worth celebrating. And some tweaks add up to a lot more: in this post, we’ll look at how small changes to a single algorithm reduced the memory footprint of one of our Pingora-based services significantly. That allowed us to reclaim more than 100TB of RAM globally, on top of the 100TB of memory the DNS team was able to shed last month.  ## Waste not  Maintaining equitable resource sharing between teams is not easy, especially in large organizations. One of the ways Cloudflare ens…
