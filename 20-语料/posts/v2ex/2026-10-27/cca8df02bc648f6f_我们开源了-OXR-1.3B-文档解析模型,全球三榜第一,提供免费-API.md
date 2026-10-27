---
type: "corpus"
item_id: "cca8df02bc648f6f"
title: "我们开源了 OXR： 1.3B 文档解析模型，全球三榜第一，提供免费 API"
source: "v2ex"
source_name: "V2EX"
url: "https://www.v2ex.com/t/1252155"
project_url: "https://free-oxr.somark.cn/"
author: "ybs885"
published_at: "2026-10-27T02:51:09"
captured_at: "2026-10-27T23:56:38+08:00"
lang: "zh"
kind: "post"
topic: "开发者工具"
shard: "2026-10-27"
pub_day: "2026-10-27"
tags:
  - 语料
  - v2ex
  - 17
metrics: {"replies": 0}
comments_count: 0
comments_total: 0
discovered_via: "v2ex:独立开发"
---

# 我们开源了 OXR： 1.3B 文档解析模型，全球三榜第一，提供免费 API

> [!info] 一句话导读
> 首先先自我介绍一下，我是 SoMark 团队的 CTO 。

> [!meta]- 语料信息（点开展开）
> 来源：V2EX（post）
> 原帖：<https://www.v2ex.com/t/1252155>
> 指标：回复=0
> 作者：ybs885　|　发布：2026-10-27T02:51:09
> 项目链接：<https://free-oxr.somark.cn/>
> 采集：2026-10-27T23:56:38+08:00　|　id：`cca8df02bc648f6f`

## 正文

首先先自我介绍一下，我是 SoMark 团队的 CTO 。

我们最近开源了一个新的文档智能解析模型—— **OXR （ Optical Everything Recognition ）。**

它可以把 PDF 和文档图片转成 Markdown / JSON ，支持表格、公式、化学式、代码块等 13 类元素，并且解析结果中包含版面坐标信息。

**OXR 的主模型只有 1\.3B ，在全球****三项文档解析基准****测试中其****总分都排到了第一****：**OmniDocBench 97\.18 、olmOCR\-Bench 87\.84 、DocParsingBench 87\.76 。

速度也做了同条件实测：单张 RTX PRO 6000 Blackwell （ 96GB ），**解析 100 页从 OmniDocBench 里随机抽取的文档，OXR 平均用时约 101 秒，在参测的 21 个开源模型中最快，其中包括 Paddle 和 MinerU 。**

**OXR 创新采用 RSI 训练范式，结合巧妙的架构设计，达到了精度与速度双 SOTA 。同时 OXR 的版面分析模块独立、可插拔。**大家可以直接用我们的内置模型，也可以按照业务需求进行替换。

*OXR 项目地址：[https://github\.com/SoMarkAI/OXR]( https://github.com/SoMarkAI/OXR)*

下面向大家介绍一下 OXR 的具体使用方法。

### 一、不部署，先跑一份文档

想先看看效果，可以直接打开 [在线 Demo]( https://free-oxr.somark.cn/)，上传 PDF 或文档图片，对照原文查看解析出的 Markdown 和版面结果。

**为了方便大家调用，我们也开放了免费 API ，不用注册，也不用申请 Key 。**装好 CLI ，就能把自己的 PDF 转成 Markdown 和 JSON：

```Bash
pip install somark

somark --base-url https://free-oxr.somark.cn/api/v1 --api-key dummy \
  parse document.pdf --formats md,json --out ./parsed-output/
```

把 `document.pdf` 换成你的文件路径，结果会保存到 `./parsed-output/`。其中 `dummy` 只是工具参数的占位值，不是真实 Key 。

*我们将持续提供免费 API 服务，直至我们的服务器顶不住压力。*

*⚠️ 注意：不建议将免费 API 用于线上环境，我们没有稳定性保证，也设置了排队机制，速率略有浮动。*

### 二、本地部署 OXR

本地部署的配置要求如下，准备好后下载我们提供的代码和模型，即可通过 Docker 或源码启动服务。

|项目|环境要求|
|---|---|
|操作系统|Linux|
|GPU|支持 BF16 的 NVIDIA GPU|
|驱动|兼容 CUDA 13\.0 的 NVIDIA 驱动|
|容器引擎|Docker （仅 Docker 启动需要）|
|GPU 容器支持|NVIDIA Container Toolkit （仅 Docker 启动需要）|
|Python|Python 3\.12 （用于下载模型和源码启动）|
|显存（起步建议）|单卡 24GB ，用于低并发试用|
|显存（推荐配置）|单卡 48GB 及以上，为长文档和较高并发预留空间|

**1\. 下载代码和模型。**权重可从 [Hugging Face]( https://huggingface.co/SoMarkAI/OXR-1.0) 或 [ModelScope]( https://modelscope.cn/models/SoMark/OXR-1.0) 获取，这里以 Hugging Face 为例：

```Bash
git clone https://github.com/SoMarkAI/OXR.git
cd OXR
pip install -U huggingface_hub
hf download SoMarkAI/OXR-1.0 --local-dir ./models/OXR-1.0
```

**2\. 启动服务。**推荐使用 docker 配置服务，一次性启动所有服务。首次启动可能较慢，默认启动等待上限为 900 秒。

```Bash
docker build -f docker/Dockerfile.allinone -t oxr-1.0 .
docker run --rm --gpus all --ipc=host \
  -p 127.0.0.1:8000:8000 \
  -v "$PWD/models/OXR-1.0:/models/oxr-model:ro" \
  oxr-1.0
```

**3\. 打开本地 Demo ，或通过 API 调用。**

等待启动日志显示服务就绪后，打开 `http://localhost:8000/demo` 上传文档即可查看解析结果；接口文档在 `http://localhost:8000/docs`。

也可以将前面 CLI 命令的 `--base-url` 改成 `http://localhost:8000/v1`，调用本地服务。

**源码启动方式、并发和显存参数等详细说明见 [**README**]( https://github.com/SoMarkAI/OXR/blob/main/README_CN.md)。**

### 三、配套的 SoMark 生态工具

此前我们团队围绕核心产品 「 SoMark 文档智能」开发了一系列生态工具，OXR 作为我们的独立开源模型，同样适配：

||一句话简介|项目地址|
|---|---|---|
|SoMarkDown|SoMark 、OXR 官方的 Markdown 解析与渲染库|[https://github\.com/SoMarkAI/SoMarkDown]( https://github\.com/SoMarkAI/SoMarkDown)|
|SoMarkDownViewer|SoMarkDown 的实时编辑应用|[https://github\.com/SoMarkAI/SoMarkDownViewer]( https://github\.com/SoMarkAI/SoMarkDownViewer)|
|SoPDF|高性能、宽松开源许可的 PDF 处理库|[https://github\.com/SoMarkAI/SoPDF]( https://github\.com/SoMarkAI/SoPDF)|
|Docision|面向文档场景的多模态 Jev|[https://github\.com/SoMarkAI/docision]( https://github\.com/SoMarkAI/docision)|
|somark\-py|服务 SoMark 、OXR 的官方 Python SDK \& CLI|[https://github\.com/SoMarkAI/somark\-py]( https://github.com/SoMarkAI/somark-py)|
|somark\-js|服务 SoMark 、OXR 的官方 JS / TS SDK \& CLI|[https://github\.com/SoMarkAI/somark\-js]( https://github\.com/SoMarkAI/somark\-js)|

欢迎拿你们手头难处理的文档来试试。哪里没解析对，可以 [点击这里]( https://free-oxr.somark.cn/feedback) 向我们反馈。

如果对大家有帮助，一定要给我们的项目点个 🌟 Star 支持一下～😉

### 相关链接

- GitHub：[https://github\.com/SoMarkAI/OXR]( https://github.com/SoMarkAI/OXR)

- Hugging Face：[https://huggingface\.co/SoMarkAI/OXR\-1\.0]( https://huggingface.co/SoMarkAI/OXR-1.0)

- ModelScope：[https://modelscope\.cn/models/SoMark/OXR\-1\.0]( https://modelscope.cn/models/SoMark/OXR-1.0)

- 在线 Demo：[https://free\-oxr\.somark\.cn/]( https://free-oxr.somark.cn/)

- 免费 API：[https://free\-oxr\.somark\.cn/api/v1]( https://free-oxr.somark.cn/api/v1)

- OXR 官网：[https://somark\.cn/oxr]( https://somark.cn/oxr)

## 关联链接

- http://localhost:8000/demo`
- http://localhost:8000/docs`。
- http://localhost:8000/v1`，调用本地服务。
- https://free
- https://free-oxr.somark.cn/api/v1
- https://free-oxr.somark.cn/feedback
- https://github
- https://github.com/SoMarkAI/OXR
- https://github.com/SoMarkAI/OXR.git
- https://github.com/SoMarkAI/OXR/blob/main/README_CN.md
- https://github.com/SoMarkAI/somark-py
- https://huggingface
- https://huggingface.co/SoMarkAI/OXR-1.0
- https://modelscope
- https://modelscope.cn/models/SoMark/OXR-1.0
- https://somark
- https://somark.cn/oxr

## 导航

- 项目页：[[10-项目/free-oxr.somark.cn_47a79eb6]]
- 渠道页：[[50-渠道/v2ex]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
