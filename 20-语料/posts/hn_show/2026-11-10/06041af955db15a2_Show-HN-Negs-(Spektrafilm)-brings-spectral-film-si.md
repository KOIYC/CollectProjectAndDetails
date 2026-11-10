---
type: "corpus"
item_id: "06041af955db15a2"
title: "Show HN: Negs (Spektrafilm) brings spectral film simulations to the browser"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50431764"
project_url: "https://getnegs.com/try"
author: "haasisnoah"
published_at: "2026-11-09T20:41:22Z"
captured_at: "2026-11-10T09:49:42+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-10"
pub_day: "2026-11-09"
tags:
  - 语料
  - hn_show
  - author_haasisnoah
  - story_50431764
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Negs (Spektrafilm) brings spectral film simulations to the browser

> [!info] 一句话导读
> Hi HN, I'm Noah. Negs runs spektrafilm, Andrea Volpato's physically based film simulation, in your browser (it's completely rewritten in Rust and using WebGPU).…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50431764>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：haasisnoah　|　发布：2026-11-09T20:41:22Z
> 项目链接：<https://getnegs.com/try>
> 采集：2026-11-10T09:49:42+08:00　|　id：`06041af955db15a2`

## 正文

Hi HN, I'm Noah. Negs runs spektrafilm, Andrea Volpato's physically based film simulation, in your browser (it's completely rewritten in Rust and using WebGPU). Drop in a photo (JPEG, PNG, TIFF or a RAW), pick a film and a print paper, and drag the sliders. The picture updates as you drag, and nothing is uploaded: it all runs on your machine.Try it: https://getnegs.com/try/Code (GPLv3): https://github.com/noahhaasis/negsThere are also native apps on the same engine: SwiftUI on macOS, GTK4 on Linux, and Windows.Spektrafilm (it started life as agx-emulsion) isn't a LUT or a preset. It simulates the whole analog chain, negative and then print, using only the manufacturers' published datasheets. Andrea's original write-up on discuss.pixls.us is worth reading in full: https://discuss.pixls.us/t/spectral-film-simulations-from-sc.... Roughly, it goes like this:- Your RGB image is turned back into a light spectrum and exposed onto the film's three dye layers through their published spectral sensitivity curves.
- Each layer builds up density along its characteristic curve. Datasheet curves are measured with densitometers that see all three dyes at once, so they're first separated into a curve for each layer.
- DIR couplers: where one layer develops a lot of density, it releases inhibitors that hold back development nearby, in the same layer and the ones next to it. This is where film's saturation and its edge sharpness come from.
- Grain is simulated per layer, with fast and slow sub-layers, as random silver halide particles that become dye clouds. It depends on the density at each spot instead of being laid over the image.
- Halation: light passes through the emulsion, bounces off the film base and exposes the red layer again (it's at the back), which gives the red glow around highlights.
- The negative's dye spectra are then projected through a virtual enlarger with Y/M filtration onto print paper, which has its own sensitivities and curves, and the print is scanned back to RGB.Because it's a model, the controls are physical: camera exposure, print exposure, enlarger filters, how much DIR coupling, grain particle size, halation strength. Push them too far and the image breaks the way film does, with colour crossovers when it's badly over- or underexposed. And you can experimentw with each control. There are about 50 stocks: Portra, Ektar, Gold, Pro 400H, Superia, Kodachrome, Velvia and Provia slide film, Aerochrome and some B&W (HP5, FP4...). There are 9 papers and print films too, such as Endura, Crystal Archive and Vision 2383. The paper choice has a huge impact on the final look.Negs implements the entire chain and is orders of magnitudes faster than the original python Spektrafilm implementation, so you can play around with sliders and get live feedback.Feedback is very welcome, especially from people who have actually shot these stocks: tell me which ones look wrong to you.

## 关联链接

- https://discuss.pixls.us/t/spectral-film-simulations-from-sc....
- https://getnegs.com/try/Code
- https://github.com/noahhaasis/negsThere

## 导航

- 项目页：[[10-项目/getnegs.com_3e2eed9e]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
