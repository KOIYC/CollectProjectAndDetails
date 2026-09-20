---
type: "corpus"
item_id: "f14518634e641c17"
title: "Show HN: I was able to run tiberian sun on cncnet on an M4 MacBook Pro"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49112215"
project_url: "https://github.com/piyiotisk/cncnet-ts-client-package/blob/master/docs/running-tiberian-sun-on-apple-silicon-macos.md"
author: "piyiotisk"
published_at: "2026-07-30T16:25:03Z"
captured_at: "2026-09-21T03:16:05+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-07-30"
tags:
  - 语料
  - hn_show
  - author_piyiotisk
  - story_49112215
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:83d"
---

# Show HN: I was able to run tiberian sun on cncnet on an M4 MacBook Pro

> [!info] 一句话导读
> docs/running-tiberian-sun-on-apple-silicon-macos.md

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49112215>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：piyiotisk　|　发布：2026-07-30T16:25:03Z
> 项目链接：<https://github.com/piyiotisk/cncnet-ts-client-package/blob/master/docs/running-tiberian-sun-on-apple-silicon-macos.md>
> 采集：2026-09-21T03:16:05+08:00　|　id：`f14518634e641c17`

## 正文

# docs/running-tiberian-sun-on-apple-silicon-macos.md

- Branch: master
- Repository: piyiotisk/cncnet-ts-client-package

---

# Running CnCNet Tiberian Sun on Apple Silicon macOS

The ARM64 CnCNet client runs natively on Apple Silicon, while the original 32-bit Windows game runs through Wine.

## Compatibility status

Tested with:

- Apple M4
- macOS 26.5.2
- .NET 8.0.129
- Wine 11.0

The launcher, CnCNet lobby connection, local skirmish, graphics, mouse, and keyboard were verified. Audio, Intel Macs, a completed live online match, and client updates have not been verified.

## What you need

- An Apple Silicon Mac
- Homebrew
- Rosetta 2
- Internet access
- Terminal

## Install

Install Homebrew from brew.sh if it is not already installed. Then open Terminal and run:

```bash
softwareupdate --install-rosetta --agree-to-license
brew install dotnet@8
brew install --cask wine-stable
mkdir -p ~/Developer
cd ~/Developer
git clone https://github.com/piyiotisk/cncnet-ts-client-package.git
cd cncnet-ts-client-package
./TSLauncherUnix.sh --check
```

The final command performs a preflight check and reports whether the required runtime, Wine setup, Rosetta support, and package files are available.

Wine Homebrew casks are deprecated for Gatekeeper and will be disabled **2026-09-01**. The `wine-stable` command above is the currently tested installation path and remains the recommendation before that deadline.

After 2026-09-01, use a maintained release from Gcenx macOS Wine builds. That fallback has **not** been validated for this guide. If macOS blocks the downloaded app, approve it only through the normal prompt in **System Settings > Privacy & Security**; do not remove quarantine attributes or bypass Gatekeeper. Select its Wine executable with the supported absolute-path override on every preflight and launch:

```bash
WINE="/absolute/path/to/the/installed/Wine.app/Contents/Resources/wine/bin/wine" ./TSLauncherUnix.sh --check
```

## How to run it

Homebrew `wine-stable` users can use the plain launcher for the first launch and future sessions:

```bash
cd ~/Developer/cncnet-ts-client-package
./TSLauncherUnix.sh
```

Gcenx/manual fallback users must provide the absolute Wine path on every launch because a shell variable from a previous Terminal session does not persist:

```bash
cd ~/Developer/cncnet-ts-client-package
WINE="/absolute/path/to/the/installed/Wine.app/Contents/Resources/wine/bin/wine" ./TSLauncherUnix.sh
```

After the first successful preflight, `--check` is optional. Use it again whenever you want to verify the setup without launching the client.

## Display settings

In the CnCNet client settings:

1. Choose **1600×900** as the client resolution.
2. Disable **borderless client mode**.

The launcher sets `SDL_VIDEO_HIGHDPI_DISABLED=1` so Retina display scaling does not misalign the mouse coordinates. Keep the in-game resolution separate from the client resolution: changing the game resolution does not replace the client settings above.

## Important: skip every unvalidated update

If the client offers an update, including 7.07 or 7.08, click **No** unless that specific update has been validated for this setup. `versionconfig.ini` includes `TSLauncherUnix.sh` and `wine-ts.sh`, but omits `macos-common.sh`. An update can therefore replace the launchers without updating the helper they depend on and break this setup.

## How it works

- `clientogl.dll` runs through native ARM64 .NET 8.
- The launchers always use the isolated package-local 64-bit Wine prefix at `wineprefix/`.
- Any ambient `WINEPREFIX` value is ignored; the prefix location is not an override point.
- Wine WoW64 runs the original 32-bit `game.exe`.
- Rosetta 2 supports the required Intel execution path.
- CnC-DDRAW translates the game's legacy DirectDraw rendering to OpenGL.
- `wine-ts.sh` forwards CnCNet spawn arguments to the game unchanged.

This split keeps the modern CnCNet interface native while using Wine only for the original Windows game.

## Troubleshooting

### Missing .NET 8

If preflight reports that ARM64 .NET 8 or `Microsoft.NETCore.App 8.x` is missing, run:

```bash
brew install dotnet@8
```

Then rerun `./TSLauncherUnix.sh --check`.

### Missing Wine

Before 2026-09-01, if preflight reports that Wine or WoW64 support is missing, run:

```bash
brew install --cask wine-stable
```

Then rerun `./TSLauncherUnix.sh --check`. Homebrew Wine casks will be disabled after that date; use the unvalidated maintained fallback and absolute `WINE` override described in Install.

### A stale runtime override or PATH selects the wrong executable

`DOTNET` takes precedence over `DOTNET_ROOT`, and both take precedence over automatic .NET discovery. `WINE` takes precedence over Wine discovery. Clear stale overrides and let the launcher discover the installed tools:

```bash
unset DOTNET DOTNET_ROOT WINE
export PATH="/opt/homebrew/opt/dotnet@8/bin:/opt/homebrew/bin:/usr/bin:/bin"
./TSLauncherUnix.sh --check
```

Alternatively, select known executables explicitly. Use `DOTNET` or `DOTNET_ROOT`, not both:

```bash
unset DOTNET_ROOT
DOTNET="/opt/homebrew/opt/dotnet@8/bin/dotnet" \
WINE="/Applications/Wine Stable.app/Contents/Resources/wine/bin/wine" \
./TSLauncherUnix.sh --check
```

For a `DOTNET_ROOT` setup:

```bash
unset DOTNET
export DOTNET_ROOT="/opt/homebrew/opt/dotnet@8/libexec"
./TSLauncherUnix.sh --check
```

Replace the Wine path with the absolute executable path inside the app you installed. To diagnose an unexpected `PATH` choice before setting an override, run `command -v dotnet` and `command -v wine`.

### `WINEARCH=win32` is unsupported

Current macOS Wine does not support a 32-bit-only prefix. If `WINEARCH=win32` is set in your Terminal session, unset it and use the normal 64-bit WoW64 prefix:

```bash
unset WINEARCH
./TSLauncherUnix.sh --check
```

### macOS blocks Wine

If Gatekeeper blocks Wine, use the normal approval shown in **System Settings > Privacy & Security**, then retry. Do not disable Gatekeeper.

### Mouse pointer is offset

Confirm that you launched through `./TSLauncherUnix.sh`, selected a **1600×900 client resolution**, and disabled **borderless client mode**. Retina scaling or borderless client mode can cause the visual pointer and click coordinates to differ.

### Missing `Language.dll`

The launcher normally creates `Language.dll` from `Resources/language_1024x720.dll` without overwriting an existing file. If preflight reports any missing package file, restore or reclone the checkout. The error prints the exact expected path; do not substitute an unrelated file with the same name.

### The launcher exits and the Terminal prompt returns

The launchers use `exec`, so the Terminal remains attached to the client or game process and the prompt normally returns when that process exits. A clean exit does not print a separate launcher-complete message.

If the prompt returns with an error or a nonzero status, capture the output and report the exact command, status, and `launcher.log` instead of assuming the cause:

```bash
./TSLauncherUnix.sh >launcher.log 2>&1
status=$?
cat launcher.log
printf 'launcher status: %s\n' "$status"
```

### Pause-menu artwork does not fill the screen

Some pause-menu artwork has a fixed size and may not cover the full screen at higher in-game resolutions. This is a cosmetic limitation, not a failed launch.

### Run the automated checks

From the package directory, run:

```bash
./tests/macos-launcher-tests.sh
```

## What was verified

The macOS launcher test suite passed all **28 automated tests**. Manual checks verified that the native client launches, connects to the CnCNet lobby, starts a local skirmish, and provides working graphics, mouse, and keyboard input. Audio, a completed live online match, and client updates were not tested.

## Legal and credits

EA released Tiberian Sun as freeware. This package and guide rely on the work of CnCNet, Wine, MonoGame/.NET, and CnC-DDRAW. Their respective projects and trademarks remain with their owners.

# OrangeCrumbs HN Reader - CrumbTrail for Hacker News

## 关联链接

- https://github.com/piyiotisk/cncnet-ts-client-package.git

## 导航

- 项目页：[[10-项目/github.com_4246a412]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
