---
type: "corpus"
item_id: "33f302345d7960c0"
title: "Show HN: HSL-Noise – A noise generator mapped to the HSL color space"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49745917"
project_url: "https://hsl-noise.mitpit.com/"
author: "MitPitt"
published_at: "2026-09-17T20:14:57Z"
captured_at: "2026-09-20T14:02:52+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-17"
tags:
  - 语料
  - hn_show
  - author_MitPitt
  - story_49745917
  - show_hn
metrics: {"points": 2, "comments": 1, "engagement_velocity": 2}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:90d"
---

# Show HN: HSL-Noise – A noise generator mapped to the HSL color space

> [!info] 一句话导读
> HUE centre frequency

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49745917>
> 指标：点赞=2 · 评论=1 · engagement_velocity=2
> 作者：MitPitt　|　发布：2026-09-17T20:14:57Z
> 项目链接：<https://hsl-noise.mitpit.com/>
> 采集：2026-09-20T14:02:52+08:00　|　id：`33f302345d7960c0`

## 正文

HSL-Noise Generator

# HSL-Noise

Color

—

———

▶ Start audio

master 70-6.9 dB

HUE centre frequency

136

SATURATION bell width

30

LIGHTNESS recut

↺

50

ALPHA density

↺

100

COMB FILTER

↺

0

Energy normalization

(?)

Hold RMS at that of white noise of the same lightness. Off = raw spectrum, expect big level drops.

Auto‑sweep hue

(?)

Slowly pans the centre frequency to audition the hue axis.

Stereo

(?)

Synthesise the left and right channels independently, for a wide, decorrelated field. Off = one stream upmixed to both channels. Same mask and level either way.

Randomize HSL Randomize HSLA Randomize All

Spectra

theoretical mask

linear dB

legend

bell B before lightness final mask A — plateau + displaced tails (up) / cut bell (down) cut line / plateau edges log f · dots = the actual bins sent to the worklet

live spectrum

legend

live FFT (pre‑master tap) theoretical shape (auto‑aligned) dBFS/bin · log f

Waveform

±0.6 full scale · pre‑master

Stats

idle

centre f c —

bandwidth (FWHM)—

σ (octaves)—

Q / Q max here—

sat. gamut at hue—

plateau / cut—

active bins—

gain applied—

rms predicted—

rms measured—

peak measured—

lightness law—

density (P)—

events / sec—

Presets

Classical Noise Colors 8

White Brownian Noise Pink Noise Blue Noise Violet Noise Velvet White Fuzzy White Black

Favourites 16

Neutral Green Highway Bridge Amber Warmth Honey Golden Brown Distant Fireworks Cicada Forest Plastic Taps Wood Taps Glass Taps Geiger Counter Fan Heater Granny Smith Distant Train Horn Rocket Engine Power Lines

CSS Reds, Oranges & Browns 37

darkred maroon firebrick red indianred lightcoral rosybrown mistyrose tomato salmon darksalmon coral orangered lightsalmon sienna seashell saddlebrown chocolate sandybrown peachpuff peru linen bisque darkorange burlywood antiquewhite tan navajowhite blanchedalmond papayawhip moccasin orange wheat oldlace floralwhite darkgoldenrod goldenrod

CSS Yellows & Greens 21

cornsilk gold lemonchiffon khaki darkkhaki ivory lightyellow lightgoldenrodyellow yellow olive olivedrab darkolivegreen greenyellow yellowgreen darkseagreen lightgreen palegreen limegreen forestgreen seagreen mediumseagreen

CSS Cyans & Blues 19

aquamarine turquoise lightseagreen mediumturquoise paleturquoise darkslategray cadetblue powderblue lightblue skyblue lightskyblue steelblue dodgerblue slategray lightsteelblue cornflowerblue royalblue midnightblue lavender

About

HSL-Noise is an experiment trying to map noise profiles to colors. Because classical Colors of noise (White, Brownian, Pink, Blue, Violet) are far from enough. HSL-Noise lets you fine-tune your favorite noise profiles and give it a precise color name.

This noise generator uses HSL color space paired with Gaussian distributions:

- Hue is the center frequency of the bell curve. Hue is limited from red (0° = 20hz) to blue (240° = 20khz). Violets and magentas are omitted to signify that it's not a circle — audio frequencies don't perceptually mix the same way colors do. Green (120°) also places itself in the middle — a truly neutral color, neither warm nor cold.
- Saturation decides the width of the bell curve. Fully desaturated colors become grey (white noise). Fully saturated color becomes an (almost) pure tone.
- Lightness artificially cuts or expands the bell. Dark colors have their bell's skirt trimmed, making them sound dull or hollow. Bright colors sound fuller until it's all white noise again.

There's also some bonus effects:

- Alpha, or opacity replicates Velvet noise. Transparent colors are sparse, they sound fuzzy or grainy.
- Comb filter is just that — it adds a ringing resonance, like the "twang" of raindrops hitting glass or metal.

Slider controls are tweaked to be responsive and give perceptually varied results.

Actual settings are reflected in the URL, so you can copy it to share with friends. Also try doing complex noises by starting two browser tabs at once, like fire hum + fire crackle.

HSL-Noise can't perfectly recreate classical noises like Brownian or Pink, because they have straight slopes, not bell curves. But they can be approximated close enough.

Personally I am a fan of Green noise — it reminds me of a distant highway. I feel like this type of noise is under-represented in the community of background noise enjoyers.

Source code is available on Github, along with notes on math and design decisions. You can contact me at hello@mitpit.com

Error fetching https://chromewebstore.google.com/detail/kora-â-focus-reader-websi/kbkcobapaoaoilpfgbaaeaedlincbpmi?hl=en: CRAWL_UNKNOWN_ERROR

## 评论（1/1）

> **blobdole** · 2026-09-17T23:15:42.000Z　
> I love noise generators and this concept is very cool!I need to dig into it more, but a common problem is having noticeable patterns or repeating transitions, especially if you are listening for hours at a time. But since this actually generated sound instead of trying to blend clips of audio together, I would imagine it does a pretty good job of avoiding that issue.

## 关联链接

- https://chromewebstore.google.com/detail/kora-â-focus-reader-websi/kbkcobapaoaoilpfgbaaeaedlincbpmi?hl=en:

## 导航

- 项目页：[[10-项目/hsl-noise.mitpit.com_62aecf88]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
