---
type: "corpus"
item_id: "8932e75dc77ab366"
title: "Show HN: AirFlick Drop – AirDrop for Windows with zero mobile app installs"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50329581"
project_url: "https://github.com/k39139215-gif/airflick-drop"
author: "Snapmotion3421"
published_at: "2026-11-01T20:38:02Z"
captured_at: "2026-11-02T09:37:22+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-02"
pub_day: "2026-11-01"
tags:
  - 语料
  - hn_show
  - author_Snapmotion3421
  - story_50329581
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: AirFlick Drop – AirDrop for Windows with zero mobile app installs

> [!info] 一句话导读
> k39139215-gif/airflick-drop

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50329581>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：Snapmotion3421　|　发布：2026-11-01T20:38:02Z
> 项目链接：<https://github.com/k39139215-gif/airflick-drop>
> 采集：2026-11-02T09:37:22+08:00　|　id：`8932e75dc77ab366`

## 正文

# k39139215-gif/airflick-drop

⚡ AirDrop alternative for Windows, Android & iOS. Transfer up to 15GB over local Wi-Fi, Hotspot, or 5G with zero-RAM streaming, Bump-to-Top, and zero app installs.

- Stars: 2
- Forks: 0
- Watchers: 2
- Open issues: 0
- Homepage: https://k39139215-gif.github.io/airflick-drop/
- Default branch: main
- Created: 2026-10-24T17:05:56Z

## Languages

- Batchfile
- HTML
- JavaScript
- Python
- Shell
- VBScript

## Topics

- airdrop
- airdrop-alternative
- android
- cross-platform
- file-transfer
- flask
- ios
- local-share
- offline-first
- pwa
- pyqt6
- quick-share
- snapdrop-alternative
- windows
- zeroconf

## Top Contributors

- k39139215-gif (23 contributions)

---

## README

# ⚡ AirFlick Drop

> **The zero-friction, cross-platform AirDrop alternative for Windows, Android, and iOS.**
> Flick photos, 4K videos, and files up to **15 GB** from any phone to your computer with zero-RAM chunked streaming, 3D physics gestures, smart Bump-to-Top placement, and **zero app installs on mobile**.

 🌐 Open Live Web App (Permanent Domain)

---

## 🌟 The Cross-Ecosystem Breakdown

Apple AirDrop is brilliant inside the Apple walled garden, but completely breaks down across platforms:
- ❌ **iPhone ➔ Windows**: AirDrop does not exist on Windows. Users resort to slow cables, WhatsApp compression, or emailing files to themselves.
- ❌ **Android ➔ Mac**: Quick Share doesn't work on macOS.
- ❌ **Snapdrop / WebRTC Clones**: Disconnect constantly when networks switch, freeze on files over 500 MB, and require both devices on the exact same router.

**AirFlick Drop fixes all of them permanently:**
- 📱 **Send from ANY Phone**: iPhone (Safari), iPad, Android (Chrome, Samsung Internet) — **Zero apps to install**!
- 💻 **Receive on Windows**: Desktop companion with silent Windows startup, auto-detecting Wi-Fi/Hotspot transitions, and Desktop Bump-to-Top sorting.
- 🌐 **Works Anywhere**: Seamlessly switches between **100% Offline Local Wi-Fi** (0 MB internet) and **Worldwide 5G/Mobile Data** (via secure Cloudflare Tunnel).

---

## 📊 Feature Comparison: Why AirFlick Drop?

| Feature | AirFlick Drop ⚡ | Apple AirDrop 🍎 | Samsung / Google Quick Share 📱 | Snapdrop / ShareDrop 🌐 |
| :--- | :---: | :---: | :---: | :---: |
| **Windows 10/11 Support** | ✅ **Native Companion** | ❌ No | ⚠️ Windows App Only | ⚠️ Browser Only |
| **iPhone ➔ Windows** | ✅ **Native Zero-Lag** | ❌ Impossible | ❌ Impossible | ⚠️ Drops connections |
| **Android ➔ Windows** | ✅ **Instant** | ❌ Impossible | ⚠️ Same account needed | ⚠️ WebRTC freezes |
| **Mobile App Install** | ❌ **Zero (PWA Web)** | ⚠️ Built-in iOS only | ⚠️ Android only | ❌ Zero |
| **Max File Size** | 🚀 **Up to 15 GB** | ⚠️ ~4 GB practical | ⚠️ 3 GB limit | ❌ Crashes >500 MB |
| **Different Networks (5G)**| ✅ **Full 5G Support** | ❌ Same Wi-Fi only | ❌ Same Wi-Fi only | ❌ Same Wi-Fi only |
| **100% Offline (No Internet)**| ✅ **Local Wi-Fi / Hotspot** | ✅ Ad-hoc Wi-Fi | ⚠️ Needs Bluetooth handshake | ❌ Needs signaling server |
| **Desktop Auto-Sort** | ✅ **Smart Bump-to-Top** | ❌ Dumps into Downloads | ❌ Dumps into Downloads | ❌ Dumps into Downloads |
| **Device Pairing & Privacy** | 🛡️ **Cryptographic Token** | ⚠️ Broadcasts to contacts | ⚠️ Account required | ❌ Public / Unsecured |

---

## 🚀 Key Features

* **📱 Flick-to-Screen Gestures**: Drag the file card and flick upward toward your computer screen with real-time 3D tilt perspective, Web Audio synthesized whoosh effects, and physical haptic feedback.
* **⚡ 15 GB Large File Streaming**: Uses 4MB chunked streaming over local HTTP. Files stream directly to disk without bloating mobile or laptop RAM.
* **⏸ Pause, Resume & Cancel**: Real-time Transfer HUD with live MB/s speed, progress bar, `⏸ Pause` / `▶ Resume`, and `✕ Cancel` (with automatic partial file cleanup).
* **🚀 Smart Bump-to-Top on Desktop**: When a file lands on Desktop, AirFlick silently refreshes its timestamp to the current second so it immediately appears at the top of your Desktop grid.
* **🛡️ Zero Data Breach Security**: Server only accepts uploads; it contains **zero file-browsing or download endpoints**. Unpaired strangers are rejected with `401 Unauthorized`.
* **🔄 Dual-Engine Connectivity**:
 * **Online Mode (Anywhere)**: Connects across 5G/Mobile Data and home Wi-Fi via secure Cloudflare Tunnel.
 * **Offline Mode (100% Offline)**: Connects over local Wi-Fi router or laptop Hotspot with zero internet required.
* **🔌 Silent Windows Autostart**: Launches silently in the Windows system tray on boot — zero black terminal windows or annoying popups.

---

## 🛠️ Architecture

```
airflick-drop/
├── main_window.py      # PyQt6 desktop GUI (QR code, network change listener, tray)
├── server.py           # Flask HTTP chunked streaming server (CORS + Token auth)
├── tunnel.py           # Cloudflare Tunnel manager with auto-sync to cloud Gist
├── autostart.py        # Windows Startup registration (StartAirFlick.vbs)
├── web/                # Mobile client PWA web app (served via GitHub Pages)
│   ├── index.html      # Mobile UI with 3D flick physics & full-fit preview
│   ├── manifest.json   # PWA manifest with native AirFlick icon
│   ├── sw.js           # Offline service worker cache
│   └── icon.png        # 512x512 app icon
├── tests/              # Automated unit test suite (pytest)
│   ├── test_server.py  # Server endpoint tests
│   └── test_tunnel.py  # Tunnel binary and health tests
├── docs/               # System documentation
│   ├── ARCHITECTURE.md # Network topology & data flow
│   └── TROUBLESHOOTING.md # Comprehensive troubleshooting guide
└── scripts/
    └── doctor.py       # Automated diagnostic health-check CLI tool
```

---

## 🚀 Quickstart

### 1. Prerequisites
* Python 3.10+
* Windows 10/11, macOS, or Linux
* Any modern mobile browser (iOS Safari, Android Chrome, Samsung Internet)

### 2. Installation
```bash
git clone https://github.com/k39139215-gif/airflick-drop.git
cd airflick-drop
pip install -r requirements.txt
```

### 3. Run AirFlick
**On Windows:**
```bash
python main_window.py
```
*(AirFlick will also automatically install a silent Windows startup launcher so it runs in the background on every reboot).*

### 4. Connect Phone
1. Scan the QR code displayed on the companion window with your phone's camera.
2. Pick any photo, document, or huge 4K video.
3. **Flick it up toward your screen** — it lands on your computer's Desktop instantly!

---

## ❓ Frequently Asked Questions (FAQ)

### Can I transfer files from iPhone to Windows without iTunes or cables?
Yes! AirFlick Drop works directly in iOS Safari with zero app installs. Simply open the QR code or link, pick your photos/videos from the native iOS picker, and flick them to your Windows PC.

### Does AirFlick Drop compress my 4K videos or photos?
No. Unlike WhatsApp or Telegram which compress your photos, AirFlick Drop transfers the exact raw byte stream untouched with 100% original quality.

### Does it work when my internet is offline?
Yes! Connect both devices to the same Wi-Fi router (even with no internet connection) or turn on your laptop's Mobile Hotspot. AirFlick will transfer directly over local Wi-Fi waves at up to 80 MB/s.

### Is my data safe from strangers?
Yes. AirFlick server has zero file-browsing or download endpoints — your computer files can never be viewed from the outside. In addition, every desktop generates a cryptographic pairing token so only your paired phone can flick files.

---

## 📄 License
MIT License. Open source and free for personal and commercial use.

# nouli-ai/nouli

## 关联链接

- https://github.com/k39139215-gif/airflick-drop.git
- https://k39139215-gif.github.io/airflick-drop/

## 导航

- 项目页：[[10-项目/github.com_2e11dee0]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
