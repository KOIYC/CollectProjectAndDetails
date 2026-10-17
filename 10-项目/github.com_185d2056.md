---
type: "project"
title: "Show HN: Putaway – sorts your Mac's Downloads into the folders you have"
project_url: "https://github.com/devYRPauli/putaway"
first_seen: "2026-10-17T13:35:15+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_yashrajpandey
  - story_50122669
  - show_hn
lang: "en"
---

# Show HN: Putaway – sorts your Mac's Downloads into the folders you have

> [!info] 一句话导读
> My Downloads folder is full of files like download (3).pdf, IMG_4821.jpg, and Untitled.docx. I already have folders for them in Documents. I never move them bec…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/devYRPauli/putaway>
> 首次收录：2026-10-17T13:35:15+08:00
> 来源渠道：HN Show HN
> 标签：author_yashrajpandey, story_50122669, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-17T13:35:15+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-10-17/13f447c6e25731b7_Show-HN-Putaway-–-sorts-your-Mac's-Downloads-into]] |

## 摘要正文

My Downloads folder is full of files like download (3).pdf, IMG_4821.jpg, and Untitled.docx. I already have folders for them in Documents. I never move them because I have to open each file to know what it is. Putaway does that part.It reads the start of each file on your Mac: PDF text, OCR for scans and photos, Word, Excel, CSV, and HTML. Then it picks one of the folders you already have. It never makes new folders. It shows you the plan first. Nothing moves until you click Move, and Undo puts everything back.Demo (this run uses a SubQ key, so some files are ready to move): https://github.com/devYRPauli/putaway/blob/main/docs/demo.gi...You choose the model. The default is Apple Intelligence on your Mac. It is free, and nothing leaves your Mac. You can also use your own model through any OpenAI-compatible server, such as Ollama or LM Studio. Or you can add your own SubQ or Jev API key. Those two give a probability for each folder, so Putaway moves the files they are sure about. With Apple or your own model, you confirm each file.I tested the released build on 107 files with messy names: public IRS forms, papers, receipts, photos, and spreadsheets, plus fake secret files and a parti…
