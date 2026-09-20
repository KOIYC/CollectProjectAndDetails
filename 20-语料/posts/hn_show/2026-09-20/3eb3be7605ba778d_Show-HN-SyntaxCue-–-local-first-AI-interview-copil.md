---
type: "corpus"
item_id: "3eb3be7605ba778d"
title: "Show HN: SyntaxCue – local-first AI interview copilot (whisper.cpp and BYOK)"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49738454"
project_url: "https://syntaxcue.com/how-syntaxcue-captures-system-audio"
author: "zetbaur"
published_at: "2026-09-17T09:48:19Z"
captured_at: "2026-09-20T09:36:54+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-17"
tags:
  - 语料
  - hn_show
  - author_zetbaur
  - story_49738454
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: SyntaxCue – local-first AI interview copilot (whisper.cpp and BYOK)

> [!info] 一句话导读
> How SyntaxCue Captures System Audio Locally

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49738454>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：zetbaur　|　发布：2026-09-17T09:48:19Z
> 项目链接：<https://syntaxcue.com/how-syntaxcue-captures-system-audio>
> 采集：2026-09-20T09:36:54+08:00　|　id：`3eb3be7605ba778d`

## 正文

How SyntaxCue Captures System Audio Locally · SyntaxCue

# How SyntaxCue Captures System Audio and Answers You — Without a Server

By SyntaxCue · Updated 2026-08-17 · 8 min read

SyntaxCue turns the audio of a live technical interview into a streamed answer suggestion, on-device, in a few hundred milliseconds — without ever recording the call or sending audio anywhere. This piece walks the whole pipeline: the OS audio API, voice-activity detection, local transcription, and the streamed model response, with the actual APIs and the actual measured numbers. It’s written for a reader who wants to know whether “local transcription, no backend” is a real architectural claim or a marketing one, so most of it is specifics — which CoreAudio call, why an aggregate device, and why Windows once took 25 seconds per transcription when macOS took a fraction of a second.

## The pipeline, end to end

The system is four stages: capture system audio → cut the continuous stream into utterances → transcribe each utterance locally → send the text to the user’s own LLM and stream the answer back. Capture is the only stage that’s platform-specific. Everything after it is shared code that never learns which OS produced the bytes.

### 1. Capturing system audio, not the microphone

The first design decision drives everything downstream: SyntaxCue listens to system audio — the mixed output of whatever’s playing, i.e. the call — not the microphone. That’s why it never has to solve “is this the candidate’s voice or the interviewer’s?” It captures the same mixed output a screen recorder’s audio track would, not two separate input channels. There’s nothing to diarize; there’s one stream.

On macOS (14.2+, Sonoma or later), this uses the CoreAudio Process Tap API: `AudioHardwareCreateProcessTap` with a `CATapDescription` configured as `monoGlobalTapButExcludeProcesses` — a system-wide tap, not scoped to one application — with `isPrivate = true` and, importantly, `muteBehavior = .unmuted`. That last flag matters: the tap reads a copy of the stream while the user keeps hearing their call completely normally. Nothing is intercepted, muted, or rerouted.

A raw process tap isn’t independently readable. To pull audio through a normal CoreAudio IO cycle, it has to be wrapped in a private aggregate device via `AudioHardwareCreateAggregateDevice`, which then delivers buffers through a standard IO callback. This part runs as a small Swift sidecar binary, compiled separately and shipped alongside the main Tauri binary, because the Process Tap API has no Rust binding — it’s Swift/Objective-C only. So on macOS there are two processes: the Rust/Tauri app and a thin Swift audio helper feeding it PCM.

On Windows, capture uses WASAPI loopback, and it runs entirely in-process — no separate sidecar, unlike macOS. WASAPI is plain COM, reachable directly from the Rust process, so there’s no second binary to build, bundle, or code-sign on this platform. Two details shape how this actually works, and they’re less obvious than “loopback capture” makes it sound:

- Loopback is a render endpoint opened for capture. There’s no separate “what’s playing” device to enumerate. You take the default playback device and initialize its audio client in the Capture direction — that’s specifically what sets `AUDCLNT_STREAMFLAGS_LOOPBACK`. Nothing here ever asks for a microphone.
- It polls instead of being event-driven. WASAPI’s event handle only signals while the render endpoint is actively pulling buffers — on a silent or idle endpoint, it never fires, so an event-driven loop would simply hang the moment the call goes quiet. Polling avoids that, and gives the idle branch a place to synthesize the silence the endpoint stops delivering once nothing is playing.

Both platforms converge on exactly the same wire format before anything else touches the audio: raw interleaved PCM, 32-bit float, 16 kHz, mono. From here on, voice-activity detection and transcription are identical shared code that doesn’t know or care whether a CoreAudio aggregate device or a WASAPI loopback client produced the samples.

### 2. Cutting the stream into utterances

A continuous PCM stream isn’t transcribable as-is — something has to decide where one spoken chunk ends. SyntaxCue does this with energy-based voice-activity detection: plain RMS amplitude thresholding, no ML model for this step.

The rules, exactly:

- Silence is any window with RMS amplitude below 0.006.
- A segment closes and is sent to transcription once the stream has been voiced (had signal above threshold) and either: (a) silence has run for ≥0.7 seconds and the segment so far is ≥1.0 second long, or (b) the segment hits a hard cap of 20 seconds, so an unbroken monologue doesn’t grow unbounded before transcription even starts.
- Independently of segmentation, a live audio-level meter is emitted to the UI roughly every 100 ms, so there’s continuous visual confirmation that audio is being captured, whether or not a segment has closed yet.

The interesting part is why this is deliberately unsophisticated. A neural VAD would be more precise about exact speech boundaries, but precision isn’t the bottleneck here — latency and CPU cost are, on a stage that runs continuously against a live stream. More importantly, a wrong split is cheap: if the RMS heuristic closes a segment slightly early or late, the transcription step just receives a marginally short or long chunk of the same speech, not a wrong one. When the cost of an error is that low, a neural model in the hot path is the wrong trade.

### 3. Transcription, fully local

Each closed segment goes to whisper.cpp, running on-device. No audio and no transcription text leave the machine at this stage, or any other — there’s no server in the audio path at all, full stop (the Security page lists the one narrowly-scoped exception elsewhere in the app: a free-tier hint counter that only ever sees a hashed device ID, never audio or transcription). The GPU backend is platform-specific: Metal on macOS, Vulkan on Windows. The bundled default model is whisper.cpp’s Small model, shipped with the app; larger models are optional downloads. We haven’t benchmarked a word-error-rate figure for it, so we won’t quote one.

The measured cost that does matter is model load — a one-time cost paid when the user clicks “Start listening,” not per question: ~271 ms on macOS with Metal, versus ~650–870 ms on a Windows machine without GPU acceleration (CPU-only). We haven’t separately benchmarked live per-utterance transcription latency for Metal the way we did for Windows, so rather than invent a number to make the comparison symmetric, we’ll just say the macOS side hasn’t been isolated that way — the load figure is the one we can stand behind.

The Windows number, though, is a story worth telling in full, because it changed how we think about “cross-platform.”

## Why we measured instead of assuming

The initial assumption about Windows was the boring, reasonable one: it’d be “a bit slower than the Mac.” Same model, same code above the capture layer — expect a tuning-level difference.

The reality wasn’t a tuning difference. Before the Vulkan backend was wired up, whisper.cpp on Windows ran CPU-only, and it paid a fixed ~25-second cost per transcription pass — regardless of utterance length. A one-second “yes, exactly” and a fifteen-second answer cost the same 25 seconds. For a tool whose entire value is answering within the few seconds a candidate has to respond, that isn’t slow — it’s non-functional. Twenty-five seconds per utterance means the answer to the first question arrives around the time the interviewer is asking the third.

The instinct in that situation is to start tuning: a smaller model, shorter segments, thread-count knobs. All of that would have treated a symptom. The actual cause was that there was no GPU backend at all on Windows — whisper.cpp was doing the entire inference on CPU because nothing had told `whisper-rs` to use the GPU. It wasn’t a slow path; it was the wrong path entirely.

Wiring up the Vulkan backend for `whisper-rs` on Windows changed the numbers by two orders of magnitude. Warm transcription of a ~6-second utterance dropped to ~330 ms. There’s a one-time ~8-second GPU “warm-up” on the very first transcription of a session — paid once, not per question — and after that, warm passes are in the range the product actually needs.

The lesson generalizes past this one bug: assuming rough parity between platforms and tuning from there would have meant chasing a 20% improvement on a path that was 100× off for a categorical reason. The gap between 25 seconds and 330 milliseconds wasn’t hiding in a config value; it was a missing backend. You only find that by measuring the real number on the real machine instead of reasoning about what should be comparable. Cross-platform parity is a hypothesis, not a default.

### 4. The answer streams from the user’s own model

Once an utterance is transcribed, the text (optionally with a screenshot image, if the user captured one for a coding problem) goes out over direct HTTPS to the user’s own LLM provider — either `api.anthropic.com/v1/ messages` or `api.openai.com/v1/chat/completions`, whichever they configured, authenticated with their API key. There is no SyntaxCue server anywhere in this path; the request goes from the user’s machine straight to Anthropic or OpenAI and nowhere else.

There’s no official Anthropic or OpenAI SDK for Rust, so these are direct HTTP calls against the documented wire formats — the response body is consumed as a byte stream, each provider’s own delta format (e.g. Anthropic’s `content_block_delta` events) is parsed as it arrives, and each extracted text fragment is forwarded to the UI immediately as its own event, rather than waiting to assemble a complete response first.

That streaming behavior is the product, not an implementation footnote. During a live call, perceived latency is what the user experiences — they’re reading or paraphrasing the suggestion out loud within seconds, so time-to-first-token is the metric that matters. A blocking call that returned a perfect, complete answer two seconds later would be a worse product than a streamed one whose first line lands in a few hundred milliseconds.

## Why a native desktop app, not a browser tab

The pipeline above couldn’t run in a browser tab, for specific reasons, not aesthetic ones.

A single window transforms in place between a full setup view and a compact hint panel — no second window, no second tab. That panel needs a global hotkey that works while the user’s focus is inside the call app (Zoom, Meet, Teams). A browser tab can’t register a truly global hotkey or react while unfocused; a native app can, and for a tool used while your attention is on the interviewer, that’s not optional.

There’s also an optional setting to keep the hint panel out of the user’s own screen-capture or recording stream, using native window-level APIs on each platform. It’s off by default and framed entirely around the user’s own screen and their own choice to share it — a browser tab has no comparable control over whether it appears in the user’s own capture stream.

## Closing

That’s the whole path: a system-audio tap (CoreAudio Process Tap on macOS, WASAPI loopback on Windows) → RMS-based segmentation → local whisper.cpp transcription (Metal / Vulkan) → a streamed response from the user’s own LLM, with no SyntaxCue server anywhere in it. The specifics — the aggregate-device wrapper, the polling loopback loop, the 0.006 silence threshold, the 25-seconds-to-330ms Vulkan fix — are the honest shape of building something that has to answer within the few seconds a live interview gives you.

# AskMe — AI Support Agent for Discord, Telegram, Slack, WhatsApp & Web Chat

## 导航

- 项目页：[[10-项目/syntaxcue.com_5b20fae9]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
