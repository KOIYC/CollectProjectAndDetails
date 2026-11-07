---
type: "project"
title: "My iOS app froze for testers and I only found out because I pulled crash files off a phone by hand. So I added Sentry, very carefully"
project_url: "https://apps.apple.com/app/id6775021634"
first_seen: "2026-11-07T09:44:39+08:00"
sources:
  - reddit
tags:
  - 项目
  - reddit
  - r/buildinpublic
lang: "en"
---

# My iOS app froze for testers and I only found out because I pulled crash files off a phone by hand. So I added Sentry, very carefully

> [!info] 一句话导读
> I'm building Echo, a small iOS app that shows you one old photo from your own camera roll every day. The whole pitch is that your photos stay on your phone. So …

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://apps.apple.com/app/id6775021634>
> 首次收录：2026-11-07T09:44:39+08:00
> 来源渠道：Reddit 独立开发版块
> 标签：r/buildinpublic
> 最新指标：得分=3 · 评论=7 · 赞踩比=1

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-07T09:44:39+08:00 | Reddit 独立开发版块 | 得分=3 · 评论=7 · 赞踩比=1 | [[20-语料/posts/reddit/2026-11-07/7d0c0577b0cd3036_My-iOS-app-froze-for-testers-and-I-only-found-out]] |

## 摘要正文

I'm building Echo, a small iOS app that shows you one old photo from your own camera roll every day. The whole pitch is that your photos stay on your phone. So for months I had zero crash reporting, on purpose.  Then version 1.41 started freezing on testers. The system watchdog was killing the app and I had no idea. I only found it because I got the .ips crash files off a test phone by hand and read them.  That was the push to add Sentry. What I actually configured, in case it helps anyone with a privacy-heavy app:  - **No screenshots.** The screen is literally people's photos. - **No view hierarchy.** Labels can contain their notes and place names. - **No session replay, no performance tracing, no IP, no email.** - **Scrubbing before send.** File paths, photo IDs and locations are stripped from every event. - **One anonymous ID across tools.** The user id is the same anonymous ID RevenueCat uses, so a crash can be matched to a purchase problem without knowing who anyone is. - **A remote kill switch.** A feature flag can turn Sentry off without shipping an update. - **The free plan is enough.** It gives 5k errors a month, and I capped the DSN at 300 events an hour. - **dSYMs upload…
