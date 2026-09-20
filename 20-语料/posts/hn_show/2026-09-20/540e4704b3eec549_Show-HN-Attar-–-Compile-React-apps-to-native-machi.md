---
type: "corpus"
item_id: "540e4704b3eec549"
title: "Show HN: Attar – Compile React apps to native machine code"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49751702"
project_url: "https://attar.dev/"
author: "ifdotpy"
published_at: "2026-09-18T08:47:08Z"
captured_at: "2026-09-20T09:36:42+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-20"
pub_day: "2026-09-18"
tags:
  - 语料
  - hn_show
  - author_ifdotpy
  - story_49751702
  - show_hn
metrics: {"points": 6, "comments": 0, "engagement_velocity": 6}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: Attar – Compile React apps to native machine code

> [!info] 一句话导读
> Attar — the web, compiled.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49751702>
> 指标：点赞=6 · 评论=0 · engagement_velocity=6
> 作者：ifdotpy　|　发布：2026-09-18T08:47:08Z
> 项目链接：<https://attar.dev/>
> 采集：2026-09-20T09:36:42+08:00　|　id：`540e4704b3eec549`

## 正文

Attar — the web, compiled.

# The web, compiled.

 Build desktop apps with React, TypeScript and CSS.

 Attar turns your JavaScript into native code before the app runs. It keeps Chrome’s rendering engine for the interface.

## Write a web interface.

- JavaScript / TypeScript / TSX
- React 19 / state, effects, refs
- CSS / Tailwind 4 / SVG
- UI libraries / selected Radix & shadcn components

## Compile. Link. Package.

 Your code and supported dependencies compile together. The linker keeps the engine code they need.

 Native code Web rendering App packaging

03 / Desktop application

## Run a desktop app.

 The result opens in its own native window. Blink, Chrome’s rendering engine, draws your HTML and CSS.

 The app runs compiled code, with no Electron or Node.js runtime.

 The aim: keep familiar web development while reducing the runtime your users need to download and run.

### Start with a React interface on macOS.

This early SDK is for developers exploring standalone desktop UI. Start with the included TSX project or a source example, then check the APIs your app needs. Electron app migration is planned for a separate release.

Explore source examples ↗

## Familiar code. Already compiling.

 The SDK already compiles stateful React interfaces, generated stylesheets and selected UI components. Each link below shows the supported APIs and their limits.

01

### JavaScript & TypeScript

 Functions, classes, closures, modules and async code, compiled before the app runs. Executable dependencies resolve at build time.

JS · TS · TSX ↗

02

### Stateful React interfaces

 Components, hooks, refs, controlled inputs and keyed updates. React updates the interface through a native host connected to Blink.

React 19 ↗

03

### CSS from your build tools

 Static stylesheets, compiled Tailwind utilities, React style values, bundled fonts and SVG. Blink provides layout and paint.

CSS · Tailwind 4 ↗

04

### Existing UI components

 The source example compiles 15 unchanged shadcn/ui component families from the pinned Radix / New York v4 set.

Radix · shadcn/ui ↗

05

### Rust & native integration

 A C ABI connects the UI engine to native programs. Explore the Rust and C host adapters and their client-SDK requirements.

C ABI · Rust ↗

 Support is scoped to the listed APIs and component variants. The compatibility guide distinguishes working subsets, unavailable features and unverified behavior. React is the current framework adapter; more frameworks will follow.

 Explore compatibility Libraries & APIs ↗ Inside the SDK release Scope & targets ↗ The engineering behind Attar Inside the compiler ↗

## Less to download. Less memory to run.

We compared the Etcher USB-flashing app on Electron with an Attar research build on the same Mac. That build came from our experimental Electron compatibility work. Attar Electron is planned and is outside this SDK release.

 Same Etcher app. Less to ship. Application size / MiB

Electron 375.1

 Chromium + V8 + Node.js + your app 375.1

Attar 73.3

73.3 80% smaller on disk

 Measured on balena Etcher, macOS, Apple silicon. Read the methodology ↓

 Measured Electron and Attar Etcher resource use

| Measurement | Electron | Attar |
| --- | --- | --- |
| Application on disk MiB | 375.1 | 73.3 |
| Memory at idle MB, all processes | 293.9 | 91.8 |
| First window ms, median of 5 launches | 1,081 | 469 |
| Processes at idle | 5 | 1 |
| Threads at idle | 383 | 13 |
| CPU at idle % of one core | 2.99 | 2.06 |

How we measured

Application
: balena Etcher: Electron 37.2.4 and the Attar research build.
Hardware
: Apple M5 Max, macOS 27. Both apps on the same machine.
Launch
: Five launches timed to the first window through the Accessibility API.
Idle
: Three samples of 60 seconds. Physical footprint and CPU summed across every app process.
Conditions
: Four concurrent builds, load 5 to 12. These results describe this comparison, not a performance ceiling or a guarantee for other apps.

How we checked the application

Etcher built by Attar was driven through the same five recorded journeys as the Electron original: file selection, source URL, settings, valid logos and malformed logos.

Sixteen screen comparisons recorded a remaining red-channel rounding difference of one code value. These checks cover those journeys; they do not establish complete Electron compatibility.

 These earlier research results describe one app and one machine. Read the roadmap ↗

Behind the SDK The first eight weeks

## React can run as compiled code.

Attar compiles React’s rendering logic together with your application. A native host connects React’s updates to Blink, the same engine that gives Chrome its HTML and CSS behavior.

That is how familiar components and styles can become a desktop interface. The compiled JavaScript runtime still handles objects and memory; the UI engine still handles layout, text and input.

We are two cofounders working with AI across the compiler, engine and native tooling. Explore the work behind the SDK, or read how its C interface connects to Rust and other native code.

Inside the engineering ↗ Rust & native integration ↗

## Where Attar fits today.

Can I move an existing Electron app to Attar?

The current SDK builds standalone apps. Attar Electron, the planned Electron and Node API compatibility layer, is a separate project and is not included. The Etcher measurements above come from that research work. Read the roadmap.

What does “native” mean here?

Your JavaScript is compiled into native code before the app starts. HTML and CSS render through Blink in a native window. The interface keeps web rendering behavior; it is not converted into AppKit or Windows widgets. JavaScript runtime services, including memory management, still exist. How the engine works.

Will my existing web app and npm packages work?

It depends on the libraries and APIs they use. React 19, static CSS, compiled Tailwind utilities and selected shadcn components have a supported scope. Executable dependencies must be known at build time; runtime code loading and `eval` are unsupported.

The standalone SDK also lacks some common browser APIs, including networking, storage and the Clipboard API. Check compatibility before planning a port.

Check libraries and APIs ↗

Which platform should I start with?

Use macOS 15 or newer on Apple silicon for the standalone React workflow. Linux x86_64 compiler packages are available, but equivalent React and shadcn coverage is not verified. This release has no supported Windows package. See the release scope.

Do I need an AI agent to use Attar?

No. You can use the SDK directly. When you do write code with an agent, we recommend our published Attar skill for project setup, supported APIs and build instructions. The compiled application does not require an AI service.

## Build your first app.

 Install the SDK, create the included TSX starter and build it. Start on macOS for the standalone React workflow. Source examples show the project files and where to find the built application.

### Coding with an agent?

 We recommend installing the Attar skill first. It provides the project layout, accepted APIs, compiler diagnostics and the build-and-verify loop for a standalone app.

```
npx skills add occam-tech/attar-skills
```

 Published as `attar-demo`. Includes a starting project. View the repository ↗

macOS · Apple silicon

```
brew install occam-tech/attar/attar
attar init my-app --template tsx
attar build my-app
```

 macOS 15 or newer on Apple silicon, with Xcode Command Line Tools. Builds a signed `.app`.

Linux · x86_64

```
curl -fsSL https://attar.dev/install.sh -o install.sh
sh install.sh
export PATH="$HOME/.local/bin:$PATH"
attar init my-app --template tsx
attar build my-app
```

 glibc 2.39 or newer, with Python 3.11, gpg and binutils. Ubuntu and Debian can use the signed apt repository instead. The standalone React / shadcn path is not yet verified on Linux. Check Linux scope.

 Every package is signed. The installer pins the release key and checks the archive against the signed index. Releases and checksums ↗

## 关联链接

- https://attar.dev/install.sh

## 导航

- 项目页：[[10-项目/attar.dev_33bca50b]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
