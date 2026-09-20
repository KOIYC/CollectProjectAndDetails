---
type: "corpus"
item_id: "33b5e6c4a827167e"
title: "Show HN: Three Slicer, I ported OrcaSlicer to run in the browser"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49508763"
project_url: "https://slicer.kimgh06.com/"
author: "kimgh06"
published_at: "2026-08-31T12:18:38Z"
captured_at: "2026-09-21T03:11:23+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-08-31"
tags:
  - 语料
  - hn_show
  - author_kimgh06
  - story_49508763
  - show_hn
metrics: {"points": 4, "comments": 2, "engagement_velocity": 4}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:52d"
---

# Show HN: Three Slicer, I ported OrcaSlicer to run in the browser

> [!info] 一句话导读
> Three Slicer — an online 3D printing slicer that runs in your browser

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49508763>
> 指标：点赞=4 · 评论=2 · engagement_velocity=4
> 作者：kimgh06　|　发布：2026-08-31T12:18:38Z
> 项目链接：<https://slicer.kimgh06.com/>
> 采集：2026-09-21T03:11:23+08:00　|　id：`33b5e6c4a827167e`

## 正文

Three Slicer — an online 3D printing slicer that runs in your browser
Three Slicer converts STL, OBJ, 3MF, AMF, PLY and STEP models into G-code directly in the
 browser, using a WebAssembly build of the OrcaSlicer kernel. There is nothing to install and
 nothing is uploaded to a server — the slicing runs on your own machine, in the tab.
 Open the slicer .
What it does
Import — STL, OBJ, 3MF, AMF and PLY, plus STEP through a loader that only
 downloads when a STEP file is opened. Drag and drop, several models at once.
Arrange — move, rotate, scale, duplicate, split to objects, place on bed,
 and lay work out across multiple plates.
Slice — Arachne variable-width walls, gyroid / honeycomb / crosshatch
 infill, tree and grid supports, support painting and material painting, skirt, brim, raft,
 ironing, arc fitting, and multi-material printing with a real prime tower.
Resin — mSLA printers are a second technology in the same kernel: support
 points, support tree and pad come from PrusaSlicer 2.9.6's own chain, previewed as layer masks
 and written out as an .sl1 archive, which can also be opened again.
Preview — a layer slider and single-layer view, travel moves, and toolpath
 colouring by feature, speed, layer height, extrusion width, fan speed or temperature.
Export — G-code with print-time and filament-usage estimates, an
 .sl1 archive for resin, or a .3mf project that keeps the plate
 layout, settings and painting.
Settings — the full OrcaSlicer option set, 976 options, with search and a
 simple/advanced/expert filter.
Questions
Do my models get uploaded anywhere?
No. The slicing kernel is compiled to WebAssembly and runs inside the browser tab, so the model
 file never leaves the machine it was opened on. There is no account and no server-side queue.
Which file formats can it slice?
STL, OBJ, 3MF, AMF and PLY are read directly, and STEP is read through a loader that is only
 fetched when a STEP file is actually opened; an .sl1 resin archive can be opened as
 well. The output is G-code for filament printers, or an .sl1 archive for resin ones.
Is it based on a real slicer?
Yes. The kernel is a port of OrcaSlicer ,
 itself a PrusaSlicer and Slic3r descendant. Arachne wall generation, tree supports,
 multi-material segmentation and the prime tower are ported from that source rather than
 reimplemented, so the toolpaths come from the same code a desktop slicer runs. The resin
 support-point generator, support tree and pad are ported from PrusaSlicer 2.9.6 the same way.
Can I use the slicer in my own site or app?
Yes, as two npm packages.
 three-slicer (AGPL-3.0-or-later) is the
 slicing kernel for Node or the browser.
 three-slicer-viewer (MIT) is the React
 viewer and settings panel on their own — model and G-code preview with no slicing and no AGPL code,
 usable in closed-source products. Installing three-slicer gives you both. The
 integration demos show it embedded in an
 instant-quote form, a printer showcase and a CAD page, and the source is on
 GitHub .
How it was built
Porting OrcaSlicer to WebAssembly — what actually
 broke : the missing PrintObject , a TBB header stub that runs serial by default,
 COOP/COEP cross-origin isolation and the two kernel builds behind it, the partial-link build
 groups, and the byte-identical G-code gate the whole port is checked against.
 About the project covers what it deliberately does not do, how the output is
 verified, and what AGPL-3.0 means for using it.

## 评论（2/2）

> **stan-ely** · 2026-08-31T13:12:03.000Z　
> have never been comfortable with 3d models, even though have had my fair share of encounters. its sure is cool what is possible as a static website

---

> **DylanMerigaud** · 2026-08-31T14:03:27.000Z　
> Great effort, wishing you luck with it.

## 导航

- 项目页：[[10-项目/slicer.kimgh06.com_3b95219c]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
