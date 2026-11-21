---
type: "corpus"
item_id: "0b86eba1dea60b56"
title: "krisgfx9/Wireless-Device-Battery-Monitor"
source: "github_new"
source_name: "GitHub 新星仓库"
url: "https://github.com/krisgfx9/Wireless-Device-Battery-Monitor"
project_url: "https://github.com/krisgfx9/Wireless-Device-Battery-Monitor"
author: "krisgfx9"
published_at: "2026-11-16T19:28:29Z"
captured_at: "2026-11-21T14:48:29+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-11-19"
pub_day: "2026-11-16"
tags:
  - 语料
  - github_new
  - C++
  - created:>2026-11-07
metrics: {"stars": 5434, "forks": 455, "open_issues": 3591}
comments_count: 0
comments_total: 0
discovered_via: "github:14d"
---

# krisgfx9/Wireless-Device-Battery-Monitor

> [!info] 一句话导读
> Formerly **Wireless Battery**. Version 1.1.0 renamed the app; an update keeps your settings, startup choice and battery history.*

> [!meta]- 语料信息（点开展开）
> 来源：GitHub 新星仓库（post）
> 原帖：<https://github.com/krisgfx9/Wireless-Device-Battery-Monitor>
> 指标：stars=5434 · forks=455 · open_issues=3591
> 作者：krisgfx9　|　发布：2026-11-16T19:28:29Z
> 项目链接：<https://github.com/krisgfx9/Wireless-Device-Battery-Monitor>
> 采集：2026-11-21T14:48:29+08:00　|　id：`0b86eba1dea60b56`

## 正文

# BatteryHub

*Formerly **Wireless Battery**. Version 1.1.0 renamed the app; an update keeps your settings, startup choice and battery history.*

[![Support me on Ko-fi](https://img.shields.io/badge/Ko--fi-Support%20me-FF5E5B?logo=ko-fi&logoColor=white)](https://ko-fi.com/krisgfx)
[![Donate with PayPal](https://img.shields.io/badge/PayPal-Donate-00457C?logo=paypal&logoColor=white)](https://www.paypal.com/paypalme/krisgfx)
[![GitHub Sponsors](https://img.shields.io/badge/GitHub-Sponsor-EA4AAA?logo=githubsponsors&logoColor=white)](https://github.com/sponsors/krisgfx9)
[![Join our Discord](https://img.shields.io/badge/Discord-Join%20us-5865F2?logo=discord&logoColor=white)](https://discord.gg/ZgDDUPP8ye)
[![Star on GitHub](https://img.shields.io/github/stars/krisgfx9/Wireless-Device-Battery-Monitor?style=flat&logo=github&label=Star)](https://github.com/krisgfx9/Wireless-Device-Battery-Monitor)
[![Share on Reddit](https://img.shields.io/badge/Reddit-Share-FF4500?logo=reddit&logoColor=white)](https://www.reddit.com/submit?url=https%3A%2F%2Fgithub.com%2Fkrisgfx9%2FWireless-Device-Battery-Monitor&title=Wireless%20Battery%3A%20battery%20levels%20of%20your%20wireless%20devices%20on%20the%20Windows%20taskbar)
[![Report a device](https://img.shields.io/badge/Report-a%20device-2EA44F?logo=github&logoColor=white)](https://github.com/krisgfx9/Wireless-Device-Battery-Monitor/issues/new)
[![Help translate](https://img.shields.io/badge/Help-translate-6F42C1?logo=googletranslate&logoColor=white)](https://github.com/krisgfx9/Wireless-Device-Battery-Monitor/pull/129)

Battery levels of your wireless mouse, headset, keyboard and controller, right on the Windows taskbar.

![BatteryHub on the taskbar](docs/screenshot.png)

> **Just want it working?** Download **[BatteryHub-Setup](https://github.com/krisgfx9/Wireless-Device-Battery-Monitor/releases/latest)** from the latest release. Use the per-user installation for setup without administrator rights; see the [installation notes](#install) for unsigned-app warnings and the all-users option.
>
> **Experienced users** can grab the portable zip, use the [command-line options](#command-line), or [build it from source](#build) with `make` or `build.bat`.
>
> **Like it?** BatteryHub is free and open source. If it saves you a trip into vendor software, you can support it on [Ko-fi](https://ko-fi.com/krisgfx), [PayPal](https://www.paypal.com/paypalme/krisgfx) or [GitHub Sponsors](https://github.com/sponsors/krisgfx9). It helps me keep my apps free alongside my studies. Not able to donate? A ⭐ star, sharing it, or reporting an unsupported device with a `--dump` helps just as much.

- **Tiny**: a ~350 KB app using about 2 MB of RAM. It's plain C++/Win32, with no runtime and no background service, and supports per-user installation without administrator rights.
- **Vendor apps usually aren't required**: most drivers query devices directly. Some headsets use the bundled [HeadsetControl](https://github.com/Sapd/HeadsetControl) helper. Device-specific setup, firmware patches and conflicts with vendor apps are described in the table and [Limitations](#limitations).
- **Many brands**: Logitech, Razer, SteelSeries, Corsair, HyperX, Glorious, Jabra, JBL, PlayStation and Xbox controllers, Samsung Galaxy Buds, any Bluetooth device Windows knows a battery level for, and every headset the bundled [HeadsetControl](https://github.com/Sapd/HeadsetControl) supports.

## Display

**On the taskbar (default):** `🎧 30%  🖱 93%` next to the notification area, drawn with the Windows icon font.
- **Low battery:** a red number means 15% or less.
- **Charging:** a blue ⚡ appears next to the number. Once the device is fully charged and still on power, it turns into a green ✓.
- **Asleep:** dimmed text means the device is asleep and the last known value is shown. Turn off *Dim sleeping devices* in the menu to keep that value at full brightness.
- **Disconnected (optional):** turn on *Show disconnected devices* to display a dimmed `×` for devices whose driver explicitly reports an offline wireless link. This does not infer disconnection from a missed battery poll; the default remains to hide offline devices.
- **Two devices of one kind:** with two mice (or two controllers...) both would get the same icon, so each one gets a tiny caption of up to 3 letters in the corner of its icon, taken from its name (`MX`, `PRO`), or a number when the names do not tell them apart. A device that is alone in its kind shows no caption.
- **Theme:** it follows light/dark mode and DPI scaling.
- **Transparent taskbar themes** (e.g. Windhawk's Taskbar Styler): turn on *Background behind taskbar text* in the menu to keep the text readable over the wallpaper.
- **Several monitors:** the widget shows on every monitor's taskbar, next to its clock, so it stays visible while a game runs fullscreen. *Show the widget on* in the menu picks *All monitors*, *Main monitor only*, or one display (e.g. only *Display 3*).
- **More display options:** *Icons above percentages* stacks each icon over its level to save width; *Brand colors* shows known brands in their color (Razer green, HyperX red, ...) with a small level bar; two devices of the same kind get a tiny caption so they can be told apart; left and right taskbars get a column of devices.
- **Languages:** English, العربية, Deutsch, Español, فارسی, Français, עברית, 日本語, 한국어, Magyar, Polski, Português (Brasil), Русский, Svenska, Tiếng Việt, Türkçe, Українська, 简体中文 and 繁體中文. The app follows the Windows display language; *Language* in the menu picks another one. See [Translations](#translations) to add or improve a language.
- **Brand colors:** devices of 15 known brands get their maker's color, with a soft glow and a thin level bar under the
  percentage: Razer green, Logitech blue, SteelSeries orange, Corsair yellow, HyperX / ROG / ZOWIE red, PlayStation,
  Xbox, Samsung, Apple, Jabra, JBL, Cooler Master and Steam. Each color has a dark- and a light-taskbar shade. The brand
  comes from the driver that found the device, then the vendor ID, then the name; colors and rules are in
  `src/brands.cpp`. Turn it off with *Brand colors* in the menu.

**Tray icons:** one icon per device with the number drawn in it, plus a "Low battery" notification at 15%. The app switches to this automatically when the taskbar is vertical or can't be found.

**Custom device names:** open the device submenu and select *Rename device...* to set a name
(up to 64 characters). The name is shown in the taskbar widget's tooltip/caption,
tray tooltip and notifications, and the device menu. Use *Reset to original name*
to restore the driver's name. Names are stored locally in the current user's
Windows registry (`Software\WirelessBattery`, `DeviceAliases`), using the stable
device key. Renaming never changes driver matching, protocol queries, or `--list` /
`--dump` diagnostic output. No account or network access is needed.

Hover for details. Click for the menu: every device (click one to hide or show it), display mode, *Refresh now*, *Start with Windows*, and *Exit*. Levels refresh every 60 seconds (*Check battery every* in the menu changes this), and right away when a device is plugged in or the PC wakes up.

## Smart Battery Alerts (experimental)

You can set a **per-device low-battery notification threshold** from each device's
submenu: **Battery alerts** → *Use default (15%)*, *Disable notifications*,
or one of 5%, 10%, 15%, 20%, 25%, 30%, 35%, 40%. The existing 15% default stays
unchanged unless you choose an override. Settings are stored by device key in
the current user's Windows registry (`Software\WirelessBattery`, `AlertThresholds`).

An alert is triggered only from a real, fresh 0–100% battery reading when the
device is connected, awake and not charging. An alert is issued once, and will
re-arm after the level climbs more than 10 percentage points above the chosen
threshold (or when charging begins). Missing readings or sleeping devices do
not retrigger alerts. Hidden devices don't produce notifications. Disabling
notifications for one device does not hide it or change its percentage.

Both taskbar-widget and tray-icon modes support notifications. Since Windows
needs a notification-area icon to display a legacy balloon, widget mode may
show a temporary notification icon for up to one minute after an alert.
Widget colours and the low-battery highlight still use the project's
original global 15% threshold, independently of the notification setting.

## Battery history & insights

Right-click a device in the taskbar widget or tray menu and choose **Battery history...**.
The native, DPI-aware viewer (it follows the Windows light/dark theme) shows recorded battery levels with connected sample lines over the last **24 hours**, **7 days**, or **30 days**, along with the latest reading, lowest/highest level, change in percentage points, and sample count. You can clear the selected device's history from the viewer.

History is recorded **locally only** for connected, awake devices reporting a numeric percentage. Readings are sampled at most once every 30 minutes per device (except charging-state transitions, with a 60-second minimum). Data is kept for up to 30 days and the local file is kept under about 2 MB. The app never probes hardware beyond its existing polling, sends no history data over the network, and makes a conservative, approximate time-to-empty estimate from recent discharge observations only. At least four points, two hours, a three-percentage-point decline, a fresh reading and a stable discharge segment are required. Charging, old readings or insufficient data suppress the estimate; device-reported runtime is not available. The estimate is not a guarantee. Missing chart data is shown as gaps, not interpolated.

Turn off **Record battery history** in the menu to stop saving readings; what was already saved stays until you clear it in the viewer. The file is stored in `%LOCALAPPDATA%\WirelessBattery\battery_history.tsv`. Its device identities are encoded (not encrypted); the file is local to your Windows account. In `--demo`, the chart uses synthetic data that is never saved. **Note:** history starts collecting only after this feature is installed and the app has been running for a while.

## Supported devices

Match your model, receiver VID:PID, connection mode and any firmware requirements to the table; `BatteryHub.exe --dump` shows the IDs. A brand name alone does not confirm support for every model. Hardware-test labels apply only to the stated devices and behaviors.

Redragon M602-KS battery percentage was verified on the 2.4 GHz receiver (`258A:002F`).

| Vendor | Devices | How |
|---|---|---|
| **NuPhy** | WH80 over USB cable (`19F5:A011`) or Bluetooth (`19F5:324A`), hardware-tested | USB: read-only NuPhyIO battery query; Bluetooth: Windows battery level with keyboard classification ([protocol notes](docs/nuphy.md)) |
| **DARKRIM** | SHADOW (寸渊影弑) on its `3654:6901` USB receiver (hardware-tested) | Read-only CRC-checked battery query and charging flag; observed coarse readings in 10% steps, finer precision unverified ([protocol notes](docs/darkrim.md)) |
| **Inphic** | IN10R MAX / IN10 MAX on the KP 8K receiver (`1D57:FA65`; model `73` hardware-tested, model `74` untested) | Passive Xenta status reports; two matching frames confirm the level ([protocol notes](docs/inphic.md)) |
| **ASTRO** | A50 X (`046D:0B0B`, tested), A50 Gen 5 (`046D:0B1C`), A50 Gen 4 (`9886:002C` tested, `002D`/`002A`), A50 Gen 3 (`9886:0015` tested, `0014`/`0018`/`001D`/`0026`), A20 Wireless (`9886:0037`–`0045`), via USB base station | Battery percentage, charging and docked status |
| **Logitech** | Mice and keyboards on Unifying, Bolt, Lightspeed (including the PRO X3 SUPERSTRIKE dongle `046D:C54F`) and Nano receivers, over USB or Bluetooth; G headsets (G533, G535, G633/G635/G733/G933/G935, G PRO/PRO X); G435 on the newer `046D:0ADF` dongle | HID++ 1.0 / 2.0 with feature discovery: unified battery, battery level, voltage, ADC; G435: CRC-16 framed vendor reports, `GET_BATTERY` in mV |
| **Razer** | Wireless mice, keyboards and dongles; BlackShark V2 HyperSpeed, V2 Pro (2020/2023), V3 / V3 Pro / V3 X headsets, V3 Pro for Xbox (`1532:0A55` receiver, `0A4E` cable); Barracuda X (2022) on its 2.4 GHz receiver (`1532:0550` or `1532:0552`); Barracuda Pro (`1532:053A`) | Razer feature-report protocol; BlackShark vendor protocols (V3 / V3 Pro / V3 X queried every 5 min); Barracuda X: Airoha battery and cable queries through the receiver |
| **SteelSeries** | Arctis 1/7/7+/9/Pro/Pro Wireless, Arctis Nova 3P/5/7/7X/7P/Pro Wireless (including `1038:225D`), Arctis Nova Elite (base station `1038:2244`), GameBuds; Aerox 3/5/9 Wireless (Aerox 5 Diablo IV `1038:1860`, untested), Aerox 3 Wireless CS2 Dragon Lore Edition (receiver `1038:1878`, cable `187A`), Aerox 3 Wireless Gen 2 (receiver `1038:1890`, cable `1892`), Prime Wireless, Rival 3 Wireless (Gen 2), Rival 650, Rival Pro | Vendor HID reports; Aerox/Prime and Rival 650 share one entry across receiver and USB cable, preferring the cable reading when both answer |
| **Corsair** | Void / Void Pro / Void Elite / HS70 / HS80 wireless; Bragi devices (Virtuoso, Void V2, HS80 MAX, Slipstream mice and keyboards, including the newer Slipstream receiver `1B1C:2B00`, e.g. Scimitar Elite SE Wireless, and Dark Core RGB Pro SE); Sabre V2 Pro Ultralight Wireless (`1B1C:2B2A`), Sabre v2 PRO WIRELESS MG (`1B1C:2B34`, untested) | Vendor HID reports, Bragi `GET` (read-only), Compx 17-byte battery protocol (read-only) |
| **Cooler Master** | MM712, MM731 (2.4 GHz dongle or USB cable) | Vendor HID status report (read-only) |
| **Press Play** | ICARUS V2 Nearlink on its `7768:6434` 2.4 GHz receiver (hardware-tested at 90%; protocol captured at 100% and 90%) or Bluetooth (hardware-tested; battery detected through Windows Bluetooth support) | Receiver: read-only output report `06 05` on `FFB2:0001`; Bluetooth: Windows battery level when available |
| **HyperX** | Cloud III Wireless, Cloud III S Wireless, Cloud II Wireless (HP, Kingston, DTS), Cloud II Core Wireless, Cloud Alpha Wireless, Cloud Alpha 2 Wireless, Cloud Flight (`03F0:0C8C` for PS, untested), Cloud Flight S, Cloud Stinger Core Wireless (including DTS `03F0:0A8E`, tested), Cloud Core Wireless DTS, Pulsefire Haste 2 Core Wireless (2.4 GHz dongle), Pulsefire Haste 2 Wireless, Pulsefire Haste 2 Mini (2.4 GHz dongle) (2.4 GHz dongle `03F0:0F98`, tested; `0D97` untested) | Vendor HID reports (Haste 2: [protocol notes](docs/hyperx_haste_2.md)) |
| **Glorious** | Model O / O- / D / D- Wireless, Model O 2 / D 2 PRO | Vendor feature report |
| **Hitscan** | Hyperlight X, Hyperlight N | Vendor feature report (same protocol as Glorious) |
| **Kysona / Pulsar / ATK (VXE) / Hitscan** | Kysona M600 / Mercury, Pulsar and ATK VXE wireless mice (e.g. VXE X3 Pro, VXE Dragonfly R1 / R1 Pro Max / R1 SE+, ATK F1 Extreme), Hitscan Hyperlight, Chimera V2 (receiver 3554:F512) | Shared vendor protocol with checksummed replies |
| **Pulsar X2 V3** | X2 V3 on the 1K dongle (`3710:5402`) or USB cable (`3710:3402`); X2 V3 eS on the 8K dongle (`3710:5403`) or USB cable (`3710:3406`) | 64-byte vendor feature report, battery register `08 81 01` (read-only) |
| **ATK / VXE NK** | VXE R1 NK and other NearLink mice on the NK mouse NANO dongle (`373B:1216`) | ATK BITMOUSE output report 08 on `FF05:0001` (battery and charging) |
| **ATK Zero** | USB cable (`373B:1154`) and 8K L0 / L1 receivers (`373B:124F` / `373B:1155`) on Windows | 64-byte ATK BITMOUSE report 08 on `FF05:0001` (battery on both links, charging over the cable) |
| **ATK 8K Nano** | ATK / VXE mice on the ATK 8K Nano Dongle (`373B:1178`) | Holtek GetConfigData (`82`) feature report on `FF10:0001` (from ATK HUB; battery and charging) |
| **ATK headsets** | ATK N9 Pro, N9 Ultra (first generation) | Virtual COM port protocol (the ATK desktop app must be closed) |
| **G-Wolves** | Fenrir, Fenrir Pro / Max / Asym, HTX, HTS, HSK, HTR, HT-S2, Lycan, WARG, VUK and their 8K dongles | Glorious or Kysona protocol, depending on the model |
| **Keychron mice** | M4 and other Keychron mice on the 2.4 GHz receiver; 4K mice (M4 4K, M3 4K, M3 mini 4K, M6 4K ...) on the Keychron 4K Link receiver (`3434:D038`); 8K mice (M5 8K, G6 HE 8K ...) on the TurboLink 8K receiver; 8K mice on the Ultra-Link 8K receiver (`3434:D028`); older mice (M1, M2, M3, M3 mini, M6, M7 ...) on the 1K receiver (`3434:D030` / `D031`); Nape Pro trackball on the Link-KM receiver or cable | Vendor report from Keychron Launcher (1K receiver: feature report 51 06, as used by the Keychron desktop app; Ultra-Link 8K: reports B5 03 / B3 06 on `FFC1`; Nape Pro: raw HID A7 31) |
| **Keychron keyboards** | K5 Max (`3434:0A50`, tested) on the Keychron Link receiver (`3434:D030`) or USB cable; other Keychron QMK wireless keyboards once built with the same patch | Raw HID on `FF60:0061`: `B2` asks the receiver which keyboard is linked, `A4` returns level, voltage and charging. **Needs patched keyboard firmware:** see [docs/keychron_keyboard_firmware/README.md](docs/keychron_keyboard_firmware/README.md). Stock firmware only reports over Bluetooth |
| **CHERRY** | MX 3.0S Wireless keyboard on its 2.4 GHz dongle (`046A:00EA`, tested) or USB cable (`046A:00E3`, tested)Cherry XTRFY wireless mouse on the 1K receiver (`046A:0330`, tested) | MX 3.0S: vendor HID query `1A` on `FF1C:0092` (read-only), with USB-powered state. Bluetooth is covered by the Bluetooth support.XTRFY mouse: CompX 17-byte battery protocol (`08 03` link status, `08 04` GetPower), same framing as the Corsair Sabre V2 Pro (read-only) |
| **Arbiter Studio** | Akitsu (`373E:000A` 8K receiver, `373E:0009` cable), Akitsu 3950 (`373E:0039` 8K receiver, `373E:0038` cable), Akitsu Medium (`373E:0067` 8K receiver and `373E:0066` cable, both tested) | Read-only vendor feature report `0x83` on `FFFF:0000` from Arbiter Web HUB (battery and charging) |
| **LAMZU** | Maya X, Maya, Maya M, Tachi, Inca, Paro, Thorn, Atlantis Mini / OG Champion, Orcus (cable, 1K and 4K/8K dongles) | Vendor feature report from LAMZU Aurora |
| **Endgame Gear** | OP1w 4k (v1 / v2), XM2w 4k (v1 / v2) on the 4K dongle; XM2we on its original receiver (`3367:1961`) | Vendor feature report `A1`, battery command `B4` (read-only) |
| **ATK / VGN / Evision keyboards** | ATK V75X and VGN / VXE keyboards (S99, V98 Pro / V98 Pro V2, N75 Pro, VXE75 / VXE75 V2, VXE V87) on the shared 2.4 GHz receiver (`320F:5088`) or USB cable (`320F:5055`), recognized by product name; keyboards whose `320F:5088` receiver is named "Wireless Gaming Keyboard", e.g. Feker Alice80 (tested) | Evision output report `04`, battery command `1A` (from ATK HUB and VGN HUB); asked at most every 10 minutes over the receiver |
| **ATK Z87** | ATK Z87 Dongle (`373B:1012`, 2.4 GHz receiver) | Battery percentage and charging status on `FF1C:0092`. Battery percentage verified on hardware while discharging |
| **Redragon (Evision)** | K1NG M999 (tested) on the `320F:226F` 2.4 GHz receiver; the receiver id may be shared by other models | Same Evision protocol as the ATK keyboards (report `04`, command `1A` on `FF1C:0092`), asked on every poll; charging shown on the magnetic dock; with the USB cable plugged in the receiver keeps repeating the old level and no charging state |
| **Audeze** | Maxwell on the USB dongle (`3329:4B19`) or USB-C cable (`3329:4B1A`); Maxwell 2 on the USB dongle (`3329:4B29`, tested); Xbox ids untested | Vendor report `06` / input report `07`, battery attribute `0CD6` (single read-only query) |
| **ENDORFY** | Viro Wireless on its 2.4 GHz dongle (`3738:0072`, untested) | Airoha RACE "get battery" (`0CD6`) on vendor report `06` / input report `07`, the same read-only query as Audeze and Skullcandy dongles; no charging state |
| **Turtle Beach** | Stealth 700 Gen 3 on the USB transmitter (`10F5:2251`, tested in HaloBattery; PC version `10F5:2262`, untested) or the headset's own USB cable (`10F5:2253`) | RACE `0x9942` (enable the CoAP client) and a CoAP `GET /GSI` tunnelled in RACE `0x9902`, as Swarm II does; battery from key `240` (no charging flag) |
| **AKG** | N9 Hybrid on its USB dongle (`0ECB:20D9`, tested) | Airoha RACE on `FF13:0001`: output report `06`, input report `07`, battery attribute `0CD6` (single read-only query) |
| **NZXT** | Lift Elite Wireless on its dongle (`1E71:2101`) or USB cable (`1E71:2129`) | Vendor read `4E 02 81 .. B0` (from NZXT CAM captures) |
| **Poly / Plantronics** | Voyager 8200 UC and other headsets behind the BT600 adapter (`047F:02EE` / `02F7`) | Report `07` get/set protocol, battery item `0A 1A` (read only) |
| **WLMouse** | YING Magnesium (YING 8K receiver `36A7:A874`); Beast X 8K, Beast X Mini / Mini Pro, Beast X Pro, Beast MAX, Sword X 8K (receiver or cable; not the Beast X 4K); Beast X V2 (8K receiver `36A7:A856`); Beast G (8K receiver `36A7:A860` or cable `36A7:A861`; untested) | Vendor feature report, status command `0x83` (YING: same protocol as Glorious) |
| **VAXEE** | Wireless mouse on the VAXEE 4K receiver (`3057:1002`) or 8K receiver (`3057:2002`, e.g. NP-01 Ergo Wireless 8K); ZYGEN NP-01S V2 Wireless over USB cable (`3057:1011`) | Read-only vendor feature report `0E` on `FF05:0001`; battery in 5% steps, charging state ([protocol notes](docs/vaxee.md)) |
| **Finalmouse** | UltralightX on its 2.4 GHz dongle (`361D:0100`, tested); Starlight X on its dongle (`361D:0300` / `0301`, tested). Not on the mouse's own cable | xpanel vendor reports on `FF00`: read-only GETs, then *wake/all* (`0xE0`); battery voltage on xpanel's curve, or the Starlight X's own percentage, plus charging state |
| **Scyrox** | V12M on its 2.4 GHz receiver (`395A:0006`) | S-Center 2.0 profile read (output report `08`, command `01`) on `FF00:0002`; battery only, no charging state |
| **HECATE** | G5M PRO and other HECATE mice on the same receiver, and USB cable `35BB:D3FA / D3FC / D3FD` | Kysona protocol |
| **Redragon** | Compx-based wireless mice: M916 Pro 1K (tested), M913 Impact Elite (tri-mode), G49 (receiver or cable) | Kysona protocol (the Areson `25A7` receivers are listed under Areson) |
| **Taidu (钛度)** | TSG808 on its Compx 2.4 GHz receiver `3554:F5D5` (tested) | Kysona protocol |
| **Areson (Redragon)** | M915RGB-WL (tested), original M913 Impact Elite and other mice on the `25A7:FA07` / `FA08` receiver | 17-byte `GetPower` feature report; level in 10% steps and a charging flag |
| **Ninjutso** | Sora V2 on the 1K receiver (`1915:AE1C`, tested) or USB cable (`1915:AE11`, tested); Ten Air (receiver `093A:EB01` and USB cable `093A:E020`, tested) / Ten (`093A:EB01` / `E020`, untested) | NinjaForce feature report `0x05` (`0x15` for Sora V2) and `0x06` (`0x13`/`0x12`/`0x11` for Ten / Ten Air) |
| **Sprime** | PM1 on the 2.4 GHz receiver (`1915:AC1C`, tested; `1915:AD8C`) or USB cable | Same feature report 0x05, status command 0x15, from Sprime's web driver (sprime.pro) |
| **RAWM / SADES** | Leviathan V4 on the RAWM HS Receiver (`1915:2346`, tested); ES21 / ES21 Pro / ES21M, ER21 / ER21 Pro / ER21M, ES11, G11 / G11 Plus / G11 Pro, SA-* and SADES Dagger mice on their RAWM receivers (`1915:232A`–`234B`) or USB cable | RAWM HUB 2.0 device-info query through the receiver (JSON with battery % and charging), read-only ([protocol notes](docs/rawm.md)) |
| **AULA** | F75 / F87 Pro / F99 wireless keyboards on the 2.4 GHz receiver | Report 0x13 frame, command 0x4A, sum checksum (Bluetooth and wired modes untested) |
| **AULA mice** | X9 Ultra (tested) on AULA-8K Dongle `320F:22A0`; receiver ID shared with V9 models | Report `04`, read-only battery command `1A` between START `01` / END `02` on `FF1C:0092`; 2.4 GHz only |
| **DAREU** | EM901X on the `260D:1074` 2.4 GHz receiver or `260D:1090` USB cable (battery reading tested on both; receiver dock/undock charging-flag transitions tested)A84 keyboard (`260D:0022`, untested)A980 Pro on the `260D:1131` multi-mouse receiver and on its USB cable (`260D:1148`) (battery level tested on hardware; charging flag confirmed while plugged in) | EM901X: battery-only feature report `08`, command `04`; reply `09` on a separate vendor collection. Requires one unambiguous input/feature pair per product ID. Prefers a valid USB reading when both are connected; the receiver can return cached telemetry even with the mouse switched off.A84: SONiX feature report on interface 0, command `04 F6` (the official A84 driver's battery read); level in percent, no charging flag.A980 Pro: Togran protocol: 65-byte feature report `0A` on the consumer-control collection; slot query (class 0 / `A0`) then battery query (class 7 / `80`), on slot 0 over the cable. Read-only |
| **SONiX keyboards (AJAZZ / AULA / EPOMAKER)** | AJAZZ AK820 MAX (tested), EPOMAKER EA75 (tested), AULA F108 Pro on the `05AC:024F` 2.4G dongle; AJAZZ AK980 V2 on the `0C45:FEFE` dongle; AJAZZ AK820 Pro on the `0C45:FDFD` or `0C45:FEFE` dongle; EPOMAKER P75 on `342D:E479` (hardware untested) | Vendor report `20 01` on usage page FF60, sum checksum (2.4G mode only; no charging indication) |
| **Additional SONiX receivers (hardware untested)** | RK Royal Kludge R75 (`342D:E485`); Redragon Arlokks K742B (`342D:E4BC`); M1 V5 VIA (`342D:E4C2`); Lucky65V2 (`342D:E407`); Lofree Flow2 (`388D:0003`); MSI FORGE TKL W FRIEREN EDITION (`0DB0:0CA0`); Essential75 (`36B0:30BD`); NUT65 (`342D:E51A`); RK 2.4G Dongle (`342D:E487`); WEIKAV MAX102 (`342D:E537`); Lofree Flow2 (`388D:0002`); NuPhy Air75V2 (`19F5:3245`); SKN Qinglong (`362D:D028`); Lemokey Link (`362D:D030`); Wireless Link (`362D:D101`); Spade65-QMK-2.4GHz (`342D:E49F`) | Same battery-only `20 01` query; exact VID:PID and FF60:0061 collection with 33-byte reports required; 2.4G only, no charging indication |
| **36B0 keyboards (PMO / WOBKEY / URX / EVO80)** | PMO (WOBKEY) Wave 75 RGB on the `36B0:3002` 2.4G dongle or USB cable `36B0:3009` (protocol tested on both by the reporter of #343); Aurora 80 (`3004`), PMO P75 (`302B`), PMO 80 (`3012`) on the same dongle or cable (untested); URX Core75 on the dongle (confirmed in HaloBattery); EVO80 (untested) | PMO Hub firmware: `START_COMM` / `GET_BATTERY` (`AA 30`) / `STOP_COMM` on usage page FF60, from pmohub.cn. URX / VIA firmware: VIA custom-get `08 00 07` (channel 0, value 7), from URX HUB via HaloBattery. No charging indication |
| **Sharkoon** | Skiller SGM50W on `260D:1125` (untested) | Same Compx query as the DAREU EM901X (feature report `08`, command `04`; reply `09` on `FF01:0000`); Sharkoon's firmware updater for it is a Compx tool on VID `260D` |
| **Zenith** | Zenith Pro on the `260D:1114` 2.4 GHz receiver (battery reading tested; charging untested) or `260D:1143` USB cable (untested) | Same Compx command (`08`, `04`) as an output report on `FF02:0002`; reply `08 04` on the same collection with percent, charging flag and millivolts, checked by the `0x55` byte sum |
| **AJAZZ AK992** | Telink 2.4 GHz receiver `320F:50C3` (tested) | EVision battery query on HID collection `FF1C:0092` |
| **ZOWIE** | EC1/EC2/EC3-CW, DW series (U2-DW, S2-DW ...) and U2 on its 2.4 GHz receiver | Community-documented read-only vendor commands |
| **Royal Kludge (RK)** | MG6 Pro on the 2.4 GHz dongle (`2E3C:00A6` / `00E6`) or USB cable (`2E3C:00A5` / `00E5`) | QiWang 64-byte frame from RK's web driver, `GET_BATTER_VOL` read (percent, voltage, charging) |
| **ASUS ROG** | Strix Scope II 96 (RX), Azoth, Falchion keyboards; Keris, Harpe, Gladius, Chakram, Spatha, Pugio, Strix Impact mice; Pelta headset (2.4 GHz dongle); Cetra Open Wireless earbuds (SpeedNova dongle `0B05:1CAC`, L / R / case); the Omni Receiver | ROG HID battery query |
| **Machenike** | L7 Arctic / L7 Mix on the `248A:FF4C` 2.4 GHz receiver or `248A:FF4E` USB cable (both tested) | Read-only feature report `51`, status command `06`; battery and charging. [Protocol notes](docs/machenike.md) |
| **MCHOSE** | L7 / L7 Pro / L7 Ultra (L7 Ultra tested), M7 / M7 Ultra, A7 / A7 Ultra, K7 mice on the 2.4 GHz receiver or USB cable; A5 V2 Ultra (2.4 GHz receiver `3837:100C`, tested), K7 Ultra (2.4 GHz receiver `3837:1001`, tested; A7 V2 Ultra+ `3837:100B` expected to work, issue 227); G3 V2 (2.4 GHz receiver `3837:4245` and USB cable `3837:418C`)K7 V2 Ultra+ on the 2.4 GHz receiver `3837:1014` or on its USB cable `3837:4028` (both tested; the other new-family receiver ids `1018`, `1016`, `102C`, `102D` are untested) | Vendor feature report, inverted payload (protocol from alexfrih/mchose-linux); Realtek `3837` dongles answer the same query with the vid field set to `41E4` (A5 V2 Ultra) or `3837` (K7 Ultra); G3 V2: read-only vendor query on `FF01:0010`.K7 V2 Ultra+: 64-byte report `0x4D`, device-info command `0x0900` on `FF01:0001` (protocol from M HUB's web driver) |
| **MSI** | VERSA 300 ELITE WIRELESS on its 2.4 GHz dongle (`0DB0:9E22`); CLUTCH GM31 Lightweight Wireless (2.4 GHz receiver `0DB0:0D3C`, tested; USB cable `0DB0:0D3B`) and CLUTCH GM41 Lightweight Wireless (receiver `0DB0:0D4C` / cable `0DB0:0D4B`, from an owner's captures) | Read-only vendor query `0F 20` on `FF0D:00B0` and `FF00:0001`; battery and charging flag in one byte (protocol from MSI Center's Gaming Gear module); GM41: passive `A0 xx 07 …` reports on `FF10:0006` |
| **MCHOSE A5 (first generation)** | A5 Pro / A5 Pro Max on the 1K or 4K 2.4 GHz receiver (`2023:F013`, `2023:F015`, `2023:F018`) or the USB cable (`2023:F017` A5 Pro, `2023:F019` A5 Pro Max); untested here | Read-only battery command `0x83` (page 0) in a 64-byte feature report on `FFFF`, reply marked `0xA1` (protocol from the z750sasr A5 Pro Max web driver and HaloBattery, ids from Klegus/mchose-macos) |
| **MCHOSE headsets** | V9 Pro 2 on the 2.4 GHz dongle (`3837:6011`, tested) | M HUB's read-only "MC" battery frame (report `0x55`, sub-command `0x0B`) on `FF07:0222`; battery and charging flag in one byte (protocol from M HUB's web driver) |
| **AULA / MCHOSE / Redragon keyboards** | AULA F75 / F87 Pro / F99; MCHOSE K99 V2, G75 Pro, X75 and the other M HUB keyboards; Redragon Horus Pro / Pro V2 (K618RGB-PRO) on the 2.4 GHz receiver (`3554:FA09`, `41E4:2001`); MCHOSE K87 on the `05AC:024F` receiver (BY layout on interface 1, not the SONiX one) | Report 0x13 frame, command 0x4A (MCHOSE and Redragon models identified by command 0x05, as in M HUB); Bluetooth and wired modes not covered |
| **MCHOSE K87 V3** | K87 V3 keyboard on the `3837:1015` 2.4 GHz receiver (battery reported working by the contributor in PR #2934; charging transitions, USB and Bluetooth untested here) | Read-only modern M HUB device-info command `0x0900`, report `0x4D` on `FF80:0001`; shared with the modern MCHOSE mouse driver, queried every three minutes |
| **MCHOSE keyboards** | G75 V2 on the 2.4 GHz receiver `3837:3033` (tested); the same receiver ships with the G87 V2 and K99 V3 (same protocol, untested); the K87S pairs the same receiver id with a different protocol and is not covered | M HUB's read-only "GLW" func-config query on the id-less 64-byte `0001:0000` collection: request flag `0x55`, command `0x05`, battery in payload byte 32 (bit 7 = charging), additive checksum |
| **AULA SC580** | SC580 / SC580X mouse over USB cable (`088D:062E`, tested) or its 2.4 GHz receiver (`089D:062F`, tested) | Read-only command `0x30` (device info) on the 33-byte vendor collection FF02:0000, sum checksum; while charging the mouse reports a fixed 100, so the last level is shown; Bluetooth mode not covered |
| **AULA HERO 68 Air** | HERO 68 Air on the 8K Wireless Receiver (`372E:106C`) | Acknowledged 20-byte frames on usage page FF60 (four data frames and a trailer per message), read-only battery command 0x87, charging flag 0x10 after the level; Bluetooth and wired modes not covered |
| **EWEADN (前行者)** | S7 Max / Pro / Ultra and S9 Max / Pro / Ultra / Ultra+ on the "Gaming 2.4G" receiver (`372E:103D`); S9 Ultra on its USB cable (`372E:1027`) | Read-only feature report `03` on `FF00:0001`: link check `47`, device basics `4F 81` (battery percent and charging bit), from EWEADN's web driver |
| **Rapoo VT** | VT3 Max Gen 2 (tested); VT9 Gen 2 (tested); other Nordic 54L VT mice exposing the same status interface; legacy VT3 Pro (experimental); VT1 Pro Max (from the owner's USB captures) | Passive HID status report `07` on `FF00:0002` (16 or 19 bytes; 13 bytes on some VT3 Max Gen 2 receivers); legacy `BB` restricted to VT3 Pro `1215/4415` and VT1 Pro Max `1233/4433`. Receiver and USB cable, with charging state |
| **Motospeed / Delux / Ajazz** | Motospeed X6, Delux M900 Pro (Xenta models 30/50; legacy 3D), Delux M800 Pro, Ajazz AJ179 family; AJ159 and other AJ-series mice on the 3151 receiver; AJ139 V2 MC (`A8A5:2255` receiver, `A8A4:2255` cable) | Vendor reports (M900 Pro: passive Xenta events 40/41; AJ-series: 0xF7 status poll, then feature report 0x05) |
| **Incott** | G23 V2 / G24 (`093A:522C` receiver, `093A:622C` cable) | Read-only status feature report 09 |
| **Attack Shark and other Chinese brands** | Rongyuan receivers (81 models: Attack Shark R3 and AJAZZ AJ179 Pro on `3151:402D`, K86, X82 PRO HE, Ajazz keyboards, some MSI and others; the K86 over Bluetooth is shown as a keyboard); Xenta receivers (Attack Shark X6 / R1, X11, X3 Max, V3 Pro, V6; the X6 also on `1D57:FA61`, untested); Semico 1A2C keyboards (Attack Shark X98 on `1A2C:8FFF` dongle, tested, and `1A2C:A034` cable; AJAZZ AK820 Max Plus on `1A2C:8FFF` / `1A2C:A036`) | Rongyuan status report; Xenta passive broadcasts; Semico read-only `0x0E` status query (`AA 55 CC 33` on `FF02:0002`; charging flag omitted because X98 reports `state=1` both on battery and while charging) |
| **Wraith** | W1 / W1 Freestyle (`093A:522C` receiver, `093A:622C` cable; same ids as Incott, told apart by the model code) | Read-only per-button reads `86` (feature report 09) over all buttons, then the pushed status input report 09 |
| **Fantech** | Helios Go XD5 (wired `25A7:FA7B`, dongle `25A7:FA7C`); Raigor III (tested), Raigor II WG10 and other generic 2.4G Mouse devices on the reused `1EA7:0066` / `1EA7:0064` dongle | Helios Go XD5: vendor feature report `08`, command `04`, sum-to-`0x55` checksum. Raigor/2.4G Mouse: read-only `B5` status-page query on `FFB5:0001`, chunk `94` = last reported percent (may be stale while asleep, off or charging; no charging state) |
| **Sony** | DualShock 4, DualSense, DualSense Edge (USB, Bluetooth, wireless adapter); INZONE H9 II and H5 headsets; INZONE Buds (USB-C dongle) | Input report; INZONE vendor protocol |
| **Fractal Design** | Scape headset on its 2.4 GHz dongle or USB-C cable | Vendor `GET_DEVICE_STATE` query from Fractal's Adjust Pro web app (usage page FF00) |
| **Jabra** | Every Jabra headset that speaks the GN Protocol (Evolve2 / Evolve3 and others), on its own USB cable or behind a Jabra Link dongle; no product id list, DECT bases (Engage, PRO 9xx, GO 6400, Link 400) left out; name read from the headset | GNP status query (class 12 / op 02) on usage page FF00, usage 05 or 01, at GNP address 08 (USB) or 04 (dongle) |
| **Flydigi** | Vader 5 Pro / 黑武士 5 Pro (`37D7:2401`), 2.4 GHz receiver or USB; Apex 5 (`37D7:2501`), 2.4 GHz receiver or USB | Vendor HID info query on `FFA0:0001`; 0–5 battery level mapped to 0–100% in 20% steps, with charging state; no Space Station service required |
| **GameSir** | Nova Lite, Nova 2, Nova 2 Lite on the 2.4 GHz receiver; Nova 2 Lite on USB; G7 Pro (tested: Zenless Zone Zero edition, receiver `3537:105E`) and other GameSir pads in Xbox (GIP) mode; Cyclone 2 (XInput mode, receiver or cable); Cyclone Pro on its 2.4 GHz dongle (`3537:1015`, pair the pad with Windows over Bluetooth once) | Vendor device-info query (usage page FF7A); Windows.Gaming.Input battery report (real %) in Xbox mode; Cyclone 2: vendor battery request (usage page FFF0); Cyclone Pro: GameSir app base-info request over Bluetooth LE (service `0x8650`), read every 2 min |
| **GameSir SAPJoy** | Super Nova / NovaPro (`3537:103E` receiver, tested; `3537:100E` cable, untested); Tarantula Pro (`3537:103E` / `3537:1050`, untested) | Read-only device-info query on `FFA0` with battery and charging; matching cable/receiver addresses share one reading ([protocol notes](docs/gamesir_sapjoy.md)) |
| **8BitDo** | Ultimate 2 Wireless (X-input `2DC8:310B` tested on 2.4 GHz dongle, D-input `2DC8:6012`: hold B while turning it on, firmware 1.03+, dongle / USB cable / Bluetooth), Ultimate 2C Wireless, Ultimate 3-mode, Ultimate 2.4G, Ultimate Bluetooth, Pro 3, Pro 2, SN30 Pro, SF30 Pro | Vendor HID status query (`FF7A`/`FFA0`) and SDL gamepad input report `01`/`04`, with charging state |
| **BEITONG** | KP20 / BTP-KP20 on its 2.4 GHz receiver (`20BC:5128`, XInput mode, tested) and KP40D / BTP-KP40D on its receiver (`20BC:515C`, XInput mode); BEITONG iControl not required | Vendor "get base info" query on usage page `00FF` (report `02`, nibble-scrambled payload), with charging state |
| **Samsung** | Galaxy Buds, Buds+, Buds Live, Buds Pro, Buds2, Buds2 Pro, Buds FE, Buds Core, Buds3 / Buds3 Pro / Buds3 FE (Bluetooth) | Status frame the earbuds push on Samsung's RFCOMM (SPP) service, read-only. The tray shows the lower earbud; the tooltip lists left, right and case. The Galaxy Buds app must be closed |
| **Nothing / CMF** | Nothing Ear (3a) (tested), Ear (a), Ear (2), Ear, CMF Buds (Bluetooth) | Read-only `0xC007` battery query on Nothing's NT Link RFCOMM service (`aeac4a03-dff5-498f-843a-34487cf133eb`). The tray shows the lower earbud; the tooltip lists left, right and case |
| **Akko** | Akko Air 01 (`3151:5006`, 2.4 GHz receiver, tested) and Akko V9 Dash Pro (`38EE:000C`, 2.4 GHz receiver, tested)Akko Dash V9 Ultra (`38EE:000F`, 2.4 GHz receiver, tested) | Air 01: Rongyuan `0xF7` status report; V9 Dash Pro: read-only 64-byte `0x1A` status query on `FF1C:0092` with charging state.Dash V9 Ultra: read-only 64-byte `0x1A` status query on `FF1C:0092` |
| **MOONDROP** | GM01 Pro headset on its 2.4 GHz dongle (`35D8:0133`); on its USB cable it shows as charging with the last level | WalkPlay vendor read command on report `4B` (read-only) |
| **VGN** | OMNISOUND (ZHOUTING) headset on its 2.4 GHz dongle (`372E:10BB`, tested) | V HUB "ZHOU" query: output report `55` with payload `65 01` on the control collection `000C:0001` (32-byte input, 64-byte output reports); the percentage comes back in the reply (read-only) |
| **JBL** | Quantum 650 Wireless (tested, 2.4 GHz dongle); Quantum 520, 650X, 850, 950, 950X Wireless (dongle or USB cable, same protocol, untested)Quantum 350 Wireless (tested on Windows with the `0ECB:206B` 2.4 GHz receiver); Quantum 610 Wireless (`0ECB:205C` 2.4 GHz dongle, untested on Windows); Quantum 360 Wireless (`0ECB:2115` 2.4 GHz dongle, untested) | 520/650/650X/850/950/950X: JBL "HIDV3" device-info query for the battery feature (usage page FF12), with charging state.350/610/360: HIDV1 feature reports for wireless connection and battery percentage |
| **Xbox** | Controllers on the Xbox Wireless adapter, USB or Bluetooth; headsets plugged into a controller | Windows.Gaming.Input battery report (real %), XInput fallback |
| **Switch Pro-compatible** | Controllers presenting as `057E:2009` (tested: GameSir Tarantula Pro via the 2.4 GHz receiver in Switch mode) | Five battery levels from HID report `0x30` after Steam Input or another host enables full reports |
| **Apple AirPods / Beats** | AirPods Max (tested, `200A` Lightning and `201F` USB-C), AirPods Pro 3 (tested, `2027`), AirPods Pro 1 / 2, AirPods 1–5 and Beats headphones/earbuds | BLE "proximity pairing" (`0x07`) broadcasts (single battery for AirPods Max and Beats headphones; left, right and case for earbuds, in 10% steps with charging state), matched to the paired model |
| **Phones (Phone Link)** | Any Android phone linked with Microsoft Phone Link, over Wi-Fi or Bluetooth (tested: Nothing Phone (4a) Pro) | Battery and charging state from Phone Link's Windows 11 Start menu card (`StartMenuCompanion.json`); no Bluetooth needed |
| **Darmoshark** | M3 (`248A:FF30`) and M3S (`248A:FF31`) on their 2.4 GHz receivers on WindowsM3S Pro on the Nordic 1K receiver (`1915:0723`) | M3/M3S: HID feature report for mouse identity and battery.M3S Pro: vendor HID status query on the `FF0A` collection |
| **Alienware** | AW920H headset on its 2.4 GHz dongle (`413C:A515`, tested); over Bluetooth it is covered by the Bluetooth row | Vendor query `06 C0 0A` on `FF13:0001`, reply report `07` with an XOR checksum; level, charging and critical-level fields as decoded by Alienware Command Center's AW920H plugin |
| **Niceboy** | MW400 on its 2.4 GHz receiver (`248A:FA02`, tested) | Read-only report `05` query `24 FA 48`; battery voltage mapped to 10% steps with the vendor app's table, charging flag |
| **Bluetooth** | Anything that shows a battery in *Settings → Bluetooth & devices* (earbuds, headphones, BLE mice and keyboards). Google Fast Pair earbuds (Jabra Elite 8 Active tested; Pixel Buds and many Sony / JBL / Bose models) also get left, right and case levels | Windows device property; Fast Pair battery broadcasts (BLE service data `FE2C`), matched to the paired device by Bluetooth address |
| **Generic HID** | Devices reporting the standard HID *Battery Strength* usage | HID usage page 0x06 / 0x85 |
| **HeadsetControl** | [Every headset it supports](https://github.com/Sapd/HeadsetControl#supported-headsets) (Audeze, Jabra, Sony INZONE, newer Logitech and more) | Bundled; runs `headsetcontrol -o json` |
| **MAONO PD200W** | 2.4 GHz receiver (352F:040E) | Battery percentage; hardware-tested |

**Tested on real hardware:**

These reports cover the listed connection modes and behaviors; battery confirmation does not imply every charging or power transition was tested.

- Glorious Model O Wireless
- HyperX Cloud III Wireless
- Cooler Master MM712 (dongle)
- Rapoo VT3 Max Gen 2 (receiver `24AE:1417` and USB cable `24AE:4617`; see the table for other models and their test status, and [Rapoo protocol notes](docs/rapoo.md))
- Redragon M916 Pro 1K (receiver `3554:F55D`)
- Taidu TSG808 (receiver `3554:F5D5`)
- Redragon M915RGB-WL (receiver `25A7:FA07`; other Areson models are untested, see [Areson protocol notes](docs/areson.md))
- SteelSeries Rival 650 Wireless (receiver `1038:1726` and USB cable `1038:172B`)
- HECATE G5M PRO (receiver `35BB:D3FB`)
- WLMouse YING Magnesium (8K receiver `36A7:A874`)
- ATK N9 Ultra (receiver `373B:1204`)
- Corsair Scimitar Elite SE Wireless (Slipstream receiver `1B1C:2B00`)
- DAREU EM901X (receiver `260D:1074` and USB cable `260D:1090`; battery tested on both, receiver dock/undock charging transitions tested; sleep/wake untested)
- Jabra Evolve3 75 on a Link 390 (`0B0E:2E51`)
- MCHOSE G3 V2 (receiver `3837:4245` and USB cable `3837:418C`)
- AJAZZ AK820 MAX (dongle `05AC:024F`)
- AirPods Pro 3 (Bluetooth, model `2027`)
- Sprime PM1 (receiver `1915:AC1C`)
- MOONDROP GM01 Pro (dongle `35D8:0133`)
- SteelSeries Arctis Nova Pro Wireless (base station `1038:225D`; battery reading tested, charging and power transitions untested)
- Delux M800 Pro (receiver `248A:5B2F`)
- Razer Barracuda X (2022) (receiver `1532:0550`; battery level read, charging transitions untested)
- Razer BlackShark V3 X (HyperSpeed dongle `1532:057D`)
- Fantech Helios Go XD5 (dongle `25A7:FA7C`)
- Corsair Dark Core RGB Pro SE (Slipstream receiver `1B1C:1BDC`)
- Finalmouse UltralightX (dongle `361D:0100`)
- Finalmouse Starlight X (on its dongle)
- Fantech Raigor III (dongle `1EA7:0066`; charging not reported by the firmware)
- HyperX Cloud Stinger Core Wireless (PlayStation receiver `0951:1713`; charging untested)
- HyperX Cloud Core Wireless DTS (receiver `0951:173F`; full-charge level untested)
- MSI VERSA 300 ELITE WIRELESS (dongle `0DB0:9E22`; charging and sleep handling untested)
- MSI Clutch GM31 Lightweight Wireless (receiver `0DB0:0D3C`; the GM41 uses the same driver from an owner's captures)
- HyperX Pulsefire Haste 2 Core Wireless (dongle `03F0:0AB5`; see the HyperX table row for the separately tested Haste 2 Wireless and Mini)
- AirPods Max (Bluetooth, model `200A`)
- AULA HERO 68 Air (8K Wireless Receiver `372E:106C`)
- AULA SC580 (USB cable `088D:062E` and receiver `089D:062F`, including charging and sleep)
- Ninjutso Ten Air (receiver `093A:EB01` and USB cable `093A:E020`)
- MCHOSE K7 Ultra (receiver `3837:1001`)
- MCHOSE K7 V2 Ultra+ (receiver `3837:1014` and USB cable `3837:4028`; charging shown while plugged in)
- Corsair Sabre V2 Pro Ultralight (2.4 GHz receiver `1B1C:2B2A`; battery reading verified)
- Chimera V2 (receiver `3554:F512`; battery level and charging read)
- Machenike L7 Arctic / L7 Mix (`248A:FF4C` receiver and `248A:FF4E` cable), including charging and cable/receiver duplicate suppression. Bluetooth and low-battery/full-charge boundaries were not hardware-tested.
- MCHOSE V9 Pro 2 (`3837:6011` dongle); battery level read, charging and sleep untested.
- EPOMAKER EA75 on its `05AC:024F` 2.4 GHz receiver, using the existing SONiX driver from [PR #60](https://github.com/krisgfx9/Wireless-Device-Battery-Monitor/pull/60). Battery percentage, receiver reconnection and power-on recovery were verified. Charging indication and wired battery reporting are not supported by this driver; Bluetooth battery reporting was not tested. The reported percentage can jump to 100% when USB power is attached, which is not a reliable charging indicator.
- SteelSeries Aerox 3 Wireless CS2 Dragon Lore Edition (receiver `1038:1878` and USB cable `1038:187A`), including charging, switching off (the last level stays, dimmed) and with SteelSeries GG running; GG only shows a three-step bar, which the level matched.
- RAWM Leviathan V4 (RAWM HS Receiver `1915:2346`; battery level read, charging untested).

**Hardware coverage:** Devices without recorded hardware confirmation are implemented from protocol documentation and other projects. Fantech Raigor II WG10 is still untested (it shares the tested Raigor III's `1EA7:0066` dongle and collection). If you own an untested device, please report whether it works by [opening an issue](https://github.com/krisgfx9/Wireless-Device-Battery-Monitor/issues).

## Install

[![Latest version](https://img.shields.io/github/v/release/krisgfx9/Wireless-Device-Battery-Monitor?label=latest%20version&style=for-the-badge)](https://github.com/krisgfx9/Wireless-Device-Battery-Monitor/releases/latest)

1. Download **`BatteryHub-Setup-<version>.exe`** from the [latest release](https://github.com/krisgfx9/Wireless-Device-Battery-Monitor/releases/latest).
2. Run the installer. The default per-user installation needs no administrator rights.
   **Install for all users** requires administrator permission. Windows may show a SmartScreen warning because the app is not code-signed (see below).
3. No separate runtime is required. HeadsetControl is bundled for the headsets that use it; check your device's table entry and [Limitations](#limitations) for any setup or firmware requirements.

The installer adds a Start menu entry and an uninstaller (*Settings → Apps*), and can start the app
when you sign in. Prefer no installer? Download `BatteryHub-<version>-portable.zip`, unzip it
anywhere and run `BatteryHub.exe`.

**Notes:**
- **SmartScreen warning:** the exe is not code-signed, so Windows may say "Windows protected your PC". Click *More info → Run anyway*, or build it yourself.
- **Tray-icon mode on Windows 11:** new tray icons go to the `^` overflow. Drag them onto the taskbar or enable them in *Settings → Personalization → Taskbar → Other system tray icons*.
- **Keeping the app away from a device:** if a device misbehaves while the app is running, list it in the registry string `IgnoreDevices` under `HKCU\Software\WirelessBattery` as `VID:PID` pairs (hex, separated by commas, e.g. `28BD:0947, 1234:ABCD`; `--dump` shows the ids). The app then never opens it. Drawing tablets are skipped automatically.

## Updates on Windows

Official stable Windows builds check the project's latest published stable release in the
background, 30 seconds after startup and then every 24 hours while the app is running. Open the
menu to see **Update available: vX.Y.Z...**, or choose **Check for updates...** yourself.
Update information appears only in this menu: battery icons, percentages and tooltips stay the
same, and automatic checks never show a notification or dialog. Turn off
**Automatically check for updates** in the menu to disable background checks.

For an installed copy, click the update entry and **Download and install**. Nothing is installed
without that click. The app downloads the release's `SHA256SUMS.txt` and its signature, checks the
signature against the maintainer's public key built into the app, downloads the Windows installer,
and runs it only if its SHA-256 is the one in the signed list (and the one GitHub lists for it). It
then updates the existing installation. Settings and startup preference are
preserved, and the app reopens after installation. An installation for all users can ask for
administrator permission. **Release notes** opens the official release page; **Later** keeps
your current version. Portable copies offer the release page for downloading the ZIP manually.

Checks contact GitHub's public API without an account or token. No device or battery information
is sent. Offline failures and GitHub rate limits leave battery monitoring running; a previously
found release stays in the menu until a successful check supersedes it or it is installed.
Cancelling a download waits for the current network operation to finish its finite timeout.
The installer never restarts Windows automatically.

**Why updates are safe to install:** the signing key never goes to GitHub. The maintainer signs
each release's checksum list on their own PC (see [docs/releasing.md](docs/releasing.md)), so
even someone who took over the GitHub account or its build workflow could not publish an update
the app would install. A release without a valid signature is shown in the menu but can only be
downloaded by hand. The signature does not replace Windows' own SmartScreen or UAC prompts.

Install the first release containing this feature manually once. Development/test builds disable
official update checks so local changes cannot be replaced accidentally. Updates for Linux and
automatic replacement of portable copies are deferred.

## Command line

```
BatteryHub.exe --list     # print every device and its battery level, then exit
BatteryHub.exe --json     # print a JSON array of devices and battery levels, then exit
BatteryHub.exe --dump     # every HID collection, HID devices that could not be opened, all USB devices (also ones
                               # without a HID interface) and Bluetooth devices; also saved to %TEMP%\BatteryHub-dump.txt
BatteryHub.exe --report   # open the "Request support for a device" window
BatteryHub.exe --demo     # sample devices of every brand instead of real ones (screenshots, checking colors)
BatteryHub.exe --quit     # close the running instance
```

The Linux build uses the same flags with `wireless-battery` instead of `BatteryHub.exe`, and
also accepts `--help`. `--json` prints a stable array that scripts and bar widgets can parse:

```json
[{"key":"kysona:373B:1085","name":"CX Wireless mouse","via":"2.4 GHz receiver","kind":"mouse",
  "percent":85,"level":"","detail":"","charging":false,"asleep":false,"connected":true,
  "millivolts":4029,"graceSec":1800}]
```

`graceSec` is how long the app keeps showing the last known level while the device is asleep.
Adding new fields is backwards compatible.

**Device not shown?** Right-click the widget or tray icon and choose **Request support for a device...**. Pick the device, check
what will be sent (it is shown word for word: the device name, its type, its USB/HID ids and interface layout, and your optional
name and notes) and click **Send**. It goes on the public list at [krisgfx.com/tools](https://krisgfx.com/tools/#requested) and
opens or updates a GitHub issue. **Copy full report** puts the complete `--dump` on the clipboard for the issue.
Report data is sent only when you click Send. Official Windows builds can also contact GitHub
to check for updates, as described in [Updates on Windows](#updates-on-windows); update checks
do not send device or battery information.

## Build

You need [MinGW-w64](https://www.mingw-w64.org/), e.g. from [MSYS2](https://www.msys2.org/) (`pacman -S mingw-w64-x86_64-gcc make`).

```
make                                      # development build, version 0.0.0
build.bat                                 # plain cmd with g++ and windres on PATH
make VERSION=1.2.3 CHANNEL=test            # versioned build, official updates disabled
build.bat 1.2.3 test                       # equivalent versioned cmd build
make test VERSION=1.2.3 CHANNEL=test       # device and updater regression tests
```

To build the installer and portable zip, install [Inno Setup](https://jrsoftware.org/isinfo.php),
first build with the intended version (for example `make VERSION=1.2.3 CHANNEL=test`), then run
`powershell -File installer\build-installer.ps1 -Version 1.2.3`. Packaging rejects a version that
differs from the executable. It downloads the pinned
HeadsetControl release and verifies its checksum. GitHub Actions does all of this automatically:
pushing a tag like `v1.0.0` publishes a release with the installer, the portable zip and the
HeadsetControl source (as its GPL license requires).

Windows builds also need PowerShell for generating the shared executable/resource version.
The official repository's version tags build with `CHANNEL=stable`; local builds default to
`dev`. Forks and pull requests do not enable official updates automatically.

`BatteryHub.exe` on its own also works. Without `headsetcontrol.exe` next to it (or on `PATH`) you
just lose the extra headsets.

## Linux (experimental)

A Linux build sits alongside the Windows app. It uses the same vendor drivers with a hidraw-based
HID backend and a GTK4 StatusNotifierItem tray icon; the Windows code path is unchanged.
All Linux-only files are in `linux/` and `src/linux/`, and `build-linux.sh` builds it (Windows keeps using `build.bat`).

| | Fedora | Ubuntu / Debian |
|---|---|---|
| Compiler & make | `sudo dnf install gcc-c++ make` | `sudo apt install g++ make` |
| GTK4 + Cairo | `sudo dnf install gtk4-devel cairo-devel` | `sudo apt install libgtk-4-dev libcairo2-dev` |

No extra HID library is needed (hidraw is used directly).

```sh
./build-linux.sh
./build-linux.sh test         # unit test for the HID report-descriptor parser
./wireless-battery --list     # print detected levels and exit
./wireless-battery --dump     # list HID collections
./wireless-battery --quit     # close the running tray instance
```

HID access needs a udev rule, otherwise the app starts but finds no devices:

```sh
sudo cp linux/99-wireless-battery.rules /etc/udev/rules.d/
sudo udevadm control --reload-rules && sudo udevadm trigger
# log out and back in
```

The tray icon works natively on KDE Plasma; GNOME needs an AppIndicator host such as
`gnome-shell-extension-appindicator`. The optional launcher is `linux/wireless-battery.desktop`
(install it plus `linux/wireless-battery.svg` and the binary into `~/.local/`).

Phase 1 covers Logitech, Razer, SteelSeries, Corsair, HyperX, PlayStation, Cooler Master, Glorious,
Finalmouse and the shared Kysona/Pulsar/ATK/G-Wolves protocols. Bluetooth/UPower fallbacks, HeadsetControl and
the remaining vendors are planned follow-up phases.

## Limitations

- **Crowded taskbars:** with a very full centered Windows 11 taskbar, the app buttons can reach the widget. On Windows 10 the task-button area is narrowed automatically.
- **Phones:** read from a file Phone Link writes for the Start menu companion card, which is not a documented API and may change with Phone Link updates. The phone shows while Phone Link reports it as connected; a card older than 3 hours is shown dimmed. The card also says when the phone is charging, which shows as the charging bolt.
- **Sleeping devices:** a device that is asleep may not answer. Its last value stays visible, dimmed unless *Dim sleeping devices* is turned off in the menu. Logitech receivers drop sleeping devices from the link, so their last value is kept for 30 minutes.
- **HECATE G2 Wireless 7.1 headset** (2.4 GHz dongle `35BB:A009` / `A209`): no battery query for its dongle is documented yet, so it is not read. A USB capture while the HECATE software shows the headset battery (see CONTRIBUTING.md) is the way to add it.
- **Keychron keyboards:** with stock firmware they only report their battery over Bluetooth (shown via the Bluetooth support). Over the 2.4 GHz receiver or the cable they need firmware with the battery patch ([docs/keychron_keyboard_firmware/README.md](docs/keychron_keyboard_firmware/README.md)); updating the keyboard from Keychron Launcher removes it. Keychron mice are supported.
- **Baseus AeQur GH02 headset:** the 2.4 GHz dongle (`10D6:4802`, Actions chip) only carries audio, media keys and the chip's firmware-update channel, not the battery. Connect the headset over Bluetooth to see its level (shown via the Bluetooth support when Windows reports one).
- **Weikav Lucky65 v1 keyboard:** the firmware does not report its battery over the 2.4 GHz dongle (`0603:0351`, Novatek chip). The keyboard has no battery-check shortcut, and the official configurator only connects over the USB cable, not through the dongle, so there is no battery reading to show.
- **Rapoo:** supported VT mice push their status, so a refresh can wait up to 4 seconds per matching interface. Sleeping mice may stay dimmed with their last reading for up to 30 minutes. Support is for Nordic 54L report `07` and legacy `BB` (VT3 Pro, VT1 Pro Max); CH584 report `08`, office MT/M-series mice and other firmware protocols are not covered by this driver.
- **GameSir Cyclone Pro:** the dongle carries no battery level, so it is read from the pad over Bluetooth LE. Pair the pad with Windows once (Settings > Bluetooth & devices > Add device > Bluetooth > `GameSir-Cyclone Pro`), and keep playing through the dongle. The PC needs Bluetooth. The level refreshes every 2 minutes, and there is no percentage while charging. Without pairing, the dongle shows as an Xbox controller at "Full". Details in [docs/gamesir_cyclone_pro.md](docs/gamesir_cyclone_pro.md).
- **RAWM:** the mouse is asked through its receiver, so a sleeping mouse does not answer; it stays dimmed with its last reading for up to 30 minutes and adds about a second to a refresh while it sleeps. Only the Leviathan V4 on the RAWM HS Receiver (`1915:2346`) is tested; the other models are taken from RAWM HUB's device table. The Leviathan V4 GT and NYX60 (VID `373E`, RAWM HUB 3.0) and the RAWM HS keyboards use other protocols and are not covered.
- **Flydigi:** this driver targets Vader 5 Pro and Apex 5; Bluetooth and other Flydigi models (for example Apex 6) are not covered. Percentages represent coarse battery levels. Apex 5 was tested on real hardware over the 2.4 GHz receiver and a USB cable; Vader 5 Pro follows SDL and Windows hardware traces.
- **Not supported yet:** MSI devices outside the models listed in the table, Razer Kraken headsets, Barracuda models other than the Barracuda X (2022) (`1532:0550` / `0552`) and Barracuda Pro (`1532:053A`), HyperX Pulsefire mice other than the Haste 2 Wireless / Haste 2 Core Wireless / Haste 2 Mini, and the Xbox Wireless Headset on the Xbox adapter are not covered by the current drivers. The Xbox Wireless Headset works over Bluetooth. A USB capture from an owner (see CONTRIBUTING.md) can help add support.
- **Other devices:** some 2.4 GHz devices use undocumented protocols and are not supported yet. See [CONTRIBUTING.md](CONTRIBUTING.md) for how to help add one.

## How it works

Each vendor driver in [`src/drivers/`](src/drivers) recognises its devices by USB vendor and product ID, and

## 关联链接

- https://discord.gg/ZgDDUPP8ye
- https://github.com/Sapd/HeadsetControl
- https://github.com/Sapd/HeadsetControl#supported-headsets
- https://github.com/krisgfx9/Wireless-Device-Battery-Monitor/issues
- https://github.com/krisgfx9/Wireless-Device-Battery-Monitor/issues/new
- https://github.com/krisgfx9/Wireless-Device-Battery-Monitor/pull/129
- https://github.com/krisgfx9/Wireless-Device-Battery-Monitor/pull/60
- https://github.com/krisgfx9/Wireless-Device-Battery-Monitor/releases/latest
- https://github.com/sponsors/krisgfx9
- https://img.shields.io/badge/Discord-Join%20us-5865F2?logo=discord&logoColor=white
- https://img.shields.io/badge/GitHub-Sponsor-EA4AAA?logo=githubsponsors&logoColor=white
- https://img.shields.io/badge/Help-translate-6F42C1?logo=googletranslate&logoColor=white
- https://img.shields.io/badge/Ko--fi-Support%20me-FF5E5B?logo=ko-fi&logoColor=white
- https://img.shields.io/badge/PayPal-Donate-00457C?logo=paypal&logoColor=white
- https://img.shields.io/badge/Reddit-Share-FF4500?logo=reddit&logoColor=white
- https://img.shields.io/badge/Report-a%20device-2EA44F?logo=github&logoColor=white
- https://img.shields.io/github/stars/krisgfx9/Wireless-Device-Battery-Monitor?style=flat&logo=github&label=Star
- https://img.shields.io/github/v/release/krisgfx9/Wireless-Device-Battery-Monitor?label=latest%20version&style=for-the-badge
- https://jrsoftware.org/isinfo.php
- https://ko-fi.com/krisgfx
- https://krisgfx.com/tools/#requested
- https://www.mingw-w64.org/
- https://www.msys2.org/
- https://www.paypal.com/paypalme/krisgfx
- https://www.reddit.com/submit?url=https%3A%2F%2Fgithub.com%2Fkrisgfx9%2FWireless-Device-Battery-Monitor&title=Wireless%20Battery%3A%20battery%20levels%20of%20your%20wireless%20devices%20on%20the%20Windows%20taskbar

## 导航

- 项目页：[[10-项目/github.com_0b86eba1]]
- 渠道页：[[50-渠道/github_new]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
