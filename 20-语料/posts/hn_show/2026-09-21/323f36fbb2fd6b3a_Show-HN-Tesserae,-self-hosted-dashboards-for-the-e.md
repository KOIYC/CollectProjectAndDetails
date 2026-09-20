---
type: "corpus"
item_id: "323f36fbb2fd6b3a"
title: "Show HN: Tesserae, self-hosted dashboards for the e-paper panel you own"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48732157"
project_url: "https://tesserae.ink/"
author: "xDaftTurtle"
published_at: "2026-06-30T13:02:02Z"
captured_at: "2026-09-21T02:53:06+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-06-30"
tags:
  - 语料
  - hn_show
  - author_xDaftTurtle
  - story_48732157
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:113d"
---

# Show HN: Tesserae, self-hosted dashboards for the e-paper panel you own

> [!info] 一句话导读
> Tesserae Overview Panels Compose Gallery Install How Hardware Open Why v0.419.3

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48732157>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：xDaftTurtle　|　发布：2026-06-30T13:02:02Z
> 项目链接：<https://tesserae.ink/>
> 采集：2026-09-21T02:53:06+08:00　|　id：`323f36fbb2fd6b3a`

## 正文

Tesserae Overview Panels Compose Gallery Install How Hardware Open Why v0.419.3
Catalog Flasher GitHub
 01 02 03 04 05 06 07 08 09
 Free, open-source dashboard server
 Self-hosted dashboards for e-ink displays.
 Compose a dashboard in the browser; Tesserae renders it, dithers it to your panel's bit depth, and pushes the frame over MQTT or REST. Thirteen panels verified on real hardware, twenty-nine supported. One server, no accounts, no cloud.
 Install
 View on GitHub Read the docs
AGPL-3.0 no tracking no accounts Melbourne
Morning board 800×480
See it live
One shelf · one server · one house Weather · now playing · F1 · calendar
 No glow. No notifications. No refresh until something changes.
 0.4W average per panel · weeks per charge
Two ways to compose
 Cards editor · MCP canvas · 35 widgets, 18 community
 01 · Place it yourself
 The cards editor: split the panel with a layout, drop a widget into each cell, and tune it in the form. The preview re-renders after every change; 14 themes bundled, then bind to a panel and hit Push.
Widget editor
 Place it yourself. Cell by cell.
 Split the panel with a layout, drop a widget into each cell, and tune it in the form. The live preview re-renders after every change. No code, no agent.
Morning board Saved 800 × 480 Save Push Layout
Single Halves Sidebar 1 + 2 Quad Thirds
 Cell —
Click a cell in the preview to configure it.
Live preview
HTML view Panel view
Weather
Weather
14°
 Light rain · feels 12°
 Now 14° 3pm 16° 9pm 11°
Clock
Clock
 09:41
 Thursday 12 June
 Week 24 Sunrise 06:58
Calendar
 Today
 09:30 Team standup
 12:00 Lunch — Ada
 15:30 1:1 with Sam
Climate
Living room
 21.5°
Target 22° · 48% RH
800 × 480 · reTerminal E1001
A faithful mock of the built-in dashboard editor. The self-hosted app carries 35 bundled widgets, 18 more in the community catalog, a theme builder, per-cell overrides, scheduling and rotations. Read the source
02 · Or describe it
 Prefer to describe it? The same freeform editor, driven by an MCP agent: it runs the real tool loop — create the canvas, add a code element, append each source — and composes the panel while you watch. Entirely optional.
Canvas editor · MCP
 Or just describe it. Watch it build.
 The same freeform editor, driven by an MCP agent. Ask in plain language and it runs the real tool loop, composing the panel in the canvas while you watch.
Daily Brief experimental
Save Choose device… Send to panels
 Appearance
Standard Display Mono
Widgets drag onto canvas
Weather
Now
Forecast
Hourly
Wind
Air Quality
Clock
Digital
Analog
World
Word
Home Assistant
 Climate
 Lights
 Sensor
 Energy
Calendar
 Day
 Week
 Schedule
Media
 Now Playing
 Album Art
 Queue
News
 Hacker News
 RSS / Atom
 Reddit
Layers 0
 No elements yet.
THURSDAY 12 JUNE
 09:41
87%
 14 °
Partly cloudy
 Feels 12° · Melbourne
 3PM
 16° 6PM
 14° 9PM
 11° 12A
 9°
Up next
 Team standup
 9:30 AM · Zoom
12:00 · Lunch with Ada
Now playing
 Avril 14th
 Aphex Twin
0:47 2:03
Daily Brief 600 × 400
Element
Waiting for the agent
 The MCP agent will add a code element and bind its data sources here as it composes the panel.
tesserae · mcp agent
 you ▋
A faithful mock of the editor being driven over MCP. The real tool loop (create_canvas_page → bind_devices → add_element → append_code → render_preview → push) composes the panel exactly like this. Read the source
Dashboard examples
 Real renders · 16 dashboards · four panel sizes
 Canvas editor
 Brutalist Daily · 1872×1404 · A System-7 broadsheet: a photo of the day, PostHog page views, weather, top artists and a GitHub heatmap.
 Canvas editor
 Tuesday · 1200×1600 · A colourful bento: weather, moon phase, a six-day outlook, the agenda and field conditions.
 Canvas editor
 Mernda Line · 1200×1600 · Live City-Loop departures, service status, a rain-radar chart and the forecast.
 Canvas editor
 Pokédex · 480×800 · A Game-Boy Pokédex entry: sprite, type, base-stat bars and the dex blurb.
 Canvas editor
 Nexus · HOME.OS · 1872×1404 · A grayscale HUD: ambient climate, perimeter locks, live power draw, an energy ledger and the day vector.
 Canvas editor
 Mesh · Radar · 800×480 · An amber tactical radar of Meshtastic nodes with signal, distance and hop counts.
 Canvas editor
 Unknown Pleasures · 480×800 · A Joy-Division homage: the day’s weather drawn as a ridgeline, indoor climate below.
 Canvas editor
 South Morang · 480×800 · A clean weather + transit board: current conditions, a six-day forecast and the next departures.
 Canvas editor
 System 7 · Books · 480×800 · A Macintosh reading tracker: a Goodreads shelf, challenge progress and the weather, in classic chrome.
 Canvas editor
 KDN · Ops · 1872×1404 · An operations wall: mesh traffic, climate, litter telemetry, contributions and the schedule.
 Cards editor
 Morning board · 800×480 · Weather, a word clock, and climate control for the kitchen wall.
 Cards editor
 Weather · 1200×1600 · A four-day forecast, sun times, and a live wind compass.
 Cards editor
 GitHub · 1872×1404 · Contributions, streaks, stars, and live traffic for the office wall.
 Cards editor
 Now playing · 1200×1600 · The current Spotify track, top artists, and Hacker News headlines.
 Cards editor
 Home dashboard · 1200×1600 · Weather, climate zones, device batteries, and home-server energy.
 Cards editor
 Calendar · 1872×1404 · A month grid, the day's agenda, and the forecast.
Install
 Yours, on your own hardware.
 One container, a one-line script, a Home Assistant app, an LXC container, or straight from source. Open the UI, set a password, start composing. Nothing leaves the house.
 01
 Run the server
 One container on the box you already own. Open the UI, set a password. No account, no cloud.
02
 Pair a panel
 Flash Seeed/Waveshare from the browser, or install the Pi, Kindle or TRMNL client. It appears under Discovered.
03
 Compose a dashboard
 Drag widgets onto the grid — or ask the agent — then bind the page to a panel and hit Push.
04
 Put it on a cadence
 Every N minutes, or daily at a set time. Battery panels render just before each wake with smart sync.
docker home assistant shell lxc source
 $ mkdir ~/tesserae && cd ~/tesserae
 $ curl -fsSLO tesserae.ink/docker-compose.yml
 $ docker compose up -d
 → localhost:8765 · set a password
 Full docker guide →
 # Settings → Apps → app store → ⋮ → Repositories
 # Add repo: github.com/dmellok/homeassistant-tesserae-addon
 $ Install Tesserae, then Start
 → Open Web UI (no password; HA's own auth gates it)
 Full home assistant guide →
 $ curl -fsSL tesserae.ink/install.sh | bash
 $ cd ~/tesserae && ./run.sh
 → localhost:8765 · set a password
 Full shell guide →
 # In an unprivileged Debian/Ubuntu container:
 $ apt update && apt install -y git python3 python3.13-venv
 $ curl -fsSL tesserae.ink/install.sh | bash
 → :8765 · set a password
 Full lxc guide →
 $ git clone https://github.com/dmellok/tesserae.git
 $ cd tesserae && python3 -m venv .venv
 $ .venv/bin/pip install -e ".[dev]"
 $ .venv/bin/python -m app.main --dev
 → localhost:8765 · hot-reload dev server
 Full source guide →
No account No cloud No tracking Runs anywhere
 13
 Panels verified
2,680
 Passing tests
0
 Accounts
One server, many panels
 renderers/ · transports/ · devices/
 BROWSER EDITOR
 compose ↓
 TESSERAE SERVER
 render → dither → fan out ↓
 Most e-paper projects are one firmware pinned to one panel. Tesserae splits rendering from transport from hardware.
MQTT
 Raspberry Pi
 Always-on. The server pushes a new frame the moment a page changes. Inky Impression, every size.
 pi-png / pi-bin client
REST
 ESP32
 Wakes, pulls its frame over HTTP, sleeps again. Smart sync renders just before each wake.
 tesserae-device-firmware
MQTT
 Kindle
 A jailbroken Paperwhite becomes a panel via the KOReader plugin. 758×1024, 1-bit.
 koreader plugin
HTTP
 TRMNL & custom
 BYOS firmware points at your server. Anything else: a small adapter and a custom panel size.
 openapi 3.0 · drop-a-folder plugins
16 panels, verified on real hardware
 29 supported · report yours
 PANEL SETUP RESOLUTION STATUS
 Seeed Studio tesserae-firmware
 reTerminal E1001 Setup 800×480 VERIFIED
 reTerminal E1002 Setup 800×480 VERIFIED
 reTerminal E1003 Setup 1872×1404 VERIFIED
 reTerminal E1004 Setup 1200×1600 VERIFIED
 reTerminal Sticky Setup 480×800 VERIFIED
 XIAO 13.3" ePaper (EE02) Setup 1200×1600 VERIFIED
 TRMNL 7.5" OG DIY Kit Setup 800×480 VERIFIED
 M5Stack tesserae-firmware
 M5Paper Setup 540×960 VERIFIED
 PaperS3 Setup 540×960 VERIFIED
 PaperMono / PaperMono Lite Setup 480×800 VERIFIED
 Pimoroni Inky pi-png / pi-bin
 Inky Impression 4" Setup 640×400 VERIFIED
 Inky Impression 5.7" Setup 600×448 VERIFIED
 Inky Impression 7.3" Setup 800×480 VERIFIED
 Inky Impression 13.3" Setup 1600×1200 VERIFIED
 Inky pHAT / wHAT — various
 PENDING
 Waveshare ESP32
 Waveshare 13.3" Spectra 6 Setup 1200×1600 VERIFIED
 Waveshare 7.3" PhotoPainter Setup 800×480 VERIFIED
 Waveshare 10.85" e-Paper HAT+ (G) Setup 1360×480 VERIFIED
 Waveshare E-Paper ESP32 Driver Board + 7.5" B/W Setup 800×480
 PENDING
 Waveshare 4.2" B/W — 400×300
 PENDING
 Xteink ESP32 · crossink
 Xteink X3 Setup 528×792 VERIFIED
 Xteink X4 Setup 480×800 VERIFIED
 TRMNL-compatible HTTP pull
 TRMNL OG — 800×480
 PENDING
 TRMNL X — 1872×1404 VERIFIED
 Kindle Paperwhite 2 (jailbroken) — 758×1024 VERIFIED
 paperlesspaper tesserae-firmware
 OpenPaper 7 Setup 800×480 VERIFIED
 OpenPaper L Setup 1200×1600
 PENDING
 PicPak ESP32-C3 · community
 PicPak 4.2" photo frame Setup 400×300 VERIFIED
 CircuitPython REST
 Generic CircuitPython client (400+ boards) — per-panel PLANNED
Some links here are affiliate links: buying a Seeed panel through one gets you a discount at checkout and pays a small commission back into Tesserae. Nothing is listed because of it, and a panel's verified status means exactly what it says.
 Anything else: Settings → Panel → custom, set the dimensions. Report a working panel and it joins the table.
Shortest path
 The Seeed reTerminal E-Series
 Four pre-assembled, battery-powered ePaper devices sharing one Tesserae-native firmware you flash from the browser. No assembly, no soldering, no toolchain.
E1001
 7.5" mono · 800×480
E1002
 7.3" Spectra 6 · 800×480
E1003
 10.3" 16-grey · 1872×1404
E1004
 13.3" Spectra 6 · 1200×1600
Firmware flasher
 Flash your panel from this page.
 Web Serial writes the firmware over USB. Every image checked against its SHA-256 before a byte lands.
 Open the flasher CHROME OR EDGE
Open all the way down
 No accounts · no black boxes
 Design
 Drag-resize cells, live preview 14 themes bundled, 60+ community Layout presets per panel Schedules and rotations
Devices
 Pi: Inky, every size ESP32: Waveshare, PhotoPainter Kindle via KOReader TRMNL-compatible BYOS
Integrations
 Home Assistant + MQTT discovery Open-Meteo, bundled CalDAV, Google, iCloud Spotify, GitHub, OctoPrint, F1
Developer
 Drop-a-folder plugins OpenAPI 3.0 REST API AGPL-3.0-or-later 2,680 passing tests
Built in the open. PRs welcome.
 Every feature, bug and design decision lives in the issue tracker. Pick one and send a PR — or run it on a panel nobody has tried yet and file the report.
 Good first issues
 labels/good first issue
 Discussions
 setup · ideas · show-and-tell
 Roadmap
 milestones/
 Sponsor
 github/sponsors/dmellok
Why AGPL, and what your server sends
 The AGPL keeps the server free even when run as a service. No accounts. Online features are off by default — nothing is sent unless you enable them under Settings → System → Online features. With them on, the app contacts api.tesserae.ink for update checks and an anonymous count of which marketplace widgets are in use; a coarse country is derived from the IP, then discarded.
 Read the source Read the privacy page Security policy
Why I built it
 Beautiful ambient displays, tied to nobody's cloud.
 Tesserae grew from a weekend project into a plugin platform spanning several hardware families and rendering pipelines. A solo project, built in Melbourne. If it earns a place on your wall, sponsor the work — or just send a panel report.
 View on GitHub Read the docs
Tesserae
 Self-hosted dashboards for e-ink displays. Compose, render, push. Your pixels, your walls.
 AGPL-3.0-or-later · no tracking · no subscriptions · Melbourne
PRODUCT
 Compose Panels Catalog Install Hardware
 DOCS
 Documentation Widgets Clients Privacy
 PROJECT
 GitHub Issues Releases License

## 关联链接

- https://github.com/dmellok/tesserae.git

## 导航

- 项目页：[[10-项目/tesserae.ink_685d471b]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
