---
type: "corpus"
item_id: "7e9f5064139163a3"
title: "Show HN: Noctty – A fast, native terminal for Windows"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50341301"
project_url: "https://github.com/amanthanvi/noctty"
author: "amanthanvi"
published_at: "2026-11-02T18:29:09Z"
captured_at: "2026-11-03T09:40:36+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-03"
pub_day: "2026-11-02"
tags:
  - 语料
  - hn_show
  - author_amanthanvi
  - story_50341301
  - show_hn
metrics: {"points": 3, "comments": 1, "engagement_velocity": 3}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Noctty – A fast, native terminal for Windows

> [!info] 一句话导读
> A fast, native terminal for Windows. Formerly winghostty. 🌙

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50341301>
> 指标：点赞=3 · 评论=1 · engagement_velocity=3
> 作者：amanthanvi　|　发布：2026-11-02T18:29:09Z
> 项目链接：<https://github.com/amanthanvi/noctty>
> 采集：2026-11-03T09:40:36+08:00　|　id：`7e9f5064139163a3`

## 正文

# amanthanvi/noctty

A fast, native terminal for Windows. Formerly winghostty. 🌙

- Stars: 448
- Forks: 16
- Watchers: 448
- Open issues: 6
- License: MIT License
- Homepage: https://noctty.com
- Default branch: main
- Created: 2026-04-05T20:48:17Z
- Fork: yes

## Languages

- Batchfile
- C
- C#
- C++
- CMake
- CSS
- Dockerfile
- Elvish
- GLSL
- HLSL
- HTML
- JavaScript
- Lua
- Makefile
- Metal
- Nix
- Nushell
- PowerShell
- Python
- Shell
- Zig

## Topics

- terminal
- terminal-emulator
- windows

## Top Contributors

- mitchellh (10842 contributions)
- jcollie (689 contributions)
- qwerasd205 (498 contributions)
- amanthanvi (491 contributions)
- jparise (226 contributions)
- pluiedev (200 contributions)
- jacobsandlund (156 contributions)
- ghostty-vouch[bot] (129 contributions)
- bo2themax (129 contributions)
- dependabot[bot] (117 contributions)

---

## README

 A native Windows terminal built on Ghostty's terminal core.

 Tabs, splits, and session restore · Win32 and OpenGL · No telemetry

 Download
 ·
 Website
 ·
 Getting started
 ·
 Windows guide
 ·
 Status
 ·
 Contributing

 Formerly winghostty. Renamed in August 2026 after a trademark request from the Ghostty team.

---

Noctty is a Windows terminal that pairs the terminal core from
Ghostty with a native Win32 app
written for this fork.

- **Native Windows UI:** tabs, splits, and context menus, per-monitor DPI
 scaling, and IME input.
- **Your shells, found for you:** a shell picker for PowerShell, cmd, Git Bash,
 and WSL distributions.
- **Session restore:** windows, tabs, splits, and working directories come
 back the next time you launch. Running programs are not restored.
- **Command palette:** find and run actions from the keyboard.
- **Know which tab needs you:** tools and coding agents that report their
 status (OSC 7501) mark their tab
 as working, blocked on you, done, or failed, and a notification tells you
 when a background tab needs you.
- **Ghostty config and themes:** most Ghostty options and themes work as they
 are.
- **Private by default:** no telemetry, and crash dumps never leave your PC.

Noctty is young and has one maintainer. It installs alongside your current
terminal and does not replace it, so you can try both side by side. It runs on Windows
only; macOS and Linux are not planned. See docs/status.md for
what works and what is still experimental, and the
capability matrix for a feature-by-feature
comparison with upstream Ghostty.

## Install

**Requirements:** Windows 10 version 1809 (build 17763) or later, or
Windows 11, on x64 or ARM64. The default renderer needs a GPU driver that
supports OpenGL 4.3 or later.

- Where OpenGL 4.3 cannot start (common over Remote Desktop and in VMs
 without 3D acceleration), Noctty switches on its own to its Direct3D 11
 renderer (beta): hardware Direct3D 11, then Microsoft's WARP software
 renderer, with a banner saying so. It draws text without OpenGL; custom
 shaders, background images, and Kitty images need OpenGL. Set
 `renderer = d3d11` (or `renderer = d3d11-warp` for WARP alone) to start
 with it. Remote Desktop has not been measured
 (details).
- On Windows on Arm PCs, install the free **OpenCL, OpenGL, and Vulkan
 Compatibility Pack** from the Microsoft Store
 (why),
 or use the Direct3D 11 renderer (beta). The ARM64 build includes it.

The latest release is
noctty 1.3.134,
published 2026-10-20.

### With WinGet

```powershell
winget install --id AmanThanvi.noctty -e
```

### With Scoop

```powershell
scoop bucket add noctty https://github.com/amanthanvi/scoop-noctty
scoop install noctty/noctty
```

### Direct download

The installer adds a Start menu entry, an "Open noctty here" item to
Explorer's right-click menu, and an uninstaller. The portable ZIP runs from
any folder without installing.

| Your PC | Installer | Portable |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **x64** (Intel and AMD) | `noctty-1.3.134-windows-x64-setup.exe` | `noctty-1.3.134-windows-x64-portable.zip` |
| **ARM64** (Windows on Arm PCs) | `noctty-1.3.134-windows-arm64-setup.exe` | `noctty-1.3.134-windows-arm64-portable.zip` |

> [!NOTE]
> Releases are signed with a self-signed certificate, so Windows SmartScreen
> shows "Windows protected your PC" when you first run one. Check the download
> first, then click **More info**, then **Run anyway**. Hash the file and
> compare the result with its line in `SHA256SUMS-windows-x64.txt` or
> `SHA256SUMS-windows-arm64.txt` from the same release:
>
> ```powershell
> Get-FileHash .\noctty-1.3.134-windows-x64-setup.exe -Algorithm SHA256
> ```
>
> A matching checksum shows the file arrived intact, not who published it.
> docs/verify-release.md covers the stronger
> provenance and signature checks.

Each release also includes signed manifests of the portable ZIP contents
(`noctty-1.3.134-windows-x64-portable.manifest.ps1` and
`noctty-1.3.134-windows-arm64-portable.manifest.ps1`) and `SHA256SUMS.txt`, an
alias of the x64 checksum file kept for older auto-update clients. Newer
releases also publish a symbols zip per architecture,
`noctty- -windows- -symbols.zip`, for reading crash dumps;
docs/windows.md says which
releases have it.

Scoop puts `noctty` on your `PATH`. WinGet runs the installer, and neither the
installer nor the portable ZIP adds it.
To run the `noctty` commands in this README, add the install folder to `PATH`
or run `.\noctty.com` from that folder.

For portable mode and uninstalling, see
docs/getting-started.md. Switching terminals? There
are guides for moving from
Windows Terminal and from
Git Bash/mintty.

## Getting started

On first launch, Noctty writes a config template to
`%LOCALAPPDATA%\noctty\config.ghostty`. Every default is built into the app,
so the template sets no options: add only what you want to change. You can
also press Ctrl +, to open the Settings window.

```ini
font-family = JetBrains Mono
font-size = 12
theme = Dracula
```

Save the file, then press Ctrl + Shift +, to
reload. Run `noctty +list-themes` to browse the bundled themes.

A few keys to start with:

| Action | Keys |
| ------------------ | --------------------------------------------------------------------------------------------- |
| Copy / paste | Ctrl + Shift + C / Ctrl + Shift + V |
| New tab | Ctrl + Shift + T |
| Split right | Ctrl + Shift + \\ |
| Split down | Ctrl + Shift + E |
| Move between panes | Alt +arrow keys |
| Command palette | Ctrl + Shift + P |
| Search | Ctrl + Shift + F |
| Settings | Ctrl +, |
| Reload config | Ctrl + Shift +, |

The full list, and how to rebind keys, is in
docs/getting-started.md. To drive
Noctty from scripts and the command line, see
docs/automation.md.

## Privacy and updates

- **No telemetry.** On its own, Noctty goes online only to check for updates,
 from GitHub Releases unless you set another update feed.
- **Updates** are checked when Noctty starts and about every six hours while a
 window stays open, but no request is made if a check succeeded in the last
 24 hours. Nothing is installed until you start the update yourself. Set
 `auto-update = off` to stop checking, or `auto-update = download` to have
 Noctty download and verify the update ahead of time.
- **Crash dumps** stay on your PC in `%LOCALAPPDATA%\noctty\crash` and are
 never uploaded.

The privacy policy describes what Noctty stores on your PC, the
connections it makes, and how to remove your data. More detail on updates is
in docs/windows.md.

## Troubleshooting

- **Won't start?** If a broken config or saved session blocks launch, run
 `noctty --safe-mode`. It starts once with built-in defaults and no session
 restore, so you can fix the config. It still needs OpenGL 4.3; without it,
 see Starting without OpenGL.
- **Crashed?** `noctty +crash-report` lists the local crash dumps. For a bug
 report, `noctty +diagnostic-bundle` writes a support bundle that leaves out
 terminal content, commands, and config values by default. Crash dumps can
 hold sensitive memory, so review anything before you share it.

See docs/windows.md for more.

## Build from source

You need:

- Zig 0.15.2 or a later 0.15.x release
- Visual Studio 2022 with the MSVC toolchain on `PATH`
- Git for Windows

```powershell
git clone https://github.com/amanthanvi/noctty.git
cd noctty
zig build -Demit-exe=true
```

The app is built to `zig-out\bin\noctty.exe`, beside Microsoft's pinned ConPTY
pair, which the first build downloads. Building has no Windows version
requirement of its own, but running the result needs Windows 10 1809 or later.
HACKING.md covers the dev shell, offline builds and tests, and
PACKAGING.md covers building the installer and portable ZIP.

## Relationship to Ghostty

Noctty is a fork of Ghostty. It takes in upstream changes in planned merge
windows, normally after each Ghostty release; see the
upstream merge policy, and
docs/status.md for the Ghostty version it is
currently based on. It shares
Ghostty's terminal core, fonts, renderer, input handling, config, shell
integration, and `libghostty-vt`. The Win32 app, the updater, and the Windows
packaging were written for this fork, and the macOS and GTK apps have been
removed. When Windows conventions and upstream behavior disagree, Noctty
follows Windows.

Noctty is an independent project and is not affiliated with Ghostty.

## Contributing

Bug reports and focused pull requests are welcome. Please read
CONTRIBUTING.md and AI_POLICY.md first.

- **Questions and ideas:** Discussions
- **Bugs you can reproduce:** Issues

Pull requests are reviewed automatically by Greptile.

Greptile: The War on Bugs

## License

MIT, the same as Ghostty. Copyright © 2024 Mitchell Hashimoto, Ghostty
contributors. Changes made in this fork are released under the same license.
See LICENSE.

Error fetching https://github.com/thaimtl/Silent-Voice: CRAWL_LIVECRAWL_TIMEOUT
Error fetching https://github.com/joebew42/aido: CRAWL_LIVECRAWL_TIMEOUT

## 评论（1/1）

> **andunie** · 2026-11-02T21:58:44.000Z　
> I don't use Windows, but I appreciate the fact that this is so weird. Will try to remember it the next time I have to use a terminal on Windows.

## 关联链接

- https://github.com/amanthanvi/noctty.git
- https://github.com/amanthanvi/scoop-noctty
- https://github.com/joebew42/aido:
- https://github.com/thaimtl/Silent-Voice:
- https://noctty.com

## 导航

- 项目页：[[10-项目/github.com_12c26964]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
