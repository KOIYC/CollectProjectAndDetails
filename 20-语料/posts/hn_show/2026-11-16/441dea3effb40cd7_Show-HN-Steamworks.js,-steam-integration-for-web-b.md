---
type: "corpus"
item_id: "441dea3effb40cd7"
title: "Show HN: Steamworks.js, steam integration for web based games"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50508091"
project_url: "https://github.com/ceifa/steamworks.js"
author: "ceifa"
published_at: "2026-11-15T16:17:57Z"
captured_at: "2026-11-16T10:00:05+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-11-16"
pub_day: "2026-11-15"
tags:
  - 语料
  - hn_show
  - author_ceifa
  - story_50508091
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Steamworks.js, steam integration for web based games

> [!info] 一句话导读
> Published: 2022-01-12

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50508091>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：ceifa　|　发布：2026-11-15T16:17:57Z
> 项目链接：<https://github.com/ceifa/steamworks.js>
> 采集：2026-11-16T10:00:05+08:00　|　id：`441dea3effb40cd7`

## 正文

Published: 2022-01-12
Author: ceifa

GitHub - ceifa/steamworks.js: A steamworks implementation for nw.js/electron games

/ steamworks.js Public

Star 360

- Fork 58
- Notifications
- Pricing

A steamworks implementation for nw.js/electron games

MIT license

360 stars 58 forks Branches Tags Activity

Star

Notifications

main

Branches Tags

Go to file

Code

Last commit message

Last commit date

189 Commits

.github

.github

sdk/redistributable_bin

sdk/redistributable_bin

src

src

test

test

.gitignore

.gitignore

.prettierrc

.prettierrc

Cargo.lock

Cargo.lock

Cargo.toml

Cargo.toml

LICENSE

LICENSE

README.md

README.md

build.js

build.js

build.rs

build.rs

callbacks.d.ts

callbacks.d.ts

client.d.ts

client.d.ts

index.d.ts

index.d.ts

index.js

index.js

package-lock.json

package-lock.json

package.json

package.json

View all files

| Name | Name |
| --- | --- |

## Repository files navigation

# Steamworks.js

A modern implementation of the Steamworks SDK for HTML/JS and NodeJS based applications.

## Why

I used greenworks for a long time and it's great, but I gave up for the following reasons.

- I hate C++.
- The API implement callbacks instead of return flags or promises.
- The API it's not trustful.
- Don't have typescript definitions.
- You have to build the binaries by yourself.
- It's not context-aware.
- It's not up to date.
- It's not being maintained anymore.

## API

```
const steamworks = require('steamworks.js')

// You can pass an appId, or don't pass anything and use a steam_appid.txt file
const client = steamworks.init(480)

// Print Steam username
console.log(client.localplayer.getName())

// Tries to activate an achievement
if (client.achievement.activate('ACHIEVEMENT')) {
    // ...
}
```

You can refer to the declarations file to check the API support and get more detailed documentation of each function.

## Installation

To use steamworks.js you don't have to build anything, just install it from npm:

```
$: npm i steamworks.js
```

### Electron

Steamworks.js is a native module and cannot be used by default in the renderer process. To enable the usage of native modules on the renderer process, the following configurations should be made on`main.js`:

```
const mainWindow = new BrowserWindow({
    // ...
    webPreferences: {
        // ...
        contextIsolation: false,
        nodeIntegration: true
    }
})
```

To make the steam overlay working, call the`electronEnableSteamOverlay` on the end of your`main.js` file:

```
require('steamworks.js').electronEnableSteamOverlay()
```

For the production build, copy the relevant distro files from`sdk/redistributable_bin/{YOUR_DISTRO}` into the root of your build. If you are using electron-forge, look for#75.

## How to build

You only need to build if you are going to change something on steamworks.js code, if you are looking to just consume the library or use it in your game, refer to the installation section.

Make sure you have the latest node.js, Rust and Clang. We also need Steam installed and running.

Install dependencies with`npm install` and then run`npm run build:debug` to build the library.

There is no way to build for all targets easily. The good news is that you don't need to. You can develop and test on your current target, and open a PR. When the code is merged to main, a github action will build for all targets and publish a new version.

### Testing Electron

Go to the test/electron directory. There, you can run`npm install` and then`npm start` to run the Electron app.

Click "activate overlay" to test the overlay.

# robertodf99/hook-me-up

## 导航

- 项目页：[[10-项目/github.com_758df318]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
