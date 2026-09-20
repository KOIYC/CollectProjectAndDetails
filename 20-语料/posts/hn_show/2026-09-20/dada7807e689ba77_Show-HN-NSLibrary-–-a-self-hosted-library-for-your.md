---
type: "corpus"
item_id: "dada7807e689ba77"
title: "Show HN: NSLibrary – a self-hosted library for your Switch games and homebrew"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49765415"
project_url: "https://github.com/tuckerwales/nslibrary"
author: "tuckerwales"
published_at: "2026-09-19T10:57:21Z"
captured_at: "2026-09-20T09:48:16+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-20"
pub_day: "2026-09-19"
tags:
  - 语料
  - hn_show
  - author_tuckerwales
  - story_49765415
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: NSLibrary – a self-hosted library for your Switch games and homebrew

> [!info] 一句话导读
> tuckerwales/nslibrary

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49765415>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：tuckerwales　|　发布：2026-09-19T10:57:21Z
> 项目链接：<https://github.com/tuckerwales/nslibrary>
> 采集：2026-09-20T09:48:16+08:00　|　id：`dada7807e689ba77`

## 正文

# tuckerwales/nslibrary

Self-hosted library for your own Nintendo Switch dumps. Scan folders of NSP, NSZ, XCI, XCZ, and homebrew NRO files, fill in metadata, spot missing or duplicate content, and send titles to a modded Switch over LAN.

- Stars: 0
- Forks: 0
- Watchers: 0
- Open issues: 0
- License: Apache License 2.0
- Default branch: main
- Created: 2026-09-15T15:54:46Z

## Languages

- C
- C++
- CMake
- CSS
- Dockerfile
- HTML
- JavaScript
- Shell
- Standard ML
- TypeScript

## Topics

- nintendo-switch
- self-hosted
- switch
- switch-homebrew

## Top Contributors

- tuckerwales (2 contributions)

---

## README

# NSLibrary

CI
License

Self-hosted library for **your own** Nintendo Switch dumps. Scan folders of NSP, NSZ, XCI, XCZ, and homebrew NRO files, fill in metadata, spot missing or duplicate content, and send titles to a modded Switch over LAN.

There are no download sources, no shop scraping, and no title keys handed out. Keys (`prod.keys`) come from your own console, stay on the server, and are optional.

The web library, listing four games with their base, update, and DLC badges

> **This project is for content you dumped yourself, from your own console and your own cartridges.**
> It will not help you obtain games, keys, or firmware, and requests to add that are out of scope
> permanently. See CONTRIBUTING.md.

## Features

- **Library server** — Fastify + SQLite. Walks library folders (read-only), watches for changes, and groups base games, updates, DLC, and homebrew.
- **Web UI** — React app served by the same process: library, homebrew, problems, devices, folders, and settings.
- **Metadata** — Container listings and tickets need no keys. Names, icons, firmware requirements, and NCA hashes need `prod.keys` dumped from your console. Optional titledb (a URL or file you supply, refreshed daily if it's a URL) fills in names, which game DLC belongs to, and latest-version numbers only.
- **Device API** — A paired Switch browses the catalog and claims install jobs. The console always initiates; “Send to Switch” queues work for it to pick up.
- **Discovery** — UDP `NSLIB?1` on port 8466, plus mDNS `_nslibrary._tcp` so the server shows up in Bonjour/Avahi browsers. You can always type an IP by hand.
- **USB** — A Switch plugged into the computer running NSLibrary (Electron, or Docker on Linux with device passthrough) uses the same device API inside `NSLU` frames. Transfers time out so cancel and unplug can interrupt a job.
- **Desktop app** — Electron wraps the same server: tray, native folder picker, USB, auto sign-in on this machine.
- **Demo data** — Synthetic containers and a fake keyset so the UI is usable without real dumps. No copyrighted content.

The Switch homebrew client (C++ / Borealis) streams NSP, NSZ, XCI, and XCZ installs into SD or NAND without copying the whole file to the SD card first. Connect over LAN HTTP or USB.

The Switch app's library grid, showing five games with their installed version under each icon

## Quick start

Borealis is a submodule, so clone recursively (`git submodule update --init --recursive` if you already cloned):

```bash
git clone --recursive https://github.com/tuckerwales/nslibrary.git
cd nslibrary
```

**Docker** (Node 22 image, `linux/amd64` and `linux/arm64`, port 8465):

```bash
docker compose up --build
```

Open http://localhost:8465 and create the admin account. The first run asks for a **setup token**, which the server prints to its log on boot (`docker compose logs nslibrary`):

```
  Setup token: K7M2X-9PQRT-4WHJN-6DFYB
```

Set `NSLIB_SETUP_TOKEN` to choose your own. Then browse the demo library, mount your dumps read-only as `/library/games`, and add that path under **Folders**.

**Without Docker** (Node ≥ 22.15, pnpm 12):

```bash
pnpm install
pnpm seed
NSLIB_SEED=true \
  NSLIB_SEED_DIR="$PWD/data/demo-library" \
  NSLIB_SEED_KEYS="$PWD/data/keys/prod.keys" \
  pnpm start
```

Then `pnpm --filter @nslib/web build` so the server can serve the UI, or run `pnpm dev:web` alongside `pnpm start` / `pnpm dev:server` and use the Vite proxy on http://localhost:5173.

Production deploys (Coolify, volumes, `PUID`/`PGID`) are in docs/deploy.md.

## Repository

pnpm workspaces. Shared types live in `@nslib/shared`; parsers never write into library folders.

| Path | Package | Role |
|---|---|---|
| `packages/shared` | `@nslib/shared` | Zod schemas, error codes, USB frame constants, golden protocol files |
| `packages/formats` | `@nslib/formats` | PFS0, HFS0/XCI, NCA, CNMT, NACP, ticket, NCZ, NRO, keyset |
| `packages/fixtures` | `@nslib/fixtures` | Synthetic containers encrypted with a generated fake keyset |
| `packages/server` | `@nslib/server` | HTTP APIs, scanner, SQLite (Drizzle), keys, titledb, UDP discovery |
| `packages/web` | `@nslib/web` | React + Vite + TanStack Query UI |
| `packages/device-sim` | `@nslib/device-sim` | CLI fake Switch for the device API (`nslib-sim`) |
| `packages/usb-host` | `@nslib/usb-host` | USB frame session and node-usb attach |
| `packages/electron` | `@nslib/desktop` | Electron window, tray, USB on the desktop |
| `switch/` | — | libnx + Borealis client, host-native C++ tests |
| `docker/` | — | Image entrypoint and compose overlay |
| `docs/` | — | Device API, USB frames, keys, deploy |

## Development

```bash
pnpm install
pnpm test          # Vitest across packages
pnpm typecheck
pnpm lint
pnpm format
pnpm dev:server    # API + scanner on :8465
pnpm dev:web       # UI on :5173, proxies /api to the server
```

`nslib-sim` talks to a running server the way a Switch would:

```bash
pnpm --filter @nslib/device-sim start -- pair --code 123456
pnpm --filter @nslib/device-sim start -- hello --token <token>
```

### Switch client

Host-native tests (no devkitPro) cover PFS0, HFS0/XCI, NCZ, CNMT, tickets, JSON, the device-API codec, USB frames, and the install pipeline against the same golden files as TypeScript:

```bash
pnpm test:switch
```

The `.nro` needs devkitPro (`switch-curl`, `switch-libzstd`). From the repo root:

```bash
./scripts/build-switch.sh
```

See docs/switch.md for pairing, USB, `nxlink -s`, and NSP/NSZ/XCI installs to SD or NAND. Host tests need `libzstd-dev`. Desktop: `pnpm dev:desktop` (see docs/desktop.md).

## Configuration

| Variable | Default | Meaning |
|---|---|---|
| `NSLIB_HOST` | `0.0.0.0` | Bind address |
| `NSLIB_PORT` / `PORT` | `8465` | HTTP (web UI, `/api/v1`, `/api/device/v1`) |
| `NSLIB_DATA_DIR` | `data` | SQLite, keys, icon cache. Docker: `/data` |
| `NSLIB_WEB_DIR` | `packages/server/public` or `packages/web/dist` | Built UI; unset serves API only |
| `NSLIB_TRUST_PROXY` | off | Set `true` behind Coolify / Traefik |
| `NSLIB_POLLING` | off | Poll library folders (NFS/SMB) instead of inotify |
| `NSLIB_DISCOVERY` | on | `0` / `false` disables UDP discovery and mDNS advertising |
| `NSLIB_DISCOVERY_PORT` | `8466` | UDP port for `NSLIB?1` |
| `NSLIB_SETUP_TOKEN` | generated | Creating the admin account asks for this value. Unset, the server generates one per boot and logs it, so a server reachable before you've signed up can't be claimed by whoever opens it first |
| `NSLIB_SERVER_NAME` | `NSLibrary` | Shown in hello and discovery |
| `NSLIB_SEED` | off (on in the image) | Attach the demo library on first boot if no folders exist |
| `NSLIB_SEED_DIR` / `NSLIB_SEED_KEYS` | — | Demo library path and matching fake `prod.keys` |
| `PUID` / `PGID` | `1000` | Docker user that owns `/data` |
| `NSLIB_LOG_LEVEL` | `info` | Fastify log level |
| `NSLIB_TLS_KEY` / `NSLIB_TLS_CERT` | — | PEM files for optional HTTPS (LAN without a reverse proxy) |
| `NSLIB_NRO_PATH` | `data/update/nslibrary.nro` if present | A signed release mirrored here, so consoles without internet can update (needs `update.json` and `update.json.sig` beside it) |
| `NSLIB_FORWARDER_MAIN` | `data/forwarder/main` if present | ExeFS `main` for the HOME-menu NSP |

The server never writes into library folders. Missing files are marked, then purged after 30 days.

## Keys

Upload `prod.keys` in **Settings** (or `PUT /api/v1/keys`). Stored at ` /keys/prod.keys` with mode `0600`. The API reports which **names** are present; key material is never returned, logged, or sent to a device.

Without keys the library still lists files from containers, tickets, and filenames, and labels that metadata as unverified. Details: docs/keys.md.

## Documentation

- Architecture — how the pieces fit together, and why
- Deploy — Docker image, Coolify, volumes
- Device API — pairing, catalog, jobs, Range downloads
- USB protocol — frame layout (same messages as HTTP)
- Keys — `prod.keys` and filename mode
- Switch updates — one channel of signed `.nro` releases, fetched from GitHub or mirrored on your server

## Contributing

Issues and pull requests are welcome — start with CONTRIBUTING.md, which covers
setup, house style, and the things this project will not accept. Security vulnerabilities go through
SECURITY.md rather than the issue tracker.

## Licence

Apache License 2.0. Third-party components, including Borealis, TweetNaCl, libnx, the
devkitPro portlibs, and the bundled Archivo font, are listed in THIRD-PARTY.md.

## Legal

NSLibrary is an independent, unofficial project. It is **not affiliated with, endorsed by, or
associated with Nintendo**. Nintendo Switch is a trademark of Nintendo. All product names, logos,
and brands are the property of their respective owners, and are used only to describe what this
software interoperates with.

NSLibrary is a file manager and a transfer tool. It ships no games, no keys, no firmware, and no
copyrighted Nintendo material of any kind; every test fixture in this repository is synthetic and
generated from scratch. It provides no way to obtain content, and does not circumvent any protection
measure — `prod.keys` must already be extracted from a console you own, and is optional.

What you do with it is your responsibility. Dumping content you own is treated differently in
different countries; downloading or sharing content you do not own is not something this project
supports, and running modified system software may violate Nintendo's terms of service and can get
a console banned from online services.

# Snail Walk: Step Tracking Survival Fitness Game

## 关联链接

- http://localhost:5173.
- http://localhost:8465
- https://github.com/tuckerwales/nslibrary.git

## 导航

- 项目页：[[10-项目/github.com_e888bd5c]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
