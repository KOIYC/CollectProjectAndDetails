---
type: "corpus"
item_id: "e32cf342e531ca9d"
title: "Show HN: ABSL – 100% Integer-Only Neural Network Training in Rust"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49109785"
project_url: "https://github.com/Mojo0869/ABSL"
author: "Mojo_0869"
published_at: "2026-07-30T13:34:24Z"
captured_at: "2026-09-21T03:11:18+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-07-30"
tags:
  - 语料
  - hn_show
  - author_Mojo_0869
  - story_49109785
  - show_hn
metrics: {"points": 3, "comments": 2, "engagement_velocity": 3}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:83d"
---

# Show HN: ABSL – 100% Integer-Only Neural Network Training in Rust

> [!info] 一句话导读
> ABSL or Adaptive Bitshift learning is a lerning method only using Integers for AI i made. The goal is to make a good Integer Neuronr neuron

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49109785>
> 指标：点赞=3 · 评论=2 · engagement_velocity=3
> 作者：Mojo_0869　|　发布：2026-07-30T13:34:24Z
> 项目链接：<https://github.com/Mojo0869/ABSL>
> 采集：2026-09-21T03:11:18+08:00　|　id：`e32cf342e531ca9d`

## 正文

# Mojo0869/ABSL

ABSL or Adaptive Bitshift learning is a lerning method only using Integers for AI i made. The goal is to make a good Integer Neuronr neuron

- Stars: 2
- Forks: 0
- Watchers: 2
- Open issues: 0
- License: Other
- Default branch: main
- Created: 2026-07-28T07:36:07Z

## Languages

- Rust

## Top Contributors

- Mojo0869 (56 contributions)

---

## README

# ABSL – Adaptive Bit-Shift Learning (v1.0.0 XOR Edition)

ABSL (Adaptive Bit-Shift Learning) is an experimental, **100% integer-only learning algorithm** for neural networks, written from scratch in Rust.

By completely avoiding floating-point math (`float`), ABSL eliminates the need for expensive FPUs (Floating Point Units). This makes it natively compatible with ultra-low-power embedded systems, 8-bit/16-bit microcontrollers, and neuromorphic hardware.

Instead of traditional learning rates, ABSL dynamically scales weight updates using an adaptive bit-shifting mechanism based on integer error magnitudes.

---

## 🚀 The Breakthrough: Cracking the Non-Linear XOR Problem

Historically, solving the non-linear XOR problem required continuous floating-point gradients. ABSL v1.0.0 completely shatters the myth that integer training is bound to get stuck in local minima due to harsh rounding errors.

By scaling up the hidden layer to a **2-3-1 architecture** (2 Inputs, 3 Hidden Neurons, 1 Output), ABSL introduces enough high-dimensional redundancy to bypass integer quantization bottlenecks.

### Latest Benchmark Results (1,000 Runs)

| Metric | ABSL v3 | ABSL v5 (v1.0.0 Core) |
| :--- | :---: | :---: |
| **Perfect Runs (4/4 Correct)** | 38.7 % | **70.1 %** 🔥 |
| **Global Accuracy** | 80.0 % | **91.1 %** |
| **Avg. Correct Cases per Run** | 3.20 / 4 | **3.64 / 4** |
| **Total Failures (0, 1, or 2 Correct)** | High | **0.0 %** (Always gets ≥ 3/4) |

### Input Combination Accuracy (v1.0.0)
* **(0,0):** 88.2% *(Current tuning target: eliminating low-level integer bias leakage)*
* **(0,1):** 99.4% ✨
* **(1,0):** 99.6% ✨
* **(1,1):** 77.1% *(Current tuning target: optimizing negative integer inhibition)*

---

## 🧠 How It Works (The Core Logic)

ABSL snaps continuous gradients into a discrete integer grid using native Rust performance:

```rust
impl LearningRule for ABSLv5 {
    fn update(&self, error: i32, input: i32, weight: i32, _epoch: u32) -> i32 {
        let shift = Self::calculate_shift(error, weight);
        (((error as i64) * (input as i64)) >> shift) as i32
    }
}
```

The `shift` is dynamically calculated using bit-lengths (`ilog2`) of both the error and weight magnitudes, preventing weight explosion while keeping execution blindingly fast.

---

## 🎯 Current Roadmap & Optimization Targets

I am actively working on pushing the success rate from **70.1% to 99%+.**

### Next Steps:

- Implement a discrete integer damping factor (Momentum equivalent) to prevent weight oscillation.
- Scale to MNIST.

---

##About Me:

- I'm 15 living in Germany cirrntly in 10th grade and coded al of this on a broken s22 Ultra

- In the future i want to study and work even more with this topic
---
## License
Costum Licene please look in LICENSE

# sky.luftaquila.io

## 评论（2/2）

> **prologic** · 2026-07-30T13:44:03.000Z　
> Wow! This kid is only 15 and built some pretty cool shit™ here! Can anyone explain how this works beyond trying to read/understand the code (which might take a while). I think I get the idea of 3-hidden neurons in the hidden layer, but not how this results in how it bypasses integer quantization bottlenecks.

---

> **Mojo_0869** · 2026-07-30T15:42:52.000Z　
> By using integers instead of floats, you lose precision — weights/activations can only take on coarse, discrete values. With just 2 neurons, that severely limits the space of functions the network can represent. The 3rd neuron gives the network more degrees of freedom, so it can better approximate the target function despite the coarse resolution — not by 'stepping in' when another one fails, but by giving the network more combinatorial capacity overall.

## 导航

- 项目页：[[10-项目/github.com_f3edb2fa]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
