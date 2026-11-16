---
type: "corpus"
item_id: "3858ecabc5476b12"
title: "Show HN: Daily GPU Rental Prices Across AWS, Azure, RunPod and Vast.ai"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50449232"
project_url: "https://taipeiledger.com/gpu"
author: "khoonie"
published_at: "2026-11-11T02:50:01Z"
captured_at: "2026-11-11T13:37:17+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-11"
pub_day: "2026-11-11"
tags:
  - 语料
  - hn_show
  - author_khoonie
  - story_50449232
  - show_hn
metrics: {"points": 6, "comments": 2, "engagement_velocity": 6}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:3d"
---

# Show HN: Daily GPU Rental Prices Across AWS, Azure, RunPod and Vast.ai

> [!info] 一句话导读
> GPU rental prices

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50449232>
> 指标：点赞=6 · 评论=2 · engagement_velocity=6
> 作者：khoonie　|　发布：2026-11-11T02:50:01Z
> 项目链接：<https://taipeiledger.com/gpu>
> 采集：2026-11-11T13:37:17+08:00　|　id：`3858ecabc5476b12`

## 正文

GPU rental prices · Taipei Ledger

# GPU rental prices

What one GPU-hour costs to rent, in US dollars, by GPU model and provider. Prices of 11 November 2026.

| GPU | AWS on-demand | Azure pay-as-you-go | RunPod Secure Cloud | RunPod Community | Vast.ai marketplace median | Range |
| --- | --- | --- | --- | --- | --- | --- |
| B300 288 GB | $17.80 | – | $8.99 | $6.94 | $9.94 from $9.94 · 2 offers | $6.94 – $17.80 |
| B200 180 GB | $14.24 | – | $7.99 | $5.98 | $10.00 from $6.25 · 15 offers | $5.98 – $14.24 |
| H200 141 GB | $7.91 | – | $5.29 | $3.59 | $4.34 from $2.90 · 25 offers | $2.90 – $7.91 |
| H100 SXM 80 GB | $6.88 | $12.29 * | $3.99 | $2.69 | $2.94 from $1.34 · 21 offers | $1.34 – $12.29 |
| H100 PCIe / NVL 80–94 GB | – | $6.98 * | $2.89 | $1.99 | $2.54 from $2.14 · 17 offers | $1.99 – $6.98 |
| A100 80GB 80 GB | $3.43 | $4.10 * | $1.79 | $1.19 | $1.10 from $0.84 · 24 offers | $0.84 – $4.10 |
| MI300X 192 GB | – | – | $2.39 | – | – | |
| L40S 48 GB | $1.86 | – | $1.09 | $0.79 | $0.80 from $0.47 · 19 offers | $0.47 – $1.86 |
| RTX PRO 6000 96 GB | – | – | $2.49 | $1.69 | $1.66 from $0.87 · 76 offers | $0.87 – $2.49 |
| RTX 5090 32 GB | – | – | $1.19 | $0.69 | $0.55 from $0.33 · 64 offers | $0.33 – $1.19 |
| RTX 4090 24 GB | – | – | $0.89 | $0.34 | $0.46 from $0.34 · 64 offers | $0.34 – $0.89 |

Hover a price for the instance it comes from. * = source not updated today; last price shown.

## Price history

Daily since 02 November 2026.

B300: US$ per GPU-hour

AWS RunPod Secure RunPod Community Vast.ai median

B200: US$ per GPU-hour

AWS RunPod Secure RunPod Community Vast.ai median

H200: US$ per GPU-hour

AWS RunPod Secure RunPod Community Vast.ai median

H100 SXM: US$ per GPU-hour

AWS Azure RunPod Secure RunPod Community Vast.ai median

H100 PCIe / NVL: US$ per GPU-hour

Azure RunPod Secure RunPod Community Vast.ai median

A100 80GB: US$ per GPU-hour

AWS Azure RunPod Secure RunPod Community Vast.ai median

MI300X: US$ per GPU-hour

RunPod Secure

L40S: US$ per GPU-hour

AWS RunPod Secure RunPod Community Vast.ai median

RTX PRO 6000: US$ per GPU-hour

RunPod Secure RunPod Community Vast.ai median

RTX 5090: US$ per GPU-hour

RunPod Secure RunPod Community Vast.ai median

RTX 4090: US$ per GPU-hour

RunPod Secure RunPod Community Vast.ai median

## How these prices are measured

- Per GPU-hour. Clouds rent whole machines, so a machine's hourly price is divided by the GPUs in it (for example AWS p5.48xlarge, 8 × H100, ÷ 8). Compute only: storage, network and support are extra and differ by provider.
- List prices. AWS (US East, N. Virginia) and Azure (East US) on-demand Linux prices; RunPod Secure Cloud (its own data centres) and Community Cloud (third-party hosts). Committed-use and reserved prices are usually lower and are not shown.
- Marketplace. Vast.ai lists machines offered by many independent hosts worldwide; the median and the lowest per-GPU price of the rentable on-demand offers that day, with the number of offers. Few offers means the figure can swing.
- Checks. A list price that moves more than 50% in a day is held at the previous value until checked.

| GPU | AWS instance | Azure VM |
| --- | --- | --- |
| B300 | p6-b300.48xlarge ÷ 8 | – |
| B200 | p6-b200.48xlarge ÷ 8 | – |
| H200 | p5en.48xlarge ÷ 8 | – |
| H100 SXM | p5.48xlarge ÷ 8 | Standard_ND96isr_H100_v5 ÷ 8 |
| H100 PCIe / NVL | – | Standard_NC40ads_H100_v5 ÷ 1 |
| A100 80GB | p4de.24xlarge ÷ 8 | Standard_ND96amsr_A100_v4 ÷ 8 |
| MI300X | – | – |
| L40S | g6e.xlarge ÷ 1 | – |
| RTX PRO 6000 | – | – |
| RTX 5090 | – | – |
| RTX 4090 | – | – |

Did You Know

Taiwan and the UK have established a bilateral arrangement covering semiconductors, space, communications, net zero and AI standards.

# OddlyGoods/peep-note

## 评论（2/2）

> **mrbungie** · 2026-11-11T04:02:15.000Z　
> YMMV as this is just the compute as far as I can tell. You should also take into account ingress and egress somehow. For example some Vast.ai hosts will charge 40 USD per TB for both, it is a known "scam".

---

> **bradknowles** · 2026-11-11T05:10:19.000Z　
> And AWS is known to charge a lot for ingress and egress. This should definitely be accounted for.

## 导航

- 项目页：[[10-项目/taipeiledger.com_5412cb37]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
