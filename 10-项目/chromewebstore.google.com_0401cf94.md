---
type: "project"
title: "[Trading Strategy Optimizer] - My first paying customer found a bug that made the product impossible to activate"
project_url: "https://chromewebstore.google.com/detail/trading-strategy-optimize/pjgikffklocmefghdipdiidfebgbklon"
first_seen: "2026-09-21T13:03:23+08:00"
sources:
  - reddit
tags:
  - 项目
  - reddit
  - r/SideProject
lang: "en"
---

# [Trading Strategy Optimizer] - My first paying customer found a bug that made the product impossible to activate

> [!info] 一句话导读
> Chrome extension for traders. Free tier, $10.89/mo for the pro features. Shipped it, got the first subscriber, and within hours he emailed to say the licence ke…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://chromewebstore.google.com/detail/trading-strategy-optimize/pjgikffklocmefghdipdiidfebgbklon>
> 首次收录：2026-09-21T13:03:23+08:00
> 来源渠道：Reddit 独立开发版块
> 标签：r/SideProject
> 最新指标：得分=3 · 评论=13 · 赞踩比=0.67

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:24:22+08:00 | Reddit 独立开发版块 | 得分=3 · 评论=13 · 赞踩比=0.67 | [[20-语料/posts/reddit/2026-09-21/5f63721e2407444c_Trading-Strategy-Optimizer-My-first-paying-custome]] |
| 2026-09-20T09:49:24+08:00 | Reddit 独立开发版块 | 得分=3 · 评论=13 · 赞踩比=0.67 | [[20-语料/posts/reddit/2026-09-21/5f63721e2407444c_Trading-Strategy-Optimizer-My-first-paying-custome]] |
| 2026-09-20T14:14:38+08:00 | Reddit 独立开发版块 | 得分=3 · 评论=13 · 赞踩比=0.67 | [[20-语料/posts/reddit/2026-09-21/5f63721e2407444c_Trading-Strategy-Optimizer-My-first-paying-custome]] |
| 2026-09-20T14:58:58+08:00 | Reddit 独立开发版块 | 得分=3 · 评论=13 · 赞踩比=0.67 | [[20-语料/posts/reddit/2026-09-21/5f63721e2407444c_Trading-Strategy-Optimizer-My-first-paying-custome]] |
| 2026-09-21T00:04:45+08:00 | Reddit 独立开发版块 | 得分=3 · 评论=13 · 赞踩比=0.67 | [[20-语料/posts/reddit/2026-09-21/5f63721e2407444c_Trading-Strategy-Optimizer-My-first-paying-custome]] |
| 2026-09-21T00:07:47+08:00 | Reddit 独立开发版块 | 得分=3 · 评论=13 · 赞踩比=0.67 | [[20-语料/posts/reddit/2026-09-21/5f63721e2407444c_Trading-Strategy-Optimizer-My-first-paying-custome]] |
| 2026-09-21T02:58:14+08:00 | Reddit 独立开发版块 | 得分=3 · 评论=13 · 赞踩比=0.67 | [[20-语料/posts/reddit/2026-09-21/5f63721e2407444c_Trading-Strategy-Optimizer-My-first-paying-custome]] |
| 2026-09-21T03:12:37+08:00 | Reddit 独立开发版块 | 得分=3 · 评论=13 · 赞踩比=0.67 | [[20-语料/posts/reddit/2026-09-21/5f63721e2407444c_Trading-Strategy-Optimizer-My-first-paying-custome]] |
| 2026-09-21T03:18:40+08:00 | Reddit 独立开发版块 | 得分=3 · 评论=13 · 赞踩比=0.67 | [[20-语料/posts/reddit/2026-09-21/5f63721e2407444c_Trading-Strategy-Optimizer-My-first-paying-custome]] |
| 2026-09-21T09:55:50+08:00 | Reddit 独立开发版块 | 得分=3 · 评论=13 · 赞踩比=0.67 | [[20-语料/posts/reddit/2026-09-21/5f63721e2407444c_Trading-Strategy-Optimizer-My-first-paying-custome]] |
| 2026-09-21T13:03:23+08:00 | Reddit 独立开发版块 | 得分=3 · 评论=13 · 赞踩比=0.67 | [[20-语料/posts/reddit/2026-09-21/5f63721e2407444c_Trading-Strategy-Optimizer-My-first-paying-custome]] |

## 摘要正文

Chrome extension for traders. Free tier, $10.89/mo for the pro features. Shipped it, got the first subscriber, and within hours he emailed to say the licence key field would not accept a paste.  Not "was buggy". Would not accept a paste at all. A 36-character key that nobody is going to type by hand. The product was, functionally, unactivatable for anyone who did not happen to type it out.  Why it happened: my panel is injected into TradingView, which listens for keyboard events globally because it has chart shortcuts on most letter keys. I already had a guard stopping keyboard events from escaping my panel — keydown, keypress, keyup, beforeinput, input. Paste is not in that list, because paste is not a keyboard event. TradingView cancels clipboard events at the document level so it can paste drawings onto a chart, and my input never saw the key.  Six test suites. 130-odd assertions. Every one of them passed, because I had tested typing.  Three things I took from it:  1. I tested the mechanism and not the gesture. Nobody types a licence key. The test that mattered was "can a human get the key from the email into the box", and I never wrote it.  2. One customer found in hours what I…
