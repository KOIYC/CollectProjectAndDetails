---
type: "corpus"
item_id: "dfe16f88479aa3f3"
title: "Show HN: Radix - A WebGPU-powered 3D Gaussian Splat renderer built on Three.js"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50292475"
project_url: "https://sparkjs.dev/radix"
author: "dmarcos"
published_at: "2026-10-29T17:10:49Z"
captured_at: "2026-10-30T09:46:09+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-30"
pub_day: "2026-10-29"
tags:
  - 语料
  - hn_show
  - author_dmarcos
  - story_50292475
  - show_hn
metrics: {"points": 10, "comments": 0, "engagement_velocity": 10}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Radix - A WebGPU-powered 3D Gaussian Splat renderer built on Three.js

> [!info] 一句话导读
> 3D Gaussian splats in typed-array tables on the CPU and GPU, drawn by three.js's WebGPURenderer on WebGPU or its WebGL2 backend. This site has the example pages…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50292475>
> 指标：点赞=10 · 评论=0 · engagement_velocity=10
> 作者：dmarcos　|　发布：2026-10-29T17:10:49Z
> 项目链接：<https://sparkjs.dev/radix>
> 采集：2026-10-30T09:46:09+08:00　|　id：`dfe16f88479aa3f3`

## 正文

Radix
3D Gaussian splats in typed-array tables on the CPU and GPU, drawn by three.js's WebGPURenderer on WebGPU or its WebGL2 backend. This site has the example pages, the documentation and the sources.
The code
The repository is github.com/sparkjsdev/radix ; the library (npm package @sparkjsdev/radix ) lives in src/ .
Built from b831cc5 on 2026-10-29
Getting started
Copy Code
Copy the following code into an index.html file and serve it over http(s). It draws a butterfly on WebGPU, or on the WebGL2 backend where WebGPU is missing.

 CDN

 Radix imports three , three/webgpu and three/tsl , so the map names all three. The workers' code is inlined into the bundle, so there is no separate worker file to serve.
NPM
npm install three@0.186 @sparkjsdev/radix
 From a local checkout instead (npm builds dist/ on install through the prepare script):
cd radix && npm install # also builds dist/
cd ../my-app && npm install three@0.186 ../radix
 TypeScript apps need TypeScript 5.7 or newer, and the WebGPU types: TypeScript 6's DOM types include them, older versions need @webgpu/types .
Develop
git clone git@github.com:sparkjsdev/radix.git
cd radix
npm install
npm run build # dist/, the example pages and the test pages
npm run serve # http://localhost:8000
 Then open:
Examples and Spark ports: http://localhost:8000/build/examples/
Docs: http://localhost:8000/docs/
To build and preview this site:
npm run build:site # into build/site/
npm run serve:site # http://localhost:8002/
On this site
Examples The example pages (splat viewer, scenes, WebXR, games, fractals) and the ports of the SparkJS examples.
 Spark ports Every SparkJS 2.3.1 example: ported, partial or blocked, and why.
 Documentation How Radix works, the API reference, recipes, and the comparison with SparkJS.
 Sources The library and example sources, highlighted, with a file tree.

## 关联链接

- http://localhost:8000
- http://localhost:8000/build/examples/
- http://localhost:8000/docs/
- http://localhost:8002/
- https://cdn.jsdelivr.net/npm/@sparkjsdev/radix@0.0.1/dist/radix.module.js
- https://cdn.jsdelivr.net/npm/three@0.186.0/build/three.tsl.js
- https://cdn.jsdelivr.net/npm/three@0.186.0/build/three.webgpu.js
- https://cdn.jsdelivr.net/npm/three@0.186.0/examples/jsm/
- https://storage.googleapis.com/forge-dev-public/asundqui/radix/261009/rdx/butterfly-ai.rdx

## 导航

- 项目页：[[10-项目/sparkjs.dev_83f1f6c5]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
