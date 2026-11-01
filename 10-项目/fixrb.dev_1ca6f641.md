---
type: "project"
title: "Show HN: Fix 1.0 – Ruby tests written as RFC 2119 specifications"
project_url: "https://fixrb.dev/framework/release/2026/10/31/fix-1.html"
first_seen: "2026-11-01T09:38:09+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_cyrilllllll
  - story_50320472
  - show_hn
lang: "en"
---

# Show HN: Fix 1.0 – Ruby tests written as RFC 2119 specifications

> [!info] 一句话导读
> October 31, 2026

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://fixrb.dev/framework/release/2026/10/31/fix-1.html>
> 首次收录：2026-11-01T09:38:09+08:00
> 来源渠道：HN Show HN
> 标签：author_cyrilllllll, story_50320472, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-01T09:38:09+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-11-01/eab6ac325a6599b8_Show-HN-Fix-1.0-–-Ruby-tests-written-as-RFC-2119-s]] |

## 摘要正文

Fixrb Blog Code Guide Fix 1.0 is here October 31, 2026 · Cyril Kato Fix 1.0 is out. Fix is a testing framework for Ruby in which a test suite is a specification: a document that says what a subject MUST , SHOULD or MAY do, in the words of RFC 2119 , and nothing about how the subject is made. I started it in Osaka in 2014 and have reworked it many times since; this is the first version I consider finished. If it quacks like a duck Ruby knows a duck by what it does: that is duck typing . A specification of Fix does the same: it names no class, and the test, at the end of the file, picks the subject. Here, a duck and a rubber duck, against one specification: require "fix" Fix :Duck do  on :quack do  it MUST eq "Quack!"  end on :swim do  it SHOULD eq "Splash!"  end on :fly do  it MAY be_true  end  end class Duck  def quack = "Quack!"  def swim = "Splash!"  def fly = true  end class RubberDuck  def quack = "Quack!"  def swim = "Splash!"  end exit([  Fix [ :Duck ].test { Duck .new },  Fix [ :Duck ].test { RubberDuck .new } ].all?) ruby duck_fix.rb  duck_fix.rb:5: Success: expected "Quack!" to eq "Quack!" duck_fix.rb:9: Success: expected "Splash!" to eq "Splash!" duck_fix.rb:13: Success: …
