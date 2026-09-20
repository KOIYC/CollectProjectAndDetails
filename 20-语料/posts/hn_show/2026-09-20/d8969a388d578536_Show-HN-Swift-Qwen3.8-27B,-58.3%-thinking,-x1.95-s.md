---
type: "corpus"
item_id: "d8969a388d578536"
title: "Show HN: Swift-Qwen3.8-27B, -58.3% thinking, x1.95 speed, accuracy of xhigh"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49727511"
project_url: "https://huggingface.co/ukisai/Swift-Qwen3.8-27b"
author: "kisjovan"
published_at: "2026-09-16T14:24:05Z"
captured_at: "2026-09-20T14:04:11+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-16"
tags:
  - 语料
  - hn_show
  - author_kisjovan
  - story_49727511
  - show_hn
metrics: {"points": 29, "comments": 17, "engagement_velocity": 29}
comments_count: 17
comments_total: 17
discovered_via: "hn:show_hn:90d"
---

# Show HN: Swift-Qwen3.8-27B, -58.3% thinking, x1.95 speed, accuracy of xhigh

> [!info] 一句话导读
> Swift-Qwen3.8-27B is UkisAI's reasoning-efficient derivative of Qwen3.8-27B, using 58.3% fewer thinking tokens while maintaining near-identical performance (<1%…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49727511>
> 指标：点赞=29 · 评论=17 · engagement_velocity=29
> 作者：kisjovan　|　发布：2026-09-16T14:24:05Z
> 项目链接：<https://huggingface.co/ukisai/Swift-Qwen3.8-27b>
> 采集：2026-09-20T14:04:11+08:00　|　id：`d8969a388d578536`

## 正文

# Swift-Qwen3.8-27B

Swift-Qwen3.8-27B is UkisAI's reasoning-efficient derivative of Qwen3.8-27B, using 58.3% fewer thinking tokens while maintaining near-identical performance (<1% loss) and as a result getting a x1.95 speed-up on several tasks.

The prompt is a sample from LiveCodeBench v6

## Training approach

We built Swift by identifying reasoning-marker tokens that, in our analysis, trigger overthinking in Qwen’s reasoning rollouts. We then fine-tuned Qwen by penalizing usage of those tokens while it reasons.

Swift produces shorter reasoning traces. In our testing, we also observe fewer overthinking errors.

For maximum gains, Swift also includes a transfer component derived from BottleCap AI's ThinkingCap-Qwen3.6-27B.

## Evaluation scope

> All results below compare the Qwen3.8-27B BF16 base with the same base plus the Swift adapter.

## Benchmarks

| Benchmark | Score | | Mean tokens | | | Median tokens |
| --- | --- | --- | --- | --- | --- | --- |
| | Base | Swift | Base | Swift | Reduction | Reduction |
| General reasoning | | | | | | |
| GPQA-Diamond | 88.38% | 88.28% | 15,014 | 8,855 | ↓ 41.0% | ↓ 58.3% |
| MMLU-Pro | 85.47% | 84.95% | 2,980 | 1,603 | ↓ 46.2% | ↓ 28.3% |
| C-Eval | 90.00% | 90.62% | 1,492 | 804 | ↓ 46.1% | ↓ 19.3% |
| IFBench | 73.53% | 71.80% | 8,052 | 4,657 | ↓ 42.2% | ↓ 50.5% |
| Mathematics | | | | | | |
| AIME 2026 | 98.67% | 94.00% | 22,014 | 16,143 | ↓ 26.7% | ↓ 50.2% |
| HMMT (Nov 2025) | 99.33% | 96.00% | 22,032 | 15,189 | ↓ 31.1% | ↓ 45.9% |
| Multimodal | | | | | | |
| ERQA | 67.45% | 66.30% | 4,137 | 2,045 | ↓ 50.6% | ↓ 54.6% |
| Agentic coding | | | | | | |
| Terminal-Bench 2.1 | 66.74% | 65.84% | 37,086 | 27,272 | ↓ 26.5% | ↓ 38.7% |
| LiveCodeBench v6 | 76.76% | 81.55% | 11,374 | 8,615 | ↓ 24.3% | ↓ 45.8% |

How to reproduce

Serving: BF16 · vLLM 0.27.1 · Qwen3 parser · context 262,144 · thinking xhigh. Sampling: temperature 1.0 · top_p 0.95 · top_k 20 · min_p 0 · presence_penalty 0 · repetition_penalty 1. Benchmarks: averages over five seeds (0–4) per model; five trials per task for Terminal-Bench.

| Benchmark | Output cap |
| --- | --- |
| GPQA-Diamond | 100,000 |
| MMLU-Pro | 100,000 |
| C-Eval | 16,384 |
| IFBench | 81,920 |
| AIME 2026 | 250,000 |
| HMMT Nov 2025 | 250,000 |
| ERQA | 100,000 |
| Terminal-Bench 2.1 | Agent/task limits |
| LiveCodeBench v6 | 32,768 |

## Efficiency across and versus reasoning efforts

Qwen3.8's `reasoning_effort` setting lets users choose how much the model thinks. For Swift to be useful across these settings, it needs to reduce thinking while keeping accuracy close to the base. We therefore tested `xhigh`, `medium`, and `low`: thinking-token savings persist at every level.

| Reasoning effort | Mean thinking reduction |
| --- | --- |
| Xhigh | ↓ 41.0% |
| Medium | ↓ 22.7% |
| Low | ↓ 25.8% |

The efficiency also holds up against the base's own lower effort settings. On GPQA-Diamond (198 questions, 5 seeds, 990 paired calls), Swift at `xhigh` is compared with the base at `xhigh` and at `medium`:

| GPQA-Diamond | Score | Mean tokens | Median tokens |
| --- | --- | --- | --- |
| Base · xhigh | 88.38% | 15,014 | 6,642 |
| Swift · xhigh | 88.28% | 8,855 | 2,771 |
| Base · medium | 84.14% | 4,451 | 1,753 |

Swift retains the accuracy of `xhigh` while using about half the tokens, although it uses about double the tokens of `medium`.

## Quantized models

Quantized deployment is the intended use for Swift: lower-memory weights paired with shorter reasoning. The INT4 evaluations below retain token savings across GPQA, IFBench, and AIME. On AIME, Swift matches or improves accuracy and reduces output-cap failures by 31–33%.

| Benchmark / quantization | Base accuracy | Swift accuracy | Mean token reduction | Median token reduction |
| --- | --- | --- | --- | --- |
| GPQA-Diamond Mixed-precision quant W4A16 · thinking tokens | 88.69% | 88.38% | ↓ 32.1% | ↓ 50.2% |
| IFBench Mixed-precision quant W4A16 · completion tokens | 72.58% | 71.25% | ↓ 30.1% | ↓ 38.0% |
| AIME 2026 Mixed-precision quant W4A16 · completion tokens | 84.00% | 84.00% | ↓ 19.0% | ↓ 37.5% |
| AIME 2026 AWQ INT4 · completion tokens | 82.67% | 84.00% | ↓ 22.8% | ↓ 34.8% |

Quantized evaluation settings

Each row compares the same quantized base with and without the Swift adapter. GPQA and AIME use five seeds; IFBench uses four samples per prompt and strict scoring. Output caps: GPQA 100,000; IFBench 81,920; AIME 32,768. GPQA and IFBench use saved historical base runs. AIME uses template-default effort and counts truncated answers as incorrect. Its shorter cap makes it a separate comparison from the BF16 table.

### GGUF download

The GGUF version is available for compatible llama.cpp-based runtime.

### UkisAI API

Swift is served through an OpenAI-compatible API at `https://ukisai.com/api/swift/v1`. It is free for research purposes and needs no API key. The model id is `swift`.

```python
from openai import OpenAI

client = OpenAI(base_url="https://ukisai.com/api/swift/v1", api_key="none")
response = client.chat.completions.create(
    model="swift",
    messages=[{"role": "user", "content": "Explain speculative decoding in two sentences."}],
)
print(response.choices[0].message.content)

```

```bash
curl https://ukisai.com/api/swift/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "swift", "messages": [{"role": "user", "content": "Hello, Swift."}]}'

```

### Transformers

```python
import torch
from transformers import AutoModelForImageTextToText, AutoProcessor

model_id = "ukisai/Swift-Qwen3.8-27b"
processor = AutoProcessor.from_pretrained(model_id)
model = AutoModelForImageTextToText.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

```

### vLLM

```bash
vllm serve ukisai/Swift-Qwen3.8-27b \
  --dtype bfloat16 \
  --tensor-parallel-size 1 \
  --max-model-len 262144 \
  --reasoning-parser qwen3 \
  --enable-auto-tool-choice \
  --tool-call-parser qwen3_coder \
  --port 8000

```

### SGLang

Alternatively, use a current SGLang build with Qwen3.8 support:

```bash
python -m sglang.launch_server \
  --model-path ukisai/Swift-Qwen3.8-27b \
  --dtype bfloat16 \
  --tp-size 1 \
  --context-length 262144 \
  --reasoning-parser qwen3 \
  --tool-call-parser qwen3_coder \
  --port 8000

```

Adjust tensor parallelism and context length to your GPU memory. See the base model's vLLM recipe and SGLang recipe for installation and hardware-specific settings.

### Optional MTP decoding

The published weights include the base model's MTP head. To enable self-speculative decoding, append the corresponding flags to the server command above:

```bash
# vLLM
--speculative-config '{"method":"mtp","num_speculative_tokens":3}'

# SGLang
--speculative-algorithm EAGLE --speculative-num-steps 3 \
  --speculative-eagle-topk 1 --speculative-num-draft-tokens 4

```

## License and access

Swift weights are distributed through gated access under the Swift Open License v1.0. Personal, research, educational, evaluation, and commercial use are free for individuals and organizations with annual recurring revenue, including affiliates, of up to US$1,000,000. Above that threshold, commercial use requires a separate Swift Enterprise License. Contact UkisAI for terms.

## Citation

```bibtex
@misc{swift-qwen3.8-27b,
  title  = {Swift-Qwen3.8-27B},
  author = {UkisAI},
  year   = {2026},
  url    = {https://huggingface.co/ukisai/Swift-Qwen3.8-27b}
}

```

## Acknowledgements

We acknowledge the NVIDIA Innovation Lab for providing access to 8× NVIDIA H100 GPUs to train Swift.

Downloads last month
: 59

Safetensors

Model size 28B params

Tensor type

BF16

## Model tree for ukisai/Swift-Qwen3.8-27b

Qwen/Qwen3.8-27B

 Finetuned

(328)

3 models

Inference providers allow you to run inference using different serverless providers.

# Automatic Plant Watering System | Sam Burns' Tech Blog

## 评论（17/17）

> **kisjovan** · 2026-09-16T14:26:56.000Z　
> I will TLDR you on our thought process, research, training and benchmarks.1. When running our quantized Qwen 3.8 27B instances we were very annoyed by random reasoning loops (in the paper bellow refered to as "overthinking errors". These random loops were persistent throughout medium and low reasoning settings.2. We found a paper by Meta that's supposed to target this phenomenon in PTQ, but when used straight out of the box got mixed results. https://arxiv.org/abs/2606.002063. We figured to try if it's a matter of the targeting the right keywords and tuning the parameters, so we used our 8xH100 box and and generated a large amount of different (ofc out of distribution) domain (coding, language, vision, agentic) traces.4. We then grouped the ones with overthinking and found "common denominator" tokens between them and targeted the most prominent ones.5. We then built an inference-time penalizer of those tokens as seen in the paper with the hopes of simply generating traces and doing cross-entropy SFT over them.6. Did not work at all, but the penalizer seemed to work much better than the tokens provided in the paper and not only for lower precision models but for bf16 as well. Hence we kept experimenting with it. We built a loss function using the tokens we identified and ran LoRa SFT over the traces prev generated and reasoning seemed to be falling off significantly but the accuracy seemed to follow. The reasoning reduction seemed to be generalizing.7. After a significant amount of tinkering (literally since the day of Qwen 3.8 27B release) we were satisfied with the reasoning reduction. After that we searched for ways of restoring the accuracy. We experimented with several methods, including RL(GSPO), On-Policy Distillation and using the ThinkingCap 3.6 27B adapter chunks until we were satisfied with our accuracy loss. We managed to restore it to <1% loss on almost all of our OOD in house tests8. We then performed intensive intensive benchmarks, across several reasoning efforts, precision variants etc. We ran into a few problems, one of which is that to get a reliable score we needed to run each benchmark 10x (5x on base + 5x with our adapter, this being the standard procedure on the Qwen 3.6 27B model card on Terminal Bench which we followed). After running it, the performance converged to 40-60% token reduction with <1% accuracy loss across GPQA, MMLU, Terminal Bench 2.1, LiveCodeBench v6, ERQA, C-Eval, IFBench, HMMT25, with an exception being AIME26 with an accuracy loss of 4.6%, which we later linked to a bug during training with a specific token relevant for math-related reasoning being penalized and are planning to fix it in an updated release.

---

> **danilotodorovic** · 2026-09-16T14:30:31.000Z　
> I've been using this and it's quite amazing for the amount I've used it. Thanks for the hard work.

---

> **founderjoeNY** · 2026-09-16T14:32:34.000Z　
> How does it perform on real long horizon tasks?

---

> **bellowsgulch** · 2026-09-16T17:17:16.000Z　
> I so wanted to be able to use Qwen3.8-27B locally on my fully loaded M1 Max 64GB when spider-mario recommended I use MTPLX[1], but I still found the general MLX MTP acceleration to be so poor, I'd rather just use cheap tokens from OpenCode Zen and Go.It's just too slow of a model. I know, I know there's new hardware, but my business paid like 4-5 grand for this MBP at the time, and I just don't feel the need to pay 7-8 grand to step up to current hardware when token spend is what it is.[1]: https://news.ycombinator.com/item?id=49611128#49612229

---

> **Sev7eNup** · 2026-09-16T21:36:31.000Z　
> does the model sometimes fall in loops?

---

> **zionsati** · 2026-09-17T07:01:14.000Z　
> Very nice! Is there a lower quant like Q4? There's research showing lower quants suffer from low confidence in its own reasoning and tend to overthink because of that. I wonder if this helps?

---

> **pu_pe** · 2026-09-16T17:41:43.000Z　
> Congrats, seems like a promising concept. I'll give it a go in my local setup. My prior is thinking this will definitely work for speed but also definitely compromise accuracy (I've seen this happen so many times), though benchmark results are encouraging of course.Nice explanation too. Now that everything reads like a sad blur, it felt refreshing to read your writeup.

---

> **alpha_trion** · 2026-09-16T18:00:55.000Z　
> Nice. Going to dl and give it a whirl.

---

> **billziss** · 2026-09-16T22:11:48.000Z　
> I tried an oMLX quant of your model (suzu89/Swift-Qwen3.8-27b-oQ8-mtp -- not mine) and liked it. It certainly seems to cut down on thinking compared to stock Qwen3.8 27B in my (limited) testing.A couple of questions:- Have you tried the peculiar-ragdoll/Qwen-Sharp-Chat-Templates with it? They replace the default chat_template.jinja with one that encourages less thinking.- When are you releasing Swift-Qwen3.8-Flash-Next? :)

---

> **kisjovan** · 2026-09-16T14:31:52.000Z　
> Thank you so much!! It would be great if you could share some numbers with the community :)

---

> **kisjovan** · 2026-09-16T14:45:34.000Z　
> You should check out our TerminalBench2.1 score for that, the tasks there can run up to 4h! We got almost no loss (we got Base 66.74% vs Swift 65.84%) with -38.7% thinking token reduction. There's also quite a few independent evals on the reddit link as well.Please let me know when you try the model and if I can help you set it up :)

---

> **serf** · 2026-09-16T17:48:46.000Z　
> slow as in the output is slow, or slow as in slow token rates?qwen3.8 has been fantastic as far as token rates are concerned for me, but the overthinking thing with higher reasoning levels takes some coercion to get right.fwiw pi and hermes both handle that model fairly well. omp required a lot of tuning. I didn't bother figuring out why, I presume it's because qwen3.8 expects reasoning declarations a bit differently. nothing a proxy can't fix.

---

> **kisjovan** · 2026-09-17T16:27:45.000Z　
> It does, but very rarely (as opposed to the Base Qwen 3.8 27B), making it actually usable for day-to-day work - which is why we even trained it

---

> **kisjovan** · 2026-09-17T16:28:13.000Z　
> There is! We've got 20+ community quants

---

> **kisjovan** · 2026-09-17T16:27:06.000Z　
> Thank man appreciate it! Did you get the chance to try it?

---

> **kisjovan** · 2026-09-17T16:27:16.000Z　
> Did you get to try it?

---

> **kisjovan** · 2026-09-17T16:26:45.000Z　
> Thank you so much for trying it! I personally haven't tried it - the community has noted that it does indeed work though. On the Swift Qwen3.8-Flash-Next, we're running the benchmarks right now and will get it out end of this or start of next week! You'll for sure find it on r/LocalLlama

## 关联链接

- https://huggingface.co/ukisai/Swift-Qwen3.8-27b}
- https://ukisai.com/api/swift/v1
- https://ukisai.com/api/swift/v1/chat/completions
- https://ukisai.com/api/swift/v1`.

## 导航

- 项目页：[[10-项目/huggingface.co_214533b2]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
