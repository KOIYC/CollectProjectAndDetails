---
type: "corpus"
item_id: "b88a2290c00e8152"
title: "Show HN: Docx-to-Markdown – layout-aware Word to Markdown converter"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49728477"
project_url: "https://docx-editor.dev/solutions/word-to-markdown"
author: "thisisjedr"
published_at: "2026-09-16T15:24:31Z"
captured_at: "2026-09-20T14:04:03+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-16"
tags:
  - 语料
  - hn_show
  - author_thisisjedr
  - story_49728477
  - show_hn
metrics: {"points": 5, "comments": 5, "engagement_velocity": 5}
comments_count: 5
comments_total: 5
discovered_via: "hn:show_hn:90d"
---

# Show HN: Docx-to-Markdown – layout-aware Word to Markdown converter

> [!info] 一句话导读
> Word to Markdown converter with page references

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49728477>
> 指标：点赞=5 · 评论=5 · engagement_velocity=5
> 作者：thisisjedr　|　发布：2026-09-16T15:24:31Z
> 项目链接：<https://docx-editor.dev/solutions/word-to-markdown>
> 采集：2026-09-20T14:04:03+08:00　|　id：`b88a2290c00e8152`

## 正文

Author: EigenPal

Word to Markdown converter with page references | DOCX Editor

# Convert Word to Markdown with page references

Convert .docx to .md in TypeScript. Keep layout-aware page references for document agents and RAG.

Output

Markdown + pages[]

Runtime

Node.js and browsers

License

Apache 2.0

## Extract text with page context

Convert Word (.docx) files to paginated Markdown for agents and retrieval-augmented generation (RAG). Keep page references with body text and read headers and footers separately.

### Pages from document layout

The layout engine calculates page boundaries. Retrieve Markdown by page, or use the continuous document body.

### Separate headers and footers

Read each page's header and footer separately. Index the body without repeating document labels in every chunk.

### Structured content and review data

Extract headings, lists, tables, comments, and tracked changes. Enable image extraction when needed. Check warnings for omitted content.

### Why do page references need a layout engine?

Page boundaries depend on fonts and document layout. Saved page-break hints can be missing or stale. The converter calculates layout before exporting Markdown.

## Build RAG with page references

Attach source metadata before splitting text into retrieval chunks. Pass the retrieved text and its page references to your model.

1. 01

### Convert a document snapshot

Convert DOCX bytes with the library. Set fonts and revision visibility; both affect page boundaries.

Configure fonts
2. 02

### Store the source with each page

Store the document ID, version, export ID, and page number with each chunk.

Build page citations
3. 03

### Let readers inspect the source

Include the document version and page reference in each answer. Retain the export so readers can check the source.

Add a document viewer

### Convert DOCX to .md in TypeScript

Save the document as Markdown or read each page separately. Use page numbers to keep source references with retrieved text.

Check conversion warnings. Page breaks can differ from Word.

Read the integration guide

$ npm install @docx-editor.dev/docx-to-markdown @docx-editor.dev/core Copy command

convert.mts Node.js / TypeScript

```
import { readFile, writeFile } from 'node:fs/promises';
import { exportMarkdown } from '@docx-editor.dev/docx-to-markdown';

const bytes = await readFile('document.docx');
const result = await exportMarkdown(bytes);

await writeFile('document.md', result.markdown, 'utf8');

for (const page of result.pages) {
  console.log(page.number, page.markdown);
}

console.log(result.warnings);
```

## Add paginated Markdown to your ingestion pipeline

### Create documents from each page

Map page Markdown to LangChain documents. Keep source and page metadata when splitting text into retrieval chunks.

### Add a DOCX conversion step

Use this converter for DOCX alongside Docling for other formats. Map the page output to your pipeline's text and metadata fields.

### Index text with page references

Embed the text and store it in Elasticsearch or another vector store. Keep the document version and page number with each chunk for citations.

## Common questions

How do I save DOCX output as a .md file in Node.js?

Write the continuous Markdown output to a UTF-8 .md file. The Node.js example on this page saves document.md. Store page records separately for citations; a .md file does not retain page metadata.

Can I convert a legacy .doc file to Markdown?

Save the .doc file as .docx in Word or another compatible application first. The converter accepts .docx input only.

Will the page numbers match Microsoft Word?

Not always. Fonts, document features, and revision visibility can change page breaks. Configure fonts and check representative files against Word. Page numbers identify physical pages starting at 1, not printed labels that restart by section.

Does Markdown preserve the Word page design?

Markdown preserves supported content and structure, not the full page design. The converter uses layout to group content by page. Continuous Markdown joins split content and omits repeated headers and footers.

Do I need Pro to export pages or review data?

No. Conversion, page output, and review extraction use Apache 2.0. Interactive review editing requires Pro. Bundled fonts retain their own licenses.

Can I run conversion in a serverless function?

Yes. Use a supported Node.js runtime and bundle the WebAssembly and font assets. Allocate CPU and memory for layout. Next.js Edge is unsupported.

Why is DOCX pagination difficult for retrieval tools?

Text extraction alone cannot determine page numbers. Fonts, spacing, and tables affect pagination. A layout engine calculates which text belongs to each page.

For background, see the MarkItDown page-number request, Docling explanation of DOCX page information, and LangChain report of incorrect page metadata.

## Convert your first document

# FainLane | Paste screenshots over SSH

## 评论（5/5）

> **spawrks** · 2026-09-16T15:29:12.000Z　
> This is great, working on a soon to launch Markdown editor soon so this is especially relevant. I'll play around with it later but I'm curious, how are you deciding pagination boundaries? I've found word and docx and various open source projects vary on philosophy and implementation.

---

> **verdverm** · 2026-09-16T16:25:49.000Z　
> How hard is it to go the other direction?I've been doing some writing things where they use Docx and I use Markdown (have been since before the LLM craze). Boy is it annoying to go back and forth, will be trying the one direction anyhow

---

> **thisisjedr** · 2026-09-16T15:30:49.000Z　
> Thanks! Our core product is a Word editor that you can embed in your React / Vue app. So we just repurposed the layout engine to be an accurate converter. You can see how our layout engine "sees" the document in the left tab of the demo.

---

> **thisisjedr** · 2026-09-16T16:27:27.000Z　
> Docx to markdown is a lossy conversion, so getting .docx back is possible but will lose most formatting details

---

> **verdverm** · 2026-09-16T16:43:19.000Z　
> In this case, I would imagine two scenarios1. I have markdown, I want a docx version, that is equivalent to html rendering, markdown's whole point, almost certainly many options out there2. I have docx, I want to make edits in markdown (because vim motions), need to sync those edits back. Ideally just some value swaps in the "DOM"It may very well be the case that Office now supports Markdown natively. I seem to recall possibly seeing that. Google Workspace is as well iirc. One of the two already had support, the other was just releasing the first takes (back when I last looked )

## 导航

- 项目页：[[10-项目/docx-editor.dev_e3cb5ff5]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
