---
type: "project"
title: "Show HN: Inkfeed – RSS Reader for Kindle"
project_url: "https://inkfeed.xyz/"
first_seen: "2026-09-21T01:44:01+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_adhamsalama
  - story_48325703
  - show_hn
lang: "en"
---

# Show HN: Inkfeed – RSS Reader for Kindle

> [!info] 一句话导读
> Hello.The Kindle is my favorite device and I read a lot on it, but I also like reading RSS feeds, which aren't supported on the Kindle.This requires me to eithe…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://inkfeed.xyz/>
> 首次收录：2026-09-21T01:44:01+08:00
> 来源渠道：HN Show HN
> 标签：author_adhamsalama, story_48325703, show_hn
> 最新指标：点赞=4 · 评论=1 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:27:24+08:00 | HN Show HN | 点赞=4 · 评论=1 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-21/8ed3259809dc1769_Show-HN-Inkfeed-–-RSS-Reader-for-Kindle]] |
| 2026-09-21T01:44:01+08:00 | HN Show HN | 点赞=4 · 评论=1 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-21/8ed3259809dc1769_Show-HN-Inkfeed-–-RSS-Reader-for-Kindle]] |

## 摘要正文

Hello.The Kindle is my favorite device and I read a lot on it, but I also like reading RSS feeds, which aren't supported on the Kindle.This requires me to either download the article and copy it to my Kindle (using Calibre) or sending it via Amazon's Send To Kindle feature. I dislike both options.I wanted to read RSS feeds just like I read books on my Kindle, so I (with the help of Claude) built a web-based RSS reader that's compatible with the Kindle's experimental browser (tested on PaperWhite 11). It doesn't use any JS frameworks for maximum compatibility.This RSS reader allows you to read feeds directly on the Kindle's browser, and you can also download the article directly on your Kindle or email it to yourself.Initially it was a just a simple RSS reader using a CORS proxy, and saved RSS feeds and user preferences like font size to local storage, but the Kindle browser clears local storage after a while, so I decided to add a backend to save them, then I thought why stop here?So I added the ability to email the article to yourself in case you want to add it to your Kindle library. A user tried Inkfeed and suggested I add the ability to browse Wikipedia, so I implemented that t…
