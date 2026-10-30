---
type: "corpus"
item_id: "5134b51edfea3d92"
title: "[分享] 给科研人员做了一个 Zotero AI 插件 BibGenie"
source: "v2ex"
source_name: "V2EX"
url: "https://www.v2ex.com/t/1252984"
project_url: "https://bibgenie.com/"
author: "RuiCBai"
published_at: "2026-10-29T13:35:12"
captured_at: "2026-10-30T09:52:25+08:00"
lang: "zh"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-30"
pub_day: "2026-10-29"
tags:
  - 语料
  - v2ex
  - 17
metrics: {"replies": 0}
comments_count: 0
comments_total: 0
discovered_via: "v2ex:独立开发"
---

# [分享] 给科研人员做了一个 Zotero AI 插件 BibGenie

> [!info] 一句话导读
> 大家好，我是 [BibGenie]( https://bibgenie.com) 的开发者，来分享一下自己做了一年多的东西，也想听听 V 站里还在用 Zotero 看文献的朋友的真实反馈。

> [!meta]- 语料信息（点开展开）
> 来源：V2EX（post）
> 原帖：<https://www.v2ex.com/t/1252984>
> 指标：回复=0
> 作者：RuiCBai　|　发布：2026-10-29T13:35:12
> 项目链接：<https://bibgenie.com/>
> 采集：2026-10-30T09:52:25+08:00　|　id：`5134b51edfea3d92`

## 正文

大家好，我是 [BibGenie]( https://bibgenie.com) 的开发者，来分享一下自己做了一年多的东西，也想听听 V 站里还在用 Zotero 看文献的朋友的真实反馈。

## 背景说明

用 Zotero 的应该都知道，它是科研圈最主流的开源文献管理工具，但本身没有任何 AI 能力。我自己读论文时有个很具体的痛点：把论文丢给 AI 问，答案说得头头是道，但我根本不知道它是从哪篇、哪一页得出的结论，最后还得自己回去翻 PDF 核对，费时费力。

所以我做了 BibGenie （去年叫 Zotero Copilot ，但因为 Zotero 商标的问题改了名），一个原生跑在 Zotero 里面的 AI 插件，侧边栏形态，可以直接访问官网 https://bibgenie.com 查看首页的展示视频，视频会更加直观。

迭代了一年多，目前更新到 v0.9.4 版本了，核心功能都已经开发完成了，今天来 V2EX 求一点反馈
（顺便吐槽一下，现在很多独立开发者只顾哐哐开发新产品，却不管维护，我也是深受其害。）

## 核心功能大概是这几块：

1. 直接和自己的 Zotero 整个文库对话。 不用导出文件、不用把 PDF 一个个上传到网页工具。在 Zotero 里面直接用 @ 或者右键 Add to Chat ，就能把条目、PDF 的某几页、EPUB 章节、批注、笔记、标签、整个集合拉进同一个对话里，多篇论文一起对比之类的。

2. **引用可追溯到文本块。** 这是我最在意、也花时间最多的功能。AI 回答里给出的引用，点一下能跳回 PDF 对应页，并高亮出它引用的那个文本块； EPUB 、网页快照也是一样定位到段落。科研场景下，我觉得这个功能真是刚需。

3. **本地优先，支持 BYOK**。聊天记录存在本地 Zotero 数据库里，不上传服务器；文库的语义索引也是在本地建的。模型这边三条路随便选：自带 Key （ OpenAI 、Claude 、DeepSeek 、OpenRouter 、各种兼容接口都支持，请求直连服务商，不消耗额度）；本地模型（ Ollama 、LM Studio ，聊天和 embedding 都配成本地的就可以完全不出本机）；或者用 bibgenie 官方模型开箱即用，什么都不用配置。

4. **内置了一个 Zotero MCP Server**。这个估计 V 站的朋友会比较感兴趣。插件里直接起了个本地 MCP Server （ Streamable HTTP ，长这样：127.0.0.1:23119/bibgenie/mcp ），不用再单独装什么 Python 服务。Claude Code 、Claude Desktop 、Cursor 、Cherry Studio 连上之后，可以直接检索我的 Zotero 文库、做语义搜索、读 PDF 附件（页面还能渲染成图片，看图表和扫描页没问题）、读笔记和快照，也能在客户端自己的权限确认下建笔记、整理集合。

5. 帮着整理 Zotero 文库。 可以让它整理集合、清洗标签、核查元数据（时间长了，zotero 文献库的标签，分类之类的都乱了，可以直接来整理）。元数据是交叉比对 arXiv 、Semantic Scholar 、OpenAlex 、DBLP 、OpenReview 这几个来源的。所有改动先出一张 diff 预览卡，点批准了才写进去。

## 关于定价

所有的功能都是免费的，需要购买的只有模型的 token 。免费用户每月送 200 credits ，Pro 是 $9.99/月，有 10000 credits （ Pro 肯定够用了!!）。现在还有个 $199 的 Lifetime Pro ，v1.0 之后会下架（当然已经买了的不受任何影响，下架只针对新购），独立开发的小产品确实长期扛不住终身制, 前期已经倒贴了不少了。

官方模型目前是通过 OpenRouter 接入的，我在成本价上只加 7% 用来覆盖服务器和其他支出，目前没打算靠 token 差价赚钱（毕竟也支持自定义模型）。


官网和文档在这：
官网： https://www.bibgenie.com
文档： https://www.bibgenie.com/docs

最后想认真求一波反馈，尤其是平时用 Zotero 的朋友。批评也完全欢迎，这东西的不少功能就是被用户骂出来的。感谢阅读。

（很抱歉，没有福利带给大家，毕竟这个产品是免费的，相信 V 友都有能力接入自定义模来使用，如果确实有想订阅的，可以留下邮箱，我给你 8 折优惠券。 当然，有 llm 服务商愿意支援 token 网页是欢迎的。）

## 关联链接

- https://bibgenie.com
- https://www.bibgenie.com
- https://www.bibgenie.com/docs

## 导航

- 项目页：[[10-项目/bibgenie.com_e4d7b79e]]
- 渠道页：[[50-渠道/v2ex]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
