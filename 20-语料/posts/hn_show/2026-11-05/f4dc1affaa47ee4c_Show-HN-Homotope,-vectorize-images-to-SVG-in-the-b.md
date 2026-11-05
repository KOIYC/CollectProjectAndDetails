---
type: "corpus"
item_id: "f4dc1affaa47ee4c"
title: "Show HN: Homotope, vectorize images to SVG in the browser, MIT engine on NPM"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50370248"
project_url: "https://github.com/stevenroman91/homotope-engine"
author: "sroman91"
published_at: "2026-11-04T19:18:26Z"
captured_at: "2026-11-05T11:21:45+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-05"
pub_day: "2026-11-04"
tags:
  - 语料
  - hn_show
  - author_sroman91
  - story_50370248
  - show_hn
metrics: {"points": 3, "comments": 1, "engagement_velocity": 3}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Homotope, vectorize images to SVG in the browser, MIT engine on NPM

> [!info] 一句话导读
> stevenroman91/homotope-engine

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50370248>
> 指标：点赞=3 · 评论=1 · engagement_velocity=3
> 作者：sroman91　|　发布：2026-11-04T19:18:26Z
> 项目链接：<https://github.com/stevenroman91/homotope-engine>
> 采集：2026-11-05T11:21:45+08:00　|　id：`f4dc1affaa47ee4c`

## 正文

# stevenroman91/homotope-engine

Raster-to-vector engine (PNG/JPEG → SVG, DXF, PDF, EPS, centerline) in pure TypeScript: no DOM, no dependencies, runs in a Web Worker and in Node. Powers homotope.app. MIT, on npm as @homotope/engine. Public mirror produced from the private repo: releases are cut on engine-v* tags, not by PRs here.

- Stars: 0
- Forks: 0
- Watchers: 0
- Open issues: 0
- License: MIT License
- Homepage: https://homotope.app
- Default branch: main
- Created: 2026-10-07T12:06:34Z

## Languages

- JavaScript
- TypeScript

## Topics

- centerline
- dxf
- image-tracing
- png-to-svg
- png-to-svg-converter
- potrace-alternative
- raster-to-vector
- svg
- typescript
- vectorize
- web-worker

## Top Contributors

- stevenroman91 (1 contributions)

---

## README

# @homotope/engine

This is the engine of Homotope, an image vectorizer that runs in the
browser: nothing is uploaded. Try it in the workshop (free, no
account needed for SVG and PNG).

Raster-to-vector engine in pure TypeScript: turns a PNG or JPEG (any RGBA pixel buffer) into a
clean **SVG**, and from that SVG into **DXF**, **PDF** or **EPS**. Released under the MIT license.

**What this package is not**: it has no editor, no server, no REST API, no MCP server and no
printer checks; those live in the hosted service. The npm package is frozen at 0.2.0: what it
contains is complete and usable on its own.

- **No DOM, no runtime dependencies.** The core runs unchanged in a Web Worker, in the main
 thread and in Node. Pixel data stays on the machine: nothing is uploaded anywhere.
- **Topology first.** The image is quantized in OKLab, segmented into regions, and every shared
 boundary is fitted **once**: two neighbouring shapes never overlap and never leave a gap. Holes
 are kept (an "O" stays an "O").
- **Presets** for logos, illustrations, pixel art, line art, black & white, photos, and a
 **centerline** mode that traces strokes as single open paths (plotters, engraving, embroidery).
- **Fabrication exports**: DXF (layers per colour, shared edges cut once), PDF, EPS, colour
 separations, and a cut-readiness check (tiny islands, too-close edges, node counts).
- An alternative to Potrace: no GPL code, full colour, exact shared borders.

## Install

```bash
npm install @homotope/engine
# Node only, to decode PNG/JPEG files (optional peer dependencies):
npm install pngjs jpeg-js
```

Requires an ES2022 runtime (Node ≥ 22, any current browser). ESM only.

## Entry points

| Import | What | Dependencies |
| --------------------------- | ------------------------------------------------------------------ | ------------------ |
| `@homotope/engine` | `vectorize`, `presetOptions`, `PRESET_NAMES`, all types | none |
| `@homotope/engine/export` | `convertSvg` (SVG → PDF, DXF, EPS), `exportLayers`, `sceneFromSvg` | none |
| `@homotope/engine/cutcheck` | `checkSvg`, `simplifySvg`: cut-readiness report for cutters | none |
| `@homotope/engine/node` | `decodePng`, `decodeJpeg`, `encodePng`, `encodeJpeg` | `pngjs`, `jpeg-js` |

Browser bundles only receive what they import: the core never imports `pngjs` or `jpeg-js`.

## Node example

```ts
import { readFileSync, writeFileSync } from 'node:fs';
import { vectorize, presetOptions } from '@homotope/engine';
import { convertSvg } from '@homotope/engine/export';
import { decodePng } from '@homotope/engine/node';

const image = decodePng(new Uint8Array(readFileSync('logo.png')));
const result = vectorize(image, presetOptions('logo'), {
  onProgress: (e) => process.stdout.write(`\r${e.stage} ${Math.round(e.progress * 100)}%`),
});

writeFileSync('logo.svg', result.svg);
writeFileSync('logo.dxf', convertSvg(result.svg, 'dxf'));
console.log(`\n${result.palette.colors.length} colours, ${result.stats.paths} paths`);
```

## Browser example (Web Worker)

`vectorize` is synchronous on purpose: run it in a worker so the page stays responsive. Its
input is any `ImageData`-like object `{ width, height, data: Uint8ClampedArray }` (RGBA, not
premultiplied).

```ts
// main.ts
const bitmap = await createImageBitmap(file);
const canvas = new OffscreenCanvas(bitmap.width, bitmap.height);
const ctx = canvas.getContext('2d')!;
ctx.drawImage(bitmap, 0, 0);
const { width, height, data } = ctx.getImageData(0, 0, bitmap.width, bitmap.height);

const worker = new Worker(new URL('./vectorize.worker.ts', import.meta.url), { type: 'module' });
worker.onmessage = (e: MessageEvent<{ svg: string }>) => {
  const url = URL.createObjectURL(new Blob([e.data.svg], { type: 'image/svg+xml' }));
  document.querySelector<HTMLImageElement>('#preview')!.src = url; // or offer it as a download
};
worker.postMessage({ width, height, data }, [data.buffer]);
```

```ts
// vectorize.worker.ts
import { vectorize, presetOptions, type RasterImage } from '@homotope/engine';

self.onmessage = (e: MessageEvent<RasterImage>) => {
  const { svg } = vectorize(e.data, presetOptions('illustration'));
  self.postMessage({ svg });
};
```

Cancellation is cooperative: pass `{ cancel: { cancelled: boolean } }` as the third argument
(for example backed by a `SharedArrayBuffer`); `vectorize` then throws a `CancelledError`
between and inside stages.

## Presets

`presetOptions(name)` returns a full, independent options object that you can tweak.

| Preset | For |
| -------------- | ------------------------------------------------------------------- |
| `logo` | Flat colours, crisp corners, straight lines kept straight |
| `illustration` | Up to 32 colours, smoother curves, light gradients, stacked shapes |
| `pixel-art` | Exact pixel grid, no curves, zero error |
| `line-art` | Ink drawings and text: two colours, filled shapes |
| `centerline` | Strokes traced as single open paths (plotter, laser engraving) |
| `black-white` | Two colours from an automatic (Otsu) threshold |
| `photo` | Up to 64 colours, denoising, small regions absorbed, stacked shapes |

```ts
import { presetOptions, vectorize } from '@homotope/engine';

const options = presetOptions('logo');
options.quantize.colors = 4; // fixed number of colours instead of 'auto'
options.export.precision = 1; // decimals in path data
options.export.mode = 'stacked'; // fewer nodes: shapes stacked instead of cut out
const { svg } = vectorize(image, options);
```

Every option is typed and documented in `VectorizeOptions` (`preprocess`, `quantize`,
`segment`, `fit`, `export`, `centerline`).

## SVG output

- `viewBox` in the pixel coordinates of the original image, cubic Béziers, one ` ` per
 colour by default (`export.mergeByColor`).
- `export.mode: 'cut'` (default): every region is an exact path with its holes
 (`fill-rule="evenodd"`), no overlap; `'stacked'`: shapes stacked by depth, fewer nodes.
- Transparent pixels (`preprocess.alphaMode: 'keep'`) produce no path.
- `result.palette` lists the colours (sRGB and OKLab, pixel counts); `result.stats` the number
 of paths and nodes; `result.timings` the time spent per stage.

## Hosted version and API

homotope.app runs this engine in the browser with a visual editor
(palette, presets, before/after), plus optional server processing, a REST API and an MCP
server for AI assistants: see the API documentation.

## Development

```bash
npm install
npm test           # Vitest, no DOM
npm run typecheck
npm run lint
npm run eval       # renders every fixture and measures the error (Resvg)
npm run build      # dist/ (ESM + .d.ts)
```

See CONTRIBUTING.md.

## License

MIT.

# skerrysoft/safeagent

## 评论（1/1）

> **ggm** · 2026-11-04T20:03:39.000Z　
> Very nice gui. Did exactly what I'd want and expected.

## 关联链接

- https://homotope.app

## 导航

- 项目页：[[10-项目/github.com_05bce895]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
