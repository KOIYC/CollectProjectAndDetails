---
type: "project"
title: "Show HN: Negs (Spektrafilm) brings spectral film simulations to the browser"
project_url: "https://getnegs.com/try"
first_seen: "2026-11-10T09:49:42+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_haasisnoah
  - story_50431764
  - show_hn
lang: "en"
---

# Show HN: Negs (Spektrafilm) brings spectral film simulations to the browser

> [!info] 一句话导读
> Hi HN, I'm Noah. Negs runs spektrafilm, Andrea Volpato's physically based film simulation, in your browser (it's completely rewritten in Rust and using WebGPU).…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://getnegs.com/try>
> 首次收录：2026-11-10T09:49:42+08:00
> 来源渠道：HN Show HN
> 标签：author_haasisnoah, story_50431764, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-10T09:49:42+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-11-10/06041af955db15a2_Show-HN-Negs-(Spektrafilm)-brings-spectral-film-si]] |

## 摘要正文

Hi HN, I'm Noah. Negs runs spektrafilm, Andrea Volpato's physically based film simulation, in your browser (it's completely rewritten in Rust and using WebGPU). Drop in a photo (JPEG, PNG, TIFF or a RAW), pick a film and a print paper, and drag the sliders. The picture updates as you drag, and nothing is uploaded: it all runs on your machine.Try it: https://getnegs.com/try/Code (GPLv3): https://github.com/noahhaasis/negsThere are also native apps on the same engine: SwiftUI on macOS, GTK4 on Linux, and Windows.Spektrafilm (it started life as agx-emulsion) isn't a LUT or a preset. It simulates the whole analog chain, negative and then print, using only the manufacturers' published datasheets. Andrea's original write-up on discuss.pixls.us is worth reading in full: https://discuss.pixls.us/t/spectral-film-simulations-from-sc.... Roughly, it goes like this:- Your RGB image is turned back into a light spectrum and exposed onto the film's three dye layers through their published spectral sensitivity curves. - Each layer builds up density along its characteristic curve. Datasheet curves are measured with densitometers that see all three dyes at once, so they're first separated into a cur…
