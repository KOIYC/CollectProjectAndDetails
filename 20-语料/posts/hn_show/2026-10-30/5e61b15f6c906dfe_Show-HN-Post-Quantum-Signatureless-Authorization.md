---
type: "corpus"
item_id: "5e61b15f6c906dfe"
title: "Show HN: Post-Quantum Signatureless Authorization"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50296097"
project_url: "https://zenodo.org/records/23778742"
author: "ignotusnemo"
published_at: "2026-10-29T21:13:59Z"
captured_at: "2026-10-30T09:57:35+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-10-30"
pub_day: "2026-10-29"
tags:
  - 语料
  - hn_show
  - author_ignotusnemo
  - story_50296097
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Post-Quantum Signatureless Authorization

> [!info] 一句话导读
> Published: 2026-10-29

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50296097>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：ignotusnemo　|　发布：2026-10-29T21:13:59Z
> 项目链接：<https://zenodo.org/records/23778742>
> 采集：2026-10-30T09:57:35+08:00　|　id：`5e61b15f6c906dfe`

## 正文

Published: 2026-10-29
Author: Nemo, Ignotus

Post-Quantum Signatureless Authorization | Zenodo

 Published October 29, 2026 | Version 1.0.0 Preprint Open

### Authors/Creators

- Nemo, Ignotus

## Description

Digital signatures authorize transactions, commands and other requests. Quantum attacks threaten widely used signature schemes, while their post-quantum replacements can be costly to verify inside proofs of execution. Signatureless authorization binds knowledge of an authority secret to a canonical request through a freshly randomized proof capsule. The public statement consists of a request identifier and a 32-byte authority commitment. Application rules enforce context, policy and freshness. The interface supports standalone requests and recursive proof composition.

The construction combines a masked degree-ten authority reduction over GF(2^128), embedded in GF(2^256), with a bank-and-companion code proof. Source restoration gives expected polynomial-time public-coin extraction. An adaptive witness-free simulator and a same-experiment source extractor establish a quantum chosen-request authorization reduction in the stated address-compatible random-completion model. The public authority circuit and its address input slice are fixed. One permutation supplies the native transcript and commitments. Finite orbit-profile and resource conditions are explicit. The reduction quantifies simulation and extraction losses alongside authority-preimage hardness and canonical intent binding. For S <= T and T <= 2^24 charged native calls, the combined simulation and extraction loss is below 2^-67, including the uniform-slice setup failure.

Parano1d supplies a blockchain implementation and recursive verifier. Canonical capsules are bounded by 92,696 bytes. On four CPU threads, median proving takes 0.81 to 0.89 seconds and verification takes approximately 25.6 milliseconds for two request fixtures.

The accompanying reproducibility archive contains the manuscript sources, exact arithmetic and finite operator checks, simulation tests, recorded measurements, Rust reproduction programs and authenticated production source files. Its README provides the reproduction commands.

Contact: dev@parano1d.org License information: The paper and accompanying written documentation are licensed under Creative Commons Attribution 4.0 International (CC BY 4.0). Original software in the reproducibility artifact is licensed under the Apache License, Version 2.0. Third-party dependencies retain their respective licenses.

## Files

Post-Quantum Signatureless Authorization Ignotus Nemo dev@parano1d.org 29 October 2026 Abstract Digital signatures authorize transactions, commands and other requests. Quantum attacks threaten widely used signature schemes. Their post-quantum replacements can be costly to verify inside proofs of execution. Signatureless authorization binds knowledge of an authority secret to a canonical request through a freshly randomized proof capsule. The public statement consists of a request identiﬁer and a 32-byte authority commitment. Application rules enforce context, policy and freshness. The interface supports standalone requests and recursive proof composition. The construction combines a masked degree-ten authority reduction over F 2 128 ⊂ F 2 256 with a bank-and-companion code proof. Source restoration gives expected polynomial-time public-coin extraction with error at most 5− 65 + 701202001642/ 2 255. The native model ﬁxes the public authority circuit and its address input slice, then samples a uniform permutation completion elsewhere. Under explicit ﬁnite orbit-proﬁle con- ditions, classical authorization requests and coherent forward and inverse queries admit the bound Pr[Forge Q] ≤ Adv Q pre +ε Q sim + ε Q ext + ε Q id. An adaptive witness-free simulator and ex- pected polynomial-time source extractor give explicit error terms for the shared native tran- script and commitment permutation. The source bank proves the ﬁxed authority circuit’s relation. For the ideal 256-bit authority-preimage task, constant-success generic quantum search has query scale 2 128. Parano1d supplies a blockchain implementation and recursive veriﬁer. It uses a 2,048-cell bank and 65 code queries, with canonical capsules bounded by 92,696 bytes. On four CPU threads, median proving takes 0.81 to 0.89 seconds and veriﬁcation takes approximately 25.6 milliseconds for two request ﬁxtures. 1 Introduction Quantum algorithms for factoring and discrete logarithms threaten authorization based on these problems [Sho95]. NIST identiﬁes aﬀected standards and post-quantum replacements [MPR+ 26]. The ML-DSA parameter sets in FIPS 204 use 1,312 to 2,592-byte public keys and 2,420 to 4,627-byte signatures [Nat24a]. SLH-DSA signatures in FIPS 205 occupy 7,856 to 49,856 bytes [Nat24b]. Applications that certify both authorization and execution must also represent authorization veriﬁcation in their proof arithmetic. Post-quantum Privacy Pass studies this coupling through STARK-oriented Dilithium [PWFHW23]. This motivates the following design question: how to bind each request to its authority within the same arithmetic used to prove execution, while protecting a reusable secret across repeated authorizations. The resulting relation must also support recursive veriﬁcation and a stable boundary between authority and public execution. We therefore consider a direct proof of knowledge of an authority secret. Signatureless authorization binds freshly randomized proofs of knowledge of an authority secret to canonical requests. For intent I, identiﬁer m = ID(I) and required 32-byte authority commitment a, the public statement and authority relation are x = (m, a), R own(a, s) = [Addr(s) = a]. (1) 1

The adapter binds context and authority. Application rules check execution, policy and freshness. For ﬁxed intent and authority, the same capsule remains veriﬁable when the public execution witness is updated within the intent’s constraints. The construction reduces the address relation to eleven linear functionals of a 2,048-cell bank. The code argument is an interactive oracle proof (IOP). Exact masking ranks and con- stant Owner ﬁbers give causal simulation. Finite-list restoration gives round-by-round knowl- edge. A native compiler preserves complete response groups, the Owner bridge and the shared transcript and commitment permutation. Complete simulation and extraction establish quan- tum authorization in the address-compatible random-completion model under ﬁnite slice-proﬁle conditions, with coherent forward and inverse access. Parano1d supplies the blockchain and recursive-veriﬁcation case study. Related work includes signatures of knowledge [CL06] and post-quantum signatures built from symmetric primitives [CDG+ 17]. The algebra uses binary-ﬁeld permutations [GKK+ 25], multilinear reductions [LFKN92, GKR08], Libra masking [XZZ+ 19] and binary-tower code com- mitments [ZCF23, DP24]. 2 Statements, authority and execution For s = (s 0, s 1) ∈ F 2 2 128 , ﬁxed address capacity (ι 0, ι 1) and the width-four Poseidon2b permuta- tion, Addr(s) = ﬁrst 2 P (s 0, s 1, ι 0, ι 1) ∈ F 2 2 128 . (2) The witness stores the initial linear layer and 66 nonlinear rounds. Two linear boundaries ﬁx its initial capacity and two its ﬁnal address. Lemma 2.1 (Address witness). With exact arithmetic and authenticated permutation constants, a state table satisfying the 66 · 4 transitions and four boundaries determines a secret s with Addr(s) = a. Proof. Invert the initial linear layer. Its ﬁrst two coordinates give s and the other two are ﬁxed by the initial boundaries. Induction identiﬁes the prescribed trace. Its ﬁnal boundaries give a. Intents. The application deﬁnes domain, operation, context, action data and execution con- straints in m = ID(I) = H intent(domain, encode(I)). (3) Canonical encoding ﬁxes lengths, ﬁeld order and unused records. The authority adapter derives a from this checked intent and policy. Services bind audience, operation, parameters and nonce. Devices bind target, command, counter and validity. Artifact approvals bind digest, intended use and policy. Ledgers bind context, resources and action terms. Execution checks the applicable authority, policy and freshness. A freshness condition consumes a nonce, counter or resource reference. Algorithms. Statement(I, c) validates intent and authority context, then returns x = (ID(I), a). Authorize(s, x) checks the address and uses fresh randomness to produce the capsule. CheckAuth(x, π) checks shape and replays transcript, reduction and code openings. Execute(I, st, c) checks state, context, authority, policy and freshness, then returns the permitted successor state. The public vector is (m 0, m 1, a 0, a 1) ∈ F 4 2 128 . (4) The veriﬁer derives all challenges and ordered claims itself. 2

 Files (754.7 kB)

| Name | Size | |
| --- | --- | --- |
| post-quantum-signatureless-authorization.pdf md5:94ea03103501ebb7d6964ea4bc51ade6 | 221.8 kB | Preview Download |
| signatureless-authorization-artifact.zip md5:7d6f41727238d2884327f4e5c4f3bd82 | 533.0 kB | Preview Download |

## Versions

Cite all versions? You can cite all versions by using the DOI 10.5281/zenodo.23778741. This DOI represents all versions, and will always resolve to the latest one. Read more.

DOI
: Copy to clipboard

DOI Badge

#### DOI

```
10.5281/zenodo.23778742
```

### Markdown

```
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23778742.svg)](https://doi.org/10.5281/zenodo.23778742)
```

### reStructuredText

```
.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.23778742.svg
  :target: https://doi.org/10.5281/zenodo.23778742
```

### HTML

```
<a href="https://doi.org/10.5281/zenodo.23778742"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.23778742.svg" alt="DOI"></a>
```

### Image URL

```
https://zenodo.org/badge/DOI/10.5281/zenodo.23778742.svg
```

### Target URL

```
https://doi.org/10.5281/zenodo.23778742
```
Resource type
: Preprint
Publisher
: Zenodo
Languages
: English

License
: Creative Commons Attribution 4.0 International

 The Creative Commons Attribution license allows re-distribution and re-use of a licensed work on the condition that the creator is appropriately credited. Read more
: Apache License 2.0

 A permissive license whose main conditions require preservation of copyright and license notices. Contributors provide an express grant of patent rights. Licensed works, modifications, and larger works may be distributed under different terms and without source code. Read more
Copyright
: © 2026 Ignotus Nemo, Parano1d

Error fetching https://github.com/cjus/audio-chat-box: CRAWL_LIVECRAWL_TIMEOUT
Error fetching https://github.com/kishormorol/cli-faq-shortcuts: CRAWL_LIVECRAWL_TIMEOUT
Error fetching https://github.com/saranyan/breakout-coordinator: CRAWL_LIVECRAWL_TIMEOUT

## 关联链接

- https://doi.org/10.5281/zenodo.23778742
- https://github.com/cjus/audio-chat-box:
- https://github.com/kishormorol/cli-faq-shortcuts:
- https://github.com/saranyan/breakout-coordinator:
- https://zenodo.org/badge/DOI/10.5281/zenodo.23778742.svg

## 导航

- 项目页：[[10-项目/zenodo.org_650700cf]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
