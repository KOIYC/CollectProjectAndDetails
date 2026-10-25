---
type: "corpus"
item_id: "b474e7b3c6f9b902"
title: "Show HN: A Truly Modular Keyboard"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50228115"
project_url: "https://github.com/notaroomba/keybytes"
author: "NotARoomba"
published_at: "2026-10-25T03:47:56Z"
captured_at: "2026-10-25T23:24:35+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-10-25"
pub_day: "2026-10-25"
tags:
  - 语料
  - hn_show
  - author_NotARoomba
  - story_50228115
  - show_hn
metrics: {"points": 4, "comments": 1, "engagement_velocity": 4}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: A Truly Modular Keyboard

> [!info] 一句话导读
> A truly modular keyboard

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50228115>
> 指标：点赞=4 · 评论=1 · engagement_velocity=4
> 作者：NotARoomba　|　发布：2026-10-25T03:47:56Z
> 项目链接：<https://github.com/notaroomba/keybytes>
> 采集：2026-10-25T23:24:35+08:00　|　id：`b474e7b3c6f9b902`

## 正文

# notaroomba/keybytes

A truly modular keyboard

- Stars: 22
- Forks: 1
- Watchers: 22
- Open issues: 0
- Default branch: main
- Created: 2025-12-19T21:55:32Z

## Languages

- Assembly
- C
- C++
- CMake
- Linker Script
- Makefile
- Python

## Top Contributors

- notaroomba (40 contributions)

---

## README

A truly modular keyboard with rearrangeable keys, magnetic cases and Bluetooth!

KiCad
STM32
RISC-V
Onshape
Blender

 Key Features •
 Video Demo •
 PCB •
 Case •
 Credits •
 License

## Video Demo

https://github.com/user-attachments/assets/19bec26d-6e01-4ee0-906e-7e69bace2f9c

## Key Features

- **Rearrangeable layout** where every key is its own 1u PCB
- **CH32V003** RISC-V microcontroller on every key
- **STM32WB55RGV6** main board with Bluetooth and USB
- **Pogo pins on all 4 sides** of every key for power and I2C
- **Magnetic cases** to hold the modules together
- **Key programming** from the main board over pogo pins
- **2MB QSPI flash** (W25Q16JV) to store the key firmware
- **Battery charging** with the BQ25895 and solder pads for a 1S LiPo
- **Buck-Boost converter** (TPS631000)
- **RGB status LED**
- **USB-C** with ESD protection
- **Ceramic Bluetooth antenna**

## PCB

Designed in KiCad! There are two boards, the Keybit and the Keyword, and both are 1u (19.05mm x 19.05mm).

### Keybit

A single key with a Cherry MX switch and a CH32V003. Every side has pogo pins for 3.3V, GND and I2C so it can connect to the keyword or to other keybits, and the pads on the corners are for programming.

**Schematic:**

**Layout:**

### Keyword

The main board that the keybits connect to. It is split into two PCBs that stack on top of each other. The top one has the STM32WB55RGV6, the antenna and the flash, and the bottom one has the USB-C, the charger and the buck-boost converter. The 3 pogo pins on the top are for programming the keybits.

**Schematic:**

**Layout:**

**3D View:**

## Case

Custom designed cases in Onshape, the STEP files are in the `cad` folder.

## Credits

This project uses:

- KiCad
- OnShape for case design
- Blender for 3D renders
- STM32CubeMX
- Hack Club Forge

## You may also like...

- Ember - A USB-C powered reflow hotplate with Bluetooth
- Cyberboard - A Raspberry Pi Pico-sized STM32 development board with Bluetooth
- Trace - A comprehensive PCB ruler with reference footprints
- Linea - An EMR tablet

## License

MIT

---

> notaroomba.dev  · 
> GitHub @NotARoomba  · 

# vid-t/whatsapp-bridge

## 评论（1/1）

> **NotARoomba** · 2026-10-25T03:47:56.000Z　
> A while back I was frustrated when wanting to buy a keyboard that there were no triangle-shaped keyboards or circle-shaped keyboards. This lack of peculiar keyboard shapes gave me the idea to make a keyboard that could be reconfigurable into any shape my heart desired. I’m still working on the firmware and making more keys but I wanted to share my progress so far. Heres the source if anyone’s interested in how I made it: https://github.com/notaroomba/keybytes

## 关联链接

- https://github.com/user-attachments/assets/19bec26d-6e01-4ee0-906e-7e69bace2f9c

## 导航

- 项目页：[[10-项目/github.com_68e16cd5]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
