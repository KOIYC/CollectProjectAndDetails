---
type: "corpus"
item_id: "6ffbc603a9f6e9b7"
title: "Show HN: A patch to make Codex's browser control work in Arc"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50027194"
project_url: "https://github.com/brianlzhou/arc-browser-use"
author: "piplupness"
published_at: "2026-10-09T22:09:38Z"
captured_at: "2026-10-10T09:53:50+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-10"
pub_day: "2026-10-09"
tags:
  - 语料
  - hn_show
  - author_piplupness
  - story_50027194
  - show_hn
metrics: {"points": 2, "comments": 1, "engagement_velocity": 2}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: A patch to make Codex's browser control work in Arc

> [!info] 一句话导读
> brianlzhou/arc-browser-use

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50027194>
> 指标：点赞=2 · 评论=1 · engagement_velocity=2
> 作者：piplupness　|　发布：2026-10-09T22:09:38Z
> 项目链接：<https://github.com/brianlzhou/arc-browser-use>
> 采集：2026-10-10T09:53:50+08:00　|　id：`6ffbc603a9f6e9b7`

## 正文

# brianlzhou/arc-browser-use

- Stars: 2
- Forks: 0
- Watchers: 2
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-10-08T20:19:00Z

## Languages

- Python

## Top Contributors

- brianlzhou (2 contributions)

---

## README

# Arc Browser Use

Make Codex's browser use work in Arc.

Codex controls browsers through the **Chrome** plugin in the ChatGPT desktop app. In Arc, that connection stalls on the first tab Codex opens. This project fixes that by building a lightly patched copy of OpenAI's ChatGPT extension on your Mac.

Codex's separate **Computer Use** plugin, which operates Mac apps by clicking and typing, doesn't need this project.

## How it works

Codex reaches a browser through three parts:

1. The **Chrome plugin** in the ChatGPT desktop app.
2. A **native connector** that the plugin installs. Arc finds it in the same place Chrome does, even if Chrome isn't installed.
3. OpenAI's **ChatGPT extension**, running inside the browser.

Only the extension needs changing. It waits for Chrome's tab-group API before it loads each tab, and Arc never answers that API. `arc_browser_use.py build` does these things:

- It downloads the extension from the Chrome Web Store and checks its signature.
- It applies two small patches, listed in What the patches change.
- It writes **the build** to `~/Library/Application Support/Arc Browser Use/extension`.

You load that folder into Arc once. After that, Codex lists Arc as a browser it can use.

## Set up with an agent

Paste this into Codex, or into any coding agent that can run commands on your Mac:

```text
Set up Arc for Codex browser use by following
https://github.com/brianlzhou/arc-browser-use/blob/main/SETUP.md
```

The agent runs the commands and asks you when it needs a click in Arc.

## Set up by hand

You need these things:

- macOS and Arc.
- The ChatGPT desktop app, with the **Chrome** plugin installed from its plugin list. You don't need Google Chrome itself.
- Python 3.9 or later. It comes with Apple's Command Line Tools. If it's missing, running `python3` makes macOS offer to install it.

```sh
git clone https://github.com/brianlzhou/arc-browser-use.git
cd arc-browser-use
python3 arc_browser_use.py build
```

Then, in Arc:

1. Open `arc://extensions` and turn on **Developer mode**.
2. If a **ChatGPT** extension is listed, click **Remove** on it.
3. Click **Load unpacked**. Press **⇧⌘G**, paste `~/Library/Application Support/Arc Browser Use/extension`, press Return, and click **Select**.

Check the setup:

```sh
python3 arc_browser_use.py doctor
```

Every line should start with `ok`. Then ask Codex: *"Use my Arc browser to open example.com and tell me the page title."* Codex should answer "Example Domain".

## Updating

The build doesn't update itself. When `doctor` reports `FAIL The build is the latest store version`, run this:

```sh
git pull
python3 arc_browser_use.py build
```

Then, in `arc://extensions`, turn the ChatGPT extension off and on again. Don't use **Reload**. It doesn't reconnect to the ChatGPT app, so Codex keeps talking to the old copy.

Here is what happens when OpenAI changes the extension:

- **Routine releases.** The patches find their targets by method and property names, which survive OpenAI's minifier. A new release that leaves those parts alone builds without changes.
- **A required patch no longer applies.** `build` stops and names the patch. Your build folder is left as it was. SETUP.md explains how to update the patch.
- **Only the optional patch no longer applies.** That patch makes Codex list Arc by name. `build` skips it, warns, and finishes. Codex then lists Arc as "Chrome".

A weekly CI job builds the newest store version. If a patch fails or the version is untested, it opens an issue in this repository.

## What the patches change

| Patch | Change | Why |
| --- | --- | --- |
| `skip-tab-groups` (required) | `ensureAgentTabGroup` returns immediately. | The extension puts each tab Codex opens into a tab group before loading it. Arc never answers tab-group calls, so the tab never loaded. |
| `arc-display-name` (optional) | The browser reports its name as "Arc". | Without it, Codex lists Arc as "Chrome". |

`build` also changes two things outside `background.js`:

- It adds the publisher's public key to `manifest.json` as `key`. The copy then keeps the official extension ID, and the native connector accepts only that ID.
- It removes `_metadata`, the store's verification data, which doesn't apply to a modified copy.

This repository contains no OpenAI code. Each user builds their copy on their own Mac.

## Limitations

- Arc turns off unpacked extensions when Developer mode is off. Keep Developer mode on.
- The extension's side panel doesn't open in Arc, because Arc doesn't support Chrome side panels. Chat in the ChatGPT app instead. Browser use isn't affected.
- Only macOS is supported.
- CHANGELOG.md lists the extension versions that each release was tested with.

## Uninstall

```sh
python3 arc_browser_use.py uninstall
```

Then remove the ChatGPT extension in `arc://extensions`. To go back to the official extension, install it from the Chrome Web Store.

## Acknowledgments

- claude-arc-patch found the same tab-group problem in Claude's extension.
- Claude-in-Arc adapts Claude's extension to Arc.
- codex-computer-use-firefox-zen brings Codex browser use to Firefox and Zen.

## Disclaimer

This project isn't affiliated with OpenAI or The Browser Company. ChatGPT and Codex are trademarks of OpenAI. You run a modified build of OpenAI's extension at your own risk.

## License

MIT

# ritza-co/hn-jev-sorter

## 评论（1/1）

> **piplupness** · 2026-10-09T22:09:38.000Z　
> Codex can drive your real browser through OpenAI's ChatGPT extension, which should cover all of the Chromium browsers. But because of an issue in the tab-group API, Arc never opens the first tab.It's similar to Arcodex, but rebuilds your browser extension if there's ever a version update published by OpenAI.

## 关联链接

- https://github.com/brianlzhou/arc-browser-use.git
- https://github.com/brianlzhou/arc-browser-use/blob/main/SETUP.md

## 导航

- 项目页：[[10-项目/github.com_1f8f9c3d]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
