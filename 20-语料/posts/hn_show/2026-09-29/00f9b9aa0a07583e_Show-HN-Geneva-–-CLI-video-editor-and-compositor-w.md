---
type: "corpus"
item_id: "00f9b9aa0a07583e"
title: "Show HN: Geneva – CLI video editor and compositor with a native HTML/CSS engine"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49877953"
project_url: "https://github.com/geneva-render/geneva"
author: "fbnt"
published_at: "2026-09-28T13:51:02Z"
captured_at: "2026-09-29T09:42:56+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-29"
pub_day: "2026-09-28"
tags:
  - 语料
  - hn_show
  - author_fbnt
  - story_49877953
  - show_hn
metrics: {"points": 4, "comments": 1, "engagement_velocity": 4}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Geneva – CLI video editor and compositor with a native HTML/CSS engine

> [!info] 一句话导读
> geneva-render/geneva

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49877953>
> 指标：点赞=4 · 评论=1 · engagement_velocity=4
> 作者：fbnt　|　发布：2026-09-28T13:51:02Z
> 项目链接：<https://github.com/geneva-render/geneva>
> 采集：2026-09-29T09:42:56+08:00　|　id：`00f9b9aa0a07583e`

## 正文

# geneva-render/geneva

Video edits as JSON, overlays as HTML+CSS, rendered without a browser.

- Stars: 5
- Forks: 0
- Watchers: 5
- Open issues: 0
- License: MIT License
- Homepage: https://genevarender.com
- Default branch: main
- Created: 2026-09-28T10:15:25Z

## Languages

- HTML
- JavaScript
- PowerShell
- Python
- Rust
- Shell
- TypeScript
- WGSL

## Topics

- cli
- json
- motion-graphics
- rust
- video
- video-editing
- video-editor
- video-processing

## Top Contributors

- fbnt (280 contributions)

---

## README

**Video edits as JSON, overlays as HTML+CSS, rendered without a browser.**

This started as a rewrite of ffmpeg's CLI in Rust. The core codecs still come from libav*, but everything on top of them is new: a planner that works out the cheapest way to produce an edit, a proper compositor with layers, keyframes, masks, transitions etc., and a layout engine that draws titles and graphics written in plain HTML and CSS, natively and quickly. No filtergraphs, no Playwright, no headless browsers. All in a single binary, without dependencies.

https://github.com/user-attachments/assets/e6da7c2a-62eb-4852-8523-c9ea0ed192cf

 An AI agent made this on its first try, from one prompt, with nothing but whisper-cli and a single geneva command. The prompt is below.

## Install

```sh
# Linux, macOS
curl -fsSL https://raw.githubusercontent.com/geneva-render/geneva/main/scripts/install.sh | sh
```

```powershell
# Windows (PowerShell)
irm https://raw.githubusercontent.com/geneva-render/geneva/main/scripts/install.ps1 | iex
```

Or download an archive from Releases. It runs on Linux (x64, arm64), macOS on Apple silicon and Windows x64, and everything it needs is inside the binary.

## The everyday things

```sh
geneva trim match.mp4 -o goal.mp4 --from 41:10 --to 41:40   # no re-encode, done in a blink
geneva concat day1.mp4 day2.mp4 -o trip.mp4 --crossfade 1s
geneva convert talk.mov -o talk.mp4 --for web               # sensible codec, size and settings for the destination
geneva subtitles talk.mp4 -o talk-subbed.mp4 --burn talk.srt
geneva probe talk.mp4                                       # what's actually in the file
```

Every command is translated into a validated JSON document describing the edit, which geneva renders as-is. You can also add `--show-timeline` to see it. All commands and flags are here: docs/cli.md.

## How it works

This is an example of a name card that slides in two seconds into ten seconds of footage and fades out four seconds later. The card is an HTML file, so it looks and moves the same when you open it in a browser:

```html



<div class="card">
  <h1>Dragon CRS-17</h1>
  <p>BERTHING AT THE ISS  ·  NASA</p>
</div>
```

Then a JSON document says when it appears:

```json
{
  "geneva": "1.1",
  "output": { "width": 1280, "height": 720, "fps": 30 },
  "assets": { "iss": { "src": "iss.mp4" }, "card": { "src": "card.html" } },
  "layers": [
    { "id": "footage", "clips": [ { "source": { "kind": "video", "asset": "iss" } } ] },
    { "id": "card", "clips": [ { "source": { "kind": "html", "asset": "card" }, "start": "2s", "duration": "4s" } ] }
  ]
}
```

```text
$ geneva render dragon.json -o dragon.mp4
note[N600]: smart cut: 165 of 300 frames copied from the source, 135 encoded in 1 run around the cuts and overlays
note[N600]: H.264 runs encoded with the system's x264 (build 164) at CRF 18
wrote dragon.mp4 (300 frames, 10s of video)
```

The box grows to fit its text. Percentages are relative to the frame, so the same card works at any output size. Frames with nothing on them aren't re-encoded: with an H.264 source and x264 installed they're copied straight from the source; otherwise they go from decoder to encoder without touching the compositor.

The full example, examples/lower-third.json, also adds word-by-word captions: one more layer that reads the Whisper transcript as it is.

### The same card in ffmpeg

```sh
ffmpeg -i iss.mp4 -filter_complex "
  color=c=0x0a0f14@0.8:s=422x82:d=4,format=rgba,
  drawbox=w=5:h=ih:c=0xc4362f:t=fill,
  drawtext=fontfile=LiberationSans-Bold.ttf:text='Dragon CRS-17':fontsize=29:fontcolor=0xf2f5f7:x=29:y=14,
  drawtext=fontfile=LiberationSans-Regular.ttf:text='BERTHING AT THE ISS  ·  NASA':fontsize=13:fontcolor=0x94a6b6:x=29:y=56,
  fade=t=in:d=0.3:alpha=1,fade=t=out:st=3.7:d=0.3:alpha=1,
  setpts=PTS+2/TB[card];
  [0:v][card]overlay=x='56-422*pow(1-min((t-2)/0.5\,1)\,3)':y=54:eof_action=pass
" dragon.mp4
```

This kinda works, eh. But `drawbox` can't read the width `drawtext` measured, so every size in there is a pixel a human (or an AI) had to measure. There are no rounded corners, no letter-spacing and no blurred shadow on the box, so the card above has to be made in another tool first. Word-by-word captions need a script to turn the transcript into an ASS file, and ASS still can't round the box or keep it even behind the lit word. And all 300 frames get re-encoded, including the 180 with nothing on them.

## Why not just use an ffmpeg wrapper, or a browser?

Wrappers like ffmpeg-python or fluent-ffmpeg only give you a nicer way to write the same filtergraph, so they can't do anything the filtergraph can't. geneva never writes an ffmpeg command. It reads the whole edit first, then decides how to do it:

- **It does less work.** Anything that can be copied is copied. A frame-accurate cut only re-encodes the frames up to the next keyframe (with x264 on your system), frames with nothing drawn on them skip the compositor, and changing only the sound leaves the picture alone. ffmpeg can do most of this if you know the flags. geneva just does it.
- **It catches mistakes before rendering.** The whole edit is checked first, and every problem comes back with a code, where it is in the document, and usually a hint:

  ```text
  error[E200]: unknown asset "crad"
    --> /layers/2/clips/0/source/asset = "crad"
     = help: did you mean "card"? assets are declared under "assets"
  ```

 ffmpeg will happily hand you a broken file and exit 0. In a small test I ran (20 editing tasks, one model, twice; I wrote the tasks, so take it as a hint), 8 of the ffmpeg files exited 0 and were quietly wrong: shifted colours, cuts a few tens of milliseconds off, sound drifting out of sync. The geneva ones were all right both times, after I fixed the one bug the test found.
- **It has a real compositor.** It handles layers, keyframes, masks, blend modes and transitions, all frame-exact and blended in linear light, keeps the colour metadata and tone-maps HDR when needed. Every frame is computed from its timestamp, so frame 1234 always looks the same. It uses the GPU if you have one, and the CPU if you don't.
- **It tells you what it did.** Each run ends with a few notes: which encoder it picked, what it copied, what it had to guess about your source. `--format json` gives you the same, machine-readable.

### What about Playwright or Remotion?

You can screenshot the HTML frame by frame in a headless browser and have ffmpeg lay the shots over the footage, and people do. But you have to fake the browser's clock for every frame, it's a second full encode, and you need Chromium, Node and ffmpeg installed first. Remotion packages the same idea, and its docs tell you not to use CSS `@keyframes`, since frames render out of order. geneva plays them as written.

It's also slower. I timed all three on the same machine, a cloud VM with 4 vCPUs of an Intel Xeon at 2.1 GHz, 16 GB of RAM and no GPU, each encoding with x264 at the same settings. The name card and captions above took geneva 4.3 seconds, Playwright + ffmpeg 16.4 and Remotion 14.5, and the Popeye video at the top took 74 seconds against 131 for Playwright + ffmpeg. Across seven real-world jobs geneva was quicker than both every time: 2 to 6 times with footage, and about twice as quick as Remotion on motion graphics alone.

What the browser does better: the rest of CSS, and JavaScript. geneva covers what titles and graphics actually use (flexbox, gradients, shadows, clip paths, blend modes, keyframes), but not grid or inline spans. And no JavaScript, which you don't really need for nice graphics anyway.

## Made to be driven by agents

Everything an agent needs is in the binary: `geneva guide` prints the manual, `geneva explain ` explains any error, and `--format json` works on every command. Documents are plain JSON with a published schema, and graphics are HTML and CSS, which models already write well.

The video at the top is an agent's first attempt with that and nothing else. It worked out the layout, wrote the lower third in HTML and CSS, pulled the headlines from a Whisper transcript of the clip, and rendered it, all from this prompt:

> Using only the built-in geneva guide and whisper-cli, take a 1m clip
> from public-domain popeye and overlay a realistic CNN style animated
> lower third for the whole clip (change the CNN logo to GNN, keep the
> style), with headlines derived from the clip itself. The source is 4:3,
> so output 16:9 1080p with the empty sides filled by a blurred copy of
> the video.

## H.264 and x264

geneva ships with OpenH264 for H.264. If x264 is installed on your system, geneva uses it instead, and you get noticeably smaller files. I don't bundle it because it's GPL and geneva is MIT.

```sh
sudo apt install libx264-164   # Debian 12, Ubuntu 24.04 (libx264-163 on 22.04)
brew install x264              # macOS
```

On Windows, drop `libx264-.dll` next to `geneva.exe` (MSYS2's `mingw-w64-ucrt-x86_64-libx264` has one), or point `GENEVA_X264` at it.

## Docs

- Commands and flags
- The document format
- Examples
- For scripts and agents
- Error codes
- Colour and HDR
- Benchmarks
- Architecture
- Changelog

## How this was built

This was built almost entirely with Fable/Opus, which wrote the code,
tests and docs under my guidance. I am being upfront about that so you
can decide how much you trust the code.

## Where it's at

geneva is young, and for now it's just the engine: no GUI, no hosted service. What I build next depends on what people make with it, so if that's you, or you'd like it to be, I'd love to hear what you're working on. Issues and discussions are open.

## Building from source

```sh
scripts/build-media-libs.sh   # builds the media libraries once, takes a while
cargo build --release
```

CONTRIBUTING.md has the toolchain for each platform and how to run the tests.

## Licence

MIT. Bundled libraries and their licences are listed in THIRD-PARTY-NOTICES.md.

## 评论（1/1）

> **fbnt** · 2026-09-28T13:51:16.000Z　
> Hi everyone, this is Francesco (fbnt). Geneva is a CLI video editor: you describe an edit as JSON, write titles and graphics in plain HTML and CSS, and it renders everything in one pass, from a single binary, without chrome or filtergraphs.I've been working with video encoding, subtitles and basically anything that is "layer things on top of videos" for many years now, and lately I started wondering if there was a more efficient way to do it without relying on the usual methods and libraries. Basically, every time you paint stuff over a video, you create the overlays with 'some' tool (something that generates cards as PNGs, or a headless browser for more complex animated designs.. or other techniques), and then use good old ffmpeg to merge the composition together, or eventually use ffmpeg's complex filtergraphs with all their quirks and limitations if you're desperate, but nobody does that anymore.But what if ffmpeg could do proper composition, natively? That's probably a bit out of scope for them, so I set out to start rewriting ffmpeg's CLI in Rust with some extras.. because, why not. Of course, the codecs still comes from libav*, but everything above it is new: a planner that figure out the cheapest way to produce the output (frames with nothing drawn on them aren't re-encoded), a compositor with layers, keyframes, masks and transitions, and a layout engine for the part of CSS that is most commonly used: flexbox, gradients, shadows, clip paths, blend modes, and @keyframes played as written.Now I have something that paints pretty animated graphics natively over videos very quickly, and without using playwright or chrominum.
> You can see some benchmarks here against two of the most common methods used to achieve this here: https://github.com/geneva-render/geneva/blob/main/docs/bench...As you probably guessed, this was all written by Fable/Opus under my guidance. Just stating it plainly so you can decide whether to trust it or not.
> This is just the engine, and I have a couple of ideas on how to move it forward, but I'd like to hear some feedback before carrying on blindly, so feel free to reply here or get in touch.Some rendered examples are in the repo and here: https://genevarender.com

## 关联链接

- https://genevarender.com
- https://github.com/user-attachments/assets/e6da7c2a-62eb-4852-8523-c9ea0ed192cf
- https://raw.githubusercontent.com/geneva-render/geneva/main/scripts/install.ps1
- https://raw.githubusercontent.com/geneva-render/geneva/main/scripts/install.sh

## 导航

- 项目页：[[10-项目/github.com_9323b766]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
