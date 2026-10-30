---
type: "project"
title: "[分享] 给科研人员做了一个 Zotero AI 插件 BibGenie"
project_url: "https://bibgenie.com/"
first_seen: "2026-10-30T09:52:25+08:00"
sources:
  - v2ex
tags:
  - 项目
  - v2ex
  - 17
lang: "zh"
---

# [分享] 给科研人员做了一个 Zotero AI 插件 BibGenie

> [!info] 一句话导读
> 大家好，我是 [BibGenie]( https://bibgenie.com) 的开发者，来分享一下自己做了一年多的东西，也想听听 V 站里还在用 Zotero 看文献的朋友的真实反馈。

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://bibgenie.com/>
> 首次收录：2026-10-30T09:52:25+08:00
> 来源渠道：V2EX
> 标签：17
> 最新指标：回复=0

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-30T09:52:25+08:00 | V2EX | 回复=0 | [[20-语料/posts/v2ex/2026-10-30/5134b51edfea3d92_分享-给科研人员做了一个-Zotero-AI-插件-BibGenie]] |

## 摘要正文

大家好，我是 [BibGenie]( https://bibgenie.com) 的开发者，来分享一下自己做了一年多的东西，也想听听 V 站里还在用 Zotero 看文献的朋友的真实反馈。  ## 背景说明  用 Zotero 的应该都知道，它是科研圈最主流的开源文献管理工具，但本身没有任何 AI 能力。我自己读论文时有个很具体的痛点：把论文丢给 AI 问，答案说得头头是道，但我根本不知道它是从哪篇、哪一页得出的结论，最后还得自己回去翻 PDF 核对，费时费力。  所以我做了 BibGenie （去年叫 Zotero Copilot ，但因为 Zotero 商标的问题改了名），一个原生跑在 Zotero 里面的 AI 插件，侧边栏形态，可以直接访问官网 https://bibgenie.com 查看首页的展示视频，视频会更加直观。  迭代了一年多，目前更新到 v0.9.4 版本了，核心功能都已经开发完成了，今天来 V2EX 求一点反馈 （顺便吐槽一下，现在很多独立开发者只顾哐哐开发新产品，却不管维护，我也是深受其害。）  ## 核心功能大概是这几块：  1. 直接和自己的 Zotero 整个文库对话。 不用导出文件、不用把 PDF 一个个上传到网页工具。在 Zotero 里面直接用 @ 或者右键 Add to Chat ，就能把条目、PDF 的某几页、EPUB 章节、批注、笔记、标签、整个集合拉进同一个对话里，多篇论文一起对比之类的。  2. **引用可追溯到文本块。** 这是我最在意、也花时间最多的功能。AI 回答里给出的引用，点一下能跳回 PDF 对应页，并高亮出它引用的那个文本块； EPUB 、网页快照也是一样定位到段落。科研场景下，我觉得这个功能真是刚需。  3. **本地优先，支持 BYOK**。聊天记录存在本地 Zotero 数据库里，不上传服务器；文库的语义索引也是在本地建的。模型这边三条路随便选：自带 Key （ OpenAI 、Claude 、DeepSeek 、OpenRouter 、各种兼容接口都支持，请求直连服务商，不消耗额度）；本地模型（ Ollama 、LM Studio ，聊天和 embedding 都配成本地的就可以完全不出本机）；或者用 bibgenie 官方模型开箱即用，什么都不用配置。  4. **内置了一个 Zotero MCP Server**。这个估计 V 站的朋友会比较感兴趣。插件里直接起了个本地 MCP Server （ Streamable HTTP ，长这样：127.0.0.1:23119/bibgenie/mcp ），不用再单独装什么 Python 服务。Claude Code 、Claude Desktop 、Cursor 、Cherry Studio 连上之后，可…
