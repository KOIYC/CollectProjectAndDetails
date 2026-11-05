---
type: "project"
title: "Show HN: Zero-axiom Lean 4 proof that Yang-Mills on R^4 is a \"round square\""
project_url: "https://zenodo.org/records/23918639/files/RoundSquare.lean?download=1"
first_seen: "2026-11-05T11:21:45+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_DRLogvinovich
  - story_50371709
  - show_hn
lang: "en"
---

# Show HN: Zero-axiom Lean 4 proof that Yang-Mills on R^4 is a "round square"

> [!info] 一句话导读
> On October 26, OpenAI announced a claimed "bare existence" proof in Balaban's RG programme on pure R^4—but notably stopped right before claiming the mass gap Δ …

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://zenodo.org/records/23918639/files/RoundSquare.lean?download=1>
> 首次收录：2026-11-05T11:21:45+08:00
> 来源渠道：HN Show HN
> 标签：author_DRLogvinovich, story_50371709, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-05T11:21:45+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-11-05/d8b4f6073db9d208_Show-HN-Zero-axiom-Lean-4-proof-that-Yang-Mills-on]] |

## 摘要正文

On October 26, OpenAI announced a claimed "bare existence" proof in Balaban's RG programme on pure R^4—but notably stopped right before claiming the mass gap Δ > 0. It turns out there is a rigorous mathematical reason why no compute cluster can bridge that gap on flat infinite space.I wrote a 2,576-line self-contained Lean 4 script (`RoundSquare.lean`) that formally proves a negative-result resolution to the Clay Millennium Yang-Mills problem on pure R^4. In the tradition of Gödel and Turing, it proves that demanding BOTH the full Osterwalder-Schrader/Wightman axioms AND a strict spectral gap Δ > 0 on non-compact R^4 is a structural contradiction.Bare existence (Δ = 0) satisfies the OS axioms on R^4. But forcing a strict gap (Δ > 0) strictly requires an infrared cutoff via the Gribov horizon and a non-local θ-vacuum projector on the boundary S^3_∞, which immediately destroys Wightman microcausality (Strocchi's theorem) and Wick holomorphicity (GZ complex poles).The Lean 4 script compiles in 2 seconds with ZERO axioms. No `sorry`, no `Classical.choice`, no `propext`. Every single one of the 74 `#print axioms` checks outputs `does not depend on any axioms`.While corporate AI labs kee…
