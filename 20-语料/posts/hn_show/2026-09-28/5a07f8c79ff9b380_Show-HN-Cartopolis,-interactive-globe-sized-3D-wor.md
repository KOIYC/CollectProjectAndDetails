---
type: "corpus"
item_id: "5a07f8c79ff9b380"
title: "Show HN: Cartopolis, interactive globe-sized 3D world"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49870394"
project_url: "https://code.garage44.eu/jeroen/cartopolis"
author: "jvanveen"
published_at: "2026-09-27T20:14:53Z"
captured_at: "2026-09-28T09:47:28+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-28"
pub_day: "2026-09-27"
tags:
  - 语料
  - hn_show
  - author_jvanveen
  - story_49870394
  - show_hn
metrics: {"points": 12, "comments": 1, "engagement_velocity": 12}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Cartopolis, interactive globe-sized 3D world

> [!info] 一句话导读
> You've already forked cartopolis

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49870394>
> 指标：点赞=12 · 评论=1 · engagement_velocity=12
> 作者：jvanveen　|　发布：2026-09-27T20:14:53Z
> 项目链接：<https://code.garage44.eu/jeroen/cartopolis>
> 采集：2026-09-28T09:47:28+08:00　|　id：`5a07f8c79ff9b380`

## 正文

Explore
Help
Sign in
jeroen / cartopolis
Watch
1
Star
0
Fork
You've already forked cartopolis
0
Code
Issues
6
Pull requests
5
Projects
1
Releases
1
Packages
Activity
Actions
A networked 3D virtual world built with Rust and Bevy.
 https://cartopolis.org
fediverse
foss
groningen
mapping
metaverse
social
1,308 commits
99 branches
1 tag
274 MiB
Rust
93.5%
TypeScript
2.6%
WGSL
1.8%
Shell
0.7%
HTML
0.5%
Other
0.8%
main
Find a file
HTTPS
Download ZIP
 Download TAR.GZ
 Download BUNDLE
Open with VS Code
Open with VSCodium
Open with Intellij IDEA
Exact
Exact
Union
RegExp
Repository files (latest commit first)
Filename
 Latest commit message
 Latest commit date
viberfox-agent
59ae15af94
All checks were successful
CI / test cartopolis (push) Successful in 13m30s
Details
CI / wasm & android targets (push) Successful in 3m3s
Details
feat(mcp): fix what the first two bot sessions ran into
...
 Read back from the viberfox bot's own sessions. Each problem is now a
change:
- `walk_to` takes `wait_s` and answers when the walk ends. The bot had
 polled `me` about once a second, 30-odd times on one walk.
- A walk wedged on a hedge or fence corner sidesteps (left, right,
 back-and-aside, skipping a route corner) before giving up. Two walks
 near the Prinsentuin jammed a few metres in.
- `sign_out` and `sign_in` end and restart the session while the client
 keeps serving. Asked to disconnect, the bot had no way to.
- `view` returns a seven-field summary unless asked for `details`. It
 was returning about a hundred measurements the bot never read.
- `read_chat` leaves out the agent's own lines, which doubled every
 exchange.
- A waiting call whose caller already gave up is dropped. Answering it
 advanced the chat cursor and spent the line on nobody.
- `me` explains unnamed avatars, and lists nobody while signed out.
The waits only work once the host allows a call longer than Claude
Code's 60 s default; the per-server `timeout` in `.mcp.json` does that,
and the note records it.
2026-09-27 21:39:51 +00:00
.cargo
ci(web): name the browser build's deploy deploy-wasm
2026-09-23 20:30:17 +00:00
.claude /skills
docs(slots): say what each slot renders on instead of sending shots to the Deck
2026-09-27 20:58:45 +00:00
.forgejo /workflows
refactor(atlas): make the web UI the site root, and stop calling it the console
2026-09-24 20:34:46 +00:00
assets
style(chat): follow the v1 mockup's inbox, thread and World view
2026-09-26 13:28:19 +00:00
crates
feat(mcp): fix what the first two bot sessions ran into
2026-09-27 21:39:51 +00:00
deploy
chore: drop the references to the retired cartopy repository
2026-09-23 22:01:21 +00:00
docs
feat(mcp): fix what the first two bot sessions ran into
2026-09-27 21:39:51 +00:00
tools
refactor(atlas): make the web UI the site root, and stop calling it the console
2026-09-24 20:34:46 +00:00
.git-blame-ignore-revs
build: gate rustfmt in CI, and keep git blame readable across the reformat
2026-08-06 17:20:50 +02:00
.gitattributes
refactor(brand): rename viberfox to cartopolis, cool the surface ramp
2026-08-11 17:52:22 +00:00
.gitignore
refactor(brand): rename viberfox to cartopolis, cool the surface ramp
2026-08-11 17:52:22 +00:00
AGENTS.md
docs: add a contributor guide and point the entry points at it
2026-07-27 23:52:47 +02:00
Cargo.lock
feat(chat): send a place and its view into a private chat, and see a chat on the map
2026-09-26 07:31:34 +00:00
Cargo.toml
feat(e2ee): add a Bevy-free crate for end-to-end encrypted private chats
2026-09-26 07:31:33 +00:00
CHANGELOG.md
docs(changelog): note the tarmac that stopped being drawn on the squares
2026-09-12 12:42:23 +00:00
CLAUDE.md
feat(mcp): let an agent walk, talk and build as the signed-in account
2026-09-27 21:39:51 +00:00
LICENSE
refactor(brand): rename viberfox to cartopolis, cool the surface ramp
2026-08-11 17:52:22 +00:00
LICENSE-APACHE
feat(android): behave like an app the system can suspend, and answer Back
2026-08-10 22:27:18 +00:00
LICENSE-MIT
refactor(brand): rename viberfox to cartopolis, cool the surface ramp
2026-08-11 17:52:22 +00:00
LICENSE-THIRD-PARTY.md
feat(map): paint land cover under the map, in one style with it
2026-09-27 21:15:59 +00:00
README.md
docs(readme): cut it down to bullets
2026-09-27 20:26:38 +00:00
README.md
Cartopolis
A social map of the real world: see how a place is built, and talk about it with the people who are there.
A walkable 3D copy of the real world, built from open public data and shared between everyone looking at it. Runs in the browser, on the desktop and on Android. Free, open source, self-hostable.
Public infrastructure
Built from the registers — buildings from BAG and 3DBAG , ground from AHN , street trees, lighting and paving from the national and municipal object registers, PDOK aerial photography, live transit.
Every building has a card — year built, use, units, floor area, status, monument listing, addresses. Walk in and its storeys are there.
The world around it — real sun, real weather, routing on foot, by bike or by car, and one continuous space from a doorway to orbit.
Sharing a place
Talk where you stand — avatars, local chat scoped by distance, proximity voice, world chat, end-to-end encrypted private chats.
Point at it — a link opens your exact view in the browser or the app; saved places with photos and map pins.
Put something there — place and script objects and 3D models, swap a building for an IFC model, export and import content over an HTTP API.
Moderation — blocking, reporting and account deletion, enforced on the server; a web console for accounts and data pipelines.
For residents, communities, municipalities and governments, and planners and architects.
Screenshots
Canal ring
 Ring road tunnel by DUO
Main station and rail yard
 Grote Markt and Martinitoren
Forum Groningen
 Building card: the town hall
Groningen from 3 km
 The city from 1.2 km up
Eemshaven
 Eemshaven from the Wadden Sea
Meeting on the Grote Markt
 Earth from orbit
Generated with cargo shots from docs/shots.toml .
Where it works
Map, sky, weather, routing and the shared world: anywhere on Earth. Register detail (measured buildings and their records, relief, street objects, aerial photos, transit): the Netherlands, plus municipal data where a city publishes it. Elsewhere the ground is flat and buildings come from OpenStreetMap. Each register is one pipeline in crates/atlas .
Written in Rust on Bevy .
Try it
Browser — cartopolis.org . Needs WebGPU.
Desktop — Linux and Windows on the releases page , or build from source (macOS too). Published binaries need AVX2 and FMA (~2013+).
Android — APK at cartopolis.org/apk (arm64, Android 9+). The full client, least tested of the three ( notes ).
Running from source
cargo run -p cartopolis
 Starts offline. Sign in to a server from ☰ ▸ Sign in….
cargo run -p cartopolis -- --connect  # split mode: connect to a live sim (TLS)
cargo run -p cartopolis -- --offline # no sim: single user, no auth or persistence
cargo run -p cartopolis_simulator # the sim server, standalone
 Needs Rust, a C compiler and a GPU driver; see the development guide . Run git lfs install before cloning — assets are in Git LFS and some are compiled in.
Documentation
User manual — controls, getting around, authoring, the developer panel.
Changelog — what changed, per release.
Development guide — prerequisites, dev loop, tests, code map, conventions, CI.
Server guide — deploying the sim and the self-hosted geo services.
docs/notes/ — constraints and measurements; CLAUDE.md Known issues is the trap list.
Architecture
Crate
 Role
cartopolis_core
 Shared protocol types and tile/coordinate math
cartopolis_geo
 Bevy-free map geodata: MVT decode, road classes, tree scatter, the routing graph
cartopolis_e2ee
 End-to-end encrypted private chats (MLS); the server relays sealed bytes it cannot open
cartopolis_simulator
 The shared-world server (Tokio + SQLite): avatars, chat, voice, objects, accounts; no Bevy
cartopolis_atlas
 The register pipelines (BAG, 3DBAG, AHN, BGT, …), the terrain server and the operator web console
cartopolis
 Bevy client — rendering, ECS systems, UI
cartopolis_android
 The Android app shell around the client
big_space
 Vendored floating-origin fork, for planet-scale coordinates
Licence
Source: MIT OR Apache-2.0 ( LICENSE ). Data, avatars and font carry their own terms; LICENSE-THIRD-PARTY.md is the canonical notice list (the credits below mirror it — add new sources there).
Credits
Engine — built with Bevy .
Floating origin — big_space by Aevyrie, MIT OR Apache-2.0. Vendored here as a fork ported to the Bevy release we track.
Avatar characters — Quaternius Ultimate Modular Men/Women , CC0. Consider supporting the work on Patreon .
Map data — © OpenStreetMap contributors, under the ODbL. Building detail and POIs come from Overpass , place search and reverse geocoding from Nominatim — both self-hosted, and usable against the public instances under the OSMF usage policies .
Vector tiles — VersaTiles , in the Shortbread schema. Self-hosted mirror of their OSM-derived planet build.
Buildings (LoD2.2) — 3DBAG by the 3D geoinformation group, TU Delft, CC BY 4.0 — derived from the Kadaster's BAG registry and AHN, both via PDOK . Netherlands only.
Aerial photography — Beeldmateriaal Nederland , served as Luchtfoto RGB by PDOK , CC BY 4.0. Netherlands only.
Street objects — street trees, lighting and containers from gemeente Groningen open data , CC BY 4.0. Groningen only.
Elevation — AHN height rasters (DTM/DSM), served by PDOK , CC0. Netherlands only.
Public transport — live departures and vehicle positions from OVapi , the open key-free feed of Dutch NDOV operator data. Netherlands only.
Weather — forecasts from MET Norway , CC BY 4.0, and global cloud cover from the NOAA Global Forecast System , public domain.
Night sky — star positions and magnitudes from the HYG Database v4.1 by David Nash, CC BY-SA 4.0 — a compilation of the Hipparcos, Yale Bright Star and Gliese catalogs.
Type — Plus Jakarta Sans by Tokotype, SIL Open Font License 1.1.
Powered by Forgejo
Version:
16.0.1
Page: 44ms
 Template: 12ms
English
Bahasa Indonesia
Dansk
Deutsch
English
Español
Esperanto
Filipino
Français
Italiano
Latviešu
Magyar nyelv
Nederlands
Plattdüütsch
Polski
Português de Portugal
Português do Brasil
Slovenščina
Suomi
Svenska
Türkçe
Čeština
Ελληνικά
Български
Русский
Українська
فارسی
日本語
简体中文
繁體中文（台灣）
繁體中文（香港）
한국어
Licenses
 API

## 评论（1/1）

> **tamimio** · 2026-09-28T01:44:36.000Z　
> Loved it! But I think with advent of llm, there should be a way to somehow feed the current view and generate a realistic 3D view, based on the real data from the same location to be as accurate as possible.

## 关联链接

- https://cartopolis.org

## 导航

- 项目页：[[10-项目/code.garage44.eu_d8c68920]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
