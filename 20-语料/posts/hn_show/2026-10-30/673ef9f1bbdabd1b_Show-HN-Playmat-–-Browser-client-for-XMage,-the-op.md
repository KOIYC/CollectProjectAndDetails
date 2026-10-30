---
type: "corpus"
item_id: "673ef9f1bbdabd1b"
title: "Show HN: Playmat – Browser client for XMage, the open-source MTG engine"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50292839"
project_url: "https://github.com/arcanite24/playmat"
author: "arcanite24"
published_at: "2026-10-29T17:31:55Z"
captured_at: "2026-10-30T09:57:36+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-30"
pub_day: "2026-10-29"
tags:
  - 语料
  - hn_show
  - author_arcanite24
  - story_50292839
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Playmat – Browser client for XMage, the open-source MTG engine

> [!info] 一句话导读
> A fan-made web client for XMage, the open-source Magic: The Gathering rules engine. Hobby project, not affiliated with Wizards of the Coast.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50292839>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：arcanite24　|　发布：2026-10-29T17:31:55Z
> 项目链接：<https://github.com/arcanite24/playmat>
> 采集：2026-10-30T09:57:36+08:00　|　id：`673ef9f1bbdabd1b`

## 正文

# arcanite24/playmat

A fan-made web client for XMage, the open-source Magic: The Gathering rules engine. Hobby project, not affiliated with Wizards of the Coast.

- Stars: 10
- Forks: 1
- Watchers: 10
- Open issues: 9
- License: MIT License
- Homepage: https://arcanite24.github.io/playmat/
- Default branch: master
- Created: 2026-01-20T03:49:25Z
- Fork: yes

## Languages

- Batchfile
- CSS
- Go Template
- HTML
- Inno Setup
- Java
- JavaScript
- Makefile
- Perl
- PowerShell
- Python
- Shell
- TypeScript

## Topics

- card-game
- docker
- magic-the-gathering
- mtg
- pwa
- react
- self-hosted
- typescript
- websocket
- xmage

## Top Contributors

- theelk801 (15965 contributions)
- LevelX2 (9294 contributions)
- JayDi85 (3628 contributions)
- muz (1824 contributions)
- xenohedron (1440 contributions)
- Zzooouhh (1339 contributions)
- spjspj (1177 contributions)
- Susucre (1090 contributions)
- jeffwadsworth (1055 contributions)
- fireshoes (761 contributions)

---

## README

 A fan-made web client for XMage, the open-source Magic: The Gathering
 rules engine. A hobby project, not affiliated with Wizards of the Coast.

 Play online ·
 Website ·
 Download ·
 Run a server ·
 Working on Playmat ·
 WebSocket API

A game against the AI in Playmat

## What it is

Playmat is a fork of XMage, the open-source Magic rules engine with its cards, AI
opponents, drafts and tournaments. It adds a WebSocket bridge to the server and a browser client styled after MTG
Arena. Play it in your browser at playmat.deimos.studio, where the project runs a
public server, install it on your computer to play the AI, Career or friends on your
Wi-Fi, or run a server for a group that plays from anywhere. The engine stays XMage, merged from upstream
regularly, so the cards it supports work here too.

It's a work in progress with rough edges. Bug reports and pull requests are welcome.

Come say hi, find a game or report bugs on the Discord server. If you'd like to help
keep the server running, you can support the project on Ko-fi.

## Features

- **Playing.** Pick a deck and play the AI, or send a friend an invite link. Practice mode gives you a
 goldfish opponent and tools to put any card in hand or on the battlefield.
- **The board.** Attack arrows, a visible stack, priority shown on the table, auto-pass with the stops you choose, and
 keyboard shortcuts for passing and answering.
- **Decks.** A deck builder with card search, and an import sheet that takes a link from Archidekt,
 Moxfield and other deck sites, a pasted list or a `.dck` file. Starter decks are there from the first sign-in,
 Commander ones included.
- **Events.** Booster draft, sealed, Jumpstart and constructed tournaments. Empty seats fill with AI players.
- **Career.** An optional single-player mode: five colour campaigns with a boss at the end of each, an Academy with a school
 for every format, puzzles, a gauntlet, sealed and draft runs, a weekly challenge, booster packs to open, a collection
 to craft into and achievements, illustrated with AI-generated art.
- **Social.** Lobby chat, players online, profiles, a table browser, spectating, match history and replays.
- **Devices.** Desktop browsers, tablets, an installable web app and an Android app that keeps card
 pictures on the device. English and Spanish.
- **On your computer.** Installers for Windows, macOS and Linux with everything inside, Java included: install,
 open, play. Friends on the same network join from their browser.
- **Hosting.** One Docker Compose stack: the server, Caddy with automatic HTTPS, a Scryfall picture cache,
 nightly backups and Discord notifications.

## Play on your computer

One download with everything inside, Java included. Install it, open Playmat, and the game opens in your browser. Play
the AI and Career on your own, or have friends on the same Wi-Fi join you. Nothing else to install.

| Your computer | Download |
|---|---|
| **Windows** 10 or 11 | Playmat-Setup-Windows-x64.exe: run it and press **Install** |
| **Mac** with Apple silicon (M1 and later) | Playmat-macOS-arm64.dmg: drag Playmat to Applications |
| **Mac** with an Intel processor | Playmat-macOS-x64.dmg: drag Playmat to Applications |
| **Linux** (x64 or ARM) | `curl -fsSL https://github.com/arcanite24/playmat/releases/latest/download/install.sh \| sh` |

Prefer a terminal? These download the right file, install it and start Playmat, without the warnings below:

```bash
# macOS or Linux
curl -fsSL https://github.com/arcanite24/playmat/releases/latest/download/install.sh | sh
```

```powershell
# Windows (PowerShell)
irm https://github.com/arcanite24/playmat/releases/latest/download/install.ps1 | iex
```

**The first time**

- Windows may say it protected your PC: choose **More info**, then **Run anyway**. macOS may say it can't check
 Playmat: open **System Settings**, **Privacy & Security** and choose **Open Anyway**. Playmat is a free fan project
 without paid signing certificates; the terminal installers above skip both screens.
- The first start prepares the card database, which takes a few minutes once. Your computer may ask whether Playmat
 (Java) may accept network connections: allowing it lets friends on your network join.

**Playing**

- A small Playmat window shows what's happening and opens `http://localhost:17170` in your browser when the game is
 ready. Keep it open while you play; closing it stops the game.
- Create an account the first time; it stays on your computer and unlocks Career. Untick **Player accounts** in the
 Playmat window to sign in with just a name instead.
- Friends on the same network open the address the window shows, such as `http://192.168.1.20:17170`.
- Card pictures come from Scryfall, so an internet connection helps.
- The window tells you when a new version is out. Installing it keeps your accounts, decks and Career progress.

Every version is on the releases page.
ops/desktop/README.md covers how the app works, where it keeps its data and how releases are
built.

## Running a server

You need Docker and a machine your players can reach.

```bash
cp ops/web/.env.example ops/web/.env      # set DOMAIN, XMAGE_AUTH, XMAGE_OWNER
docker compose -f ops/web/docker-compose.yml --env-file ops/web/.env up -d
```

This runs the published images, so nothing is built. The docs on the site walk through
running a server and
updating it: the admin console's Updates section says when a
newer version is out, and with the updater turned on the owner installs it with one button.

Players open `https:// ` and sign in.
ops/web/README.md covers private LAN servers, running behind another reverse proxy, every setting,
accounts and moderation, Discord notifications, backups and capacity.

## Working on Playmat

To run it from source while you change it. Requirements: JDK 17 or later, Maven, and the Node.js version in `Mage.Web.Client/.nvmrc`.

```bash
# 1. build the server (a few minutes the first time)
mvn -T 1C -pl '!Mage.Client,!Mage.Server.Console,!Mage.Tests,!Mage.Verify,!Mage.Reports' install -DskipTests

# 2. start it: the WebSocket bridge listens on ws://localhost:17172
cd Mage.Server/release
mvn -f ../../pom.xml -pl Mage.Server -Dexec.mainClass=mage.server.Main exec:java

# 3. in another terminal, start the client on http://localhost:5173
cd Mage.Web.Client
npm ci
npm run dev
```

Sign in with any name. The client's own guide, Mage.Web.Client/README.md, covers its
architecture, tests and the Android build (`npm run android`).

## Repository map

| Path | What lives there |
|---|---|
| `Mage.Web.Client` | The Playmat client: React 19, TypeScript, Vite. Product brief in PRODUCT.md, design system in DESIGN.md. |
| `Mage.Server` | XMage's server, plus the JSON-RPC WebSocket bridge and Career services (`src/main/java/mage/server/websocket`, `.../career`). |
| `ops/web` | The Docker Compose deployment kit. |
| `ops/desktop` | The desktop app: a launcher and installers for Windows, macOS and Linux. |
| `docs` | The WebSocket API, data models and the upstream merge recipe. |
| `brand` | The Playmat logo, generated from the app's typeface by `build_logo.py`. |
| `site` | The project website, published to GitHub Pages. |
| Everything else | XMage: the rules engine, card implementations, AI, tests and the original desktop client. |

## Credits

Playmat stands on XMage and the many people who have built it since 2010: the rules engine, tens of thousands of card
implementations and the AI are their work. Card and rules bugs usually live in the engine; XMage's
issue tracker and wiki are the
places for those. Card pictures and data come from Scryfall.

Released under the MIT License, like XMage.

Playmat is unofficial Fan Content permitted under the Fan Content Policy. Not approved/endorsed by Wizards. Portions
of the materials used are property of Wizards of the Coast. ©Wizards of the Coast LLC.

# arterialist/kube32

## 关联链接

- http://192.168.1.20:17170`.
- http://localhost:17170`
- http://localhost:5173
- https://arcanite24.github.io/playmat/
- https://github.com/arcanite24/playmat/releases/latest/download/install.ps1
- https://github.com/arcanite24/playmat/releases/latest/download/install.sh

## 导航

- 项目页：[[10-项目/github.com_20dbbf7a]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
