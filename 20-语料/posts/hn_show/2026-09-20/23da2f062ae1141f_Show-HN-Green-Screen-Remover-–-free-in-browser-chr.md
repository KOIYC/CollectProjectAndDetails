---
type: "corpus"
item_id: "23da2f062ae1141f"
title: "Show HN: Green Screen Remover – free in-browser chroma key, nothing uploaded"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49749795"
project_url: "https://greenscreenremover.net/"
author: "wangqing333"
published_at: "2026-09-18T03:09:02Z"
captured_at: "2026-09-20T09:36:43+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-18"
tags:
  - 语料
  - hn_show
  - author_wangqing333
  - story_49749795
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: Green Screen Remover – free in-browser chroma key, nothing uploaded

> [!info] 一句话导读
> Green Screen Remover — Remove Green Screen from Video & Image

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49749795>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：wangqing333　|　发布：2026-09-18T03:09:02Z
> 项目链接：<https://greenscreenremover.net/>
> 采集：2026-09-20T09:36:43+08:00　|　id：`23da2f062ae1141f`

## 正文

# Green Screen Remover — Remove Green Screen from Video & Image

> Source: https://greenscreenremover.net/

Drop a video or an image shot on a green or blue screen. The backdrop is keyed out inside this browser tab — nothing is uploaded.

Drop a video or an image here

or choose a file — you can paste from the clipboard too

Runs locally in this browser tab · no upload · no account · no watermark

Raise it if patches of the screen survive. Lower it if part of the subject disappears.

Takes the green cast off hair, skin and light clothing.

## What this green screen remover does

This page is a chroma key tool for video and images. It reads the colour of the backdrop you shot against, makes those pixels transparent, and pulls the green light that bounced onto your subject back out of the edges. You get the cutout as a transparent PNG, as a PNG sequence for a clip, or as a transparent WebM video.

Everything is computed by the browser on your own machine. The file you drop never leaves the tab — there is no upload step, no account and no watermark.

## Supported formats

- Video: MP4 (H.264), WebM (VP8/VP9), and MOV or OGV when your browser can decode them. Anything the browser can play will key.
- Image: PNG, JPEG, WebP, GIF (first frame), BMP, and AVIF where the browser supports it.
- Output: transparent PNG at the full resolution of the original, a ZIP of transparent PNG frames, or a transparent WebM (VP9) recorded from the keyed canvas.
Your browser is the limit, not this page: if it cannot decode the file, the page says so instead of pretending to work.

## How to remove a green screen

- Drop your file. Drag a clip or a photo onto the page, choose one from your device, or paste an image from the clipboard. The green screen is detected from the border of the frame and keyed out straight away.
- Fix what the key got wrong. Tolerance decides how far from the key colour a pixel can be and still count as background. Edge trims the thin green halo off the outline or softens a jagged one. Spill removal pulls the green cast off the subject itself.
- Check it. Drag the divider to compare the original with the result, and switch the preview background between a checkerboard, dark and light so you can see the transparency honestly.
- Take the result. Download a transparent PNG. For a clip you can also export the current frame, a PNG sequence for the whole clip, or a transparent WebM.

## How the key works

Each pixel is converted to YCbCr, the colour space broadcast equipment has always keyed in, where Cb and Cr carry the colour and Y carries the brightness. The distance from the key colour is measured in the Cb/Cr plane only, so a light shadow falling across the screen — the same green, just slightly darker — still keys out, though deep shadows and underexposed footage call for a higher tolerance, which you can set by hand. A plain "delete every pixel near this RGB value" comparison leaves those shadows behind.

That reasoning breaks on a neutral backdrop: white, black and grey all sit at the same point in the Cb/Cr plane, so a chroma key cannot tell a white wall from a white shirt. When the key colour has almost no saturation this page measures brightness instead and keys on luminance, which is the only thing that can separate them.

## Frequently asked questions

### How do I remove a green screen from a video?

Drop the clip on the page. The key colour is read from the first frame, every frame is keyed as it plays, and the preview shows the result live. When it looks right, export a transparent WebM or a PNG sequence.

### How do I remove a green screen from an image?

Drop the photo and the background is gone on arrival. Adjust tolerance, edge and spill if the cutout needs help, then download the transparent PNG.

### Is this green screen background remover free?

Yes. No account, no sign-up, no watermark and no limit on how many files you key. There is nothing to buy because nothing runs on a server — your own machine does the work.

### Are my files uploaded anywhere?

No. The page decodes and keys the file with the Canvas API inside the tab. It keeps working if you go offline after it has loaded.

### Can I key a blue screen, or another colour?

Yes. Pick the blue or magenta preset, use the colour picker, or press Pick from media and click the backdrop in the preview. Any solid backdrop colour can be the key.

### Why is there still a green edge around my subject?

That is spill — green light from the screen bouncing onto hair, shoulders and light clothing. Drag Edge to the left to trim the contaminated rim, and raise Spill removal to neutralise the cast that landed on the subject.

### Does the exported video keep its transparency?

The WebM export is recorded from a canvas that has an alpha channel, and it keeps it — verified by decoding the file back and reading the alpha of a transparent pixel. Whether a player shows it is a different matter: VLC, Chrome, Edge and most editors show the transparency, while many video players and social platforms paint transparent video on black. The PNG and PNG-sequence exports always keep alpha everywhere.

### Is there a length limit on the video?

No cap is imposed by this page. The limits are your machine's memory and the browser's decoder. Two practical notes: the WebM export records in real time, so a 30-second clip takes about 30 seconds, and a PNG sequence is heavy — a one-minute clip at 12 frames per second is 720 files.

### Why did my subject lose a piece, or why is a green prop gone?

A key decides by colour alone, so anything the same colour as the screen goes with it. Lower the tolerance, or pick a key colour further from the subject. Unlike some tools on this page there is no manual brush, so colour is the only lever — that is stated here rather than hidden behind a button that does not exist.

## What happens after the cutout

This page stops at the key. It hands you a transparent PNG, a PNG sequence or a transparent WebM, and it deliberately does not trim the clip, put the subject on a new background, add titles or export an MP4. Those are editor jobs, and a browser tab is the wrong place to do them.

If that is the next thing you need, a desktop option is Movavi Video Editor. It is a paid product made by Movavi — a company we are not part of, and this is not an official Movavi page.

The link above is an affiliate link: if you buy through it, we may earn a commission — the price you pay stays the same.

Some links on this site are affiliate links. If you buy through one, we may earn a commission — the price you pay stays the same.

Green screen remover · chroma key for video and images · runs entirely in your browser.

## 导航

- 项目页：[[10-项目/greenscreenremover.net_e3a32fc5]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
