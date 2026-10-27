---
type: "corpus"
item_id: "157d526f95f9af2e"
title: "Show HN: TeamOnly, a place IT can approve for vibe-coded internal apps"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50258151"
project_url: "https://teamonly.dev/"
author: "xoail"
published_at: "2026-10-27T12:32:09Z"
captured_at: "2026-10-27T23:46:32+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-27"
pub_day: "2026-10-27"
tags:
  - 语料
  - hn_show
  - author_xoail
  - story_50258151
  - show_hn
metrics: {"points": 2, "comments": 1, "engagement_velocity": 2}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: TeamOnly, a place IT can approve for vibe-coded internal apps

> [!info] 一句话导读
> Skip to content Features

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50258151>
> 指标：点赞=2 · 评论=1 · engagement_velocity=2
> 作者：xoail　|　发布：2026-10-27T12:32:09Z
> 项目链接：<https://teamonly.dev/>
> 采集：2026-10-27T23:46:32+08:00　|　id：`157d526f95f9af2e`

## 正文

Skip to content Features
 For IT
 Templates
 Pricing
 Docs
 Sign in Start free EN Language
 EN English
 ES Español
 DE Deutsch
 IT Italiano
 PT Português
 AR العربية
 JA 日本語
 RU Русский
 HE עברית
 ZH 简体中文
 KO 한국어
Menu
 Close
 01 Features
 02 For IT
 03 Templates
 04 Pricing
 05 Docs
 Sign in Start free English
 Español
 Deutsch
 Italiano
 Português
 العربية
 日本語
 Русский
 עברית
 简体中文
 한국어
Private hosting for internal tools built with AI
 Your AI-built tools. Team only.
You built something useful with Claude Code or Cursor. Type one command and it is online at a private link that only your coworkers can open, with their work Google or Microsoft account or a code sent to their work email. We take care of the security. You don’t write any of it.
 Try free for 14 days See how it works
 No card needed for the trial. Then from $19 a month. You can deploy a few minutes after you start.
expenses.acme.teamonly.app
 Staff only
 Expenses
 Acme Supply Co.
 G Sign in with Google M Sign in with Microsoft
 Or get a code by email you@acme.com Email me a code
 Only @acme.com accounts can sign in.
 Built with TeamOnly
acme.com Staff DO Dana Okafor
 dana @acme.com
Signed in
$ npx teamonly deploy Live at https://expenses.acme.teamonly.app Only @acme.com accounts can sign in
01 The usual way
 You built it in an afternoon. Sharing it shouldn’t take a month.
It works on your laptop. Getting it to the five people who need it usually means a list like this.
A login system
 A database somewhere
 A server to keep running
 A safe place for passwords and keys
 A ticket to IT, and a wait
 Handled With one command
Dana's laptop
$ npx teamonly deploy
 Your link expenses.acme.teamonly.app
 Live
Your team opens it
MR Marco
 Work account Signed in
PS Priya
 Work account Signed in
LK Lee
 Work account Signed in
Dana built an expense tool that only runs on her laptop. She types one command, npx teamonly deploy, and gets a link: expenses.acme.teamonly.app. Three coworkers, Marco, Priya and Lee, open the link, sign in with their work account, and the same tool opens for each of them.
 Replay
 From one laptop to the whole team: one command, one link, and coworkers sign in with their work accounts.
 TeamOnly crosses that list off for you.
 No servers to rent, no login code to write, no ticket to IT. It is for internal apps only, by design , so the only people who ever see your tool are the people you work with.
 That includes the security. Sign-in, company-only access, who can open each app, keeping each app’s data separate and keeping your apps out of search engines: we handle all of it, and you write none of it.
02 Deploy
 One command, one link
When your tool works, you type npx teamonly deploy . A minute later it has its own address that you can paste into Slack, Teams or an email.
Terminal ~/expenses
 $ npx teamonly deploy ✔ Bundled your app ✔ Database created ✔ Login set up for acme.com ✔ Live at https://expenses.acme.teamonly.app Only @acme.com accounts can sign in
A terminal. Someone types npx teamonly deploy. The app is bundled, a database is created and login is set up for acme.com. Then: Live at https://expenses.acme.teamonly.app. Only @acme.com accounts can sign in.
 Replay
 The deploy, start to finish. The link at the end is the one you send your team. 1 Add TeamOnly
 npx teamonly init adds instructions your AI reads, so it builds the kind of app that deploys first time.
2 Ask for the tool
 In plain English. "Build an expense approval tool" is a fine start.
3 Deploy and send the link
 Change something later? Deploy again. Same link.
Or just ask your AI
 In Claude Code or Cursor, type “deploy this on TeamOnly” . It sets up the app, asks for your work email and the code we send you, and offers a 14-day free trial if your company isn’t signed up yet.
expenses Your tool . acme Your company . teamonly.app The locked door
 Every app gets an address like this. Opening it without a company account gets you a sign-in screen and nothing else.
 Every step, from your laptop to your team
Expenses app expenses.acme.teamonly.app
Staff only Checked here, before the app
 SK sam@acme.com Signed in
 ? randomperson@gmail.com Turned away
 a bot, no login Turned away
A door marked Staff only stands in front of the expenses app. Sam, signed in as sam@acme.com, is checked at the door and walks in. Next, randomperson@gmail.com and a bot are checked at the same door and turned away. They never reach the app, because the check happens at the door, before the app.
 Replay
 Someone with an @acme.com account walks in. A personal Gmail, a bot or a stranger is stopped at the door, before the app ever loads. acme.com Staff SR Sam Reyes
 sam @acme.com
Signed in gmail.com Guest U Unknown
 someone @gmail.com
Turned away
03 Who gets in
 Only your company gets in
 Coworkers sign in with the work account they already have: Google, Microsoft, or a code sent to their work email. No new account, no password to share, no extra seats.
 Anyone else is turned away at the door, even if they have the link. The check happens before your app runs, so a mistake in your app cannot let a stranger in. A forwarded link is just a very nice sign-in screen.
 How company-only login works
04 Included
 A database, file storage and secrets, already set up
 Your tool needs to remember things. On the first deploy it gets its own database and a place for files, with nothing to sign up for.
 API keys and passwords go in with npx teamonly secrets set , never in your code. Each app's data stays in that app.
First deploy
 Your app
A database
 File storage
 Secret keys
 Company login
 No setup
On the first deploy, four parts snap into place around the app like pieces of a kit: a database, file storage, secret keys and company login. There are no setup steps.
 Replay
 On the first deploy, a database, file storage and secrets click into place. Nothing to configure. Deploy receipt
 expenses.acme.teamonly.app
 Database ready
 File storage ready
 Secrets stored
 Login on
No. 1
 Live
05 Your AI tool
 Made for Claude Code and Cursor
AI tools are good at writing apps and bad at guessing where they will live. TeamOnly gives yours a short set of instructions, so it writes an app that fits: a simple front end, a small API, and our login, database and files already plugged in.
Your AI coding tool
 Build me an expense approval tool for my team
 Building it now.
 Done. Your expense tool is ready.
Expense approvals
 Taxi to client Priya $38.50 Approve
 Team lunch Marco $112.00 Approve
 Printer ink Lee $64.20 Approve
$ npx teamonly deploy
 Live at expenses.acme.teamonly.app
In an AI coding tool, someone types: Build me an expense approval tool for my team. The app's screen takes shape: a list of expenses, each with an Approve button. Then one command, npx teamonly deploy, and the tool is live at expenses.acme.teamonly.app.
 Replay
 A plain-English request becomes an app, and the app becomes a deploy. Share a Claude Code app with your team Claude reads the skill file, writes the app, and can run the deploy for you.
 Deploy a Cursor project for your team The same instructions, as rules Cursor’s agent follows.
 Built it somewhere else? How to share any AI-built app with just your team, with every option compared.
06 For IT
 IT can see every app
 People are already building these tools. Here they land in one place your IT team can see.
 Every app, its owner, who can open it and when it last changed
 Each app kept apart from the others: data, files, cookies and secrets
 Sign-in checked before any app code runs
 What IT gets, in detail
App register acme.com App Owner Who can open it Last deploy
 expenses dana@acme.com Everyone at acme.com Today, 9:41
 inventory marco@acme.com 6 people Yesterday
 lookup priya@acme.com priya, marco +3 Oct 21
 requests lee@acme.com Everyone at acme.com Oct 18
Offboarded marco@acme.com Access removed from 2 apps
An app register for acme.com fills in row by row. expenses, owned by dana@acme.com, open to everyone at acme.com, last deployed today at 9:41. inventory, owned by marco@acme.com, open to 6 people, deployed yesterday. lookup, owned by priya@acme.com, open to priya, marco and 3 others, deployed October 21. requests, owned by lee@acme.com, open to everyone at acme.com, deployed October 18. Then marco@acme.com is offboarded and every line that gave him access is struck through.
 Replay
 The app list fills in as people deploy: app, owner, who has access, last deploy.
07 Ideas
 What people build
Small tools that one team needed and nobody had time to buy. Each one starts as a sentence like these.
01 Expense approval
 For finance and every manager
> People upload a receipt, their manager approves or rejects it, and finance sees everything approved this month.
02 Inventory tracker
 For the warehouse and the front office
> Track stock by bin. Anyone on the floor can log a count from their phone, and I get a list of what is running low.
03 Request form
 For office managers and ops
> A form for equipment requests. It saves who asked, I can mark each one ordered or done, and people can check their status.
See all five starting templates
Open now
 Pricing
Builder $19 a month. Team $249 a month. People who just use your apps: free .
 Try free for 14 days See plans and subscribe
09 FAQ
 Questions people ask
 All questions and answers
Do my coworkers need to make an account?
 No. They sign in with the work Google or Microsoft account they already use, or with a code sent to their work email. No new password, no invite to another tool, and people who only use your apps are not seats you pay for. How company login works .
Can someone outside my company open the link?
 No. The link opens a sign-in screen, and only accounts on your company email domain get past it. A forwarded link or a personal Gmail account is turned away before your app loads.
Do I need to know how to code?
 Not really. You describe the tool to Claude Code or Cursor, and the instructions TeamOnly adds to your project tell it how to build an app that deploys. You will type two commands, and we show you which ones .
Early access
 Put your first tool online this week.
 TeamOnly is in early access, and every plan is open now. Try it free for 14 days with no card, or subscribe. Either way, your company is ready right away, and three commands put your first app online.
 Try free for 14 days Or subscribe now No card for the trial. Then from $19 a month, cancel any time.
Not ready? Get updates
 Work email
 Get updates
 Use your work email. We write rarely, and only when there is news worth sending.
 Leave this empty
Questions go to hello@teamonly.dev , and a person answers.
Early access
 Admit one team
 Valid for your company email domain only.
Open now
Hosting for the tools your team builds with AI. Internal apps only.
Product
 How it works
 Features
 Company databases
 Templates
 Internal tools
 Pricing
 Guides
 Compare
 Start free
 Get updates
For IT
 For IT
 Security
 Shadow AI apps
 Secure an AI-built app
 Docs
 MCP server
 llms.txt
Deploy from
 Claude Code
 Cursor
 Codex
 Windsurf
 GitHub Copilot
 Lovable, Bolt, v0
 Replit
Contact
 hello@teamonly.dev
 Manage billing
 Privacy
 Terms
 Data processing (DPA)
Language
 English
 Español
 Deutsch
 Italiano
 Português
 العربية
 日本語
 Русский
 עברית
 简体中文
 한국어
 © 2026 TeamOnly
 This website is the only public thing we host.

## 评论（1/1）

> **bemeeker** · 2026-10-27T13:22:06.000Z　
> This is sweet. It’s very similar to an open source project I’ve been working on called Pando! (https://github.com/trypando/pando).It’s cool to see other people seeing this problem and trying to solve it too!

## 关联链接

- https://expenses.acme.teamonly.app
- https://expenses.acme.teamonly.app.

## 导航

- 项目页：[[10-项目/teamonly.dev_9588fa58]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
