---
type: "project"
title: "Show HN: Sidekeys – Turn an iPhone into a Mac display and agent control deck"
project_url: "https://sidekeysapp.com/"
first_seen: "2026-10-30T09:46:09+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_cmillstein
  - story_50295597
  - show_hn
lang: "en"
---

# Show HN: Sidekeys – Turn an iPhone into a Mac display and agent control deck

> [!info] 一句话导读
> Your iPhone, beside your Mac.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://sidekeysapp.com/>
> 首次收录：2026-10-30T09:46:09+08:00
> 来源渠道：HN Show HN
> 标签：author_cmillstein, story_50295597, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-30T09:46:09+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-10-30/5687f481ecb9c2c8_Show-HN-Sidekeys-–-Turn-an-iPhone-into-a-Mac-displ]] |

## 摘要正文

Skip to content Sidekeys Features Pricing FAQ Join the beta Your iPhone, beside your Mac. Sidekeys turns your iPhone into a second screen for your Mac, and a control deck that knows what you're doing. Email Get the beta I'd test on  iPhone Duo  iPhone  iPad The TestFlight beta is open. Enter your email and get the link instantly. Built for iPhone Duo, works with any iPhone or iPad. Download the Mac app Free · Apple silicon · Setup guide Xcode File Edit View Product Tue 9:41 AM TaxCalculator.swift Checkout Cart.swift LineItem.swift TaxCalculator.swift Receipt.swift Tests TaxCalculatorTests.swift import Foundation struct TaxCalculator {  let rate: Decimal /// Rounds half to even, like the receipt.  func total ( for items: [ LineItem ]) -> Decimal {  let subtotal = items. reduce ( 0 ) { $0 + $1.price }  let tax = (subtotal * rate)  . rounded (scale: 2 , .bankers)  return subtotal + tax  } } extension Decimal {  func rounded (scale: Int ,  _ mode: RoundingMode ) -> Decimal {  var value = self , result = Decimal ()  NSDecimalRound (&result, &value, scale, mode)  return result  } } Design review 12:04 MK Maya JR Jordan SL Sam You You Terminal Shell Edit View 9:41 AM claude — ~/checkout ✻…
