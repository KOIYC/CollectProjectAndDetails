---
type: "corpus"
item_id: "eab6ac325a6599b8"
title: "Show HN: Fix 1.0 – Ruby tests written as RFC 2119 specifications"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50320472"
project_url: "https://fixrb.dev/framework/release/2026/10/31/fix-1.html"
author: "cyrilllllll"
published_at: "2026-10-31T21:36:33Z"
captured_at: "2026-11-01T09:38:09+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-01"
pub_day: "2026-10-31"
tags:
  - 语料
  - hn_show
  - author_cyrilllllll
  - story_50320472
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Fix 1.0 – Ruby tests written as RFC 2119 specifications

> [!info] 一句话导读
> October 31, 2026

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50320472>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：cyrilllllll　|　发布：2026-10-31T21:36:33Z
> 项目链接：<https://fixrb.dev/framework/release/2026/10/31/fix-1.html>
> 采集：2026-11-01T09:38:09+08:00　|　id：`eab6ac325a6599b8`

## 正文

Fixrb
Blog
Code
Guide
Fix 1.0 is here
October 31, 2026 · Cyril Kato
Fix 1.0 is out. Fix is a testing framework for Ruby in which a test suite is a specification: a document that says what a subject MUST , SHOULD or MAY do, in the words of RFC 2119 , and nothing about how the subject is made. I started it in Osaka in 2014 and have reworked it many times since; this is the first version I consider finished.
If it quacks like a duck
Ruby knows a duck by what it does: that is duck typing . A specification of Fix does the same: it names no class, and the test, at the end of the file, picks the subject. Here, a duck and a rubber duck, against one specification:
require "fix"
Fix :Duck do
 on :quack do
 it MUST eq "Quack!"
 end
on :swim do
 it SHOULD eq "Splash!"
 end
on :fly do
 it MAY be_true
 end
 end
class Duck
 def quack = "Quack!"
 def swim = "Splash!"
 def fly = true
 end
class RubberDuck
 def quack = "Quack!"
 def swim = "Splash!"
 end
exit([
 Fix [ :Duck ].test { Duck .new },
 Fix [ :Duck ].test { RubberDuck .new }
].all?)
ruby duck_fix.rb
 duck_fix.rb:5: Success: expected "Quack!" to eq "Quack!"
duck_fix.rb:9: Success: expected "Splash!" to eq "Splash!"
duck_fix.rb:13: Success: expected true to be true
duck_fix.rb:5: Success: expected "Quack!" to eq "Quack!"
duck_fix.rb:9: Success: expected "Splash!" to eq "Splash!"
duck_fix.rb:13: Info: NoMethodError: undefined method 'fly' for an instance of RubberDuck
 The rubber duck cannot fly, but flying was only a MAY: its line is an info, and both ducks meet the specification. Three levels tell what is required, what is recommended and what is optional, and the lines say exactly what happened, one per expectation; the status of the process says whether the whole is met. The same specification can test a class of yours, a library you depend on, or the next version of either.
What 1.0 brings
A specification is built once, when the file is loaded, and kept as data. Anything wrong in it raises before a test runs.
Each context runs in a child process: what a subject does to a global, a constant or ENV stays in its context, and the order of the contexts cannot change a result.
The matchers are those of Matchi , where the expected value makes the comparison, so that the object under test cannot vouch for itself.
test writes one line per expectation and returns whether the specification is met; run gives the results as data; match? makes a specification a matcher, so that one may require another with fix(:Name) .
About three hundred lines of code, with tests written by hand at full coverage, on Ruby 3.3, 3.4 and 4.0, resting on four small gems, matchi , spectus , aw and defi , each short enough to read before you trust it.
Around it: fix-command runs the files of a project, fix-its adds the word its , and matchi-fix brings a specification to any other test framework.
Try it
gem install fix-command
 Then the guide : a first specification, the language, the matchers one by one, the command, and what changes when you come from RSpec. Every example on its pages is run before they are published. The README is the reference. Fix needs Ruby 3.3 or later and fork(2) .
Write a specification for something you have, and see what it says. That is what Fix is for.
Filed under framework and release. All posts
Fixrb is made by Cyril Kato and sponsored by Sashité . The gems and this site are released under the MIT license.
Bluesky
Feed
GitHub
YouTube
X

## 导航

- 项目页：[[10-项目/fixrb.dev_1ca6f641]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
