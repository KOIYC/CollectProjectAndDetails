---
type: "project"
title: "Show HN: We tried to recover blurred, pixelated and redacted text (480 cases)"
project_url: "https://datablur.app/blog/blur-recovery-study"
first_seen: "2026-09-21T03:11:23+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_legitimate_key
  - story_49508614
  - show_hn
lang: "en"
---

# Show HN: We tried to recover blurred, pixelated and redacted text (480 cases)

> [!info] 一句话导读
> Skip to content DataBlur // 3.0

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://datablur.app/blog/blur-recovery-study>
> 首次收录：2026-09-21T03:11:23+08:00
> 来源渠道：HN Show HN
> 标签：author_legitimate_key, story_49508614, show_hn
> 最新指标：点赞=4 · 评论=0 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:33:52+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-21/5324888d4242277a_Show-HN-We-tried-to-recover-blurred,-pixelated-and]] |
| 2026-09-21T03:11:23+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-21/5324888d4242277a_Show-HN-We-tried-to-recover-blurred,-pixelated-and]] |

## 摘要正文

Skip to content DataBlur // 3.0  DataBlur AI Blur image Redact PDF Blog Pro en Back to blog Framework August 18, 2026 · 9 min read  We tried to recover blurred, pixelated and redacted text. Here's what came back.  Free browser extension  Blur sensitive data on your screen in one click.  100% local — no cloud, no sign-up. Works in live demos, calls, and screen recordings. Download for Google Chrome Also available for Edge Brave, Comet Firefox Short answer: if a screenshot gives an attacker what screenshots usually give (a known UI font, a known text size, a guessable filter), then light gaussian blur and small-block pixelation are not redaction. In our 480-case test, blur with a radius of 2 to 4 px gave the original text back exactly 92 to 100% of the time. Four-pixel pixelation gave it back 71% of the time. A 20%-opacity "transparent" overlay gave it back every single time. Saving the result as JPEG afterwards, the way a chat app does, barely helped. The only treatment that leaked nothing was a solid, flat box over the text.  The rule that fell out of the data is simple. If the blur radius or the pixel block is smaller than about 0.3 times the font size in pixels, assume the text c…
