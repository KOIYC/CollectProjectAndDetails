---
type: "corpus"
item_id: "f75ab2d7bca162f3"
title: "Show HN: TurboGPT: train 22KiB transformer in 13s"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49898931"
project_url: "https://github.com/lostmsu/TurboGPT"
author: "lostmsu"
published_at: "2026-09-29T19:20:02Z"
captured_at: "2026-09-30T18:57:48+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-30"
pub_day: "2026-09-29"
tags:
  - 语料
  - hn_show
  - author_lostmsu
  - story_49898931
  - show_hn
metrics: {"points": 49, "comments": 10, "engagement_velocity": 49}
comments_count: 9
comments_total: 10
discovered_via: "hn:show_hn:3d"
---

# Show HN: TurboGPT: train 22KiB transformer in 13s

> [!info] 一句话导读
> Train a tiny GPT in under a minute (CUDA only)

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49898931>
> 指标：点赞=49 · 评论=10 · engagement_velocity=49
> 作者：lostmsu　|　发布：2026-09-29T19:20:02Z
> 项目链接：<https://github.com/lostmsu/TurboGPT>
> 采集：2026-09-30T18:57:48+08:00　|　id：`f75ab2d7bca162f3`

## 正文

# lostmsu/TurboGPT

Train a tiny GPT in under a minute (CUDA only)

- Stars: 35
- Forks: 0
- Watchers: 35
- Open issues: 0
- License: MIT License
- Default branch: master
- Created: 2026-09-23T20:21:23Z

## Languages

- C++
- Cuda
- Nix
- PowerShell
- Python

## Top Contributors

- lostmsu (9 contributions)

---

## README

# turboGPT

Tiny byte-level GPT training in CUDA C++. MIT.

## Build

Linux/NixOS:

```bash
nix-build -o build/nix-result
```

Windows, Visual Studio 2022 C++ tools, and CUDA 13.4:

```powershell
.\build.ps1 -CudaArch 86
```

`CudaArch` is the GPU compute capability from NVIDIA's CUDA GPU list.

## Run

```powershell
.\build\turbogpt.exe --data hn1g.txt --log-to runs/ctx4
```

The run stores its checkpoint at
`runs/ctx4/ctx4.pt`, containing model, optimizer, scheduler, and trainer state.
Use `--load CHECKPOINT.pt` to resume it.

`runs/ctx4/report.json` is derived from the log directory. Logs are TensorBoard-compatible:
one report per batch, capped at 8Mi reports, and flushed with periodic or final checkpoints.

## Result

- hn1g after 1.5G training tokens: **2.5295 BPB**.

## Tests

```powershell
python tests\verify.py
```

# yeet-src/agentcap

## 评论（9/10）

> **jey** · 2026-09-29T20:30:08.000Z　
> At that scale it seems like you could just solve the KKT conditions directly. Exaggerating but only a little

---

> **vjsrinivas** · 2026-09-29T21:55:05.000Z　
> Interesting trend of labeling models after how big they are on disk vs how many learnable parameters they have.

---

> **w4yai** · 2026-09-29T22:26:08.000Z　
> "hn1g.txt" => not available

---

> **_345** · 2026-09-29T22:50:02.000Z　
> Trying to be a little less negative than the guy that got flagged, I too don't understand the motivation behind these projects. I've seen a hundred of them at this point- and each of them is probably worse and has less learning value than the one Andrej Karpathy made to teach people the building blocks involved in a GPTSo, why do people keep making these? Asking genuinely

---

> **lostmsu** · 2026-09-30T01:28:57.000Z　
> Just uploaded to https://huggingface.co/datasets/lostmsu/hn1g/tree/mainBut it is a byte predictor. You can train it on any file.

---

> **alightsoul** · 2026-09-30T00:19:43.000Z　
> to add it to their resume and "prove" they know how machine learning works

---

> **Axodouble** · 2026-09-30T00:56:43.000Z　
> Fun? I am unsure why it keeps getting shared though, I too have reinvented the wheel a few times for fun.* Edit, I did however just notice literally all of this is just another vibeslopped banger, so I am not quite sure how much fun there really is, feels more like coding for the sake of keeping the wheel turning.

---

> **lostmsu** · 2026-09-30T01:12:04.000Z　
> > So, why do people keep making these? Asking genuinelyI extensively used minGPT for home experiments on transformer architecture. It is great for learning!However, if you want to scale the experiments up at home you need to go faster. Karpathy made optimized https://github.com/karpathy/nanoGPT, but it is tuned for "8XA100 40GB node in about 4 days of training".13s is a bit overkill here (my machine builds that project in 30s). But it gives some space for experimentation with architectures that don't have optimized primitives.

---

> **jazzpush2** · 2026-09-30T00:44:48.000Z　
> You mean pushing everything up in one giant commit with Claude isn't learning!?

## 导航

- 项目页：[[10-项目/github.com_8abf9ed4]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
