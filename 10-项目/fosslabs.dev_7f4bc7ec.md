---
type: "project"
title: "Had an idea for air-gapped file transfer, broke 32+ Mbps"
project_url: "https://fosslabs.dev/"
first_seen: "2026-10-26T09:43:44+08:00"
sources:
  - reddit
tags:
  - 项目
  - reddit
  - r/SideProject
lang: "en"
---

# Had an idea for air-gapped file transfer, broke 32+ Mbps

> [!info] 一句话导读
> Hi everyone! I was looking at optical file transfer and saw that Decimen was rather ineffective. Firstly, it's QR-based system really seemed to be designed for …

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://fosslabs.dev/>
> 首次收录：2026-10-26T09:43:44+08:00
> 来源渠道：Reddit 独立开发版块
> 标签：r/SideProject
> 最新指标：得分=9 · 评论=6 · 赞踩比=0.8461538461538461

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-26T09:43:44+08:00 | Reddit 独立开发版块 | 得分=9 · 评论=6 · 赞踩比=0.8461538461538461 | [[20-语料/posts/reddit/2026-10-26/8ee2ae4187a4b80c_Had-an-idea-for-air-gapped-file-transfer,-broke-32]] |

## 摘要正文

Hi everyone! I was looking at optical file transfer and saw that Decimen was rather ineffective. Firstly, it's QR-based system really seemed to be designed for paper, where binary design is necessary to  prevent ink smudging. On a screen, binary is ineffecient, although luminance makes sense. I looked at a lot of research papers and eventually found this:I saw that OFDM was the logical improvement off QR codes, as it used actual signal processing and luminance instead of binary black-and-white QR. So I decided to base my system off FOCUS. For fast decoding, I also wanted it to be GPU based rather than CPU based, and to deal with frame desync well.  [https://vs.inf.ethz.ch/publ/papers/soeroesg-mobisys2016-Focus.pdf](https://vs.inf.ethz.ch/publ/papers/soeroesg-mobisys2016-Focus.pdf) After that, I stripped the FOCUS finders (the original finders were ugly and wasted a lot of space) and came up with a custom, compact ring. the ring has around 15 bits of information distributed via Reed Solomon along the giant ring. A GPU can easily decode the ring's RS it by brute forcing the maximum likelihood of each of the 32,768 codewords.  To balance between range and maximizing speed, i created 4…
