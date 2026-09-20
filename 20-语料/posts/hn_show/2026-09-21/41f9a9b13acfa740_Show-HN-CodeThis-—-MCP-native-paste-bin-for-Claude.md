---
type: "corpus"
item_id: "41f9a9b13acfa740"
title: "Show HN: CodeThis — MCP-native paste bin for Claude Code users"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47948451"
project_url: "https://codethis.dev/"
author: "Patrity"
published_at: "2026-04-29T13:49:36Z"
captured_at: "2026-09-21T02:52:37+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-29"
tags:
  - 语料
  - hn_show
  - author_Patrity
  - story_47948451
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:174d"
---

# Show HN: CodeThis — MCP-native paste bin for Claude Code users

> [!info] 一句话导读
> New Paste Pricing Sign in Sign up

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47948451>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：Patrity　|　发布：2026-04-29T13:49:36Z
> 项目链接：<https://codethis.dev/>
> 采集：2026-09-21T02:52:37+08:00　|　id：`41f9a9b13acfa740`

## 正文

New Paste Pricing Sign in Sign up
const "hello world" () => {} if (true): async import { ... } return null => !== &&  === true .map() ### npm i await
 v1.0.0
Try the live editor below ↓
 Not your average paste bin.
 $ mcp-native paste bin · built for claude code · free forever
 Paste now Sign up free
playground.md
 Try editing — preview updates live
Syntax highlighting for 100+ languages
 JavaScript TypeScript Python Rust Go Markdown HTML CSS JSON YAML SQL Java C++ C# Swift Kotlin Ruby PHP Vue React Svelte Bash PowerShell Lua Elixir Erlang Haskell Clojure Scala Dart R Julia Objective-C Perl Shell Zsh Fish Docker GraphQL Protobuf TOML INI XML LaTeX Solidity WebAssembly Assembly F# OCaml Nim Crystal Groovy CoffeeScript JavaScript TypeScript Python Rust Go Markdown HTML CSS JSON YAML SQL Java C++ C# Swift Kotlin Ruby PHP Vue React Svelte Bash PowerShell Lua Elixir Erlang Haskell Clojure Scala Dart R Julia Objective-C Perl Shell Zsh Fish Docker GraphQL Protobuf TOML INI XML LaTeX Solidity WebAssembly Assembly F# OCaml Nim Crystal Groovy CoffeeScript
$ codethis
CodeThis is a fast, minimal paste and code-sharing service for developers — 100+ languages with syntax highlighting, rich MDC components for docs-grade pastes, and an MCP server so AI assistants like Claude can create pastes directly from chat. Free tier includes the REST API + MCP; Pro at $9/mo adds password-protected pastes, unlimited documents, and premium image export.
Features
 Everything you need
 CodeThis combines the simplicity of a paste bin with the power of rich documentation tooling.
Rich Markdown with Custom Components
Go beyond plain text. Use MDC syntax to embed alerts, steps, code groups, and more — all rendered beautifully.
# Welcome
:: alert { type= "info" }
Beautiful MDC components.
 ::
:: steps
1. Write markdown
2. Embed components
3. Ship it
 ::
100+ Language Syntax Highlighting
From JavaScript to Rust, Python to YAML — every language gets full syntax highlighting powered by CodeMirror.
const greet = ( name ) => {
 return `Hello, ${name}!`
 }
Organize with Folders
Group your pastes into folders and collections. Keep your snippets organized the way your brain works.
📁 work
 ├─ api-notes.md
 └─ deploy.sh
 📁 snippets
 └─ regex.txt
Share Links or Invite Users
Copy a public link or invite specific people by email or username. Invitees land on the doc the moment they sign up — no friction, no account-seat math.
codethis.dev/doc/xK9vAqL copied
Password Protection (Pro)
Add a password to sensitive pastes. Only people with the password can view the content. Available on Pro.
•••••••• encrypted
API & MCP Server
Integrate CodeThis into your workflow with our REST API or use the MCP server with AI assistants.
# REST API
 POST /api/pastes
 { "content" : "..." , "language" : "js" }
# MCP Server
 claude → codethis.dev/mcp
Instant Screenshots
Turn any paste into a share-ready screenshot with macOS/Windows/terminal window chromes, gradient backdrops, and 8 syntax themes. Export as PNG or WebP. Premium gradients on Pro.
See it in action
 MDC makes docs beautiful
 Write rich documentation using simple markdown syntax — no HTML, no fuss.
write .
get .
setup-guide.md
Write this
 Get this
Project Setup Guide
 Prerequisites: Node.js 18+ and pnpm installed
Clone the repository
 Install dependencies with pnpm install
 Copy .env.example to .env and fill in your values
 Run pnpm dev to start the development server
pnpm npm yarn
 pnpm install
 pnpm dev
npm install
 npm run dev
yarn install
 yarn dev
The dev server runs at http://localhost:3000 by default.
How it works
 Three steps to sharing
 No setup, no configuration. Just paste and share.
Paste
Drop in your code or write markdown with custom components. Pick your language, add a title — done.
01
Share
Copy your unique link and send it anywhere. Viewers see a beautifully rendered version, no account needed.
02
Done
That's it. Your paste lives at a shareable URL. Edit it later, add it to a folder, or protect it with a password on Pro.
03
Pricing
 Simple, honest pricing
 Free for every developer. Pro from $9/mo when you need more.
Anonymous
Try it out, no account needed.
 Free
Unlimited pastes (temporary)
 100+ language highlighting
 MDC component support
 Pastes expire after 7 days
Start pasting
Free
For developers who share regularly.
 Free
Everything in Anonymous
 Up to 100 pastes, any duration (forever available)
 Public / Unlisted / Private visibility
 Folders + public profile
 REST API + MCP server (2 keys)
Sign up free
Pro
 Most popular
 For power users who need more.
 $9
 /month
Everything in Free
 Password-protected pastes
 Unlimited documents · 5 MB per paste
 Premium image export (3× retina, WebP, custom colors)
 API: 20 keys + higher rate limits
 Collections (coming soon)
 Email support
Get Pro
See full feature comparison
Popular languages
 Each language has a dedicated landing page with examples, use cases, and highlighting notes.
See all 30+ languages →
 JavaScript TypeScript Python Rust Go Java Ruby PHP SQL Bash
How CodeThis compares
 Honest head-to-heads with the other tools developers reach for — feature matrices, clear trade-offs.
See all comparisons →
 vs
 GitHub Gist
 Git-backed snippets under your GitHub identity.
 If you need Git-grade version history on a snippet, Gist wins. For everything else — rich markdown & MDC, anonymous sharing, password protection, real expiration controls, and an MCP integration your AI assistant can actually use — CodeThis is built for it.
 vs
 Pastebin.com
 The original pastebin, in ~2008 form.
 Pastebin is what you used in 2008. CodeThis is what a pastebin should look like in 2026 — clean editor, rich markdown, MDC components, modern OG previews, and an API that isn't walled behind a "Pro" upsell on every page.
 vs
 Carbon.now.sh
 Turn code into a beautiful PNG.
 Carbon turns code into a picture. CodeThis turns code into a URL — and also a picture, right inside the Image tab on any paste. Two outputs, one tool.
Ready to paste?
 Join CodeThis and start sharing code beautifully.
Start pasting Sign up free
Docs
 API
 Languages
 Compare
 Pricing
 Contact
 Legal
© 2026 CodeThis. Not your average paste bin.

## 关联链接

- http://localhost:3000

## 导航

- 项目页：[[10-项目/codethis.dev_ac2fa787]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
