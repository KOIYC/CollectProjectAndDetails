---
type: "corpus"
item_id: "51c0cda58276b6b5"
title: "Question about Degoog"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1xr67z1/question_about_degoog/"
author: "joninjax1"
published_at: "2026-11-09T03:05:13+08:00"
captured_at: "2026-11-19T09:44:40+08:00"
lang: "en"
kind: "post"
topic: AI 工具/Agent
shard: "2026-11-19"
pub_day: "2026-11-09"
tags:
  - 语料
  - reddit
  - r/selfhosted
  - Need Help
metrics: {"score": 9, "comments": 8, "upvote_ratio": 0.8}
comments_count: 8
comments_total: 8
discovered_via: "reddit:14d+settle10"
---

# Question about Degoog

> [!info] 一句话导读
> I have degoog running, but I want to block search results from social media sites like Facebook, I added them to the block list in the settings, but I am still …

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/selfhosted/comments/1xr67z1/question_about_degoog/>
> 指标：得分=9 · 评论=8 · 赞踩比=0.8
> 作者：joninjax1　|　发布：2026-11-09T03:05:13+08:00
> 项目链接：—
> 采集：2026-11-19T09:44:40+08:00　|　id：`51c0cda58276b6b5`

## 正文

I have degoog running, but I want to block search results from social media sites like Facebook, I added them to the block list in the settings, but I am still getting results from Facebook. I have them added like this:
  "*facebook.com*",
  "*instagram.com*",
  "*tiktok.com*",
  "*.cdninstagram.com*",
  "*.fbcdn.net*"
Is that the right way to do it?

## 评论（8/8）

> **asimovs-auditor**（1 分） · 2026-11-09T03:05:31+08:00　
> Expand the replies to this comment to learn how AI was used in this post/project.

---

> **joninjax1**（1 分） · 2026-11-09T03:05:56+08:00　
> No AI

---

> **IMayBeIronMan**（4 分） · 2026-11-09T03:13:10+08:00　
> Should be a url per line so:
>
> facebook.com
>
> instagram.com

---

> **joninjax1**（1 分） · 2026-11-09T03:21:56+08:00　
> Oh, OK, I guess I misunderstood what it was saying, I will try that, thanks!
> OK, so I changed it /facebook.com/ it says to wrap the line in slashes to regex the domain, but it still shows me results from Facebook

---

> **joninjax1**（3 分） · 2026-11-09T06:45:58+08:00　
> OK, somehow I got it to work, I think they're might have been an extra space in the list.

---

> **mistycedar909**（2 分） · 2026-11-09T10:42:02+08:00　
> Thank you! I met the same problem with yours

---

> **kimiyah_Fremiot**（2 分） · 2026-11-09T15:01:12+08:00　
> it usually expects either plain domains or standard regex, not glob wildcards. if you strip out the asterisks and just list the base domain it should start filtering them out properly

---

> **joninjax1**（2 分） · 2026-11-09T23:35:37+08:00　
> I realized that. I was given some bad info when I searched on how to block social media in Degoog, I'm guessing the info I got was if I was editing the json, whatever the case was, I got it working.

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
