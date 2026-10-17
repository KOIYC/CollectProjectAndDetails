---
type: "corpus"
item_id: "13f447c6e25731b7"
title: "Show HN: Putaway – sorts your Mac's Downloads into the folders you have"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50122669"
project_url: "https://github.com/devYRPauli/putaway"
author: "yashrajpandey"
published_at: "2026-10-16T18:48:37Z"
captured_at: "2026-10-17T13:35:15+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-17"
pub_day: "2026-10-16"
tags:
  - 语料
  - hn_show
  - author_yashrajpandey
  - story_50122669
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Putaway – sorts your Mac's Downloads into the folders you have

> [!info] 一句话导读
> My Downloads folder is full of files like download (3).pdf, IMG_4821.jpg, and Untitled.docx. I already have folders for them in Documents. I never move them bec…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50122669>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：yashrajpandey　|　发布：2026-10-16T18:48:37Z
> 项目链接：<https://github.com/devYRPauli/putaway>
> 采集：2026-10-17T13:35:15+08:00　|　id：`13f447c6e25731b7`

## 正文

My Downloads folder is full of files like download (3).pdf, IMG_4821.jpg, and Untitled.docx. I already have folders for them in Documents. I never move them because I have to open each file to know what it is. Putaway does that part.It reads the start of each file on your Mac: PDF text, OCR for scans and photos, Word, Excel, CSV, and HTML. Then it picks one of the folders you already have. It never makes new folders. It shows you the plan first. Nothing moves until you click Move, and Undo puts everything back.Demo (this run uses a SubQ key, so some files are ready to move): https://github.com/devYRPauli/putaway/blob/main/docs/demo.gi...You choose the model. The default is Apple Intelligence on your Mac. It is free, and nothing leaves your Mac. You can also use your own model through any OpenAI-compatible server, such as Ollama or LM Studio. Or you can add your own SubQ or Jev API key. Those two give a probability for each folder, so Putaway moves the files they are sure about. With Apple or your own model, you confirm each file.I tested the released build on 107 files with messy names: public IRS forms, papers, receipts, photos, and spreadsheets, plus fake secret files and a partial download. There were 19 target folders, including decoy folders that apps make, such as Zoom and Adobe. Files in an acceptable folder: SubQ 88%, Jev 85%, qwen2.5 7B in Ollama 82%, Apple's on-device model 67% (of the 99 files it agreed to read). When SubQ or Jev moved a file on its own, it was right 132 of 136 times.One surprise: Apple's on-device model refused to read three blank government forms, including the IRS 1040, as unsafe content. Putaway leaves those files in place and tells you why.It never reads files with names like .env, id_rsa, or recovery-codes.txt. If a file's text looks like a private key or a token, it does not send it. It never overwrites a file, and it skips downloads that are not complete.Install (Apple Silicon, macOS 26). The install script is 33 lines, so you can read it first: curl -fsSL https://raw.githubusercontent.com/devYRPauli/putaway/main/install.sh | bash

 brew install devyrpauli/tap/putaway

It is a Swift menu bar app and a CLI, MIT-licensed, with no dependencies. I do not pay for an Apple developer account, so the app is not notarized. The curl and brew installs do not show the Gatekeeper prompt.I want to know which files it puts in the wrong folder, and which file types it misses. Keynote, Pages, and pptx files are filed by name only for now.

## 关联链接

- https://github.com/devYRPauli/putaway/blob/main/docs/demo.gi...You
- https://raw.githubusercontent.com/devYRPauli/putaway/main/install.sh

## 导航

- 项目页：[[10-项目/github.com_185d2056]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
