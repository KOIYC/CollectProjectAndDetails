---
type: "corpus"
item_id: "7e20c7f7fc126ffd"
title: "Show HN: AeonCut – Open-source silence cutter for DaVinci Resolve (Rust/egui)"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50224560"
project_url: "https://github.com/aethelisdev/aeoncut"
author: "aethelis"
published_at: "2026-10-24T19:59:27Z"
captured_at: "2026-10-25T23:24:35+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-10-25"
pub_day: "2026-10-24"
tags:
  - 语料
  - hn_show
  - author_aethelis
  - story_50224560
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: AeonCut – Open-source silence cutter for DaVinci Resolve (Rust/egui)

> [!info] 一句话导读
> Audio Silence & Breath Cutter for DaVinci Resolve 21. Powered by native Rust (egui) & Voice Activity Detection (VAD).

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50224560>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：aethelis　|　发布：2026-10-24T19:59:27Z
> 项目链接：<https://github.com/aethelisdev/aeoncut>
> 采集：2026-10-25T23:24:35+08:00　|　id：`7e20c7f7fc126ffd`

## 正文

# aethelisdev/aeoncut

Audio Silence & Breath Cutter for DaVinci Resolve 21. Powered by native Rust (egui) & Voice Activity Detection (VAD).

- Stars: 1
- Forks: 0
- Watchers: 1
- Open issues: 0
- License: GNU Affero General Public License v3.0
- Default branch: main
- Created: 2026-10-24T17:45:58Z

## Languages

- Python
- Rust

## Topics

- audio-editing
- audio-processing
- davinci-resolve-21
- egui
- rust
- rust-lang
- silence-removal
- vad
- video-editing
- voice-activity-detection

## Top Contributors

- aethelisdev (13 contributions)

---

## README

 AEON-CUT

 Audio Silence & Breath Cutter for DaVinci Resolve 21
 Powered by pure Rust (egui) GPU-accelerated interface and high-precision Voice Activity Detection (VAD).

---

---

## Highlights

* **100% Free & Open Source:** No monthly SaaS subscriptions ($10–20/mo saved).
* **Blazing Fast Native Rust GUI:** Built with `egui` / `eframe` — silky smooth 60+ FPS, instantaneous startup, and custom DaVinci Resolve dark studio aesthetic.
* **100% Local & Private:** No video or audio is ever uploaded to external servers or cloud providers.
* **Non-Destructive Editing (Handles Preserved):** All speech cuts preserve media references so edge handles can be trimmed or extended directly on the timeline anytime.
* **Multi-Language Support (i18n):**
 * 🇺🇸 English
 * 🇹🇷 Türkçe
 * 🇨🇳 简体中文
 * 🇯🇵 日本語

---

## Cutting Modes

1. **New Clean Timeline (Auto-Cut):**
 * Automatically creates a new timeline (`Timeline - AeonCut`) populated only with speech slices.
 * Switches Resolve's active viewer directly to the new timeline.
 * Silences are completely eliminated while keeping separate cut clips on Track 1.
2. **Append to Active Timeline:**
 * Appends the sliced speech clips directly onto your current working timeline.
3. **Add Clip Markers:**
 * Places non-destructive Cyan markers across speech and silence boundaries for manual review.

---

## Precision Controls

* **Silence Threshold (`dB`):** `-60 dB` to `-10 dB` (Default: `-32 dB`).
* **Min Silence Duration (`ms`):** Prevents cutting natural micro-pauses within sentences (Default: `350 ms`).
* **Start Breath Padding (`ms`):** Preserves the beginning consonant of words (Default: `120 ms`).
* **End Breath Padding (`ms`):** Softens the trailing edge of words (Default: `150 ms`).

---

## Quick Start

### Prerequisites

* Rust & Cargo (1.80+)
* Python 3 (3.6+)
* FFmpeg (Installed on system PATH)
* DaVinci Resolve Studio (21, 20, or 19)

### Running

```bash
git clone https://github.com/aethelisdev/aeoncut.git
cd aeoncut
cargo run --release
```

1. Open **DaVinci Resolve** and select a video/audio clip in your timeline.
2. In Aeon-Cut, click **"🔍 Analyze Clip"**.
3. Choose your cut mode and click **"✂ Apply Cuts to Resolve"**.

---

## Testing

Run automated Voice Activity Detection tests:

```bash
cargo test
```

---

## License

This project is licensed under the **GNU Affero General Public License v3.0 (AGPL-3.0)**.
See the LICENSE file for details.

# microsoft/Agensh

## 关联链接

- https://github.com/aethelisdev/aeoncut.git

## 导航

- 项目页：[[10-项目/github.com_1ef425ad]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
