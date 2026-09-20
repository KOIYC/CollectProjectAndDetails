---
type: "corpus"
item_id: "be565c01cf616322"
title: "Show HN: In-Browser Sanskrit ASR Model"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49731455"
project_url: "https://huggingface.co/gnumanth/sushrota-sanskrit-asr-onnx"
author: "init0"
published_at: "2026-09-16T19:04:33Z"
captured_at: "2026-09-20T09:36:58+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-20"
pub_day: "2026-09-16"
tags:
  - 语料
  - hn_show
  - author_init0
  - story_49731455
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: In-Browser Sanskrit ASR Model

> [!info] 一句话导读
> Su-śrotā Sanskrit ASR — ONNX & In-Browser INT8

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49731455>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：init0　|　发布：2026-09-16T19:04:33Z
> 项目链接：<https://huggingface.co/gnumanth/sushrota-sanskrit-asr-onnx>
> 采集：2026-09-20T09:36:58+08:00　|　id：`be565c01cf616322`

## 正文

# Su-śrotā Sanskrit ASR — ONNX & In-Browser INT8

This repository provides ONNX and INT8 quantized exports of Su-śrotā (`v13b`), a scholar-grade Sanskrit speech recognition model developed by Prof. Prathosh A P (Indian Institute of Science, Bengaluru).

These models allow running Sanskrit ASR 100% serverless in a web browser (via `onnxruntime-web`) or locally on Mac/Linux/Windows with zero PyTorch/NeMo dependencies.

## Files in this repository

| File | Size | Description |
| --- | --- | --- |
| `sushrota_sanskrit_ctc_int8.onnx` | ~178 MB | Conformer-CTC model quantized with INT8 MatMul for browser WASM / WebGPU / CoreML execution |
| `preprocessor.onnx` | ~149 KB | Neural Audio-to-Mel-Spectrogram filterbank preprocessor (16 kHz mono PCM $\rightarrow$ 80-mel log spectrogram) |
| `sanskrit_vocab.json` | ~3 KB | Tokenizer dictionary mapping 257 CTC output classes to Sanskrit characters/BPE units |

## Performance

- Parameters: ~115M active parameters (Sanskrit slice of IndicConformer)
- Local Mac CPU Latency: ~0.10s for 3.0s audio (RTF: 0.03, ~30x faster than real-time)
- In-Browser WebAssembly Latency: ~0.25s for 2.0s audio (RTF: 0.12, ~8x faster than real-time)

### 1. In-Browser (JavaScript with `onnxruntime-web`)

```html





```

### 2. Python (Without NeMo or PyTorch)

```bash
pip install onnxruntime soundfile numpy

```

```python
import onnxruntime as ort, soundfile as sf, numpy as np, json

prep = ort.InferenceSession("preprocessor.onnx")
asr = ort.InferenceSession("sushrota_sanskrit_ctc_int8.onnx")
vocab = json.load(open("sanskrit_vocab.json"))

wav, sr = sf.read("audio.wav", dtype="float32") # must be 16kHz mono
if wav.ndim > 1: wav = wav.mean(axis=1)

feats, flen = prep.run(None, {"audio_signal": wav[np.newaxis, :], "length": np.array([len(wav)], dtype=np.int64)})
logits = asr.run(None, {"audio_signal": feats, "length": flen})[0]

# Greedy decode
pred_ids = np.argmax(logits[0], axis=-1)
out, prev = [], -1
for i in pred_ids:
    if i != prev and i != 0: out.append(vocab[i])
    prev = i
print("Transcript:", "".join(out).replace("▁", " ").strip())

```

## Citation

> Prathosh A P, Su-śrotā: Scholar-grade Sanskrit ASR and metre-aware chant practice, Indian Institute of Science, Bengaluru, 2026.

Downloads last month

-

Downloads are not tracked for this model. How to track

## Space using gnumanth/sushrota-sanskrit-asr-onnx 1

# friday-memory/friday

## 关联链接

- https://cdn.jsdelivr.net/npm/onnxruntime-web/dist/ort.all.min.js
- https://huggingface.co/gnumanth/sushrota-sanskrit-asr-onnx/resolve/main/preprocessor.onnx
- https://huggingface.co/gnumanth/sushrota-sanskrit-asr-onnx/resolve/main/sanskrit_vocab.json
- https://huggingface.co/gnumanth/sushrota-sanskrit-asr-onnx/resolve/main/sushrota_sanskrit_ctc_int8.onnx

## 导航

- 项目页：[[10-项目/huggingface.co_601551ef]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
