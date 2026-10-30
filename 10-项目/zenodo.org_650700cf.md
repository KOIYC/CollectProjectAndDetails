---
type: "project"
title: "Show HN: Post-Quantum Signatureless Authorization"
project_url: "https://zenodo.org/records/23778742"
first_seen: "2026-10-30T09:57:35+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_ignotusnemo
  - story_50296097
  - show_hn
lang: "en"
---

# Show HN: Post-Quantum Signatureless Authorization

> [!info] 一句话导读
> Published: 2026-10-29

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://zenodo.org/records/23778742>
> 首次收录：2026-10-30T09:57:35+08:00
> 来源渠道：HN Show HN
> 标签：author_ignotusnemo, story_50296097, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-30T09:46:09+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-10-30/5e61b15f6c906dfe_Show-HN-Post-Quantum-Signatureless-Authorization]] |
| 2026-10-30T09:57:35+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-10-30/5e61b15f6c906dfe_Show-HN-Post-Quantum-Signatureless-Authorization]] |

## 摘要正文

Published: 2026-10-29 Author: Nemo, Ignotus  Post-Quantum Signatureless Authorization | Zenodo   Published October 29, 2026 | Version 1.0.0 Preprint Open  ### Authors/Creators  - Nemo, Ignotus  ## Description  Digital signatures authorize transactions, commands and other requests. Quantum attacks threaten widely used signature schemes, while their post-quantum replacements can be costly to verify inside proofs of execution. Signatureless authorization binds knowledge of an authority secret to a canonical request through a freshly randomized proof capsule. The public statement consists of a request identifier and a 32-byte authority commitment. Application rules enforce context, policy and freshness. The interface supports standalone requests and recursive proof composition.  The construction combines a masked degree-ten authority reduction over GF(2^128), embedded in GF(2^256), with a bank-and-companion code proof. Source restoration gives expected polynomial-time public-coin extraction. An adaptive witness-free simulator and a same-experiment source extractor establish a quantum chosen-request authorization reduction in the stated address-compatible random-completion model. The pu…
