---
type: "corpus"
item_id: "b3a67ca6e1fe9aff"
title: "Show HN: BuildBy – find out how many Electron apps are on your Mac or Windows"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48338536"
project_url: "https://github.com/wavever/buildby"
author: "wavever"
published_at: "2026-05-30T17:13:32Z"
captured_at: "2026-09-21T02:52:51+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-21"
pub_day: "2026-05-30"
tags:
  - 语料
  - hn_show
  - author_wavever
  - story_48338536
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:144d"
---

# Show HN: BuildBy – find out how many Electron apps are on your Mac or Windows

> [!info] 一句话导读
> CLI tool to detect desktop app tech stacks, code signatures, and notarization status. 桌面应用技术栈、代码签名与公证状态识别 CLI 工具。

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48338536>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：wavever　|　发布：2026-05-30T17:13:32Z
> 项目链接：<https://github.com/wavever/buildby>
> 采集：2026-09-21T02:52:51+08:00　|　id：`b3a67ca6e1fe9aff`

## 正文

# wavever/buildby

CLI tool to detect desktop app tech stacks, code signatures, and notarization status. 桌面应用技术栈、代码签名与公证状态识别 CLI 工具。

- Stars: 67
- Forks: 3
- Watchers: 67
- Open issues: 0
- License: MIT License
- Homepage: https://www.npmjs.com/package/@wavever/buildby
- Default branch: master
- Created: 2026-03-10T17:58:43Z

## Languages

- JavaScript

## Topics

- app-inspection
- cef
- cli
- codesign
- desktop-app
- desktop-applications
- developer-tools
- electron
- flutter
- macos
- nodejs
- notarization
- npm-package
- qt
- tauri
- tech-stack
- windows

## Top Contributors

- wavever (25 contributions)

---

## README

 buildby

 Detect what desktop apps are built with.

 简体中文
 ·
 Install
 ·
 Usage
 ·
 Tech Stacks

`buildby` inspects desktop applications on macOS and Windows, then tells you whether each app is built with **native technologies** (Swift, Objective-C, Win32) or a **cross-platform framework** such as Electron, Flutter, Tauri, Qt, JVM, CEF, NW.js, React Native, wxWidgets, Unity, or .NET.

It also surfaces **signature and notarization** details for single-app inspection, including developer name, Team ID, signature status, Apple notarization on macOS, Authenticode status on Windows, and Hardened Runtime status.

## Highlights

- Fast file-system based detection with no admin privileges required.
- Single-app inspection, full installed-app scan, and per-stack filters.
- Signature and notarization metadata for macOS and Windows apps.
- npm package, GitHub Release artifact, and GitHub Packages publishing.
- Works as a small global CLI: `buildby `.

## Screenshots

| Inspect a single app | Scan all installed apps | Filter by tech stack |
| :---: | :---: | :---: |
| | | |

## Install

```bash
# Install from npm
npm i -g @wavever/buildby

# Clone and link globally
git clone https://github.com/wavever/buildby.git
cd buildby
npm install
npm link

# Or run directly
node bin/buildby.js <command>
```

> Previously published as `desktop-app-build-by`. That name is now **deprecated** — please switch to `npm i -g @wavever/buildby`. The CLI command stays `buildby`. See CHANGELOG.md for details.

## Usage

### Inspect a single app

```bash
buildby wechat
buildby discord
buildby "visual studio code"
buildby "clash verge"
```

Output example:

```
  Discord
  /Applications/Discord.app

   CROSS-PLATFORM   ⚡ Electron

  Cross-platform desktop apps with web technologies (HTML/CSS/JS)
  https://www.electronjs.org

  Evidence:
    • Electron Framework.framework
    • app.asar

  Bundle ID: com.hnc.Discord
  Version:   0.0.335
  Size:      375.4 MB

  Signature & Notarization
    Developer:        Discord, Inc.
    Team ID:          53Q6R32WPB
    Signature:        Signed
    Notarization:     Notarized
    Hardened Runtime: ✓ Yes
```

> The **Signature & Notarization** section is only printed for single-app inspection (`buildby ` and `--path`). `--all` and `-- ` skip it so batch scans stay fast.

### Scan all installed apps

```bash
buildby --all
buildby -a
```

Scans all apps in `/Applications` (macOS) or `Program Files` (Windows) and groups them by tech stack with a distribution chart.

> `--scan` is still supported as a legacy alias for `--all`.

Batch scans use a local analysis cache. If an app's version and main executable fingerprint have not changed, BuildBy reuses the previous result so repeated scans are nearly instant.

```bash
buildby --all --no-cache   # Force a fresh analysis
```

### Configuration

BuildBy creates a default JSON config file on first run, then reads it on later runs:

- macOS: `~/.buildby/config.json`
- Windows: `%APPDATA%\buildby\config.json`
- Linux/other: `$XDG_CONFIG_HOME/buildby/config.json` or `~/.config/buildby/config.json`

You can also point to a custom config file with `BUILDBY_CONFIG=/path/to/config.json`; BuildBy will create that file with defaults if it does not exist.

```json
{
  "cache": true,
  "excludeApps": [
    "Xcode",
    "com.apple.Safari",
    "/Applications/VMware Fusion.app"
  ]
}
```

`cache: false` disables the analysis cache by default. `excludeApps` removes matching apps from `--all` and per-stack scans; entries can be app names, Bundle IDs, or full paths. Single-app inspection still works for excluded apps.

### Language

BuildBy follows your terminal or system language by default. To show English output without changing system language:

```bash
LC_ALL=en_US.UTF-8 buildby -a
```

You can also create an alias:

```bash
alias buildby-en='LC_ALL=en_US.UTF-8 buildby'
```

### Filter by tech stack

```bash
buildby -e     # All Electron apps (--electron)
buildby -f     # All Flutter apps (--flutter)
buildby -t     # All Tauri apps (--tauri)
buildby -q     # All Qt apps (--qt)
buildby -j     # All JVM apps (--jvm)
buildby -c     # All CEF apps (--cef)
buildby -d     # All .NET / MAUI / WPF apps (--dotnet)
buildby -b     # All Chromium apps (--chromium)
buildby -W     # All NW.js apps (--nwjs)
buildby -r     # All React Native apps (--reactnative)
buildby -w     # All wxWidgets apps (--wxwidgets)
buildby -u     # All Unity apps (--unity)
buildby -n     # All native apps (--native)
```

### Inspect a custom path

```bash
buildby --path /Applications/SomeApp.app
buildby --path "C:\Program Files\SomeApp"
```

## Detected Tech Stacks

| Stack | Description | Detection Method |
| ------------------- | -------------------------------- | ------------------------------------------------------- |
| ⚡ **Electron** | Node.js + Chromium | `Electron Framework.framework`, `app.asar` |
| 🐦 **Flutter** | Google's UI toolkit | `FlutterMacOS.framework`, `flutter_windows.dll` |
| 🌐 **CEF** | Chromium Embedded Framework | `Chromium Embedded Framework.framework`, `libcef.dll` |
| 🦀 **Tauri** | Rust + system WebView | Binary strings + `resources/` dir, `WebView2Loader.dll` |
| 🔷 **Qt** | C++ cross-platform | `Qt*.framework`, `Qt5Core.dll` / `Qt6Core.dll` |
| ☕ **JVM** | Java/Kotlin/Scala | `jbr/`, `libjvm.dylib`, `.jar` files |
| 🔵 **.NET** | Microsoft .NET / MAUI / WPF | `MonoBundle/`, `coreclr.dll`, `.dll` files |
| 🟩 **NW.js** | Node.js + Chromium (node-webkit) | `nwjs Framework.framework`, `app.nw` |
| ⚛️ **React Native** | Facebook's React for desktop | `React.framework`, `hermes.dll` |
| 🖥️ **Native** | Platform-native technologies | Fallback when no cross-platform signatures found |

## Platform Support

| Platform | App Discovery | Detection |
| -------- | ---------------------------------------------------------------- | ------------------------------------------ |
| macOS | `/Applications`, `~/Applications` | Framework dirs, `otool -L`, plist metadata |
| Windows | `Program Files`, `Program Files (x86)`, `AppData/Local/Programs` | DLL files, directory structure |

## How It Works

Detection is purely **file-system based** — no admin privileges, no binary disassembly.

1. **Framework directory scan** — check `Contents/Frameworks/` for known framework bundles (Electron Framework, FlutterMacOS, Chromium Embedded Framework, Qt*.framework, etc.)
2. **Resource file patterns** — look for `app.asar`, `flutter_assets`, `app.nw`, etc.
3. **JVM detection** — detect bundled JRE/JBR runtimes and `.jar` files
4. **Tauri detection** — use `otool -L` (macOS) to check for system WebKit linkage + `resources/` directory
5. **Metadata extraction** — parse `Info.plist` for bundle ID, version, and display name
6. **Signature & notarization** — invoke `codesign -dv` + `spctl --assess` on macOS, or PowerShell `Get-AuthenticodeSignature` on Windows, to surface developer / Team ID / publisher and Apple notarization or Authenticode trust status
7. **Fallback** — apps with no cross-platform signatures are classified as Native

Detection runs in priority order so the most distinctive signatures are checked first.

## Requirements

- Node.js >= 18
- macOS or Windows
- macOS: `otool`, `codesign`, `spctl` (all bundled with Xcode Command Line Tools)
- Windows: `powershell` on `PATH` (for Authenticode signature reading)

## License

MIT

# https://boxed.github.io/UN-condemns/

## 关联链接

- https://boxed.github.io/UN-condemns/
- https://github.com/wavever/buildby.git
- https://www.electronjs.org
- https://www.npmjs.com/package/@wavever/buildby

## 导航

- 项目页：[[10-项目/github.com_7412e523]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
