---
type: "corpus"
item_id: "3c605dc3a7e498e2"
title: "Show HN: DissPair APK– Portable BLE and Bluetooth Classic Security Testing"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50294206"
project_url: "https://github.com/threadpoolx/DissPair"
author: "threadpoolx"
published_at: "2026-10-29T19:03:46Z"
captured_at: "2026-10-30T09:46:09+08:00"
lang: "en"
kind: "post"
topic: "内容/媒体"
shard: "2026-10-30"
pub_day: "2026-10-29"
tags:
  - 语料
  - hn_show
  - author_threadpoolx
  - story_50294206
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: DissPair APK– Portable BLE and Bluetooth Classic Security Testing

> [!info] 一句话导读
> GitHub - threadpoolx/DissPair: A native Android application built with Kotlin & Jetpack Compose for security testing Bluetooth Classic and BLE in authorized lab…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50294206>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：threadpoolx　|　发布：2026-10-29T19:03:46Z
> 项目链接：<https://github.com/threadpoolx/DissPair>
> 采集：2026-10-30T09:46:09+08:00　|　id：`3c605dc3a7e498e2`

## 正文

GitHub - threadpoolx/DissPair: A native Android application built with Kotlin & Jetpack Compose for security testing Bluetooth Classic and BLE in authorized lab environments. · GitHub

## About

A native Android application built with Kotlin & Jetpack Compose for security testing Bluetooth Classic and BLE in authorized lab environments.

## Folders and files

| Name | Name | Last commit message | Last commit date |
| --- | --- | --- | --- |
| app | app | Auto-request max MTU; single "Write test" setting; drop prepare-only | Oct 13, 2026 |
| fastlane/ metadata/ android/ en-US | fastlane/ metadata/ android/ en-US | F-Droid listing: expanded description and summary | Oct 13, 2026 |
| gradle | gradle | Apply Kotlin Android plugin so app code compiles (fixes crash on launch) | Jun 16, 2026 |
| .gitignore | .gitignore | Ignore APK build artifacts | Jun 20, 2026 |
| LICENSE | LICENSE | Initial commit | Mar 7, 2026 |
| README.md | README.md | Auto-request max MTU; single "Write test" setting; drop prepare-only | Oct 13, 2026 |
| Security.md | Security.md | Create Security.md | Apr 10, 2026 |
| build.gradle.kts | build.gradle.kts | Release 2.1.2 | Jun 16, 2026 |
| disspair.py | disspair.py | Add files via upload | Apr 12, 2026 |
| disspair_logo.png | disspair_logo.png | Rename disspair_logo_192.png to disspair_logo.png | Mar 8, 2026 |
| disspair_logo_2.png | disspair_logo_2.png | Add files via upload | Sep 7, 2026 |
| gradle.properties | gradle.properties | Downgrade to Gradle 8.14 / AGP 8.7.3 for F-Droid reproducible builds | Jun 11, 2026 |
| gradlew | gradlew | Complete rewrite to Native Kotlin Android and added GitHub Safety Com… | Apr 12, 2026 |
| gradlew.bat | gradlew.bat | Complete rewrite to Native Kotlin Android and added GitHub Safety Com… | Apr 12, 2026 |
| settings.gradle.kts | settings.gradle.kts | Update MainActivity, remove foojay, and clean binaries for F-Droid | Jun 11, 2026 |
| View all files | | | |

### Bluetooth Security Toolkit

A multi-platform educational toolkit for understanding Bluetooth Classic (RFCOMM) and BLE (GATT) protocol behavior in controlled, authorized lab environments.

> ⚠️
>
> Authorized Use Only This toolkit is intended strictly for use on devices you personally own or have explicit written permission to test. Unauthorized use against third-party devices may violate local and international law. The authors assume no liability for misuse.
>
> ⚠️
>
> Potentially Harmful Capabilities & Risk Disclosure
>
> This tool contains features that can cause operational disruption to target hardware if used improperly:
>
> 1. RFCOMM Hardware Flooding: The "Flood" module intentionally injects dense byte streams into targeted Bluetooth channels. On vulnerable, legacy, or unpatched Bluetooth stacks, this can cause buffer overflows, resulting in the target device freezing, kernel panics, or complete Denial of Service (DoS).
> 2. Payload Injection & State Manipulation: The ability to inject raw AT commands (e.g., HFP handshake manipulation) and OBEX payloads can alter the operational state of target devices, potentially causing unauthorized call manipulation or disrupting audio gateways.
> 3. GATT Interaction: Unauthenticated reading/writing of BLE characteristics may expose sensitive plaintext data or alter IoT device configurations.
>
> Use exclusively on hardware you own or have explicit consent to audit.

## What is DissPair?

DissPair is a Bluetooth security learning toolkit designed for students, hardware developers, and security researchers to explore low-level behavior of:

- Bluetooth Classic (RFCOMM)
- Bluetooth Low Energy (BLE GATT)

Unlike many tools that rely purely on Service Discovery Protocol (SDP), DissPair actively probes and interacts with devices to reveal real behavior vs advertised behavior.

It is designed for use in personal lab environments — testing your own devices, understanding protocol fundamentals, and learning how Bluetooth service discovery and channel communication works under the hood.

### CVEs Discovered using DissPair

| CVE Number | Vulnerability Description | Link |
| --- | --- | --- |
| CVE-2026-31280 | An issue in the Bluetooth RFCOMM service of Parani M10 Motorcycle Intercom v2.1.3 allows unauthorized attackers to cause a Denial of Service (DoS) via supplying crafted RFCOMM frames. | View Details |
| CVE-2025-67133 | An issue in Hero Motocorp Vida V1 Pro 2.0.7 allows a local attacker to cause a denial of service via the BLE component | View Details |

## Platform Variants

| | Platform | Description |
| --- | --- | --- |
| 📱 | Android | Native Kotlin app with Jetpack Compose UI for on-device Bluetooth analysis. Field learning — explore Bluetooth environments from a mobile device. |
| 🐧 | Linux CLI | Python-based tool using BlueZ and raw Bluetooth sockets. Desktop study — terminal-based protocol analysis with minimal dependencies. |

## Core Workflow

```
Scan   →  Discover nearby Bluetooth devices (Classic BR/EDR and BLE)
  ↓
Sweep  →  Probe RFCOMM channels (1–30) on your own device
  ↓
Map    →  Identify active vs advertised services
  ↓
Analyze → Interact with protocols (RFCOMM / GATT) to study behavior

```

## Who Is This For?

- Students learning Bluetooth protocol internals on their own hardware
- Hardware hobbyists auditing and validating their own devices
- Security researchers studying RFCOMM/GATT behavior in lab setups
- Developers building Bluetooth-enabled hardware who want to validate their own implementations

## Overview

DissPair APK is a native Android application written in Kotlin with a Jetpack Compose UI. It uses Android's native Bluetooth APIs directly — including `BluetoothAdapter`, `BluetoothGatt`, and reflection-based `createRfcommSocket` / `createInsecureRfcommSocket` calls — to interact with the device's Bluetooth stack without relying on higher-level abstractions.

## Repository Structure

```
Disspair/
├── app/
│   └── src/
│       └── main/
│           ├── java/org/disspair/disspair/
│           │   └── MainActivity.kt        # Core app logic, UI, Bluetooth analysis
│           └── res/
│               └── drawable/
│                   └── disspair_logo.png  # App icon
├── build.gradle
└── README.md

```

## Requirements

- Android 6.0 (API 23) or higher
- Android 12+ (API 31) requires `BLUETOOTH_SCAN` and `BLUETOOTH_CONNECT` permissions
- Location services must be enabled for Bluetooth scanning
- For Classic device analysis: Location + Nearby Devices permissions

### Direct Install (Pre-Built APK)

1. Download `disspair.apk` from the Releases tab
2. On your Android device, allow your browser or file manager to Install unknown apps
3. Open the app and grant the requested Location and Nearby Devices permissions

> These permissions are required for Bluetooth scanning on Android 12+

#### 1. Clone the Repository

```
git clone https://github.com/threadpoolx/DissPair.git
cd DissPair
git checkout APK
```

#### 2. Open in Android Studio

- Open Android Studio (Hedgehog or newer recommended)
- Select Open and navigate to the cloned directory
- Let Gradle sync complete

#### 3. Build & Run

```
# Via Android Studio: Build > Build Bundle(s) / APK(s) > Build APK(s)

# Or via command line:
./gradlew assembleDebug
```

The compiled APK will appear in `app/build/outputs/apk/debug/`.

> Ensure you have Android SDK, Android NDK, and JDK 17 installed and configured in Android Studio.

## How It Works

```
sequenceDiagram
    autonumber
    participant D as DissPair v2 (Android)
    participant B as Android BT Stack
    participant T as Target Device

    Note over D, T: 1. Setup & Device Discovery
    D->>B: checkPermissions() and startDiscovery()
    B-->>D: onDeviceFound(Name, MAC, Type)
    D->>D: UI Update - Categorize Classic vs BLE

    Note over D, T: 2. Classic RFCOMM & Payload Mapping
    D->>T: createRfcommSocket(ch 1-30)
    T-->>D: Socket Verified Open

    Note over D, T: Classic Attack Engine
    alt Method - Flood
        D->>T: write payload in High-Speed Loop
        T-->>D: IOException (Buffer Overflow / DoS)
    else Method - Payload Injection
        Note right of D: Feature - TTY (AT Cmds), PBAP, or Custom
        D->>T: Send specific Protocol Payload
        T-->>D: Stream Response / Data Leak
    end

    Note over D, T: 3. BLE GATT & Profile Interaction
    D->>T: connectGatt() and discoverServices()
    T-->>D: onServicesDiscovered(List of GattService)

    Note over D, T: BLE Attack Engine
    alt General Profile Access
        D->>T: readCharacteristic(Generic_UUID)
        T-->>D: onCharacteristicRead (DeviceInfo/Battery)
    else Customized Profile Manipulation
        Note right of D: Targeted Write/Fuzzing
        D->>T: writeCharacteristic(Custom_UUID, malformed_data)
        T-->>D: onCharacteristicWrite status
    end

    Note over D: closeAll() - Release Hardware Resources

```

### Device Discovery

| Button | Description |
| --- | --- |
| SCAN CLASSIC | Discovers nearby BR/EDR devices using Android's `startDiscovery` API. Loops up to 5 scan cycles to maximize coverage. |
| SCAN BLE | Passively listens for BLE advertisement packets via `BluetoothLeScanner`. |

Paired devices are loaded automatically from the local Bluetooth bond cache on startup and shown via the Paired toggle.

### Classic Analysis (RFCOMM)

Tap ANALYSE on any Classic or Paired device to open the RFCOMM Channel Analysis.

#### Channel Enumeration

Probes channels 1–15 by default (expandable to 16–30 via the `PROBE 16-30` button) using direct RFCOMM connection attempts. Reports which channels are live and whether they accept unpaired (insecure) or paired (secure) connections.

#### Per-Channel Actions

| Action | Description |
| --- | --- |
| PAYLOADS | Opens the payload dialog to send a predefined or custom payload to the channel |
| FLOOD | Transmits a continuous 2048-byte burst stream to stress-test the target's RFCOMM buffer handling |

#### Payload Dialog

- AT Command: Connect — Sends `ATZ\r\n` (Hayes modem reset/ping)
- PBAP/MAP: OBEX Connect — Sends a raw OBEX `0x80` Connect PDU
- Custom Payload — Enter any AT command; `\r\n` is auto-appended
- Includes automatic HFP handshake detection and bypass — if the target opens with an `AT+BRSF` prompt, the tool auto-negotiates with `AT+BRSF=0` before injecting the chosen payload

### GATT Analysis (BLE)

Tap ANALYSE on any BLE device to open the GATT Analysis.

- Establishes a GATT connection (LE transport) and enumerates all services and characteristics
- Displays service type (General for standard 16-bit Bluetooth UUIDs, Customized for vendor UUIDs) and full property flags (`R W WnR N I SW B EXT`)
- All GATT operations go through a serialised queue with timeouts, so rapid actions are never silently dropped by the Android stack
- ATT error codes are decoded by name (e.g. `INSUFFICIENT_AUTHENTICATION`, `INSUFFICIENT_ENCRYPTION`) instead of raw numbers
- Per-characteristic actions:

| Action | Description |
| --- | --- |
| READ | Reads the current value of the characteristic |
| WRITE | ASCII or raw Hex payload; write-with-response or write-without-response (also shown for write-without-response-only characteristics) |
| SUB / UNSUB | Enables notifications or indications via the CCCD and logs every incoming value with its UUID |

- The connection automatically requests the largest ATT MTU (517); the negotiated value is shown in the header, and payload limits follow it.
- Toolbar actions:

| Action | Description |
| --- | --- |
| AUDIT | Unauthenticated access audit (see below) |
| COPY / SHARE | Exports the last audit report as text |

#### GATT Access Audit

Tests what every characteristic allows without pairing and marks each one `OPEN`, `AUTH`, `ENC`, `AUTHZ`, `KEY`, `DENY` or `ERR` for read, subscribe and (optionally) write. Characteristics usable unpaired are flagged in red and summarised in an exportable report.

- Read and subscribe tests are non-destructive; subscriptions are disabled again after the test.
- Write test is one setting: Off (default), Echo only (rewrites the value just read on readable characteristics; write-only ones are skipped), or Echo + commit payload (write-only ones really get the hex payload you choose).
- Run it on an unbonded device. If Android shows a pairing prompt mid-audit, decline it; the report flags any bond-state change.
- Toggle HEX / ASCII display for all captured values

### Advertisement Inspector (GAP)

Tap ADV on any BLE device to inspect what it broadcasts, without connecting. It updates live while SCAN BLE runs.

- Every AD structure decoded: flags, UUID lists (with names), local name, TX power, appearance, service data, manufacturer data, Mesh, URI, connection interval range, and more. Malformed length fields are flagged.
- Vendor formats: Apple Continuity messages (iBeacon, AirDrop, Proximity Pairing, Handoff, Nearby Info/Action, Find My, ...), Eddystone UID/URL/TLM/EID, Google Fast Pair, Microsoft beacons, company-ID lookup.
- Privacy: address type (public / random static / resolvable private / non-resolvable; exact on Android 14+, best-guess earlier), stale private addresses, identifiers embedded in names, tracker beacons (Find My, SmartTag, Tile).
- Over time: estimated advertising interval, RSSI graph, number of distinct payloads (live state changes), legacy vs extended PDU, connectable flag, primary/secondary PHY, advertising SID.
- Risk flags: exposed DFU or Nordic UART services.
- COPY / SHARE a full text report; ANALYSE GATT jumps to the GATT screen.

BLE scanning now uses low-latency mode (and extended advertising where supported), so it uses more battery while a scan is running.

### Appearance

- Theme: follows the system light/dark setting by default. Tap the theme icon in the top bar to cycle System → Light → Dark; the choice is remembered. In light mode the neon log colours switch to darker shades that stay readable on white.
- Icon: launcher, adaptive (circle/squircle-safe) and in-app icons are generated from `disspair_logo_2.png`.

### System Log

A live scrolling terminal log at the top of the main screen and within each overlay shows all events, discovered targets, errors, and decoded responses in color-coded monospace output.

## Overview

A Python-based command-line tool using:

- Native Linux Bluetooth sockets (`AF_BLUETOOTH`)
- BlueZ stack

Allows low-level protocol interaction without abstractions.

## Supported Platforms

- Kali Linux (recommended)
- Ubuntu / Debian

> VM users must use a USB Bluetooth adapter

## Features & Workflow

```
flowchart TB
    Start["START: Init & Dep Check"] --> ScanClassic["Scan Classic\nhcitool/bluez"] & ScanBLE["Scan BLE\nBleak Scanner"] & PairedDevices["Paired Devices\nLocal BlueZ"] & ManualMAC["Manual MAC"]
    ScanClassic --> TargetLocked["Target Locked"]
    ScanBLE --> TargetLocked
    PairedDevices --> TargetLocked
    ManualMAC --> TargetLocked
    TargetLocked --> ClassicEnum["Classic Enumeration\nBrute-force RFCOMM 1-30"] & BLEEnum["BLE GATT Enumeration\nPull Services & Chars"]
    ClassicEnum --> ClassicAttacks["RFCOMM Attacks\n- Silent Connection\n- Kali TTY Modem Noise\n- Resource Flood DoS\n- Customized Payload"]
    BLEEnum --> BLEAttacks["GATT Interaction\n- Read Hex/ASCII\n- Write Text String\n- Write Raw Hex"]

```

### System Dependencies

```
sudo apt update
sudo apt install -y bluez rfkill
```

### Python Setup

```
python3 -m venv disspair_env
source disspair_env/bin/activate
pip install bleak
```

## Usage

```
source disspair_env/bin/activate
sudo $(which python3) disspair_kali.py
```

### Step 1 — Discovery

- Scan Classic devices
- Scan BLE devices
- Load paired devices
- Manual MAC input

### Step 2 — Enumeration

- RFCOMM channel probing (1–30)
- BLE GATT enumeration

#### RFCOMM

- Connect to channel
- Send AT commands
- Flood testing

#### BLE

- Read characteristics
- Write characteristics

## Troubleshooting

```
sudo rfkill unblock bluetooth
sudo systemctl restart bluetooth
sudo hciconfig hci0 up
hciconfig -a
```

## Security & Abuse Reporting

If you need to report a security vulnerability, malicious activity, or third-party abuse related to this tool, please see the Security Policy for contact details and responsible disclosure guidelines.

## Legal & Ethical Use

Only use DissPair against:

- Devices you personally own
- Devices where you have explicit written authorization from the owner

Never use this tool against:

- Public devices
- Vehicles or infrastructure
- Third-party hardware without consent

# utkarsh261/pho

## 关联链接

- https://github.com/threadpoolx/DissPair.git

## 导航

- 项目页：[[10-项目/github.com_d748d857]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`内容/媒体`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
