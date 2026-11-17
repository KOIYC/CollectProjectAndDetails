---
type: "corpus"
item_id: "7e6309e6fa8fe410"
title: "Show HN: Emergency-AI – Offline knowledge base and AI chat (with no Internet)"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50523427"
project_url: "https://github.com/skanga/Emergency-AI"
author: "skanga"
published_at: "2026-11-16T21:17:44Z"
captured_at: "2026-11-17T11:09:12+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-17"
pub_day: "2026-11-16"
tags:
  - 语料
  - hn_show
  - author_skanga
  - story_50523427
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Emergency-AI – Offline knowledge base and AI chat (with no Internet)

> [!info] 一句话导读
> Offline knowledge and AI based assistance for use when the Internet goes down. Local AI, source-cited guides and Kiwix libraries for Windows, Linux and macOS.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50523427>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：skanga　|　发布：2026-11-16T21:17:44Z
> 项目链接：<https://github.com/skanga/Emergency-AI>
> 采集：2026-11-17T11:09:12+08:00　|　id：`7e6309e6fa8fe410`

## 正文

# skanga/Emergency-AI

Offline knowledge and AI based assistance for use when the Internet goes down. Local AI, source-cited guides and Kiwix libraries for Windows, Linux and macOS.

- Stars: 1
- Forks: 0
- Watchers: 1
- Open issues: 2
- License: MIT License
- Default branch: main
- Created: 2026-11-12T22:29:09Z
- Fork: yes

## Languages

- Batchfile
- CSS
- HTML
- JavaScript
- Python
- Shell

## Top Contributors

- skanga (8 contributions)
- sdalberto (4 contributions)
- mahrcio (1 contributions)

---

## README

 Emergency-AI

 Practical knowledge, available offline. Read guides, search reference libraries, and ask an optional AI assistant on your own computer.

 Install ·
 Getting started ·
 User guide ·
 Help

 Windows · macOS · Linux English · Português · Español

Download and configure Emergency-AI while you have internet, then use the downloaded guides, libraries, and AI model offline. The app opens in your browser and runs on your computer. You still need power-for example, a laptop with a charged battery.

Emergency-AI home screen with guide navigation, suggested questions, and model and library selectors

**Watch Emergency-AI in action**

https://github.com/user-attachments/assets/653a4d45-961d-4599-a794-f7ebf48aed10

## What you can do

| Feature | What you can do |
|---|---|
| **Included guides** | Read and search practical information about water, food, shelter, first aid, repairs, energy, and more, in English, Portuguese, or Spanish. |
| **Optional AI** | Ask questions in everyday language. The local model uses retrieved passages to write answers; source links let you check the material. |
| **Extra libraries** | Download reference collections such as medical Wikipedia, repair guides, and post-disaster manuals for offline use. |
| **Phone access** | Use a phone's browser over the same local network while the app runs on your computer. |
| **Your documents** | Add text documents to the kit and include them in searches. |

**You can start without AI.** The included guides are ready to read and search without downloading a model or extra libraries.

## Before you start

- **Computer:** Windows 10/11, macOS, or Linux on a supported x86-64 or ARM64 system. See platform details.
- **Internet:** needed for installation and optional downloads. Prepare before an outage.
- **Memory:** the lightweight AI model recommends 8 GB system RAM. A dedicated graphics card is not required. Guide search does not need the AI model.
- **Storage:** extra libraries start at about 3 GiB; the lightweight model adds about 1.1 GB. Allow additional space for software, extraction, and updates. See download choices.

The installer includes Python, the software that runs the app. You do not need to install Python or Git separately.

## Install

Create a new, empty folder where you want to keep Emergency-AI. Save the installer for your computer in that folder. On GitHub, right-click the download link and choose **Save link as**.

| Computer | Download | Run the installer |
|---|---|---|
| **Windows** | install.bat | Double-click `install.bat`. |
| **macOS** | install.sh | Open Terminal in that folder and run `sh install.sh`. |
| **Linux** | install.sh | Open a terminal in that folder and run `sh install.sh`. |

Need help opening a terminal or choosing downloads? Follow Getting started. Experienced users can use the terminal installation commands.

**Windows installation walkthrough (2:19)** - download the installer, choose the lightweight model and minimal libraries, then search a guide and ask a question. Long download waits are trimmed from the video.

https://github.com/user-attachments/assets/3c3d246f-f09e-45c0-a4ba-8772f8008c8d

When the installer asks about first-time setup, choose **Y** to add AI and libraries now. For a small starting setup, choose **Recommended choices**, the lightweight **LFM3 1.7B** model, **minimal** libraries, and **this computer**. Choose these entries explicitly; pressing Enter at every prompt does not necessarily select minimal libraries.

To begin with only the included guides, skip first-time setup and open the app. At the first-use menu, choose **Use guides now and remember this choice**. You can add downloads later.

Downloads can take a long time. Keep the installer window open until it finishes. If a download fails, use the recovery instructions.

## Open it and try it

After installation, open the launcher in your Emergency-AI folder. Use the same launcher on future visits; you do not need to install again.

| Computer | Open the app |
|---|---|
| **Windows** | Double-click `run.bat`. |
| **macOS** | Double-click `run.command`. On first use, right-click and choose **Open** if needed. |
| **Linux** | Open a terminal in the folder and run `./run.sh`. |

Your browser should open at. Keep the app's terminal window open while using it.

1. Open a guide from the sidebar, or search for a topic such as **water**.
2. Try a question using **Ask the AI**. Without a model, the app shows source passages instead.
3. Open a source link under the response to read the original material.

Before relying on the kit offline, test it without internet. To stop the app, return to its terminal window and press **Ctrl+C**.

## Guides and help

These guides are included in the project folder so you can keep them with the kit. The videos above are hosted online.

| You want to… | Read |
|---|---|
| Install for the first time and choose setup options | Getting started |
| Use guides, questions, languages, and source links | Using Emergency-AI |
| Connect a phone | Use it on your phone |
| Choose models or download more libraries | Downloads and models |
| Add documents or move the kit to another computer | User guide |
| Fix a failed download or an app that will not open | Troubleshooting |
| Configure engines, use terminal commands, or run tests | Technical reference |

## Limitations

Emergency-AI is educational material, not a replacement for emergency services or professional medical care. AI answers can be wrong, and a citation does not prove that an answer is supported. The bundled guides have known content issues awaiting review. Downloaded libraries are snapshots and may contain outdated information.

Local-network sharing is enabled by default. Connected devices can read indexed personal documents too. See phone access and sharing controls.

## Contributing and licenses

Corrections with sources, new guides, and translations are welcome. Keep a `> Source:` line in English sections containing technical or health guidance, and use the equivalent label in translations. Keep guide filenames consistent across languages. See developer checks.

Code: MIT. Included guides: CC BY-SA 4.0. Downloaded software, libraries, and models have their own licenses; see model choices.

Based on IA da Sobrevivência by Silviano Dalberto Pessi (Ideias Livres Desenvolvimentos) and contributors. Original license and copyright notices are retained. Offline terminal QR codes use Project Nayuki's MIT-licensed QR encoder.

# codenotary/agentmon-live

## 关联链接

- https://github.com/user-attachments/assets/3c3d246f-f09e-45c0-a4ba-8772f8008c8d
- https://github.com/user-attachments/assets/653a4d45-961d-4599-a794-f7ebf48aed10

## 导航

- 项目页：[[10-项目/github.com_068ec693]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
