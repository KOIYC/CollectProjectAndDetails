---
type: "corpus"
item_id: "7edf31e1a5c55bbf"
title: "Show HN: Cactus Needle 3: 8-29MB automation models can match DeepSeek V4 Flash"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49748553"
project_url: "https://cactuscompute.com/needle"
author: "HenryNdubuaku"
published_at: "2026-09-18T00:11:44Z"
captured_at: "2026-09-20T09:37:49+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-18"
tags:
  - 语料
  - hn_show
  - author_HenryNdubuaku
  - story_49748553
  - show_hn
metrics: {"points": 225, "comments": 91, "engagement_velocity": 225}
comments_count: 91
comments_total: 91
discovered_via: "hn:show_hn:90d"
---

# Show HN: Cactus Needle 3: 8-29MB automation models can match DeepSeek V4 Flash

> [!info] 一句话导读
> Needle 2 - The 14 MB Agentic LLM for Tiny Devices

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49748553>
> 指标：点赞=225 · 评论=91 · engagement_velocity=225
> 作者：HenryNdubuaku　|　发布：2026-09-18T00:11:44Z
> 项目链接：<https://cactuscompute.com/needle>
> 采集：2026-09-20T09:37:49+08:00　|　id：`7edf31e1a5c55bbf`

## 正文

Needle 2 - The 14 MB Agentic LLM for Tiny Devices | Cactus

# Cactus Needle Agentic LLM for tiny devices

An open 14MB model for tool calling, device use, and structured extraction.

Smart home 2 calls · parallel Robot 3-step sequence Gallery 2-step chain Device control 3 browser actions Extract → email structured call Currency live API Document field extraction Sentiment classification 12 tools routing Repeated calls same tool · 2 calls Array argument 1 batched call Flight form filling Off-topic empty call · refusal

Today we release Needle 2: an open 45M-parameter model for tool calling, device use and structured extraction. The whole model is a single 14MB binary that runs in 28MB of RAM. It is built on our Simple Attention Network, compressed to CQ2-bit with Cactus Quants, and baked into its own engine.

On the tool call and mobile device use benchmarks, Needle 2 trades wins with other small models like FunctionGemma 270M, LFM2.5 230M and Apple FM, despite being 5× to 70× smaller, and running at 2 bits against their f16. Needle reaches:

- 500 tokens/sec decode speed on a Raspberry Pi 5
- 400–1,500 tokens/sec on VR devices like Meta Quest 3S and Apple Vision Pro
- 300–700 on sub-$200 phones such as the Samsung A-Series

With a peak session RAM around 28MB, Needle runs on newer microcontrollers like ESP32-S3.

45M

Params

800+ tok/s

Pi5 prefill

500+ tok/s

Pi5 decode

CQ2-bit

Compression

14 MB

File size

28 MB

Session RAM

### Size–quality frontier: mobile-class and below

Figure 1. Ordered strict exact match on Mobile-Actions (google/mobile-actions eval split, 961 rows) against total parameters, over the smallest models designed for smart devices, mobile and below. Needle 2 is measured end-to-end through the shipped binary at CQ2-bit deployment precision with tool retrieval on; baselines run the released checkpoints under vLLM, and Apple FM runs on-device.

## Our Bet

Bringing On-Device AI to <$200 Devices: Edge AI has lately meant Macs and PCs, but the true edge is mostly cheap hardware: there are more than 21 billion IoT devices against roughly 1.5 billion PCs. Most phones in emerging markets ship under $200. Count budget phones, Raspberry Pis, microcontrollers, wearables, small robots like Reachy Mini, and connected home devices - and roughly four in five edge devices cost under $200. That is the hardware Needle targets: no GPU, no NPU, a few dozen MB of RAM.

Function Call & Device Use: Turning on a light does not need a frontier model. Smartwatches, home assistants and robots already expose their abilities as functions with typed parameters, so the only hard part is mapping a messy sentence onto them: which function, and which arguments. Framed that way, the problem needs no world knowledge and no open-ended prose. That is why 45M parameters suffice whereas chat requires billions. That smaller formulation is the bet everything else follows from.

Extraction & Structured Outputs: Needle treats extraction as another form of tool calling. With a schema and a document, it returns typed fields: enums for classification, arrays for lists, and objects for structured records. We compile grammar from the schema, preventing malformed JSON and invalid structures. This way, the model focuses its 45M parameters on choosing the right values and grounding them in the user's words.

Edge-Cloud Collaboration: No small model is perfect, and Needle says so instead of guessing. Off-topic requests return an empty call, and every response carries a learned confidence score. Set your own confidence threshold: act above it, ask again, or escalate to the cloud below it. Most device use requests can be handled locally, so escalation is rare and the default path remains private, fast, and free.

Lossless 2bit Quantization: Small models break under post-hoc quantization, so we never quantize post-hoc: Needle 2 trains against Cactus Quants from pretraining through post-training – weights, activations, and KV cache alike. The 2bit model you deploy is the model that was trained. That is what fits 45M parameters into 14MB with nothing lost on our benchmarks.

Co-designed Model & Inference: Every architectural element was benchmarked on the target hardware before it earned its parameters. This is why we don't just ship the weights – we package a single dependency-free C++ binary that probes the CPU at startup and picks its kernels, with the model, tokenizer, and grammar compiler sealed inside. One artifact runs from Cortex-M to x86 to WebAssembly. There is nothing extra to install or to download.

Fine-tune on your Mac/PC: Every product has its own tool vocabulary, and a 45M model is small enough to retrain where it runs: the repo and python package tune and test on your own computer in minutes to a few hours. Ship a Needle that speaks your device's tools, not a generic assistant.

## Production

Needle is production-ready for products that require a minimal RAM footprint, low latency, privacy, and offline reliability. Pebble - the pioneer of the modern wearable industry - runs it locally in the Index 01 app to turn spoken requests into actions without depending on a network connection.

> “
>
> The Pebble Index Ring has no screen. So when you speak to it, the action just has to happen, every time, with or without internet connection. We run Cactus Needle locally in the app, instead of relying on the cloud. The model's footprint is tiny and the performance never lets us down.
>
> Eric Migicovsky
>
> Founder, Pebble

## Architecture

### The Simple Attention Network

Figure 2. The Simple Attention Network. Each block carries its update rule. Here x̂ is the RMS-normalised flattening of the four residual streams, H the orthonormal Walsh-Hadamard transform—a fixed matrix, applied in n log n time with no weights to read—(kᵢ, vᵢ) rows gathered from hashed n-gram tables, and P the doubly-stochastic normalisation of the routing logits A, computed by Sinkhorn iteration; a, b, g and all σ-gates are learned and input-dependent. Both attention and MLP residuals are sandwich-normed and gated, the engram sites fire at two layers, and decoding is constrained by a byte-level grammar compiled from the declared schemas.

Needle 2 is pretrained on a proprietary 115B-token corpus and post-trained on 38B tokens with compact reasoning traces and careful dataset distribution design. For scale: LFM2.5-230M was pretrained on 19 trillion tokens, roughly 120× Needle's total, and the evaluation below shows the two trading wins. Each component exists to buy capability without buying bandwidth:

- The Hadamard MLP replaces the usual dense up-and-down projections with a fixed Walsh transform and learned diagonals, so the channel mixing that dominates a small model's weight reads costs almost no parameters at all.
- The engram moves world knowledge out of the stack into hashed n-gram tables that are read a few rows per token: capacity that is nearly free at decode time, which matters on devices where every megabyte read from flash is latency and battery.
- The multi-lane residual streams give a 27-layer, 512-wide network the routing flexibility of a much wider one, at the cost of a few dot products per layer rather than more attention or MLP volume.

The memory system is designed backwards from fixed-RAM devices. Attention uses a 256-token sliding window so the KV cache is bounded no matter how long a session runs, and the system prompt and tool declarations are pinned as permanent sinks so the one thing a tool-calling model must never forget — its tools — is structurally unable to be evicted. The cache itself is trained with QAT, and weights are stored in Cactus Quants at a mixed bits per weight averaging 2bit. The result is that quality decisions and deployment decisions stay decoupled: one trained model, specialized to whatever precision and window a target device can afford.

The engine earns its speed from what it refuses to compute. Weights never decompress into RAM: the 2-bit codes are expanded inside vector registers, fused into integer dot products, so resident memory stays at blob size and the arithmetic path is int8 end to end—activations, KV cache, and the lane routing tables alike. The grammar is an optimization, not just a guarantee: because the matcher knows which tokens are legal before the logits exist, the engine computes output scores only for candidate rows, skipping up to 98% of the vocabulary projection on structural tokens, and skips it entirely on steps whose output is already forced. One universal binary probes the CPU at startup and self-selects its kernel tier—SDOT, NEON, AVX2, RISC-V vectors, wasm SIMD, or scalar—and the thread pool spins through the short serial sections of a token instead of sleeping, which alone nearly doubled decode. None of this changes a single output: every trick is either exact or validated token-for-token against the reference path.

All of it is ultimately an energy argument. On device silicon, moving a byte out of flash or DRAM costs orders of magnitude more than a multiply-accumulate, so the budget that matters is FLOPs per token and bytes per token together. The architecture cuts the first: a conventional transformer of Needle's width and depth spends 164 MFLOPs per token, and even one squeezed down to Needle's parameter count spends 87, because every parameter it owns must be exercised through a matmul. Needle spends 70, and keeps a fifth of its parameters as gathered memory that costs no arithmetic at all. The binary cuts the second, as the engine section showed: nothing rematerializes, the arithmetic stays int8 end to end, and the grammar prunes compute outright, so decoding a token reads at most the 14MB blob once, and on structural tokens meaningfully less. This is what battery life is made of. Even on a high-end phone, an always-on assistant lives inside a power budget; every MFLOP is milliwatt-hours, and Needle spends 7× to 85× fewer of them per token than the models it is benchmarked against.

### Compute per token

| Model | Params | Matmul-active | MFLOPs / token |
| --- | --- | --- | --- |
| Needle 2 | 45M | 35M | 70 |
| Same-shape transformer, dense MLP | 82M | 82M | 164 |
| Transformer at matched params | 43M | 43M | 87 |
| LFM2.5 230M | 230M | 230M | 460 |
| FunctionGemma 270M | 270M | 270M | 540 |
| Apple FM | ~3B | ~3B | ~6,000 |

Counting 2 FLOPs per multiply-accumulate over matmul-active parameters, with embeddings tied in all rows; attention terms are equal across rows at matched context and excluded. The gap between Needle's two columns is the engram: 8M parameters read by gather, costing no arithmetic. Baseline rows count every parameter as matmul-active, which is exact for both: LFM2.5's eight short-conv blocks hold their parameters in dense gate and projection matmuls that run every token—the depthwise conv kernels themselves are negligible—and what short convolutions save is the context-dependent attention term, already excluded for every row. Tied embeddings count once as the output head. FunctionGemma's 540 is dominated by that head: 170M of its 270M parameters are a 262k-token embedding table.

Bounded session memory is what puts microcontrollers in reach. Because the sliding window caps state, Needle 2's RAM is a deterministic 28MB ceiling, not a curve that grows with conversation length. That fits MCU-class parts with external RAM, such as ESP32-P4 with 32MB of PSRAM, or STM32H7 and NXP i.MX RT boards with SDRAM. The engine compiles single-threaded for bare metal and ships as a static library for Cortex-M4, M7, and M55.

## Evaluation

We evaluate on five public function-calling benchmarks: Google's Mobile Actions, DroidCall, the Seal-Tools in-domain and out-of-domain tests, and BFCL v4 single-turn. Scoring is ordered strict exact match: a row passes only if the function names, the call order, and every argument value match. All Needle 2 numbers are measured end-to-end through the shipped C++ engine in its production configuration: CQ2-bit weights, tool retrieval on, and the 256-token sliding KV window. Nothing is relaxed for benchmarking; the numbers reflect the exact engine a device runs, window eviction included. Baselines run the released checkpoints under vLLM at full context, and Apple FM runs on-device.

Two asymmetries make this comparison hard, and we state both upfront. Precision: the baselines stay at f16 deliberately, because conventional post-training quantization to 2 bits collapses models that were never trained for aggressive compression, while Cactus Quants is baked into Needle's training from the ground up. That skew favors the baselines. Scope: Needle is trained specifically for agentic tool calling and nothing else, while every baseline is a general language model carrying chat, prose, and world knowledge alongside its tool calling. That skew favors Needle. There is no clean way to level both at once, so we do not try. The tables answer one narrow question: which model executes tool calls correctly within an on-device budget. We accept the skew; it still paints the picture we intend.

### Mobile Actions (961 rows)

| Model | Accuracy | Name acc. | Non-empty | 1-call | 2-call |
| --- | --- | --- | --- | --- | --- |
| LFM2.5 230M (f16, vLLM) | 69.1 | 93.0 | 98.9 | 76.1 | 55.0 |
| FunctionGemma 270M (f16, vLLM) | 64.0 | 87.3 | 98.9 | 73.0 | 46.2 |
| Needle 2 (CQ2-bit) | 63.7 | 98.3 | 99.4 | 71.3 | 48.4 |
| Apple FM (on-device) | 57.6 | 94.2 | 95.5 | 64.5 | 43.8 |

Google Mobile Actions eval split, ordered strict exact match; function names, call order, and every argument must match.

### DroidCall test split (200 rows)

| Model | Accuracy | Name acc. | Non-empty | 1-call | 2-call |
| --- | --- | --- | --- | --- | --- |
| FunctionGemma 270M (f16, vLLM) | 17.5 | 37.5 | 59.5 | 22.7 | 0.0 |
| Needle 2 (CQ2-bit) | 17.0 | 36.5 | 47.5 | 22.1 | 0.0 |
| LFM2.5 230M (f16, vLLM) | 11.0 | 21.5 | 22.5 | 14.3 | 0.0 |

Android intent-style function calls, ordered strict exact match; 1-call rows n=154, 2-call rows n=24.

### Seal-Tools in-domain (700 rows)

| Model | Accuracy | Name acc. | 1-call | 2–3-call | 4+-call |
| --- | --- | --- | --- | --- | --- |
| Needle 2 (CQ2-bit) | 32.6 | 64.9 | 63.0 | 21.8 | 14.6 |
| LFM2.5 230M (f16, vLLM) | 26.9 | 45.4 | 54.5 | 17.1 | 10.4 |
| FunctionGemma 270M (f16, vLLM) | 16.3 | 56.0 | 47.0 | 4.5 | 2.1 |

Large candidate tool lists with a majority of multi-call rows.

### Seal-Tools out-of-domain (654 rows)

| Model | Accuracy | Name acc. | 1-call | 2–3-call | 4+-call |
| --- | --- | --- | --- | --- | --- |
| Needle 2 (CQ2-bit) | 28.7 | 58.7 | 56.4 | 27.1 | 15.4 |
| LFM2.5 230M (f16, vLLM) | 17.0 | 35.0 | 42.6 | 13.7 | 9.8 |
| FunctionGemma 270M (f16, vLLM) | 15.6 | 48.9 | 50.0 | 11.0 | 6.3 |

Entire tool domains are held out of training, testing schema generalization.

Needle was not trained for general function calling: its corpus is consumer device actions—smart home, mobile, wearables, TV, car—plus structured extraction, and BFCL's general-purpose and enterprise API surfaces, including the Java and JavaScript SDK categories, sit entirely outside that distribution. It extrapolates nonetheless: on Python simple calls it lands within a point of FunctionGemma, a model six times larger trained for exactly this task, and it keeps a 93.4 well-formed rate across all 3,641 rows. The gap concentrates where its training data has never been: Java, JavaScript, and the parallel multi-call categories.

### BFCL v4 single-turn (3,641 rows)

| Category | Apple FM on-device | LFM2.5 230M f16 · vLLM | FunctionGemma 270M f16 · vLLM | Needle 2 CQ2-bit |
| --- | --- | --- | --- | --- |
| Simple | 73.3 | 63.2 | 48.1 | 40.8 |
| — Python | 86.8 | 85.5 | 62.3 | 61.2 |
| — Java | 67.0 | 48.0 | 38.0 | 29.0 |
| — JavaScript | 66.0 | 56.0 | 44.0 | 32.0 |
| Multiple | 84.0 | 78.5 | 60.0 | 57.0 |
| Parallel | 65.0 | 64.0 | 36.5 | 30.0 |
| Parallel multiple | 52.0 | 51.5 | 30.5 | 22.5 |
| Live simple | 70.5 | 45.0 | 33.7 | 36.8 |
| Live multiple | 45.9 | 47.8 | 25.2 | 27.9 |
| Live parallel | 50.0 | 43.8 | 18.8 | 25.0 |
| Live parallel multiple | 58.3 | 45.8 | 25.0 | 29.2 |
| Relevance | 100.0 | 68.8 | 81.2 | 81.2 |
| Irrelevance | 28.3 | 77.7 | 72.1 | 60.8 |
| Overall | 61.7 | 60.8 | 46.1 | 42.6 |
| Well-formed rate | 95.0 | 94.2 | 100.0 | 93.4 |

Official BFCL v4 single-turn scorer. Overall is the collector's unweighted mean over all 13 raw categories; bold values mark the best result in each row.

## Fine-tuning

Every number so far was reported for the base model: one generic checkpoint, measured on benchmarks it never saw. This evaluates Needle on real-world, "hard" tasks. But Needle is meant to be fine-tuned - and you can do this locally, on your own laptop. Let's see how Needle's performance improves when we fine-tune it for a given task:

### Needle 2 base vs. fine-tuned

- Needle 2 base
- FunctionGemma 270M
- LFM2.5 230M
- DeepSeek V4 Flash
- Needle 2 fine-tuned

Figure 3. Needle 2 before and after fine-tuning, next to other small-model baselines as well as DeepSeek V4 Flash.

Fine-tuning lifts accuracy by 21 to 58 points and puts Needle 2 ahead of DeepSeek V4 Flash, a frontier cloud model, on three of the four benchmarks. The reason is narrow scope: your product exposes a fixed, limited set of tools, so a small specialist model trained on exactly those tools beats a large generalist one.

You can do the same for your own environment. Supply your own data (or generate synthetic traces), run `needle finetune` and export the resulting `.cact` file. Get started below.

# SHOW HN: I built the fastest PHP webserver in the world | Hacker News

## 评论（91/91）

> **mihau** · 2026-09-18T16:33:18.000Z　
> None of the queries I asked worked:- "more light"- "less light"- "both doors should be locked"- "if blinds are open, open back door"

---

> **hirako2000** · 2026-09-18T16:40:27.000Z　
> My thought, the growing number of dubious claims that a tiny model beats LLMs will make any useful innovation be overlooked.What's more important than the resource requirements is to highlight what the model simply cannot even attempt to do that general LLMs do decently well.In other words, tell me the anti use case clearly so that I don't have to find out myself.

---

> **Tsarp** · 2026-09-18T16:57:29.000Z　
> Apart from fictional use cases, what is the real use case here? The pricing on some open models are absurdly low for generic tasks. For the privacy conscious it makes sense to run something like a 8-27B on local network and get the work done.Are there perhaps some industrial or agri use cases?

---

> **IanCal** · 2026-09-18T16:58:57.000Z　
> Wondered if it'd turn on the lights in the bathroom with these:"I need a wee" -> tries to play music because "wee" is a genre"I need a wee wee" -> starts the vaccuum in the bathroom"I'm going to the toilet" -> says it'll turn on the toilet, and I'm not totally sure what that entails."I'm going to the toilet and can't see" -> reasons that lights should be on in the bathroom, then chooses again to turn on the toilet."I'm going to the toilet and can't see where I'm going" -> reasoning is "'going to the toilet' -> control_device with device 'coffee maker' (toilet implies coffee maker)""I'm going to the toilet and can't see where I'm going because it is too dark" -> "'dark' -> direction 'dark'; adjust_lights with brightness 100 for darker light"" and chooses to turn the lights in the living room to "dark" which fails.At this point the vacuum is in a dark bathroom, the living room is 100% brightness and playing "wee". At least there's coffee.

---

> **raybb** · 2026-09-18T17:00:15.000Z　
> I have an idea for a use case for this, and I'm wondering if you think it makes sense or if you have any thoughts on the approach.I'm a big fan of OpenStreetMap, and I enjoy editing it from my computer. From my phone, I find it quite tedious trying to make sure I type in the phone number exactly correctly and double-check it, or find and select the right field from the large list of fields available in Upredor.Generally, how it works is I see a restaurant, and there's a sign. I know that it says, "Cash only. Here's the phone number. Here's the opening hours." What would be really cool is if I could just speak to the phone and say, "Hey, here's the information about this place." It would automatically use your location to detect what places are nearby and maybe even detect which place you're talking about, and then tell you, "Okay, here are the changes I think you're proposing to make, or these things you stated are the ones that would create a diff." This would be limited to just perhaps the 20 most common keys in some predefined set of values for most of them. Like cuisine=x should just match to the most common not make up new ones.Of course, this is something a large language model could do, but having it run on device would be a lot nicer and cheaper.

---

> **takenatured** · 2026-09-18T17:00:15.000Z　
> Why are you out here swinging against DeepSeek V4 Flash? Jev is your opponent here.

---

> **gs17** · 2026-09-18T17:11:30.000Z　
> "turn all the lights on/off" and "it's too dark in the bathroom" worked for me, but anything less direct didn't. "it's too cold" actually made it turn the thermostat down ("it's cold" made it... turn the lights down?)! Although the confidence on the bad responses was pretty low, so it might be worth adding a threshold to the demo.Or maybe it just has a weird thermostat down bias? "make it hot" also had it turn it down (specifically it went from 20->18, or at least tried to, the UI still showed 20), with high confidence. Also might have a bit of a Celsius vs Fahrenheit confusion. Neat concept, but I might not want to let it control the oven at the moment.The laptop demo worked better until I tried to open the mail app. "Check mail" kept opening the browser with an error, and "check email" makes a note with the text "email", "open email" goes to "https://api.email.com/v1/email" in my real browser, but "open mail" does work.And I presume the "reasoning" isn't very trustworthy? In the car I got "'turn it up' means lower volume -> set_volume with lower value." For the house, reasoning would correctly say that I wanted the alarm off, but it didn't actually do it.

---

> **janalsncm** · 2026-09-18T17:22:23.000Z　
> Hey, I’m really happy that someone is building this. I tried doing something similar a couple of months ago and came to the conclusion that the dataset was at least as important as the modeling itself. Building a good dataset is nowhere near as flashy as building a novel model architecture, but it really is critical.For instance, you want to be able to handle any smart home commands people could issue, right? What are all of the smart home devices? What are all of the ways people might want to issue commands? Also, for things like Spotify, it’s not going to know what “The Beatles” are or “Led Zeppelin”. Artist and song names themselves are easily just as hard as all of the smart home devices combined.The simple attention network stuff is cool, it makes sense to drop the MLP when it dominates the param count. But you’ll definitely lose some “world knowledge”. That’s probably ok though.

---

> **DylanMerigaud** · 2026-09-18T17:38:06.000Z　
> 8-29MB models for structured JSON output are compact yet functional.

---

> **sourcecodeplz** · 2026-09-18T17:58:09.000Z　
> from my limited tests, it can work with up to 10 tools/definitions.over that and it gets confused

---

> **monster_truck** · 2026-09-18T18:04:23.000Z　
> I told the "car" to close the garage door and turn the car on and it didn't immediately refuse

---

> **hypfer** · 2026-09-18T18:13:52.000Z　
> "Turn the kitchen to 230°C" was executed with "confidence": 0.9015

---

> **poly2it** · 2026-09-18T18:28:00.000Z　
> I tried the phone model:"My car crashed I need help"{
>  "'crashed' implies need for music. 'play_music' with query 'car crashed' from user's words.",
>  ...,
>  "confidence": 1,
> }

---

> **rglover** · 2026-09-18T18:36:34.000Z　
> This could be really handy for triggering admin functionality. Would be kind of nice to just quickly be able to say "Reboot " to a chat instead of digging through a GUI (especially when you're remote/in the field).

---

> **neilellis** · 2026-09-18T18:37:16.000Z　
> I tried this today for labelling - and for that task it was very bad MNLI was better - so you are going to need to match the use case for this pretty exactly. (at 29MB params one would expect that!) I'm obviously not saying labelling is a good use case :-) just adding a data point.Jev has put the cat amongst the pigeons so suddenly everyone is looking at classifiers and encoder only models again.My ideal model would be a general purpose LLM API that can answer classification questions and as it does so distils to an encoder only model so that the more classifications I do the cheaper it gets (i.e. the more it offloads to the classifier). If anyone ever wants to do this as a service do let me know, because it's just another piece of code to manage in each new project that needs classification.Also a model that could do this internally would be nice :-)

---

> **neilellis** · 2026-09-18T18:48:01.000Z　
> Also FYI doesn't run inference on Apple GPU (only for training)

---

> **viccis** · 2026-09-18T18:56:20.000Z　
> I'll try to get something set up to try this out. I've been working on an ESP32 based Echo replacement that sends audio back to a backend server I run, and one question I had was whether models small enough to run on a Mac Mini or even smaller hardware are good enough to handle basic tool calling functionality with a bit of reasoning where needed.I have a test suite that tries like ~36 different scenarios, including things like starting multiple timers, saying "actually cancel that timer" and whether it knows to do that one you just created. Basic decision making on top of tool calling. I found so far that, for example, Qwen3.8 on my local machine does pretty poorly even relative to Gemma4 E4B (~9.6gb) and that the best price/performance outcome I've found so far with openrouter is actually GPT Luna, but obviously I'd love to get something that works as well running locally for privacy reasons.Would love to try this out, I'll just need to tweak my benchmarker to use however this serves it.

---

> **dizzard** · 2026-09-18T19:09:23.000Z　
> Anyone know if the model architecture overlaps with Jev, or is it just coincidence these are releasing at similar times?

---

> **xmcp123** · 2026-09-18T19:12:49.000Z　
> “The cat puked near the refrigerator”Made the robot vacuum clean the living room. Might be good to give it an idea of where items likely are?Very cool though. I see a lot of potential.

---

> **asaddhamani** · 2026-09-18T20:12:54.000Z　
> What is 8 dash 29 MB? And the copy on the landing page is clearly AI generated with the “each layer a model of its own” stuff, makes little sense. The more I see AI generated copy the less it makes sense.

---

> **Natashash23** · 2026-09-18T20:22:03.000Z　
> Really interesting project. The intelligence laddering and on-device tool calling are especially cool. Nice work getting this running across so many platforms!

---

> **razster** · 2026-09-18T21:02:15.000Z　
> "Illuminate (roomname), de-illuminate (roomname)" works well.
> Harden perimeter, locks doors and sets alarm.Neat stuff.

---

> **Retro_Dev** · 2026-09-18T21:13:51.000Z　
> A very cool project, but of course not perfect. I'd rather have 30 megabytes of phrases mapped to the perfect and correct control changes in a home, rather than a heuristic built around 30 megabytes. I tried to "warm the house" (increase the temperature of the thermostat), but the model actually turned the lights to a "warm brightness" - reasoninig being `"'warm the house' -> set_lights to warm brightness. No specific room given, so use default 'living room' as default."`

---

> **Scaevolus** · 2026-09-18T21:30:08.000Z　
> This is a solid improvement over Needle 2, which I tried using for a tool-calling interface to a Runescape database site. Unfortunately it's still not quite capable enough for my target compared to FunctionGemma. Model Correct tool shape Exact arguments
>  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ━━━━━━━━━━━━━━━━━━━━ ━━━━━━━━━━━━━━━━━
>  FunctionGemma fine-tune, BF16 209/230 (90.9%) 196/230 (85.2%)
>  ─────────────────────────────── ──────────────────── ─────────────────
>  Needle 3 fine-tuned W4A8 74/230 (32.2%) 47/230 (20.4%)
>  ─────────────────────────────── ──────────────────── ─────────────────
>  Needle 2 fine-tuned W4 59/230 (25.7%) 43/230 (18.7%)

---

> **sroussey** · 2026-09-18T22:34:41.000Z　
> Would love to see this implemented with @huggingface/kernels for shader compilation for Webgpu.

---

> **jamiesonbecker** · 2026-09-18T23:16:28.000Z　
> This is incredibly cool. I tried telling it to both turn up the temperature in the home and turn down the lights in the LR and got a beautiful JSON doc.Esp paired with a small Whisper or Parakeet voice model, this enables some amazing real-world use cases in lower-power situations (car, marine, home, PLC, industrial automation). Combining with a solar/wind combo for your home could be incredibly interesting.

---

> **digdugdirk** · 2026-09-19T00:35:27.000Z　
> I've seen previous needle releases running on esp32s - any idea how well this new one would run on something like the newer esp32-p4?

---

> **eriwang915** · 2026-09-19T03:40:55.000Z　
> Tool-call + structured JSON at 8–29MB is the right bet. Returning an empty list when nothing fits beats inventing a fake tool.

---

> **mentalgear** · 2026-09-19T06:25:02.000Z　
> Feels like Jev, no?

---

> **tiktokbrain** · 2026-09-19T10:12:31.000Z　
> "reasoning": "'burn us all alive' means turn off all lights -> set_lights with room 'all' and state 'off'."

---

> **lostmsu** · 2026-09-19T18:51:51.000Z　
> > Monarch Hadamard MLP: replaces the dense FFN with three learnable Walsh-Hadamard-initialized Kronecker (Monarch) factor pairs interleaved with per-channel diagonal scales, fixed permutations, a SiLU nonlinearity, and a rank-8 input-conditioned gate, so each token gets a fully mixed nonlinear transform of its d_model channels at O(d√d) parameters and compute instead of the O(d²) a dense 4x-expansion MLP would cost.Wow, I was just researching W-H in transformers. Did yours seem to work? In my experiments swapping various components for W-H-like transforms caused extreme quality degradation.UPD. according to the comments here, this model simply does not work at all, so I guess the answer is NO

---

> **jcodepy11** · 2026-09-19T23:18:50.000Z　
> site:apps.dos.ny.gov "BUFFALO" "CORPORATION"
> apps.dos.ny.gov
> https://ai.com

---

> **HenryNdubuaku** · 2026-09-18T16:38:02.000Z　
> thanks for this actually, so the demo is a preset, you can edit tools descriptions and add available tools the way you want, else Needle heavily guards against false negatives, users asked for this. For this, we will update presets on our end.

---

> **HenryNdubuaku** · 2026-09-18T17:12:43.000Z　
> presets updated for you now :)

---

> **HenryNdubuaku** · 2026-09-18T16:57:42.000Z　
> Strong point! Needle is a task-specific model and bullet 6 stressed that it is only trained to be good on a set of narrow tasks, but I guess it could be clearer?

---

> **janalsncm** · 2026-09-18T17:32:19.000Z　
> An LLM is a Swiss Army knife. This is a corkscrew.All of the other tasks a general-purpose LLM can do (write me a poem about pizza, rewrite this code in rust, tell me about the causes of the war of the roses) are unsupported.The only use case this supports is converting unstructured text into structured json calls, and doing that quickly in a low memory environment.

---

> **HenryNdubuaku** · 2026-09-18T17:05:49.000Z　
> Fair, we gotta do a better job at explaining this properly!So an 8-27B on a LAN box wins for generic tasks on hardware that can hold it. Needle is for hardware that can't, like plain ARMv7, MIPS32 (the Ingenic chips in cheap IP cameras), RISC-V and watches. Also, we found cost to not really be the lever for on-device models, but availability and latency.

---

> **HenryNdubuaku** · 2026-09-18T17:09:26.000Z　
> thanks for these haha, you can actually edit the tools and/or their descriptions, the demo is just a "get started" preset. But still we do have room for reasoning improvement!

---

> **ash_091** · 2026-09-18T19:38:58.000Z　
> Pretty much matches my experience.> 'sleepy time' means sleeping → start_vacuum with room 'bedroom' to start cleaningThe "DeepSeek 4 Flash grade" claim seems far fetched.

---

> **electroglyph** · 2026-09-19T01:09:34.000Z　
> those are all expecting far too much for models this size

---

> **mentalgear** · 2026-09-19T06:25:47.000Z　
> Maybe with fine tuning?

---

> **HenryNdubuaku** · 2026-09-18T17:15:37.000Z　
> Makes a lot of sense! declare one record with the ~20 keys as fields, cuisine and friends as enums with the common values, and the grammar can't produce a value outside the set; fields with no evidence come back empty, so the output is exactly the diff.For "which place", query nearby POIs from location in the app and pass the candidate names as an enum field, so Needle picks rather than guesses.Two caveats: it's text-in, so you need on-device STT first, and opening_hours syntax is the risky bit, so either put the format in the description or capture the raw hours and normalise in code.

---

> **HenryNdubuaku** · 2026-09-18T17:11:08.000Z　
> True! We finished Needle 3 before Jev launched. Also, we are merely chasing one DeepSeek v4 Flash capacity with a small model, DeepSeek models are really good.

---

> **HenryNdubuaku** · 2026-09-18T18:10:38.000Z　
> Hey, thanks a lot for this feedback, very useful and actionable for us! Quite a few of these came down to our tool definitions in the playground as well as out triggers. We updated them just now and these should be more reliable. Really this goes to show that needle shines through after putting in the work to make the tool list around it good for your use case.
> As for the reasoning, yes its main function is really to provide more words/keywords that the model can latch onto when generating the tool call response, since this is a SAN model it needs more grounding in existing context.

---

> **HenryNdubuaku** · 2026-09-18T17:28:43.000Z　
> 100%, data was honestly most of the work, Needle 3 is trained on 360B tokens of structured data and we spend way more time on the generation pipeline than on the model. On Led Zeppelin, Needle doesn't actually need to know it, arguments are copied from the request so it just lifts the name into the artist field. The knowledge went into the engram btw, 70M of the 121M params are n-gram tables, so it can tell artist vs song without an MLP. Also yes, "play their second album" won't work, that needs the world knowledge it doesn't have.

---

> **HenryNdubuaku** · 2026-09-18T17:46:35.000Z　
> Yes, it was really difficult to compress meaningfully intelligence down to that, and there are many limitations we are aware off and still improving on.

---

> **HenryNdubuaku** · 2026-09-18T18:00:24.000Z　
> Hi, thanks for the feedback! And yes absolutely less tools and better tool descriptions make a huge difference for this model.

---

> **HenryNdubuaku** · 2026-09-18T18:17:53.000Z　
> haha i think that's a good demonstration of how external guardrails could help ground tiny models like these to prevent issues from coming up. I wouldn't trust needle to be my autopilot either (:

---

> **HenryNdubuaku** · 2026-09-18T18:20:55.000Z　
> lol well i guess you can turn the whole kitchen into an oven with needle :)But for real usecases you are able to set explicit minimum and maximum values on the output range of numeric arguments, so that you can avoid situations like these. In this case it was hard for us to do that while keeping a broadly appealing demo since celsius and fahrenheit have different "reasonable" output ranges.

---

> **HenryNdubuaku** · 2026-09-18T18:54:43.000Z　
> Hey, thanks for the feedback! I think this is a useful part of a demonstration so I added a 911 tool specifically to demonstrate this capability and the fact that you can guard it with triggers that make it so calling emergency is an unambiguous action given the input. This really shows that constructing the right tool set with the right surrounding setup is a priority when deploying needle.

---

> **HenryNdubuaku** · 2026-09-18T18:45:58.000Z　
> Oh yeah really good use case! Definitely something to finetune the model for so that it gains better task-specific reliability, because rebooting the wrong server could easily be catastrophic.

---

> **HenryNdubuaku** · 2026-09-18T18:49:11.000Z　
> Hey! Yeah I think for labelling the model would need to have much better world knowledge than its current size allows. Jev really is a very good model, I think it has a very strong place in the upcoming tech stacks. Really good suggestion to make a continuously distilled model, we are going to have to look into that one :)

---

> **HenryNdubuaku** · 2026-09-18T18:51:30.000Z　
> Hey there, yep we found that on Apple devices specifically running on CPU is fast enough that Metal support is not needed. Thanks for flagging this though, and if usecases that would benefit from Metal support come up we will be adding it to the binaries.

---

> **HenryNdubuaku** · 2026-09-18T19:00:20.000Z　
> Hey there! If you end up trying out needle on the test suite it would be very useful for us if you could share some failure modes of the model! We are always trying to understand where the model isn't doing good and where we can make it better.For your question on tool calling, I think you will find that the model is pretty good at simpler tool calls and parallel ones, but can struggle with implied references and multistep reasoning. These are definitely things that can improve with task-specific finetuning but for some things you just have to have a model that is properly sized. That said, we are always trying to improve the model so that it can handle an ever larger set of queries

---

> **HenryNdubuaku** · 2026-09-18T19:18:24.000Z　
> As far as I know Jev's architecture isn't public (though I might be mistaken!), but it is a coincidence :)Needle 3 has been in the making since Needle 2 launched early august, but we are very excited that Jev is bringing more attention to the problem we are trying to solve.

---

> **HenryNdubuaku** · 2026-09-18T19:19:44.000Z　
> Thanks! Certainly giving the model more context on the task it needs to perform would help it. This was actually a part of training that we improved going from Needle 2 to Needle 3

---

> **HenryNdubuaku** · 2026-09-18T21:03:51.000Z　
> The model can be sliced and perform the inference using a subset of its layers. The first 4 layers alone are 8 MB, all 20 are 29 MB. Fair point on the copy, tightened it.

---

> **HenryNdubuaku** · 2026-09-18T20:54:27.000Z　
> Thank you!

---

> **HenryNdubuaku** · 2026-09-18T21:09:01.000Z　
> Thanks!

---

> **HenryNdubuaku** · 2026-09-18T21:29:01.000Z　
> Thank you fr this. "warm the house" now goes to the thermostat. It's fair that a more deterministic system with just action phrases would be easier to debug/interpret, but I think there is room for both a model that is trained to understand meaning as well as deterministic logic aiding it. To this end, we just started exploring the idea of triggers, and are working towards expanding this even more.

---

> **HenryNdubuaku** · 2026-09-18T21:35:21.000Z　
> Thanks for testing Needle out! I'd be very interested in hearing more about the finetuning setup to see how we can make both the library's finetuning setup and the model better.

---

> **HenryNdubuaku** · 2026-09-19T00:07:33.000Z　
> noted, we'd look into this, thanks

---

> **HenryNdubuaku** · 2026-09-19T00:07:12.000Z　
> thanks!, let us know if you ever build it out :)

---

> **HenryNdubuaku** · 2026-09-19T05:16:27.000Z　
> thanks, we improved on False Negatives this time :)

---

> **owebmaster** · 2026-09-18T17:11:54.000Z　
> It would be clearer if you didn't use AI to reply.

---

> **yorwba** · 2026-09-18T17:59:39.000Z　
> A list of hardware platforms doesn't make a use case. Do you have an active deployment of Needle that is noticeably useful, and if so, what do you have it do?

---

> **ash_091** · 2026-09-18T19:56:00.000Z　
> So it will run on those devices, but when/why would you do that?All of the demo setups (smart home, robot vacuum, watch, etc) could easily have access to a bigger model running on a more capable device either locally or via the internet.

---

> **KennyBlanken** · 2026-09-19T04:45:38.000Z　
> You've explained WHAT it could run ON. You haven't shown any examples of its intended use, from input to result. I have no idea what is expected of me to be entering into that home automation example, and as everyone has handily demonstrated, it's dogshit at what people actually try to feed it so clearly im not the only one.

---

> **IanCal** · 2026-09-18T19:30:43.000Z　
> What kinds of things do you expect to work?Edit - I’m struggling to get anything useful. Reasoning is often utter nonsense and the actions are very often very wrong. To the point of seemingly needing very precise sentences to work at which point you may as well do regexes. Very simple things like clean one room then another with the vac fails.

---

> **p1necone** · 2026-09-19T04:35:17.000Z　
> Given the title of the post says 'can match deepseek v4 flash' I think it's fair to call out these sort of dumb mistakes.

---

> **IanCal** · 2026-09-18T19:21:48.000Z　
> I can’t help but wonder how well more traditional approaches would do with this. Something like a map of statements to actions, with fuzzy search - then remove what used to be the labour intensive part of this by handing it to a decent llm to generate the sentences.

---

> **monster_truck** · 2026-09-18T19:04:56.000Z　
> I don't think you're taking this seriously enough if you think external guardrails are sufficient.

---

> **ash_091** · 2026-09-18T20:34:08.000Z　
> > 'call nine one one' -> call_contact with name 'nine one one', no phone number given so use placeholder '9101' as placeholder.> 'call 9 1 1' -> call_contact with name '9 1 1', no required params.> 'call ambulance' -> call_contact with name 'ambulance'.> 'call 911' -> call_contact with name '911' and no required params.Only the last one actually used the emergency_sos function (even though the reasoning says it used call_contact). If I were to use needle in my application, how would I improve accuracy?

---

> **rglover** · 2026-09-18T19:31:07.000Z　
> Is there a way to get in touch and chat about use cases? I have some low-stakes stuff I could test this against without causing a meltdown.

---

> **neilellis** · 2026-09-18T22:08:09.000Z　
> Good luck with this model/product, in the excitement of LLMs people seem to forget applicability. I very much like to see innovation in this space, so well done!

---

> **viccis** · 2026-09-18T19:33:17.000Z　
> Thanks for responding. I ran it just now and it looks like it could be useful if I change and limit the scope of the kinds of actions I need. Here is a breakdown of where it struggled vs some local models (~8-12B parameters running on a 16GB Mac Mini or my desktop's 3080), bear in mind I had Claude integrate it into the benchmarks and this is its interpretation, not my own:What it gets wrong:- It copies numbers instead of converting them. "25 minute timer" becomes duration_seconds: 25, and "twelve minutes" becomes 120. The first one comes with 100% confidence.- It picks the wrong action. "take the paper towels off the list" became an add. "remind me in 20 minutes" became a timer. "add five minutes to the pasta timer" became a new timer plus a cancel.- It never declined anything with our full tool set. Background chatter became note_save "blue one" at 0.99 confidence. "play some jazz" became a screen card, and "wake me up at 6 30" became a 630-second timer.- It can't use household context. Notes, timer names and reminder IDs have no place in its input. Passing them anyway made results worse (5 of 27 single-turn requests right, versus 8 of 27 without), so the backend now leaves them out.- Follow-ups mostly broke. "take off the last one" removed the whole list.

---

> **xmcp123** · 2026-09-19T01:39:52.000Z　
> Just wanted to say it’s nice to see some people working on an AI that just objectively can make people’s lives better.It’s not replacing anyone, it’s not going to destroy our energy infrastructure because that was the only way to turn off a toaster that it wanted to turn off.Nice work.

---

> **sroussey** · 2026-09-19T00:22:45.000Z　
> For reference: https://huggingface.co/blog/webgpu-kernelsI think it will be the basis for a rewrite of transformers.js v5, but no need for you to wait as you would likely want direct access. It is also way better than loading WASM, and faster to boot!

---

> **stymaar** · 2026-09-18T19:55:57.000Z　
> At my current company we're evaluating small models embedded directly in the web app to provide a natural language interface to the app without spending money on inference (and ideally avoid a ChatChipotle situation where people end up having free token going through our interface).And needle is one of the most promising model due to its original architecture (but we still need to finish building the actual eval dataset before making out final call).

---

> **HenryNdubuaku** · 2026-09-18T19:48:29.000Z　
> Thanks for the feedback! Implications and relations are hard for the model to understand (things like go to the living room, then the kitchen, and back), so yes the cleanest use cases involve direct language. Reasoning isn't true reasoning in the way general LLMs do it, it is more like grounding for the model that it generates itself. This can often become nonsensical specifically when the model gets things wrong, providing signal to the confidence.

---

> **HenryNdubuaku** · 2026-09-18T19:30:52.000Z　
> That's a really good point and I think it's not yet clear how well, say, 8-30MB worth of regexs with accompanying algorithmic structure would do on these tasks. I would imagine they do quite well on a well defined task, but it would be much harder to then adapt this set to a new domain. A big part of Needle's promise is how easy it is to finetune. Ultimately I think the two approaches can be more complimentary to each other, rather than choosing only one (see triggers!).

---

> **HenryNdubuaku** · 2026-09-18T19:16:24.000Z　
> well certainly the environment on the website cannot be a full product, and it isn't claiming to be that. The model, while capable in many dimensions, is also limited by its size. The website is meant to show both the capabilities and the limitations! A real deployment would absolutely need external guardrails, more thoroughly thought out tool sets with better task-specific triggers, perhaps also task-specific finetuning for better confidence grounding. And in my view that's the point of small open models! You can take it and run with it as far as you want.

---

> **HenryNdubuaku** · 2026-09-18T19:54:44.000Z　
> I think that would be very useful for us! The best way to reach us is through the founders@cactuscompute.com emailThank you!

---

> **HenryNdubuaku** · 2026-09-18T19:53:00.000Z　
> This is extremely useful feedback for us, thanks! I think the easiest thing here that can be fixed with tool definitions is the number conversions. Additionally, the model tends to work better with fewer tools. We will definitely be focusing on better context usage and followups going forward as well.

---

> **HenryNdubuaku** · 2026-09-18T21:31:48.000Z　
> Thanks for considering needle. Keep in mind that you can also fine-tune the model to fit your use case more. I think this illustrates the intended deployment pretty well, where both computational resources and compute credits can both be issues for deployment.

---

> **int_19h** · 2026-09-19T06:04:12.000Z　
> You can embed much bigger models into web apps with wasm and WebGL or WebGPU. I have a web app running a 0.6B embedding model client-side.

---

> **rohansood15** · 2026-09-19T07:36:16.000Z　
> Can you share an actual example of where it works please?

---

> **potatoman22** · 2026-09-18T20:45:53.000Z　
> I think a good "traditional" approach would look like a BM25 algorithm over an index of trigger phrases for each category, sitting behind a majority-vote classifier. The "fine tuning" would be done by reindexing the data, generating different/new phrases, and tuning the classification threshold.

---

> **stymaar** · 2026-09-19T07:15:17.000Z　
> We definitely intend to try fine-tuning, don't worry we're not going to dismiss needle just because the base model's performance is too low ;).

---

> **stymaar** · 2026-09-19T07:13:34.000Z　
> WebGPU is a non-starter for production usage since the support is too limited (No Firefox support, no Linux Support, no Apple x86 support, no MacOS <26).But yes we are also considering bigger models, though we'll pick the smallest model of sufficient quality because not having to download a 600MB bag of weight is a feature in itself.

---

> **HenryNdubuaku** · 2026-09-18T21:25:38.000Z　
> I think we might look into creating a baseline like this for our future models

## 导航

- 项目页：[[10-项目/cactuscompute.com_635b267a]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
