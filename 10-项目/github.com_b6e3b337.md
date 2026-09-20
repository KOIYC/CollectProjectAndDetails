---
type: "project"
title: "Show HN: Open-source passive NFC tag that signs with ECDSA, verified on-chain"
project_url: "https://github.com/mwbpNFTechnology/toluTag"
first_seen: "2026-09-20T09:37:17+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_boust16
  - story_49712073
  - show_hn
lang: "en"
---

# Show HN: Open-source passive NFC tag that signs with ECDSA, verified on-chain

> [!info] 一句话导读
> mwbpNFTechnology/toluTag

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/mwbpNFTechnology/toluTag>
> 首次收录：2026-09-20T09:37:17+08:00
> 来源渠道：HN Show HN
> 标签：author_boust16, story_49712073, show_hn
> 最新指标：点赞=9 · 评论=0 · engagement_velocity=9

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=9 · 评论=0 · engagement_velocity=9 | [[20-语料/posts/hn_show/2026-09-20/68e526205d1865b1_Show-HN-Open-source-passive-NFC-tag-that-signs-wit]] |
| 2026-09-20T09:37:17+08:00 | HN Show HN | 点赞=9 · 评论=0 · engagement_velocity=9 | [[20-语料/posts/hn_show/2026-09-20/68e526205d1865b1_Show-HN-Open-source-passive-NFC-tag-that-signs-wit]] |

## 摘要正文

# mwbpNFTechnology/toluTag  Open-source passive NFC tag signing ECDSA, bridging the physical world to on-chain validation.  - Stars: 6 - Forks: 1 - Watchers: 6 - Open issues: 0 - Default branch: main - Created: 2026-09-10T12:55:06Z  ## Languages  - Java - Solidity - TypeScript  ## Top Contributors  - DorenBoust (1 contributions)  ---  ## README  # toluTag  ***T**ouch-point **O**n-chain **L**inked **U**niverse. Bridging the physical world to decentralized, on-chain validation.*  toluTag app walkthrough  Open tooling for provisioning and using **NXP SE05x** secure elements as NFC-readable Ethereum signers.  toluTag is the **root of trust** that links a real-world object to on-chain validation. The tag is the primitive; what you build on top is up to you.  A toluTag is a passive NFC tag carrying an SE05x secure element. A secp256k1 key pair is generated **on the chip** and never leaves it; the private key is not extractable by design. The chip's public key yields an Ethereum address, and the chip can sign EIP-191 messages and EIP-712 typed data on demand, so a physical object can produce signatures that any Ethereum verifier (on-chain or off-chain) can check against a fixed address.  …
