---
type: "corpus"
item_id: "adeb14b7a55e38dd"
title: "Show HN: Entropic — information-driven variable-rate media playback"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48346255"
project_url: "https://github.com/patrickxia/entropic"
author: "pxx"
published_at: "2026-05-31T15:04:46Z"
captured_at: "2026-09-21T02:52:43+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-05-31"
tags:
  - 语料
  - hn_show
  - author_pxx
  - story_48346255
  - show_hn
metrics: {"points": 4, "comments": 1, "engagement_velocity": 4}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:144d"
---

# Show HN: Entropic — information-driven variable-rate media playback

> [!info] 一句话导读
> Entropic: information-driven variable-rate media playback

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48346255>
> 指标：点赞=4 · 评论=1 · engagement_velocity=4
> 作者：pxx　|　发布：2026-05-31T15:04:46Z
> 项目链接：<https://github.com/patrickxia/entropic>
> 采集：2026-09-21T02:52:43+08:00　|　id：`adeb14b7a55e38dd`

## 正文

# patrickxia/entropic

Entropic: information-driven variable-rate media playback

- Stars: 1
- Forks: 0
- Watchers: 1
- Open issues: 0
- License: GNU General Public License v2.0
- Default branch: main
- Created: 2026-05-31T00:51:55Z

## Languages

- Python

## Top Contributors

- patrickxia (2 contributions)

---

## README

# Entropic: information-driven variable-rate media playback

Variable-rate audio/video playback that slows down for unfamiliar or high-information words and accelerates through predictable speech, using token-level surprisal from a fast local LLM.

* **vbr** (default) targets an average speed while distributing time by information content (watch 2x demo)
* **skiplow** keeps speech at 1x and only speeds up low-information segments, like an enhanced skip-silence (watch 1.5x demo)

## How it works

1. **Transcribe** with WhisperX (word-level timestamps via forced alignment)
1. **Score** each word's surprisal: unigram (word frequency) or contextual (causal LM like distilgpt2/gpt2)
1. **Estimate** each word's confidence using whisper token-level probabilities, optionally from a separate weaker model (`--uncertainty-model`)
1. **Assign speeds** per one of two modes:
 - **VBR** (default): `speed ∝ 1/surprisal`
 - **Skiplow**: words above an info-rate threshold stay at 1x; words below get sped up proportionally; silences are fast-forwarded
1. **Time-stretch** via `librubberband.so` (ctypes, real-time mode [to avoid clipping between samples and to obtain output timestamps])
1. **Retime video** (if applicable) via mkvmerge timecodes; optionally burn-in debug subtitles (requires re-encode)

### Surprisal model

- **Unigram** (default): word rarity via `wordfreq`
- **Contextual** (`--model gpt2`): causal LM surprisal with sliding window
- **Rarity blend** (`--rarity 1.5`, default when using `--model`): adds `rarity × unigram_surprisal`, see Development Notes below.

## Requirements

### System packages

```bash
# Debian/Ubuntu
sudo apt install ffmpeg mkvtoolnix librubberband-dev
```

- **ffmpeg**: audio extraction, muxing, subtitle burn-in
- **mkvtoolnix** (`mkvmerge`): video frame retiming
- **librubberband** (>= 3.0): time-stretching via C API

### Python

Requires Python 3.11+.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**Note on WhisperX**: installed from git since it's not on PyPI. It pulls in `faster-whisper`, `pyannote-audio`, and torch as transitive dependencies.

**Note on torch**: the default pip install pulls CUDA 12.x wheels (~2 GB). For CPU-only:
```bash
pip install torch --index-url https://download.pytorch.org/whl/cpu
pip install -r requirements.txt
```

## Usage

### Audio

```bash
# Basic — 1.5x average speed, unigram surprisal (VBR mode)
python entropic.py podcast.mp3

# 2x with contextual surprisal
python entropic.py podcast.mp3 -s 2 --model distilgpt2

# Custom speed bounds
python entropic.py lecture.mp3 -s 1.8 --min-speed 0.8 --max-speed 3.0 --model gpt2

# Skiplow mode — keep speech at 1x, compress silences and low-info words
python entropic.py podcast.mp3 --mode skiplow

# Skiplow targeting 2x overall speed (auto-computes threshold)
python entropic.py podcast.mp3 --mode skiplow -s 2

# Skiplow with explicit threshold (bits/s)
python entropic.py podcast.mp3 --mode skiplow --threshold 80
```

### Video

```bash
# Retime video (no re-encode, copies video stream)
python entropic.py lecture.mp4 -s 2 --model distilgpt2

# With burned-in subtitles (re-encodes video with SVT-AV1)
python entropic.py lecture.mp4 -s 2 --subtitles --model distilgpt2
```

### Options

| Flag | Default | Description |
|------|---------|-------------|
| `--mode` | vbr | `vbr` (target average speed) or `skiplow` (enhanced skip-silence) |
| `-s, --speed` | 1.5 | Target average speed. In skiplow, auto-computes threshold to achieve this |
| `--threshold` | - | Min info rate (bits/s) before speedup (skiplow only, overrides `--speed`) |
| `--min-speed` | 1.0 | Minimum playback speed |
| `--max-speed` | 3.5 | Maximum playback speed |
| `--silence-speed` | max-speed | Speed for gaps between words |
| `--model` | gpt2 | Causal LM for contextual surprisal (`gpt2`, `distilgpt2`, `none` for unigram-only) |
| `--rarity` | 0.1 | Unigram rarity weight when using `--model` |
| `--clarity` | 1.5 | Clarity penalty strength (0 = disabled) |
| `--whisper-model` | turbo | WhisperX model for transcription (`tiny.en`, `base.en`, `turbo`, etc.) |
| `--uncertainty-model` | same as `whisper-model` | Separate model for word confidence. A weaker model (`tiny.en`) gives more honest uncertainty on mumbled speech |
| `--language` | en | Language code for transcription, alignment, and word frequency |
| `--subtitles` | off | Generate word/speed/surprisal overlay. Video: burned in. Audio-only: saved as `.ass` file |
| `--device` | cpu | `cpu` or `cuda` for WhisperX and LM |
| `--transcript` | auto | Path to transcript cache JSON |
| `--no-cache` | off | Force re-transcription |

## Transcript caching

Transcripts are cached to `.transcript.json`. Re-running with different speed/spread/model parameters reuses the cached word timestamps and only recomputes surprisal and speeds. Use `--no-cache` to force re-transcription (needed when changing `--whisper-model`).

# Development notes

Maybe more suitable for a blog post, but we might as well write the beginnings of it.

## Constant information rate

Originally the design was to target a constant output information rate, so that each word's output duration depends only on its surprisal. This ends up ignoring the input duration entirely, which isn't entirely information-free (speakers might slow down naturally to indicate emphasis). Constant output information rate also causes significant distortion; already-short words were made even shorter in duration due to their low information content. The current implementation has speed inversely proportional to information only, preserving a bit more of the original speech rhythm.

## City of Manaus problem

While testing initial prototypes, the city "Manaus" was well-predicted and accelerated within context. Even a weak LLM like GPT-2 can predict reasonably well from "the Brazilian city of ", but for listeners who are not familiar with Brazilian geography, accelerating this unfamiliar word is not productive. In some ways, this indicates how even weak LLMs are "too intelligent" for this process. To compensate for this, `--rarity` was added, but the weight is a heuristic. Perhaps a pure unigram model is better for most usecases, but it still does stand to reason that rarer words, when encountered multiple times, should be sped up on repetition.

## Implementation bugs introduced by Claude Code (with model Opus 4.7)

Opus 4.7 is a very powerful model but it made some very bizarre choices, causing the introduction of many hard-to-debug bugs that had to be resolved in parallel to the design questions above. Those included:

* Transcription uncertainty was taken from the whisperx _alignment_ model, not the transcription step, entirely corrupting the confidence metric.
* Surprisal for multiple-token words was *averaged* across tokens, including punctuation, which is also essentially noise.
* A subtrahend of 12 was used to convert from `wordfreq.zipf_frequency` which is occurrences-per-billion (1e9). It's unclear why we're even using `zipf_frequency` to begin with; using the raw frequency wouldn't have this detuning knob.
* Binary search for the speedup with clamping was implemented as a bizarre greedy floodfill that would return the wrong answer frequently but not always (of note, it would never get the right answer if the naive solution of no speedup was already within the constraints). The binary search is still implemented "competition programming" style, but at least it works now.
* min-speed and max-speed kept going back to this weird implementation of multiplier applied to the target speed.
* Transcription uncertainty was multiplied into the surprisal via hacky parameters despite the fact that it can be natively described as "bits of entropy". The weight still is heuristic, so the digression here is a little more understandable.

It's very unclear if development was truly sped up by using an LLM. There are likely more bugs. Everything always _looked_ like it was working, but things would feel "off," and the debug process would take quite some time. I ran out of Opus tokens and I migrated to deepseek-v4-pro midway through, which was able to debug and fix these issues when directly pointing them out (though I'm sure Opus would have too).

Automatically debugging A/V sync issues with just the prompt "the A/V sync is broken" worked quite well though. Those are normally a nightmare to fix.

## Clarity penalty for multiple speakers

Some podcasts feature one host who is very clear and one host who mumbles all of their words (e.g. Money Stuff). The goal of the clarity penalty was to make the less comprehensible host more comprehensible. Whisper is "too good" at this -- even Matt Levine can be predicted with reasonably high accuracy. Fixing this is a WIP, but `--uncertainty-model` is maybe the first step. `tiny.en` sometimes has better average log-probability of understanding Katie Greifeld than Matt Levine but they rarely differ by much, which makes this harder. Perhaps we should inject additional noise? Was whisper trained predominantly on male voices?

# Disclaimer

This is a personal project. The views, code, and opinions expressed here do not represent those of my current or past employers.

## 评论（1/1）

> **khabib73** · 2026-05-31T18:20:31.000Z　
> looks good

## 关联链接

- https://download.pytorch.org/whl/cpu

## 导航

- 项目页：[[10-项目/github.com_bfa7e3d2]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
