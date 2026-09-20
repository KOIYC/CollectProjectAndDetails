---
type: "project"
title: "Show HN: Gander, an Android file viewer that asks for no permissions"
project_url: "https://github.com/mokshablr/gander"
first_seen: "2026-09-21T02:55:18+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_mokshablr
  - story_49119425
  - show_hn
lang: "en"
---

# Show HN: Gander, an Android file viewer that asks for no permissions

> [!info] 一句话导读
> Hi HN,I built an Android file viewer that opens PDF, Word, Excel, PowerPoint, images, video, audio, Markdown and code, and asks for no permissions at all.I have…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/mokshablr/gander>
> 首次收录：2026-09-21T02:55:18+08:00
> 来源渠道：HN Show HN
> 标签：author_mokshablr, story_49119425, show_hn
> 最新指标：点赞=211 · 评论=79 · engagement_velocity=211

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:31:46+08:00 | HN Show HN | 点赞=211 · 评论=79 · engagement_velocity=211 | [[20-语料/posts/hn_show/2026-09-21/945f405cee60ac14_Show-HN-Gander,-an-Android-file-viewer-that-asks-f]] |
| 2026-09-21T02:55:18+08:00 | HN Show HN | 点赞=211 · 评论=79 · engagement_velocity=211 | [[20-语料/posts/hn_show/2026-09-21/945f405cee60ac14_Show-HN-Gander,-an-Android-file-viewer-that-asks-f]] |

## 摘要正文

Hi HN,I built an Android file viewer that opens PDF, Word, Excel, PowerPoint, images, video, audio, Markdown and code, and asks for no permissions at all.I have always been uneasy about opening files people send me. On Android you either install a 400 MB office suite and sign in or use a small free viewer that wants storage access and ends up uploading your file to a server to render it. Also the hassle of having to download different apps for different file formats was really annoying.Gander holds no permissions, not even INTERNET so the OS itself guarantees the file cannot leave the phone.PDFs use Pdfium, media uses Media3, and Office formats are rendered by bundled JS libraries in a WebView and so no request goes to any server.It is a viewer only. Complex PowerPoint decks come out approximately right, spreadsheet charts are not drawn, and old binary .doc and .ppt are unsupported. I'll work on it as issues come up :PIt is 14 MB, MIT licensed and uploaded on Github releases.Do try it! I would love some feedback especially on files that render badly or need new support.
