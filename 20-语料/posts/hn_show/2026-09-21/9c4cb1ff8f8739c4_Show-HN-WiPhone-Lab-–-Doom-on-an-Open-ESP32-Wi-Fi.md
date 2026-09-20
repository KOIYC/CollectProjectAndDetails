---
type: "corpus"
item_id: "9c4cb1ff8f8739c4"
title: "Show HN: WiPhone Lab – Doom on an Open ESP32 Wi-Fi Phone"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49114317"
project_url: "https://github.com/mulfyx/wiphone-lab"
author: "sqshi"
published_at: "2026-07-30T19:10:48Z"
captured_at: "2026-09-21T03:11:13+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-07-30"
tags:
  - 语料
  - hn_show
  - author_sqshi
  - story_49114317
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:83d"
---

# Show HN: WiPhone Lab – Doom on an Open ESP32 Wi-Fi Phone

> [!info] 一句话导读
> Unofficial WiPhone 0.8.30 firmware fork: reproducible system benchmark, UART test harness, and optional Doom and Gravity Defied ports.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49114317>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：sqshi　|　发布：2026-07-30T19:10:48Z
> 项目链接：<https://github.com/mulfyx/wiphone-lab>
> 采集：2026-09-21T03:11:13+08:00　|　id：`9c4cb1ff8f8739c4`

## 正文

# mulfyx/wiphone-lab

Unofficial WiPhone 0.8.30 firmware fork: reproducible system benchmark, UART test harness, and optional Doom and Gravity Defied ports.

- Stars: 3
- Forks: 0
- Watchers: 3
- Open issues: 0
- Default branch: main
- Created: 2026-07-26T00:28:36Z

## Languages

- C
- C++
- Linker Script
- Makefile
- Processing
- Python
- Shell

## Topics

- arduino-esp32
- benchmark
- dma
- doom
- esp32
- firmware
- gravity-defied
- st7789
- voip-phone
- wiphone

## Top Contributors

- mulfyx (17 contributions)

---

## README

# WiPhone Lab

An unofficial fork of the **WiPhone** open-source phone firmware (v0.8.30) that
keeps the full phone working and adds a reproducible **System Benchmark**, an
on-device **test harness**, and optional **Doom** and **Gravity Defied** ports.

Not affiliated with or endorsed by MZJ Technology / HackEDA. The very first
commit, *"WiPhone 0.8.30 original firmware"*, is their pristine upstream
release; every commit after it is this fork's work.

> **How this was built.** Most of this fork was written by AI agents — the game
> ports, the shared display pipeline, the benchmark and the harness itself.
>
> The work was hardware-in-the-loop rather than code review on faith: the
> agents built firmware, flashed it to the phone, drove it over UART through
> the `@WP1` harness, and read back telemetry and frame CRCs from the running
> device. Most of the numbers in this README were measured that way, and more
> than one conclusion came from watching the panel disagree with what the
> firmware believed it had drawn — see *Display clock* below for the worst of
> them.

---

## What is WiPhone?

WiPhone is an open-source, hackable mobile phone built
around an **ESP32**. It places calls over Wi‑Fi using **SIP/VoIP**, and the
firmware is a single Arduino sketch (`WiPhone.ino`).

Target hardware / toolchain:

| | |
|---|---|
| SoC | ESP32‑D0WDQ6‑V3, dual‑core Xtensa LX6 @ 240 MHz |
| RAM | 520 KiB internal SRAM + 4 MiB PSRAM (mapped, 40 MHz) |
| Display | ST7789 240×320 over VSPI, driven by `TFT_eSPI` |
| Audio | WM8750 codec over I²S |
| Radios | Wi‑Fi (SIP/VoIP), optional LoRa messaging |
| Build | Arduino‑ESP32 **1.0.5** (pinned), ESP‑IDF 3.3.4 |

Stock firmware features (telephony, SIP, address book, messaging, settings,
etc.) are unchanged and documented in `CHANGELOG.txt`.

---

## What this fork adds

Everything below sits **on top of** the stock 0.8.30 firmware; telephony is left
fully intact. The additions are reachable from the phone's menus.

### Gravity Defied — `src/gravity_defied/`
A port of the classic J2ME motorcycle physics game.
- Deterministic fixed‑point (Q16.16) physics, level loader and renderer.
- Runs at **~22 FPS** (a fixed 45 ms frame period) using the shared raw‑VSPI
 async DMA display pipeline.
- Includes an in‑app deterministic benchmark.

A ride with the in-game FPS/LCD overlay enabled, on the device:

https://github.com/user-attachments/assets/15109be5-7dc8-4c8a-bdc0-1c27c0ace83c

### Doom — `src/doom/` (engine in `src/doom/engine/`)
A playable Doom port based on **FPDoom**.
- Full‑screen **320×240** landscape output via the async DMA pipeline
 (**~13.6 FPS** at full quality with sound — see *Performance notes*).
- **Sound:** a real SFX mixer plus **OPL2 music** (DOSBox `dbopl` emulator with
 GENMIDI instruments, MUS→MIDI conversion). SFX and music are mixed and played
 through the shared WM8750 codec/I²S using a snapshot/restore audio **lease**
 that restores the exact telephony audio state on exit.
- The Doom zone and most engine buffers live in PSRAM to fit alongside the phone
 firmware without running the internal heap out of memory.

Gameplay recorded off the device, with sound for the OPL music:

https://github.com/user-attachments/assets/53a7155e-2d7a-4339-8cc7-e69895d973ab

### Shared display pipeline — `src/display/FullScreenDmaTransfer.*`
A raw‑VSPI worker (core 0) that converts indexed frames to RGB565 and streams
them in ping‑pong DMA chunks, overlapping the game's next‑frame render. Used by
both Gravity Defied and Doom; it leases the VSPI bus from `TFT_eSPI` and returns
it cleanly on exit.

### System Benchmark — `src/system_benchmark/`, `tools/system_benchmark/`
A production diagnostics app that takes a **reproducible** performance and
correctness snapshot of the whole environment (CPU on both cores; integer,
fixed‑point, `float` and `double` kernels; internal RAM and PSRAM; audio codecs;
renderer; completed display transfers; flash reads). Deterministic workloads are
guarded by frozen CRC32 values and scored against an explicitly saved baseline,
so an optimization can be told apart from a regression or a broken computation.

### Test harness & reproducible builds
- **On‑device harness** (`TestHarness.cpp/.h`, compiled only in harness builds):
 a line‑based `@WP1` UART protocol for automated testing, driven by the Python
 host client `tools/harness/wiphone_harness.py`.
- **Reproducible builds** (`tools/system_benchmark/build.py`): produces
 `regular`/`harness` firmware with a content‑addressed **Build ID**
 (`B1-<sha256[:16]>`) and a full manifest, for provenance and stack‑trace‑able
 releases.

---

## Repository layout

```
WiPhone.ino, *.cpp, *.h       Stock WiPhone firmware (GUI, SIP, audio, storage…)
src/gravity_defied/           Gravity Defied game + in-app benchmark
src/doom/                     Doom port; src/doom/engine/ is the FPDoom engine
src/display/                  Shared raw-VSPI async DMA display pipeline
src/system_benchmark/         System Benchmark app (kernels, engine, storage, UI)
src/audio/, src/drivers/,     Codecs (G.711/G.722), device drivers,
src/TFT_eSPI/, src/…          vendored/adapted libraries
tools/                        Host-side tooling: build, harness, asset generation,
                              screenshots, icon/font converters
TestHarness.cpp/.h            Harness-only UART automation (@WP1 protocol)
CHANGELOG.txt                 Upstream WiPhone changelog
```

---

## Building, flashing & installing

### Prerequisites

- **Arduino‑ESP32 `1.0.5`** core (pinned) — newer cores are *not* compatible.
- **arduino‑cli `1.5.1`** (used by the build script) or the Arduino IDE.
- Board: **ESP32 Wrover Module** (`esp32wrover`) — PSRAM must be enabled.
- Library: **RadioHead** (`1.120`, LoRa in `lora.cpp`). `TFT_eSPI` is vendored
 in `src/TFT_eSPI/`; other libraries come with the ESP32 core.
- For flashing: `esptool.py` (`3.0.0` used here) and a USB‑UART link to the
 phone (CP2104), e.g. `/dev/ttyUSB0`.

Board / compiler identity (FQBN):

```
esp32:esp32:esp32wrover:FlashFreq=80,FlashMode=dio,PartitionScheme=default,DebugLevel=none
```

The project also compiles with `-fsigned-char -fno-common -fwrapv
-fno-strict-overflow`, and **Doom** additionally requires the PSRAM linker
script `src/doom/wiphone_doom_psram.ld` (via `-Wl,--wrap=esp_spiram_add_to_heapalloc`)
plus `-DWIPHONE_DOOM_EMBEDDED_SFX`. These are wired automatically by the build
script below.

### Option A — reproducible build (recommended)

`tools/system_benchmark/build.py` applies the Doom PSRAM linker script, pins the
toolchain, and emits a content‑addressed **Build ID** and a full manifest
(`.elf`/`.map` for later stack traces):

Phone firmware only, without the game ports:

```sh
python3 tools/system_benchmark/build.py --output <artifact-dir> --flavor regular
#   --flavor harness   also build the @WP1 UART test firmware
#   --flavor both      build regular + harness
#   --no-distrobox     run the host arduino-cli directly
#                      (default runs it inside a distrobox container "wi-phone")
```

With Doom and Gravity Defied, and with Doom's sound:

```sh
python3 tools/system_benchmark/build.py --output <artifact-dir> --flavor regular \
    --games --doom-sfx-wad /path/to/doom-with-audio.wad
```

> **`--games` is required for the game ports.** They are an optional proof of
> concept guarded by `BUILD_GAMES`, so a default build contains none of their
> code — about 1.2 MiB smaller, 59% of the app partition against 98%.
>
> **`--doom-sfx-wad` is what gives Doom sound**, and only works together with
> `--games`. It generates the embedded SFX and OPL music tables from a WAD that
> still contains its audio lumps. Without it `WIPHONE_DOOM_EMBEDDED_SFX` stays
> undefined, the sound table is empty, and the mixer task never starts — Doom
> then runs completely silent, with no error. It also costs about 780 KiB of
> flash, so a sound build sits near the app size limit (see *Doom IWAD* below).

Result: ` /regular/WiPhone.ino.bin` (+ `.elf`, `.map`,
`build-manifest.json`) and a Build ID like `B1-EA6254DAB017912D`.

### Option B — Arduino IDE

Open `WiPhone.ino`, select **ESP32 Wrover Module**, set Flash 80 MHz / DIO,
default partition scheme, PSRAM **enabled**, then Verify/Upload. This builds the
phone firmware alone. The game ports need `BUILD_GAMES` (uncomment it in
`config.h`), and a correct **Doom** build additionally needs the custom
linker/flags above — so use Option A when you want the games.

### Flashing (only `app0`, no full erase)

Write the app image to `app0 @ 0x10000`. The bootloader, partition table, NVS
and other partitions are left untouched:

```sh
esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 921600 \
  --before default_reset --after hard_reset write_flash -z \
  --flash_mode dio --flash_freq 80m --flash_size 16MB \
  0x10000 <artifact-dir>/regular/WiPhone.ino.bin
```

The app image always ends before `0x300000`, so flashing the firmware never
touches the Doom IWAD region below. That bound is enforced at build time:
`build.py` passes `upload.maximum_size` = `0x300000 - 0x10000`, so an app that
would reach the WAD fails to link instead of silently overwriting it. A sound
build currently uses about 98–99% of that budget.

### Doom IWAD (required for Doom, **not** included)

For licensing reasons no IWAD ships in this repository. The firmware expects a
**specific** IWAD (fixed size and SHA‑256, pinned in `src/doom/DoomBuildConfig.h`)
and reads it from flash at **`0x300000`** — inside the `app0` region, after the
app. Provide that IWAD yourself and flash it there:

```sh
esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 921600 \
  write_flash 0x300000 YOUR_IWAD.wad
```

Without a matching WAD the phone and Gravity Defied still work; Doom simply
reports that it cannot mount the WAD.

> The toolchain is intentionally pinned to Arduino‑ESP32 1.0.5. Its precompiled
> SDK is a hard constraint for some optimizations (see *Performance notes*).

---

## Performance notes (Doom)

Full‑screen Doom is bound by writing the framebuffer, which lives in PSRAM
clocked at **40 MHz** (`CONFIG_SPIRAM_SPEED_40M` in the frozen 1.0.5 SDK). The
two obvious speed‑ups are both blocked by that SDK:

- an **internal‑SRAM framebuffer** doesn't fit — Wi‑Fi's static RX buffers are
 never freed (`esp_wifi_deinit` is commented out in Arduino‑ESP32 1.0.5) and
 the largest contiguous internal block stays below the ~77 KiB needed;
- **80 MHz PSRAM** is not selectable without recompiling the SDK.

Measured full‑screen FPS, full detail:

| Configuration | FPS |
|---|---|
| Shipped: 40 MHz display clock, sound on | ~13.6 |
| Same build with sound disabled | ~15.3 |

The shipped default is **full quality at ~13.6 FPS**; the SFX/OPL mixer task
costs the difference.

### Display clock

Both games drive the panel through the shared raw‑VSPI pipeline at **40 MHz**.
An earlier revision used 80 MHz, which is outside what this ST7789 tolerates
here: it corrupted the panel's address state mid‑frame, producing torn and
duplicated scanlines and, in the worst case, a display that stayed white while
DMA still reported every transfer as completed — the engine, CRCs and telemetry
all looked healthy. Both Doom and Gravity Defied were affected. Dropping to
40 MHz cleared it in both, and cost no frame rate: Gravity is bound by its fixed
45 ms frame period, and Doom measured slightly *faster* than it had at 80 MHz.
`FullScreenDmaTransfer` now rejects any request above 40 MHz.

---

## License & credits

The phone firmware and the optional game ports are separate bodies of code under
different licenses. The games are a proof of concept: they link to the firmware's
interfaces but are not part of it, and they are excluded from the build unless
`BUILD_GAMES` is defined (see `config.h`).

**Phone firmware**

- © MZJ Technology / HackEDA, under the **WiPhone Public License v1.0**
 (`WiPhone_Public_License_v1.0.txt`, also at
). Stock files modified by
 this fork carry a notice to that effect, as clause 3.0.4 requires.
- `src/TFT_eSPI/` — TFT_eSPI by Bodmer, FreeBSD licence (`src/TFT_eSPI/license.txt`).
- `FairyMax.h` — Fairy-Max by H.G. Muller, released into the public domain.
- `src/audio/` — G.711 (ITU-T reference) and G.722 by Steve Underwood.

**Doom — `src/doom/`, GPL‑2.0**

- Engine: id Software's **`linuxdoom-1.10`**, released 1997‑12‑23 and relicensed
 by id under the **GNU GPL v2**; ZeniMax applied GPL‑2.0 to the official
 repository on 2024‑01‑16, which settles the older Doom Source License headers
 still present in the 1997 files. Pinned copy in
 `tools/fpdoom/vendor/id-doom/`.
- Port: **FPDoom** (`tools/fpdoom/vendor/fpdoom/`), released into the public
 domain under the Unlicense.
- Music: `opl.c`, `opl_queue.c`, `oplplayer.c`, `midifile.c` from **Chocolate
 Doom** © Simon Howard, GPL‑2.0; `mus2mid.c` and `lprintf.h` from **PrBoom**,
 GPL‑2.0; `dbopl.c` is the **DOSBox** OPL2/OPL3 emulator © The DOSBox Team,
 GPL‑2.0 or later.
- No Doom game data ships here — you supply your own IWAD.

**Gravity Defied — `src/gravity_defied/`, GPL‑2.0**

- Port derived from **gravity_defied_cpp**
 by rgimad, AntonEvmenenko and Max Logaev, GPL‑2.0.
- The original *Gravity Defied* (J2ME, 2004) and its name, logo, artwork and
 levels belong to **Codebrew Software**. This project is not associated with
 Codebrew Software, and the GPL‑2.0 above covers the port's code, not the
 original game's assets.

**Tooling**

- `tools/prboom/` is a standalone reference benchmark of Retro‑Go's PrBoom 2.5.0
 (GPL‑2.0). It is not compiled into the firmware.

# Kentucky-ai/opentakeoff

## 关联链接

- https://github.com/user-attachments/assets/15109be5-7dc8-4c8a-bdc0-1c27c0ace83c
- https://github.com/user-attachments/assets/53a7155e-2d7a-4339-8cc7-e69895d973ab

## 导航

- 项目页：[[10-项目/github.com_0c971f14]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
