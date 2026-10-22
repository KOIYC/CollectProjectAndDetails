---
type: "corpus"
item_id: "e1453fc8c7aaec11"
title: "Show HN: I built ESP32-S3 LED tubes for live coding"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50185772"
project_url: "https://github.com/genbs/reactive-leds"
author: "genbs"
published_at: "2026-10-21T18:55:02Z"
captured_at: "2026-10-22T09:46:18+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-10-22"
pub_day: "2026-10-21"
tags:
  - 语料
  - hn_show
  - author_genbs
  - story_50185772
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: I built ESP32-S3 LED tubes for live coding

> [!info] 一句话导读
> DIY LED lighting system powered by ESP32, featuring 3D-printed enclosures and real-time control for live coding performances.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50185772>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：genbs　|　发布：2026-10-21T18:55:02Z
> 项目链接：<https://github.com/genbs/reactive-leds>
> 采集：2026-10-22T09:46:18+08:00　|　id：`e1453fc8c7aaec11`

## 正文

# genbs/reactive-leds

DIY LED lighting system powered by ESP32, featuring 3D-printed enclosures and real-time control for live coding performances.

- Stars: 6
- Forks: 1
- Watchers: 6
- Open issues: 0
- License: Other
- Homepage: https://reactive-leds.genbs.dev/
- Default branch: master
- Created: 2024-12-04T21:32:27Z

## Languages

- C
- CMake
- CSS
- HTML
- JavaScript
- OpenSCAD
- TypeScript

## Topics

- 3d-printing
- diy-project
- esp32
- led
- livecoding
- neopixel
- realtime
- udp
- visuals
- vj
- websocket
- ws2812

## Top Contributors

- genbs (14 contributions)

---

## README

Firmware Build
Test shared
Test cli
Test client
License: GPL v3
GitHub last commit

# Welcome to Reactive-LEDS

Language: English | Italiano

 ▶ Watch the 44-second demo on YouTube

## Introduction

This project documents my personal experience building a 3D-printed LED tube, controllable over WiFi.

It was born out of a personal need: I wanted lights for my live coding performances, and as a software developer with a 3D printer I had fun building a system that lets me control lights from the browser with minimal latency at a reasonable cost.

The firmware and the 3D models are designed around the hardware I used. Take them as a starting point and adapt them to your own setup.

## Result

The current build is a 1-meter tube with a 24V FCOB strip, driven by an ESP32-S3 microcontroller, all powered by a 24V supply and controllable over WebSocket or UDP.
You can build as many strips as you want — just connect them to the same network.

## How it works

The complete flow:

```
browser
  → WebSocket → CLI proxy (ws)
    → UDP → ESP32-S3
      → RMT peripheral
        → LED strip
```

Browsers cannot send UDP directly, so the CLI exposes a local WebSocket proxy that bridges to the device. The ESP32 receives the UDP packets and updates the strip through the RMT peripheral, which generates the signal in hardware without involving the CPU.

The first time, the device is configured over USB from the site or the CLI, or over BLE with the CLI. After rebooting, it joins the network and is ready to receive commands.

## WLED compatibility

I started developing the firmware out of curiosity and to have full control over the realtime path. Only later did I take a closer look at WLED, which supports UDP control through DDP.

In tests with ESP32-S3 boards and 16 segments, WLED and reactive-leds were equally smooth at 60 fps. With 90 and 120 fps streams, stock WLED coalesced updates and rendered about 62 frames per second, while the included firmware rendered every frame without drops. For normal browser use at 60 fps, this difference is not significant.

WLED is not currently supported. If you would like to use it with reactive-leds, open a GitHub issue or submit a pull request.

## Repository layout

This is a small monorepo. Each main area has its own folder and its own README.

- `firmware/`: ESP32-S3 firmware and build instructions.
- `cli/`: CLI tools and scripts to configure and test the devices and to start the WebSocket control server.
- `client/`: JavaScript client for real-time control from the browser.
- `shared/`: Protocol and shared types used across packages.
- `3dprint/`: STL models and CAD sources for the enclosure and the LED rail.
- `docs/`: the project site (GitHub Pages): guided install (CLI + firmware flashing from the browser via Web Serial), live examples and the strip mapping tool.

## Getting started

- Build/flash the firmware: see `firmware/README.md`.
- CLI tools for testing: see `cli/README.md`.
- Using the JavaScript client: see `client/README.md`.
- Protocol/types: see `shared/README.md`.

## Materials

- 24V FCOB LED strip
- XL4015 DC-DC module (24V → 5V)
- ESP32-S3
- 24V power supply
- Power cable
- JST (alternative) pick the 3-pin variant (VCC, GND, DATA)
- 330 Ω resistor in series on the LED data line

These are the materials I used, but the project adapts to similar strips and components. Just make sure to configure the firmware for your strip (color order, number of segments, etc.). ESP32-S3 modules with PSRAM are fine, but PSRAM is not required for this use case: the realtime LED path uses small buffers in internal RAM.

If I were to improve the build, I would replace the somewhat fragile JST connectors and add a way to support the solder joint at the start of the LED strip.

## 3D printing

The models and settings are only a starting point — I am not a 3D printing expert.
The enclosure is designed to house the ESP32-S3 and the DC-DC module listed above, together with a 12mm LED strip rail.

For the rail I printed five 20 cm PLA pieces: either five `profile` pieces, or four `profile` pieces plus the optional `profile_head`. For the diffuser I used four 25 cm pieces of transparent PETG.

1. Print the enclosure parts (`case/*.stl`) and the LED rail (`tube/*.stl`); see `3dprint/README.md` for materials and settings.
2. Get the microcontroller, DC-DC module, power cable, JST pins, 330 Ω resistor and LED strip.
3. Assemble everything by following the photos and instructions below.
4. Flash the firmware from the project site or see `firmware/README.md`, and configure WiFi over USB or BLE with the CLI.

 1. Component overview
 2. Step down the DC-DC module voltage from 24V to 5V
 3. Solder the DC-DC module output to the microcontroller and check that the pins output 3.3V

 4. Solder the resistor to pin 18 (configurable via firmware)
 5. Insert the microcontroller into the enclosure, making sure to keep the resistor at the bottom, and position the DC-DC module compartment
 6. Once the DC-DC module is in place, you can glue the enclosure caps

 7. Insert the power cable into the other part of the enclosure, glue the JST connector and crimp the male pins onto the cables
 8. Use heat-shrink tubing to insulate the cables and insert the pins into the connector
 9. Check that the male and female JST connectors match

 10. You can now close the enclosure
 11. Overview of the enclosure with the LED strip
 12. After gluing the rail with the diffuser, you can insert the LED strip

## Transporting the tubes

At first I carried them in a cloth wrap with elastic bands, like a roll-up pencil case, but I did not feel they were secure enough.
I later built a wooden case based on this tutorial and printed PLA parts to hold the LED tubes inside it. The case fits 12 tubes.

Open wooden case with the LED tubes secured inside

## Limitations and known issues

- **Segment-level control, not per-LED**: the FCOB strip has 896 LEDs per meter but only 16 ICs per meter. Control happens per segment (16 segments/m), not per individual LED. This is a deliberate choice: I preferred a brighter strip over resolution.
- **255 LEDs per device**: `num_leds` and `start_index` are single bytes in the UDP protocol. More than enough for segment strips (~15 m of FCOB per device); it is not designed for high-density matrix panels.
- **Color order**: the RGB/WRGB byte sequence depends on the strip's IC. The firmware is configured for the strip listed in Materials. Different strips may need a different order (see `firmware/main/leds.c`).
- **WiFi sleep disabled**: the WiFi radio power-saving mode is explicitly disabled to avoid latency spikes and packet loss during real-time updates.
- **WiFi credentials in cleartext over BLE**: during provisioning the credentials are sent unencrypted. For a personal project simplicity wins, but keep it in mind on sensitive networks.

## Power and safety

The LED strip runs at 24V. Power supply sizing depends on the strip's specs and the real load — as a reference, with all LEDs on the strip draws roughly **1 A per meter**. Use a supply with adequate headroom and proper wiring.

## License

The firmware and CLI are licensed under GPL-3.0-only. The `client` and `shared` packages are licensed under MIT; see the `LICENSE` file in each directory for the full terms.

## 关联链接

- https://reactive-leds.genbs.dev/

## 导航

- 项目页：[[10-项目/github.com_5f7c8677]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
