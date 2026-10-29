---
type: "corpus"
item_id: "7415c9fa650d4680"
title: "AI 时代一群人在卷笔记软件，我想先把 Markdown 编辑器的底层做好"
source: "v2ex"
source_name: "V2EX"
url: "https://www.v2ex.com/t/1252802"
project_url: "https://docs.quirekit.com/"
author: "1244943563"
published_at: "2026-10-29T03:29:07"
captured_at: "2026-10-29T20:50:17+08:00"
lang: "zh"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-29"
pub_day: "2026-10-29"
tags:
  - 语料
  - v2ex
  - 300
metrics: {"replies": 0}
comments_count: 0
comments_total: 0
discovered_via: "v2ex:独立开发"
---

# AI 时代一群人在卷笔记软件，我想先把 Markdown 编辑器的底层做好

> [!info] 一句话导读
> AI 时代，一群人在卷编辑器：AI 写作、AI 笔记、AI 知识库，一个比一个炫。

> [!meta]- 语料信息（点开展开）
> 来源：V2EX（post）
> 原帖：<https://www.v2ex.com/t/1252802>
> 指标：回复=0
> 作者：1244943563　|　发布：2026-10-29T03:29:07
> 项目链接：<https://docs.quirekit.com/>
> 采集：2026-10-29T20:50:17+08:00　|　id：`7415c9fa650d4680`

## 正文

AI 时代，一群人在卷编辑器：AI 写作、AI 笔记、AI 知识库，一个比一个炫。

可打开底层看，大家用的还是那几套东西，遇到的也还是那几个老问题：内容存成 JSON ，来回转 Markdown 时把你的原文改掉；所见即所得和源码模式是两套编辑器，切一次丢一点；协同一上来，结构就开始出怪事。AI 生成得再快，落到这些框架里照样会丢格式、错位置。

我做 ProseMirror 相关的产品三年了，这些坑基本都踩过。这次我不想再做一个编辑器应用，我想先把编辑器框架这件事做对。这篇讲其中一条线：**MSFE （ Markdown Source-First Editor ），一个源码优先的 Markdown 编辑器框架**。

先放成品，打开就能用： https://msfe.quirekit.com

![MSFE 官网首页]( https://cdn.jsdelivr.net/gh/kingshuaishuai/ys-imgs@main/quirepub/90ecdaddea87de03c48b1ae2b890986a.png)

## 一、别人是怎么做的

先看看最近几年流行的笔记软件和编辑器，底层都是什么。开源的看了仓库源码，闭源的只采用官方文档和工程博客，官方没说的写“未公开”（截至 2026 年 10 月）：

| 产品 | 编辑方式 | 编辑时改的是什么 | 编辑器底层 | 内容存在哪 | 开源 |
| --- | --- | --- | --- | --- | --- |
| Notion | 块编辑（富文本） | 块数据，Markdown 只在导入导出时转换 | 自研 | 服务端数据库 | 否 |
| Obsidian | 实时预览：在源码里直接渲染；另有源码模式、阅读模式 | Markdown 原文 | CodeMirror 6 | 本地 Markdown 文件 | 否 |
| 飞书文档 | 块编辑（富文本） | 块树，Markdown 只在导入导出时转换 | 自研 | 云端 | 否 |
| 思源笔记 | 块编辑（富文本），可以用 Markdown 语法输入 | 节点树，Markdown 只在导入导出时转换 | 自研 Protyle | 每篇一个 `.sy` 文件，节点树 JSON | 是 |
| Typora | 所见即所得，另有源码模式 | 未公开 | 自研，内核未公开 | 本地 Markdown 文件 | 否 |
| AFFiNE | 块编辑（富文本）+ 白板 | 块数据 | BlockSuite | Yjs | 是 |
| Logseq | 大纲块编辑：正在编辑的块显示源码，离开后渲染 | 当前块的 Markdown 原文 | 每个块一个 textarea | 文件版是 Markdown/Org 文件； DB 版（ Beta ）是 SQLite | 是 |
| AppFlowy | 块编辑（富文本） | 块数据 | 自研 Flutter 编辑器 | yrs （ Rust 版 Yjs ），本地 RocksDB | 是 |
| Memos | 短笔记，块编辑 | 块结构，进出都是 Markdown | 自研 | 数据库里的 Markdown 文本 | 是 |
| MarkText | 所见即所得 + 源码模式，两套 | 所见即所得模式改的是渲染后的文档，保存时用 turndown 转回 Markdown | 自研 Muya + CodeMirror 5 | 本地 Markdown 文件 | 是 |
| 妙言 MiaoYan | 源码编辑 + 语法高亮 + 界面预览| Markdown 原文 | 系统原生文本框 + WebView 预览 | 本地 Markdown 文件 | 是 |
| NoteGen | 富文本 + 源码模式，两套 | 富文本模式改的是 Tiptap 文档树，源码模式改原文 | Tiptap 3 + CodeMirror 6 | 本地 Markdown 文件 | 是 |
| Blinko | 短笔记，Vditor 编辑器（支持所见即所得、即时渲染、分屏预览） | 取决于 Vditor 的模式 | Vditor | PostgreSQL 里的 Markdown 文本 | 是 |
| Flowix | 富文本 + 源码模式，两套 | 富文本模式改的是 Tiptap 文档树，保存时转成 Markdown ；源码模式改原文 | Tiptap 3 + CodeMirror 6 | 本地 Markdown 文件，另有 SQLite 索引 | 是 |
| Joplin （桌面） | 富文本 + 源码，两套 | 富文本模式改的是 TinyMCE 文档，切换时互相转换 | TinyMCE + CodeMirror | SQLite 里的 Markdown | 是 |

> 以上仅收集公开信息，方便对照技术路线，不评价产品好坏。每个产品的取舍都有它的场景。

按“编辑时改的是什么”，大致可以分成三类：

- **块编辑 / 富文本**：Notion 、飞书、思源、AFFiNE 、AppFlowy 。编辑的是块数据或文档树，体验最接近 Word 和 Google Docs 。Markdown 只是导入导出的格式。
- **源码派**：Obsidian 、妙言、Logseq 。改的始终是 Markdown 原文，源码不会被改写。可要么停在“源码 + 高亮 + 预览”，要么做成“实时预览”，标记符号多少都会露出来，离真正的富文本还差一点点。
- **两套编辑器**：MarkText 、NoteGen 、Flowix 、Joplin 。一套富文本加一套源码，切换时互相转换。富文本体验有了，可每切一次、存一次，都要走一遍“文档树 → Markdown”的转换。

不少主打本地、离线的产品，内容存的是数据库或 JSON ，Markdown 主要用在导入导出上。

## 二、主要问题：转换只能按规定来，你的源码保不住

富文本派要读写 Markdown ，就得在 ProseMirror 的 node 、mark 和 Markdown 源码之间来回转换。问题是，这个转换只能“按规定转”。

拿最常用的几个实现看（都是看源码得出的）：

**prosemirror-markdown 1.13.4**
- 斜体、粗体写死成 `*` 和 `**`，你写的 `_斜体_`、`__粗体__` 存一次就变了。
- 无序列表默认一律变成 `*`，你习惯的 `-` 没了。
- 有序列表会被重新编号，`1. 1. 1.` 存完变成 `1. 2. 3.`。
- 行尾两个空格的换行，统一改成 `\`。
- 文本里的 `*`、`[`、`]`、`~` 一律加反斜杠转义。
- 遇到它不认识的语法，直接报错。默认的 schema 里没有表格、脚注、删除线。

**Tiptap 官方的 @tiptap/markdown （ 3.30 ）**
- 粗体、斜体同样写死；无序列表一律输出 `-`；有序列表重新编号。
- 没有对应渲染器的节点，直接输出空字符串，内容就这么静默消失了。
- 官方文档自己也写着：这还是早期版本，批注不支持，表格每个单元格只能放一个子节点。

**社区的 tiptap-markdown** 已经停止维护。它遇到表达不了的节点，会输出一个 `[nodeName]` 占位；表格一有合并单元格就降级成 HTML ，列对齐信息也丢了。

这些不是 bug ，是这个架构必然的结果：**文档的权威是那棵 JSON 树，Markdown 只是它的一种“打印方式”**。打印方式只有一种，所以你写的那份源码，早在第一次保存时就已经不在了。

对一个人写笔记，可能无所谓。可对这些场景很要命：

- 文档放在 Git 里，改一个字，diff 却是满屏的格式变化；
- AI 只改了一段，整篇的写法却都被“规范化”了；
- 同一个文件还要给 VS Code 、静态站点、别的 Markdown 工具用。

## 三、“Markdown 做不了复杂块”，其实大错特错

常听到一种说法：Markdown 表达不了复杂结构，像多维表格、数据库视图，所以只能存 JSON 。Logseq 的联合创始人在 2024 年解释为什么做数据库版本时，也提到 Markdown 的结构化数据支持有限，缺少持久 ID 、时间戳这些东西。

持久 ID 这类问题确实存在，后面会讲。可“做不了复杂块”是错的。

Markdown 本来就有一个非常好用的容器：**代码围栏**。在 MSFE 里，多维表格、流程图、思维导图、白板都存成一个代码围栏，里面放的是可以反复打开编辑的数据：

````markdown
```quirekit-data-view
{ ...表格的字段、记录、视图... }
```
````

- 在 MSFE 里，它显示成一个能直接编辑的多维表格；
- 在 GitHub 、VS Code 或者任何普通的 Markdown 工具里，它就是一段代码，不会坏，也不会丢；
- 用户点“确定”之后，才把新数据写回同一个围栏。其他行一个字节都不动。

复杂块的问题不在 Markdown ，而在你有没有给它设计一个好的落点。

## 四、Markdown 真正的限制在哪

说 Markdown 无所不能也不诚实。它真正的限制在语法本身，我用 micromark 4.0.2 加 GFM 扩展逐条实测过：

**1. 表格单元格里只能放行内内容。** 想在单元格里放一个列表或者一段代码？表格当场被拆坏：

```markdown
| A | B |
| --- | --- |
| - 一
- 二 | x |
```

解析结果：第一行变成 `- 一` 和一个空单元格，`- 二 | x |` 被挤出表格，成了表格外面的一个列表项。代码块放进单元格也一样，整张表都乱了。单元格里想分段，只能写 `<br>`。

**2. 格式不能随便嵌套。**
- 行内代码里不能再加粗：`` `**加粗**` `` 显示的就是带星号的原文。
- 链接里不能再套链接：`[外层 [内层](b) 文字](a)`，外层链接直接失效，变回普通文字。
- 下划线、文字颜色、高亮、字号，Markdown 里根本没有，只能写 HTML 。写在行内的 `<u>**粗**</u>` 还好，HTML 和 Markdown 都能生效；可一旦写成 HTML 块，比如 `<div align="center">` 里面写 `**居中加粗**`，里面的 Markdown 就不再解析，直接显示成纯文本的星号。

**3. 中文标点会让加粗失效，这个最坑中文用户。**

```markdown
这是**“加粗”**后面的字
注意**（重要）**这里
```

这两行都不会加粗，渲染出来就是原样的星号。原因是 CommonMark 判断 `**` 能不能开始或结束强调，要看它两边是不是标点和空白。中文引号、括号是标点，后面又紧跟着汉字，规则就判它不成立。英文写作几乎碰不到这个问题，中文写作却天天碰到。

**4. 还有一些是语法层面根本没有的东西：**
- 表格没有合并单元格，没有列宽，没有单元格底色；
- 段落没有对齐、缩进、行距、段前段后；
- 块没有稳定的 ID ，“引用第 3 段”这种需求，段落一移动就失效；
- 批注、修订没地方挂，没有锚点；
- 方言太多，GFM 、各家扩展、各个软件的私有语法，同一份文件换个工具，显示就不一样。

所以我的态度是：

- **语法表达不了的，不假装能表达。** MSFE 不认识的语法，原样留在源码里，不丢也不改；
- **复杂对象，用代码围栏装数据；**
- **版式类的需求**，比如页面、字体、段落样式，交给导出模板和分页文档去做，不往 Markdown 里硬塞。

## 五、两套编辑器，又重又不尊重源码

Markdown 派想做所见即所得，最常见的做法是：一套富文本编辑器，加一套源码编辑器，切换时互相转换。

Joplin 桌面端就是 TinyMCE 加 CodeMirror 。它的官方帮助页很诚实，直接列出了在富文本编辑器里编辑 Markdown 笔记会出的问题：大多数插件格式会丢；表格没有表头会被补一个空表头；同一个列表里不能混用复选框和普通列表项； Markdown 里的 HTML 可能丢；引用式链接会被改成行内链接。

MarkText 是自研的 Muya 加 CodeMirror 5 ，读入用 marked 转成 HTML ，写出用 turndown 再转回 Markdown 。

两套编辑器意味着：

- 包体积和内存翻倍，两套快捷键、两套撤销历史、两套插件；
- 每切一次视图，就做一次“Markdown → 树 → Markdown”，这正是第二节说的那条有损的路；
- 光标、选区、滚动位置在两边对不上，切过去还得重新找刚才写到哪了。

## 六、协同：ProseMirror 的 Yjs 协同，坑比想象中多

富文本派做协同，基本都走 Yjs 加 y-prosemirror （ Tiptap 的协同也是这套）。我们做 Word 级文档时专门测过，也翻了上游的文档和 issue：

**上游自己承认的问题**（ y-prosemirror 的 CAVEATS 和 issue ）：
- **结构不合法时，直接删节点。** 两个人并发修改，可能产生不符合 schema 的结构，比如一个引用块里的段落被两个人同时删光了。绑定的处理是把整个父节点删掉，离线久了的用户尤其容易中招。
- **远端每次更新都整篇替换。** 作者在 issue 里原话是 “y-prosemirror replaces the complete document with every change”。结果是 transaction 的位置映射失效，本地的装饰、插件状态都得自己用相对位置重建。
- **拆段、合段、提升没有原生表示。** 拆段在 Yjs 里是“删掉原段落的尾巴，再插一个新节点”，并发时语义就可能跑偏。
- **撤销要换掉。** 不能用 ProseMirror 自带的 history ，要换成 Yjs 的 UndoManager 。Tiptap 文档也要求开协同时关掉 StarterKit 里的撤销重做。
- 远端更新时恢复选区可能抛错，导致这次更新在本端被跳过，两边状态分叉（ v1.3.7 ，issue 还开着）。
- v1 和 v2 的数据格式不兼容，新旧客户端不能同时编辑同一篇文档。

**我们自己实测的**（ Yjs 13.6.33 + y-prosemirror 1.3.7 、Tiptap 的 y-tiptap 3.0.9 、Yjs 14 预发布版，三组结果一致）：

| 两个人同时做的事 | 结果 |
| --- | --- |
| A 把一段拆成两段，B 在原来的后半段插字 | B 插的字跑到了前半段的末尾 |
| A 拆段，B 同时把后半段加粗 | 加粗丢了 |
| A 拆段，B 同时删掉后半段的字 | 删掉的字又回来了 |
| A 把两段合成一段，B 同时在第二段插字 | B 插的字没了 |

这些不是部署问题，换个服务器、多加几台机器都解决不了。根子在“树形文档怎么映射成 CRDT”这件事上。

**MSFE 的协同为什么没有这类问题**：MSFE 协同的是 Markdown 源码本身，一个 Yjs 文本。任何一段文本都是合法的 Markdown ，所以不存在“结构不合法要删节点”；结构是从文本重新解析出来的，所以也不存在“拆段合段没有表示”。两个人在同一个地方改，结果可能需要人看一眼，比如把同一行表格改成了不同的样子，但内容不会因为结构冲突凭空消失。撤销是协同撤销，只撤你自己的修改。

## 七、为什么一定要尊重源码

说到底，就一句话：**你写下的那份 Markdown ，就是文档本身。**

- **Git 友好**：改一个字，diff 就是一个字；
- **AI 友好**：大模型读写的本来就是 Markdown ，它改哪一段就只动哪一段，不会顺手把全文“规范化”；
- **工具自由**：同一份文件，可以在 VS Code 里改、给静态站点渲染、给别的工具处理，不被任何一个编辑器锁死；
- **长期可读**：十年后它还是一份纯文本。

## 八、CodeMirror 也能做“富文本”

很多人以为 CodeMirror 只能做源码编辑器，要做所见即所得就得上 ProseMirror 。其实 CodeMirror 6 的装饰和 widget 足够做出“看起来就是富文本”的效果：标题变大、标记符号藏起来、表格画成表格、公式渲染成公式、代码围栏里的数据渲染成流程图和多维表格。可底下的文本一个字都没变。

MSFE 本身就提供三种可以编辑的呈现：**文档视图**（标记符号全部隐藏，看起来就是富文本）、**实时预览**（编辑到哪里，哪里露出 Markdown 标记）、**源码视图**。它们是同一个 CodeMirror 实例上的不同呈现，不是三套编辑器。切换时不做任何转换，选区和撤销历史都还在，改的永远是同一份 Markdown 。

QuireKit 的 MD Editor 就是在 MSFE 上面拼出来的成品：加上工具栏、斜杠菜单这些界面，再加一个只读的阅读视图，用来渲染同一份源码。

**文档视图**：标记全部隐藏，看起来就是富文本。

![MD Editor 文档视图]( https://cdn.jsdelivr.net/gh/kingshuaishuai/ys-imgs@main/quirepub/8b8cfaa66d50e831d4e3cf71e04c4fed.png)

**实时预览**：光标在哪一行，哪一行就露出 Markdown 源码，比如这里的公式行变成了 LaTeX ，其他地方照常渲染。

![实时预览：光标所在的公式行露出 LaTeX 源码]( https://cdn.jsdelivr.net/gh/kingshuaishuai/ys-imgs@main/quirepub/003681ddd66ecb538f04991784a8c073.png)

**源码视图**：同一份内容，就是这份 Markdown 。

![同一份内容的源码视图]( https://cdn.jsdelivr.net/gh/kingshuaishuai/ys-imgs@main/quirepub/8ee0b249a9c300e5e26a6a93b9b79f87.png)

源码优先也有代价：每次输入都要更新语法树，文件一大就慢。

这个问题我其实不是第一次碰到。之前我做过一个开源项目 Incremark ，专门解决 AI 流式输出时 Markdown 的增量渲染：模型每吐出一段文字，不重新解析整篇。做 MSFE 时我发现，编辑器的增量解析和流式渲染其实是同一个问题，而且在解析器这一层能做得更彻底。于是我直接改了 Lezer 的增量解析，在它上面重写了新版 Incremark 。现在 MSFE 编辑、MD Editor 的阅读视图、AI 流式回复的显示，用的都是同一套解析。Incremark 的来龙去脉，以及我为什么放弃了第一版，后面单独写一篇细讲。

具体的优化是给 Lezer 的 Markdown 增量解析加了“复用证明”，解析器会记下哪些区间是原样复用的，编辑器据此直接跳过没变的部分。1 MiB 的文档连续输入 20 次：

| 工作量 | 优化前 | 优化后 |
| --- | --- | --- |
| 语法树访问 | 107,760 | 1,380 （少了 98.7%） |
| 语法树比较 | 153,940 | 660 （少了 99.6%） |

证明不成立的地方，会退回完整比较，所以正确性不受影响。

## 九、为什么要封装成框架

上面这些，单独做一个编辑器应用也能做。我把它做成框架，是因为这些问题每个做编辑器的人都会碰到，没必要每人重新踩一遍。

MSFE 的写法是 Tiptap 风格的，装上什么扩展，就能编辑什么：

```ts
import { createMsfeEditor } from '@quirekit/msfe-core'
import { StarterKit } from '@quirekit/msfe-starter-kit'

const editor = createMsfeEditor({
  parent,
  documentId: 'note-1',
  markdown: '# Hello\n\n**Markdown** stays the source.\n',
  mode: 'live',
  extensions: [StarterKit],
})

editor.getMarkdown() // 永远是那份源码
```

- 内核不依赖 Vue 或 React ，也提供 Vue 、React 组件；
- 现成的扩展有：标题、加粗、链接、图片、代码块、公式和 Mermaid 等扩展语法、HTML 和 HTML 沙箱、流程图、思维导图、白板、多维表格；
- 协同（含 Hocuspocus 服务端）也是扩展。

这些都是 MIT 开源。AI 读写文档、改动以“待审阅”的形式显示，以及批注，是商业组件，开发和评估免费。

## 十、MD Editor 和周边生态

不想自己拼的，直接用 MD Editor：工具栏、四种视图、斜杠菜单、表格、公式、图表都配好了，几行代码就能放进 Vue 项目。

```vue



<template>
  <MdEditor markdown="# Hello" label="Document" />
</template>
```

周边的编辑器也都是独立的包：公式编辑器（ LaTeX 和 Word 公式互转）、流程图、思维导图、白板、Mermaid / PlantUML / Graphviz 文本绘图、多维表格，以及给 AI 边生成边显示用的流式 Markdown 渲染（ Incremark ）。所有界面都来自同一套 UI 组件库，亮色暗黑一键切换。

## 十一、专业场景：Word 和 PDF ，两套方案

Markdown 写完，总有人要 Word 、要 PDF 。这里我们给了两套方案。

**开源方案（`@quirekit/md-editor-basic-export`，MIT ）**：用成熟的开源库来转。Markdown 转 Word 用 md-to-docx ，Word 转 Markdown 用 Mammoth 加 Turndown ，PDF 用 pdfmake ，全在浏览器里完成。MSFE 特有的内容会降级：流程图、思维导图、白板导出成预览图，其他嵌入块变成占位。**每一处降级都会写进导出报告，不会悄悄丢掉。**

**商业方案**：不走“Markdown 转 HTML 再转 Word”这条路，而是把 Markdown 转进和我们分页文档编辑器 Classic 同一套文档模型，再交给 Classic 的排版引擎输出 Word 、PDF 和 OFD：

- **能定模板**：页面、字体、段落样式写成导出模板，同一份 Markdown 可以按公司模板、论文模板、公文模板导出；
- **公式是 Word 原生公式**，不是图片；
- **自定义块能往返**：流程图、思维导图在 Word 里显示为图，同时把原始数据带进文件。再导回 Markdown 时，能恢复成可以继续编辑的块；
- **有损就说出来**：每次转换都会给出报告；开严格模式的话，只要有一点损失就直接拒绝；
- **和富文本打通**：因为用的是同一套模型和排版，Markdown 导出的 PDF 、OFD ，和分页文档编辑器里看到的版式一样。导出的 Word ，也能在 Classic 里接着按页编辑。

## 顺便说一下 Classic

Classic 就是上面提到的那个分页文档编辑器，是 QuireKit 的另一条线：基于 ProseMirror ，自己排版、真正分页，画在 Canvas 或 SVG 上。它解决的是另一类问题，有机会单独写一篇。官网首屏就是它，可以直接上手试： https://quirekit.com

## 最后

QuireKit 不是某一个编辑器，而是一整套编辑器生态：两套 Tiptap 风格的编辑器框架（ ProseMirror 线和这篇讲的 CodeMirror 线 MSFE ），上面是分页文档、块编辑器、Markdown 编辑器，以及一堆周边编辑器，共用一套 UI 组件库。开源部分全部 MIT ，闭源商用也可以。

目前还是 alpha ，API 还会变，欢迎来试、来挑刺：

- MSFE： https://msfe.quirekit.com
- 在线体验： https://quirekit.com
- 文档： https://docs.quirekit.com
- GitHub： https://github.com/quirekit/quirekit

觉得这个方向有意思的话，点个 Star 就是对我最大的支持。也很想听听：你们做 Markdown 编辑器时，被哪个坑卡得最久？

## 关联链接

- https://cdn.jsdelivr.net/gh/kingshuaishuai/ys-imgs@main/quirepub/003681ddd66ecb538f04991784a8c073.png
- https://cdn.jsdelivr.net/gh/kingshuaishuai/ys-imgs@main/quirepub/8b8cfaa66d50e831d4e3cf71e04c4fed.png
- https://cdn.jsdelivr.net/gh/kingshuaishuai/ys-imgs@main/quirepub/8ee0b249a9c300e5e26a6a93b9b79f87.png
- https://cdn.jsdelivr.net/gh/kingshuaishuai/ys-imgs@main/quirepub/90ecdaddea87de03c48b1ae2b890986a.png
- https://docs.quirekit.com
- https://github.com/quirekit/quirekit
- https://msfe.quirekit.com
- https://quirekit.com

## 导航

- 项目页：[[10-项目/docs.quirekit.com_f8944c73]]
- 渠道页：[[50-渠道/v2ex]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
