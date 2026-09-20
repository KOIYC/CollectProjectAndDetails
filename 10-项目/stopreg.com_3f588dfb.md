---
type: "project"
title: "Show HN: StopReg – Email API for detecting disposable email and signup abuse"
project_url: "https://stopreg.com/"
first_seen: "2026-09-20T09:23:24+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_telim2
  - story_49761700
  - show_hn
lang: "en"
---

# Show HN: StopReg – Email API for detecting disposable email and signup abuse

> [!info] 一句话导读
> I built StopReg to address a problem I encountered while testing disposable email detection across different email validation services.One possible explanation …

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://stopreg.com/>
> 首次收录：2026-09-20T09:23:24+08:00
> 来源渠道：HN Show HN
> 标签：author_telim2, story_49761700, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T02:35:34+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/96486e636759b310_Show-HN-StopReg-–-Email-API-for-detecting-disposab]] |
| 2026-09-20T02:46:51+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/96486e636759b310_Show-HN-StopReg-–-Email-API-for-detecting-disposab]] |
| 2026-09-20T02:55:58+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/96486e636759b310_Show-HN-StopReg-–-Email-API-for-detecting-disposab]] |
| 2026-09-20T03:04:29+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/96486e636759b310_Show-HN-StopReg-–-Email-API-for-detecting-disposab]] |
| 2026-09-20T03:16:53+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/96486e636759b310_Show-HN-StopReg-–-Email-API-for-detecting-disposab]] |
| 2026-09-20T03:29:12+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/96486e636759b310_Show-HN-StopReg-–-Email-API-for-detecting-disposab]] |
| 2026-09-20T03:38:50+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/96486e636759b310_Show-HN-StopReg-–-Email-API-for-detecting-disposab]] |
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/96486e636759b310_Show-HN-StopReg-–-Email-API-for-detecting-disposab]] |

## 摘要正文

I built StopReg to address a problem I encountered while testing disposable email detection across different email validation services.One possible explanation for some of the gaps we observed is that email verification services may rely heavily on third-party disposable-domain lists. Maintaining a robust detection system requires continuously researching new disposable email providers and tracking domains as they appear, change, or rotate.New disposable email services and domains appear regularly, and some providers frequently change the domains they use. This can make static or infrequently updated domain lists difficult to keep current.During our testing, we also found many disposable addresses that were able to pass signup checks on online services offering free trials or attempting to prevent disposable email registrations. In some cases, those services appeared to rely on third-party email verification platforms with limited disposable email detection.The practical problem is that missed disposable addresses can contribute to free-trial abuse, fake account creation, referral abuse, and other forms of signup abuse. They can also affect the quality of email lists when temporary…
