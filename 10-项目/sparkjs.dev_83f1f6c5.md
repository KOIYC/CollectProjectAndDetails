---
type: "project"
title: "Show HN: Radix - A WebGPU-powered 3D Gaussian Splat renderer built on Three.js"
project_url: "https://sparkjs.dev/radix"
first_seen: "2026-10-30T09:46:09+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_dmarcos
  - story_50292475
  - show_hn
lang: "en"
---

# Show HN: Radix - A WebGPU-powered 3D Gaussian Splat renderer built on Three.js

> [!info] 一句话导读
> 3D Gaussian splats in typed-array tables on the CPU and GPU, drawn by three.js's WebGPURenderer on WebGPU or its WebGL2 backend. This site has the example pages…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://sparkjs.dev/radix>
> 首次收录：2026-10-30T09:46:09+08:00
> 来源渠道：HN Show HN
> 标签：author_dmarcos, story_50292475, show_hn
> 最新指标：点赞=10 · 评论=0 · engagement_velocity=10

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-30T09:46:09+08:00 | HN Show HN | 点赞=10 · 评论=0 · engagement_velocity=10 | [[20-语料/posts/hn_show/2026-10-30/dfe16f88479aa3f3_Show-HN-Radix-A-WebGPU-powered-3D-Gaussian-Splat-r]] |

## 摘要正文

Radix 3D Gaussian splats in typed-array tables on the CPU and GPU, drawn by three.js's WebGPURenderer on WebGPU or its WebGL2 backend. This site has the example pages, the documentation and the sources. The code The repository is github.com/sparkjsdev/radix ; the library (npm package @sparkjsdev/radix ) lives in src/ . Built from b831cc5 on 2026-10-29 Getting started Copy Code Copy the following code into an index.html file and serve it over http(s). It draws a butterfly on WebGPU, or on the WebGL2 backend where WebGPU is missing.   CDN   Radix imports three , three/webgpu and three/tsl , so the map names all three. The workers' code is inlined into the bundle, so there is no separate worker file to serve. NPM npm install three@0.186 @sparkjsdev/radix  From a local checkout instead (npm builds dist/ on install through the prepare script): cd radix && npm install # also builds dist/ cd ../my-app && npm install three@0.186 ../radix  TypeScript apps need TypeScript 5.7 or newer, and the WebGPU types: TypeScript 6's DOM types include them, older versions need @webgpu/types . Develop git clone git@github.com:sparkjsdev/radix.git cd radix npm install npm run build # dist/, the example pa…
