---
type: "corpus"
item_id: "91a70c733c7febfc"
title: "Show HN: Tab – a browser engine from scratch in Rust, with a demo to install"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50585601"
project_url: "https://gettab.dev/"
author: "jakelami"
published_at: "2026-11-21T03:24:13Z"
captured_at: "2026-11-21T14:45:01+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-21"
pub_day: "2026-11-21"
tags:
  - 语料
  - hn_show
  - author_jakelami
  - story_50585601
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Tab – a browser engine from scratch in Rust, with a demo to install

> [!info] 一句话导读
> A DIFFERENT KIND OF BROWSER

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50585601>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：jakelami　|　发布：2026-11-21T03:24:13Z
> 项目链接：<https://gettab.dev/>
> 采集：2026-11-21T14:45:01+08:00　|　id：`91a70c733c7febfc`

## 正文

Tab .
The browser
 The evidence
 Security
 Try the demo
A DIFFERENT KIND OF BROWSER
Tab .
A new browser. Not a wrapper.
An independent web browser, built on its own engine in Rust. Familiar on the surface. Entirely new underneath.
Try the Linux demo
 See the test results
Pre-alpha Linux x86-64 Real engine. Real tests.
Take a look
01 / THE EXPERIENCE
The browser is the point.
No Chromium, WebKit, or Gecko behind the curtain. Just Tab, rendering its own interface with the same engine it uses for the web.
Tab's start page: plain HTML and CSS, drawn by Tab's own engine.
A pre-release build of Tab on Linux. The screenshots are unedited, and the engine drawing these pages is the one the tests below measure.
02 / YOUR TURN
Take it for a spin.
The current experimental Linux build is ready for curious people to break it. One command installs Tab and opens a demo page.
Tab is pre-alpha. It hasn't had a security audit, and plenty of real sites still break. Don't use it for banking, trading, or important logins. The first launch asks you to acknowledge this. While in pre-alpha, Tab counts its testers with one anonymous ping a day: a random ID, the version and your distro, never what you browse.
TERMINAL / INSTALL TAB
$ ./hello-world-but-make-it-a-browser
curl -fsSL https://gettab.dev/install.sh | sh -s -- --demo
 Copy command
Current build 0.1.3107, built November 21, 2026.
The script verifies SHA-256 before installing. Read the script first .
Demo builds update themselves when a new build ships, and ask you to update after seven days. Found something broken? Tell us on X .
03 / THE RECEIPTS
Tested against the web.
No Chromium, WebKit or Gecko underneath: Tab's engine is new, test-driven and spec-remedied. It passes 1,886,506 of 1,917,339 tests across five upstream suites.
Build 0.1.3096, measured November 20, 2026.
Test262 100% 102,582 of 102,582
 WPT testharness 98.59% 1,563,131 of 1,585,538
 WPT rendering 91.19% 28,166 of 30,888
 WPT remaining compatibility 90.45% 54,006 of 59,710
 WebAssembly spec 100% 138,621 of 138,621
One developer architects the engine, builds the test pipelines, checks every result and calls out anything that doesn't hold up. AI agents, mostly Claude and GPT, write most of the code. The web's own test suites decide what's done.
Pinned upstream catalogs under suite discovery/manifest rules; fixtures/support files excluded. See suite notes for catalog exclusions and identity caveats. NOT_RUN, SKIP and harness errors remain in totals; only PASS counts as a pass. Raw results
04 / THE HONEST PART
No shortcuts on trust.
About 70% of serious security bugs in Chrome are memory-safety bugs, by Chromium's own count . Writing Tab in Rust takes most of those off the table. The other 30% are logic: which site may read what, and when. That part is real work, built into the engine and tested side by side with Chromium with every request on the wire recorded. Here is where it stands.
In place
Sites can't read each other's data: cross-origin checks on fetch, XHR, redirects and preflights.
 Cookies follow HttpOnly and SameSite, across frames and redirects.
 Cross-origin images, fonts and frames can't leak through canvas, element capture or Location.
 One site's cached response is never served to another.
 Referrer Policy, Mixed Content blocking and Upgrade Insecure Requests.
 Subresource Integrity and Trusted Types.
Still open
No operating-system sandbox yet: the browser runs as a single process.
 Content Security Policy is only partly enforced.
 No independent security review yet.
245 security findings logged so far, each with its fix or the reason for a decision; 179 are fully fixed. 3 still open. Record as of November 12, 2026.
Tab . A new browser, on a new engine. An experiment you can actually run.
Download Raw test results Security notes Get in touch

## 关联链接

- https://gettab.dev/install.sh

## 导航

- 项目页：[[10-项目/gettab.dev_f073e4d4]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
