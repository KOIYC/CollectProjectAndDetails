---
type: "project"
title: "AI 时代一群人在卷笔记软件，我想先把 Markdown 编辑器的底层做好"
project_url: "https://docs.quirekit.com/"
first_seen: "2026-10-29T20:50:17+08:00"
sources:
  - v2ex
tags:
  - 项目
  - v2ex
  - 300
lang: "zh"
---

# AI 时代一群人在卷笔记软件，我想先把 Markdown 编辑器的底层做好

> [!info] 一句话导读
> AI 时代，一群人在卷编辑器：AI 写作、AI 笔记、AI 知识库，一个比一个炫。

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://docs.quirekit.com/>
> 首次收录：2026-10-29T20:50:17+08:00
> 来源渠道：V2EX
> 标签：300
> 最新指标：回复=0

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-29T20:50:17+08:00 | V2EX | 回复=0 | [[20-语料/posts/v2ex/2026-10-29/7415c9fa650d4680_AI-时代一群人在卷笔记软件,我想先把-Markdown-编辑器的底层做好]] |

## 摘要正文

AI 时代，一群人在卷编辑器：AI 写作、AI 笔记、AI 知识库，一个比一个炫。  可打开底层看，大家用的还是那几套东西，遇到的也还是那几个老问题：内容存成 JSON ，来回转 Markdown 时把你的原文改掉；所见即所得和源码模式是两套编辑器，切一次丢一点；协同一上来，结构就开始出怪事。AI 生成得再快，落到这些框架里照样会丢格式、错位置。  我做 ProseMirror 相关的产品三年了，这些坑基本都踩过。这次我不想再做一个编辑器应用，我想先把编辑器框架这件事做对。这篇讲其中一条线：**MSFE （ Markdown Source-First Editor ），一个源码优先的 Markdown 编辑器框架**。  先放成品，打开就能用： https://msfe.quirekit.com  ![MSFE 官网首页]( https://cdn.jsdelivr.net/gh/kingshuaishuai/ys-imgs@main/quirepub/90ecdaddea87de03c48b1ae2b890986a.png)  ## 一、别人是怎么做的  先看看最近几年流行的笔记软件和编辑器，底层都是什么。开源的看了仓库源码，闭源的只采用官方文档和工程博客，官方没说的写“未公开”（截至 2026 年 10 月）：  | 产品 | 编辑方式 | 编辑时改的是什么 | 编辑器底层 | 内容存在哪 | 开源 | | --- | --- | --- | --- | --- | --- | | Notion | 块编辑（富文本） | 块数据，Markdown 只在导入导出时转换 | 自研 | 服务端数据库 | 否 | | Obsidian | 实时预览：在源码里直接渲染；另有源码模式、阅读模式 | Markdown 原文 | CodeMirror 6 | 本地 Markdown 文件 | 否 | | 飞书文档 | 块编辑（富文本） | 块树，Markdown 只在导入导出时转换 | 自研 | 云端 | 否 | | 思源笔记 | 块编辑（富文本），可以用 Markdown 语法输入 | 节点树，Markdown 只在导入导出时转换 | 自研 Protyle | 每篇一个 `.sy` 文件，节点树 JSON | 是 | | Typora | 所见即所得，另有源码模式 | 未公开 | 自研，内核未公开 | 本地 Markdown 文件 | 否 | | AFFiNE | 块编辑（富文本）+ 白板 | 块数据 | BlockSuite | Yjs | 是 | | Logseq | 大纲块编辑：正在编辑的块显示源码，离开后渲染 | 当前块的 Markdown 原文 | 每个块一个 textarea | 文件版是 Markdown/Or…
