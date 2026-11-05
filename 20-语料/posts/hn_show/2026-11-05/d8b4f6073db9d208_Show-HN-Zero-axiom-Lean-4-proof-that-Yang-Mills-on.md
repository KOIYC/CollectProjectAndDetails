---
type: "corpus"
item_id: "d8b4f6073db9d208"
title: "Show HN: Zero-axiom Lean 4 proof that Yang-Mills on R^4 is a \"round square\""
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50371709"
project_url: "https://zenodo.org/records/23918639/files/RoundSquare.lean?download=1"
author: "DRLogvinovich"
published_at: "2026-11-04T21:20:31Z"
captured_at: "2026-11-05T11:21:45+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-05"
pub_day: "2026-11-04"
tags:
  - 语料
  - hn_show
  - author_DRLogvinovich
  - story_50371709
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Zero-axiom Lean 4 proof that Yang-Mills on R^4 is a "round square"

> [!info] 一句话导读
> On October 26, OpenAI announced a claimed "bare existence" proof in Balaban's RG programme on pure R^4—but notably stopped right before claiming the mass gap Δ …

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50371709>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：DRLogvinovich　|　发布：2026-11-04T21:20:31Z
> 项目链接：<https://zenodo.org/records/23918639/files/RoundSquare.lean?download=1>
> 采集：2026-11-05T11:21:45+08:00　|　id：`d8b4f6073db9d208`

## 正文

On October 26, OpenAI announced a claimed "bare existence" proof in Balaban's RG programme on pure R^4—but notably stopped right before claiming the mass gap Δ > 0. It turns out there is a rigorous mathematical reason why no compute cluster can bridge that gap on flat infinite space.I wrote a 2,576-line self-contained Lean 4 script (`RoundSquare.lean`) that formally proves a negative-result resolution to the Clay Millennium Yang-Mills problem on pure R^4. In the tradition of Gödel and Turing, it proves that demanding BOTH the full Osterwalder-Schrader/Wightman axioms AND a strict spectral gap Δ > 0 on non-compact R^4 is a structural contradiction.Bare existence (Δ = 0) satisfies the OS axioms on R^4. But forcing a strict gap (Δ > 0) strictly requires an infrared cutoff via the Gribov horizon and a non-local θ-vacuum projector on the boundary S^3_∞, which immediately destroys Wightman microcausality (Strocchi's theorem) and Wick holomorphicity (GZ complex poles).The Lean 4 script compiles in 2 seconds with ZERO axioms. No `sorry`, no `Classical.choice`, no `propext`. Every single one of the 74 `#print axioms` checks outputs `does not depend on any axioms`.While corporate AI labs keep their training data and exact models closed, I believe the future of theoretical physics and millennium-level mathematics must be 100% open-source, machine-verified, and axiom-free.I've put a 10 LTC bounty on X for anyone who can find a logical flaw in the 74 theorems or exhibit a constructive mechanism on pure non-compact R^4 that generates a strict gap while bypassing the FMR horizon cusps and the S^3_∞ projector.You can verify the code in your browser without installing anything:
1. Download the script from the URL above.
2. Go to https://live.lean-lang.org
3. Load the file from disk and check the verdicts.Full preprint with context: https://doi.org/10.5281/zenodo.21555360Would love to hear feedback from the logic and constructive math folks here.

## 关联链接

- https://doi.org/10.5281/zenodo.21555360Would
- https://live.lean-lang.org

## 导航

- 项目页：[[10-项目/zenodo.org_f3ce408c]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
