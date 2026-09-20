---
type: "corpus"
item_id: "96486e636759b310"
title: "Show HN: StopReg – Email API for detecting disposable email and signup abuse"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49761700"
project_url: "https://stopreg.com/"
author: "telim2"
published_at: "2026-09-18T23:36:15Z"
captured_at: "2026-09-20T09:23:24+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-20"
pub_day: "2026-09-18"
tags:
  - 语料
  - hn_show
  - author_telim2
  - story_49761700
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: StopReg – Email API for detecting disposable email and signup abuse

> [!info] 一句话导读
> I built StopReg to address a problem I encountered while testing disposable email detection across different email validation services.One possible explanation …

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49761700>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：telim2　|　发布：2026-09-18T23:36:15Z
> 项目链接：<https://stopreg.com/>
> 采集：2026-09-20T09:23:24+08:00　|　id：`96486e636759b310`

## 正文

I built StopReg to address a problem I encountered while testing disposable email detection across different email validation services.One possible explanation for some of the gaps we observed is that email verification services may rely heavily on third-party disposable-domain lists. Maintaining a robust detection system requires continuously researching new disposable email providers and tracking domains as they appear, change, or rotate.New disposable email services and domains appear regularly, and some providers frequently change the domains they use. This can make static or infrequently updated domain lists difficult to keep current.During our testing, we also found many disposable addresses that were able to pass signup checks on online services offering free trials or attempting to prevent disposable email registrations. In some cases, those services appeared to rely on third-party email verification platforms with limited disposable email detection.The practical problem is that missed disposable addresses can contribute to free-trial abuse, fake account creation, referral abuse, and other forms of signup abuse. They can also affect the quality of email lists when temporary addresses are collected instead of addresses belonging to users who intend to receive future communications.That's what led me to build StopReg.StopReg provides an API for validating email addresses and domains and classifying addresses as disposable, temporary, throwaway, relay, alias, role-based, public, EDU, ISP, and other categories.It also includes Form Abuse Shield, which is designed to help applications protect signup and lead-generation forms from unwanted or abusive submissions using email and domain validation signals.The enforcement layer lets an application decide what to do with a validation result:BLOCK an address
WARN and allow the submission
ALLOW the addressI also built a free Disposable Email Checker so developers can test addresses without integrating the API:https://stopreg.com/check-disposable-emailFeel free to request samples of temporary email providers to test against your current validation system for detecting temporary and disposable emails.I'm interested in feedback from developers who have dealt with disposable email, fake signups, form abuse, or maintaining disposable-domain lists themselves.In particular, I'm curious about what approaches you've found reliable for detecting new disposable email providers and how you handle false positives.

## 关联链接

- https://stopreg.com/check-disposable-emailFeel

## 导航

- 项目页：[[10-项目/stopreg.com_3f588dfb]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
