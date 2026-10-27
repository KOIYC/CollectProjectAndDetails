---
type: "project"
title: "我们开源了 OXR： 1.3B 文档解析模型，全球三榜第一，提供免费 API"
project_url: "https://free-oxr.somark.cn/"
first_seen: "2026-10-27T23:56:38+08:00"
sources:
  - v2ex
tags:
  - 项目
  - v2ex
  - 17
lang: "zh"
---

# 我们开源了 OXR： 1.3B 文档解析模型，全球三榜第一，提供免费 API

> [!info] 一句话导读
> 首先先自我介绍一下，我是 SoMark 团队的 CTO 。

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://free-oxr.somark.cn/>
> 首次收录：2026-10-27T23:56:38+08:00
> 来源渠道：V2EX
> 标签：17
> 最新指标：回复=0

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-27T23:56:38+08:00 | V2EX | 回复=0 | [[20-语料/posts/v2ex/2026-10-27/cca8df02bc648f6f_我们开源了-OXR-1.3B-文档解析模型,全球三榜第一,提供免费-API]] |

## 摘要正文

首先先自我介绍一下，我是 SoMark 团队的 CTO 。  我们最近开源了一个新的文档智能解析模型—— **OXR （ Optical Everything Recognition ）。**  它可以把 PDF 和文档图片转成 Markdown / JSON ，支持表格、公式、化学式、代码块等 13 类元素，并且解析结果中包含版面坐标信息。  **OXR 的主模型只有 1\.3B ，在全球****三项文档解析基准****测试中其****总分都排到了第一****：**OmniDocBench 97\.18 、olmOCR\-Bench 87\.84 、DocParsingBench 87\.76 。  速度也做了同条件实测：单张 RTX PRO 6000 Blackwell （ 96GB ），**解析 100 页从 OmniDocBench 里随机抽取的文档，OXR 平均用时约 101 秒，在参测的 21 个开源模型中最快，其中包括 Paddle 和 MinerU 。**  **OXR 创新采用 RSI 训练范式，结合巧妙的架构设计，达到了精度与速度双 SOTA 。同时 OXR 的版面分析模块独立、可插拔。**大家可以直接用我们的内置模型，也可以按照业务需求进行替换。  *OXR 项目地址：[https://github\.com/SoMarkAI/OXR]( https://github.com/SoMarkAI/OXR)*  下面向大家介绍一下 OXR 的具体使用方法。  ### 一、不部署，先跑一份文档  想先看看效果，可以直接打开 [在线 Demo]( https://free-oxr.somark.cn/)，上传 PDF 或文档图片，对照原文查看解析出的 Markdown 和版面结果。  **为了方便大家调用，我们也开放了免费 API ，不用注册，也不用申请 Key 。**装好 CLI ，就能把自己的 PDF 转成 Markdown 和 JSON：  ```Bash pip install somark  somark --base-url https://free-oxr.somark.cn/api/v1 --api-key dummy \   parse document.pdf --formats md,json --out ./parsed-output/ ```  把 `document.pdf` 换成你的文件路径，结果会保存到 `./parsed-output/`。其中 `dummy` 只是工具参数的占位值，不是真实 Key 。  *我们将持续提供免费 API 服务，直至我们的服务器顶不住压力。*  *⚠️ 注意：不建议将免费 API 用于线上环境，我们没有稳定性保证，也…
