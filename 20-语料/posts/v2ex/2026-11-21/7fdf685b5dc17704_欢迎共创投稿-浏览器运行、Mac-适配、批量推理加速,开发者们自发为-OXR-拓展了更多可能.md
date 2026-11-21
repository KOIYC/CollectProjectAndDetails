---
type: "corpus"
item_id: "7fdf685b5dc17704"
title: "欢迎共创投稿｜浏览器运行、Mac 适配、批量推理加速，开发者们自发为 OXR 拓展了更多可能"
source: "v2ex"
source_name: "V2EX"
url: "https://www.v2ex.com/t/1258648"
project_url: "https://free-oxr.somark.cn/feedback"
author: "ybs885"
published_at: "2026-11-20T12:49:28"
captured_at: "2026-11-21T14:55:12+08:00"
lang: "zh"
kind: "post"
topic: 开发者工具
shard: "2026-11-21"
pub_day: "2026-11-20"
tags:
  - 语料
  - v2ex
  - 17
metrics: {"replies": 0}
comments_count: 0
comments_total: 0
discovered_via: "v2ex:独立开发"
---

# 欢迎共创投稿｜浏览器运行、Mac 适配、批量推理加速，开发者们自发为 OXR 拓展了更多可能

> [!info] 一句话导读
> 上个月，我们开源了文档解析模型 **O****X****R（Optical Everything Recognition）**，并陆续整理和发布了[常见问题解答](https://github.com/SoMarkAI/OXR/blob/main/docs/FAQ_CN.md)，集中回应了大家关心的模型能力、使用环境和…

> [!meta]- 语料信息（点开展开）
> 来源：V2EX（post）
> 原帖：<https://www.v2ex.com/t/1258648>
> 指标：回复=0
> 作者：ybs885　|　发布：2026-11-20T12:49:28
> 项目链接：<https://free-oxr.somark.cn/feedback>
> 采集：2026-11-21T14:55:12+08:00　|　id：`7fdf685b5dc17704`

## 正文

上个月，我们开源了文档解析模型 **O****X****R（Optical Everything Recognition）**，并陆续整理和发布了[常见问题解答](https://github.com/SoMarkAI/OXR/blob/main/docs/FAQ_CN.md)，集中回应了大家关心的模型能力、使用环境和部署方式等问题。

不过，FAQ 能把问题讲清楚，真正用起来，还得落到各自的设备和工作流上。

在这件事上，社区已经走在了前面：OXR 直接在浏览器里用 CPU 跑了起来，有人把它适配到了 Mac，也有人为它搭起了批量处理的推理服务，并且都公开了代码、权重和测试数据。

借这篇文章，我们想把这些工作介绍给更多人，也向几位开发者道一声谢谢。

注：以上项目均由社区开发者独立开发和维护，文中数据均来自各项目公开的测试记录。

# 一、浏览器运行：CPU 本地识别

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YjRkMDhkNjlkMzkyODZlNmU1NTY3NzUwOTYwZDFiZmVfNTE2MGFjN2I3YTcxNGU5NWNhZWUzYmY1YWQ3YjY4YzBfSUQ6NzcxMDIzMjQ1NDU1MjEyODc4NV8xNzk1MTc4OTAyOjE3OTUyNjUzMDJfVjM)

**oxr\-wasm｜贡献者：andreespirela（Andres Pirela）、fusor\-rs / fusorlabs**

👉 项目地址：[https://github\.com/fusor\-rs/oxr\-wasm](https://github.com/fusor-rs/oxr-wasm)

oxr\-wasm 用 Rust 和 WebAssembly 重新实现了 OXR\-1\.0 的推理流程，使模型可以直接在浏览器中运行。整个识别过程只依赖本机 CPU，不需要服务器或 GPU；模型加载完成后，页面不再发出网络请求，图片始终保留在本地。

为了适应浏览器环境，项目对模型权重做了量化，在保持识别效果的同时将模型体积压缩到了原来的一半以下：在作者的 8 张测试图中，有 7 张的输出与原模型完全一致，另一张仅公式对齐符的位置不同，渲染结果相同。在搭载 M4 Pro 的 Mac 上用 Chrome 运行时，生成速度约为每秒 170–210 个 token。

仓库中提供了在线演示页，可以用 Chrome 或 Edge 访问。首次使用需要下载模型，之后拖入、粘贴或选择图片即可开始识别，结果会逐步显示出来。除了整页解析，也能单独识别文字、表格、公式、代码和化学结构，结果可以一键复制为 Markdown。

注：项目目前为实验版本，暂不包含 OXR 的版面分析流程；PDF 需要先转成图片再识别。

# 二、Mac 适配：基于 mlx\-vlm 本地运行

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MzBhMDkxNjZhN2VjMTAzZjlmYmU3Y2M5NTI5NWUzNzJfMDAzOTczYWNiMzcxZGE4OWIzN2FmNTBjMDVhODI5ODZfSUQ6NzcxMDIzMjQ1NTg1NjI5NTE3NF8xNzk1MTc4OTAyOjE3OTUyNjUzMDJfVjM)

**mlx\-vlm 适配｜贡献者：bxespinozar**

👉 mlx\-vlm 的 OXR 适配 PR：[https://github\.com/Neywa\-Labs/mlx\-vlm/pull/2560](https://github.com/Neywa-Labs/mlx-vlm/pull/2560)

bxespinozar 为 Apple Silicon 上的推理框架 mlx\-vlm 完成了 OXR 适配，这项工作已被维护者合入主仓库，并随 v0\.7\.11 发布到 PyPI，Mac 用户可以直接通过 pip 安装。

```Python
pip install -U "mlx-vlm>=0.7.11"
```

与之配套，bxespinozar还在 Hugging Face 上发布了两套转换权重：

- [**OXR\-1\.0\-mlx\-bf16**](https://huggingface.co/bxespinozar/OXR-1.0-mlx-bf16)：保持原模型的 BF16 精度。作者在 olmOCR\-Bench 上测得总分 87\.6，与 OXR\-1\.0 原模型的 87\.84 基本一致。

- [**OXR\-1\.0\-mlx\-8bit**](https://huggingface.co/bxespinozar/OXR-1.0-mlx-8bit)：解码器量化为 8\-bit，视觉部分保持 BF16。据作者测试，长文本解码速度比 BF16 版本快约 35%，6 个测试样本中，有 5 个的输出与 BF16 版本完全一致，另一个仅相差一个词。

除了整体评测，作者还逐条比对了具体输出，范围包括行内公式、独立公式、手写内容，以及一张长达 3,603 个 token 的复杂 HTML 表格，BF16 版本的结果都与原模型一致。模型卡中也给出了文字、手写、公式、表格、代码、化学结构等任务的提示词和调用示例。

# 三、服务端加速：面向批量文档处理的推理服务

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NjcxZjI2ODlkNDg1ZmNiMzQ2NGE2NWUyOGVjZWFjNGRfNjQxOTI2ZjBjZGE1ZDVmMWFjMjdjMWRiNmY1OTFlNzBfSUQ6NzcxMDIzMjQ1Mjc4MjE0ODg1M18xNzk1MTc4OTAyOjE3OTUyNjUzMDJfVjM)

**oxr\-inference｜贡献者：NickWilde18（Yechi Yang）**

👉 项目地址： [https://github\.com/NickWilde18/oxr\-inference](https://github.com/NickWilde18/oxr-inference)

oxr\-inference 是一套面向批量文档处理的推理服务。它复用了 OXR 的版面分析、阅读顺序和后处理代码，重新实现了识别推理引擎，并通过连续批处理、显存预分配和多进程流水线，提升持续处理时的吞吐。服务支持容器化部署，API 与 OXR 保持一致，原有的调用方式不需要调整。

作者在单张 H200 上用一份 85 页的混合文档做了测试，文档包括扫描古籍、英文论文和中文教材。测试中，完整解析的吞吐约为 8 页/秒，识别推理每秒可处理 180–190 个请求。

最新的 v1\.1\.0 版本新增了“仅版面检测”和“仅识别指定区域”两个接口，适用于只需要提取表格、公式等特定内容的场景。据作者测试，这种情况下的处理速度可达完整解析的 1\.4–3\.7 倍。完整的测试条件、准确率对照和部署说明，都已在仓库中公开。

# 写在最后

开源 OXR 的时候，我们最期待的，就是它能被更多人真正用起来。看到社区这么多自发的贡献，我们深受鼓舞。谢谢 Andres Pirela 与 fusorlabs、bxespinozar、Yechi Yang，也谢谢 mlx\-vlm 的维护者，投入时间和精力完成这些工作，并将成果公开分享。

同时，我们也希望听到更多来自实际使用的经验。为此，我们正式启动「**OXR \& SoMark 用户案例征集计划**」。

**征集方向：**

1. **行业落地与业务实践：**在金融、制造、教育、医疗、科研等具体场景中，使用 OXR 或 SoMark 搭建文档处理工作流。无论已投入业务使用，还是仍在试点探索中，都欢迎投稿。

2. **应用开发与生态集成：**基于 OXR 开发的开源项目、应用工具或衍生产品，以及将 OXR 或 SoMark 集成到 RAG / Agent、知识库或其他平台中形成的完整应用。

3. **模型与工程技术实践：**围绕 OXR 模型微调与衍生开发、版面分析模块适配、推理加速、端侧部署或软硬件集成形成的技术方案与优化成果。

4. **其他：**不属于以上方向，但你觉得值得分享的使用经验、创意玩法或探索尝试，也欢迎投稿。

**入选案例，你将有机会获得以下权益：**

- SoMark API 免费解析额度

- OXR 或 SoMark 新版内测资格

- 官方技术答疑 / 工作流优化建议

- 官方公众号、官网案例页及其他渠道展示

**参与方式：**

扫描下方二维码，填写问卷即可参与。本活动长期开放，随时欢迎投稿 👏

我们会认真阅读每一份投稿，入选案例将有专人与你联系。如有需要，案例可脱敏后展示。

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MmIzOWYzMzc2ZGFiMWRiYTJiN2ZlNTU0MThjNGVkNzJfMDk3YTgxOWFjYjU0MDNiYzBlZTA0MzdlODc3YzlmZjBfSUQ6NzcxMDIzMzkzMTAwNTkwNjIwOV8xNzk1MTc4OTAyOjE3OTUyNjUzMDJfVjM)

OXR 还在持续迭代。使用中遇到任何问题，欢迎随时通过 [GitHub Issues](https://github.com/SoMarkAI/OXR/issues) 或 [OXR 反馈页面](https://free-oxr.somark.cn/feedback) 告诉我们。

如果 OXR 对你有所帮助，也欢迎到 [GitHub](https://github.com/SoMarkAI/OXR) 为我们点亮一颗 Star。

## 关联链接

- https://github
- https://github.com/Neywa-Labs/mlx-vlm/pull/2560
- https://github.com/NickWilde18/oxr-inference
- https://github.com/SoMarkAI/OXR
- https://github.com/SoMarkAI/OXR/blob/main/docs/FAQ_CN.md
- https://github.com/SoMarkAI/OXR/issues
- https://github.com/fusor-rs/oxr-wasm
- https://huggingface.co/bxespinozar/OXR-1.0-mlx-8bit
- https://huggingface.co/bxespinozar/OXR-1.0-mlx-bf16
- https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MmIzOWYzMzc2ZGFiMWRiYTJiN2ZlNTU0MThjNGVkNzJfMDk3YTgxOWFjYjU0MDNiYzBlZTA0MzdlODc3YzlmZjBfSUQ6NzcxMDIzMzkzMTAwNTkwNjIwOV8xNzk1MTc4OTAyOjE3OTUyNjUzMDJfVjM
- https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MzBhMDkxNjZhN2VjMTAzZjlmYmU3Y2M5NTI5NWUzNzJfMDAzOTczYWNiMzcxZGE4OWIzN2FmNTBjMDVhODI5ODZfSUQ6NzcxMDIzMjQ1NTg1NjI5NTE3NF8xNzk1MTc4OTAyOjE3OTUyNjUzMDJfVjM
- https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NjcxZjI2ODlkNDg1ZmNiMzQ2NGE2NWUyOGVjZWFjNGRfNjQxOTI2ZjBjZGE1ZDVmMWFjMjdjMWRiNmY1OTFlNzBfSUQ6NzcxMDIzMjQ1Mjc4MjE0ODg1M18xNzk1MTc4OTAyOjE3OTUyNjUzMDJfVjM
- https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YjRkMDhkNjlkMzkyODZlNmU1NTY3NzUwOTYwZDFiZmVfNTE2MGFjN2I3YTcxNGU5NWNhZWUzYmY1YWQ3YjY4YzBfSUQ6NzcxMDIzMjQ1NDU1MjEyODc4NV8xNzk1MTc4OTAyOjE3OTUyNjUzMDJfVjM

## 导航

- 项目页：[[10-项目/free-oxr.somark.cn_17d7755c]]
- 渠道页：[[50-渠道/v2ex]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
