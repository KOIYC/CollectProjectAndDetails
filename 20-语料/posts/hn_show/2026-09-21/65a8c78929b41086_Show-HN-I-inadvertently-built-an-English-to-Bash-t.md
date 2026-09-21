---
type: "corpus"
item_id: "65a8c78929b41086"
title: "Show HN: I inadvertently built an English to Bash transpiler"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49778185"
project_url: "https://github.com/gioblu/NPC-Forge/blob/main/npcs/termy/README.md"
author: "gioscarab"
published_at: "2026-09-20T17:54:30Z"
captured_at: "2026-09-21T09:44:03+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-09-20"
tags:
  - 语料
  - hn_show
  - author_gioscarab
  - story_49778185
  - show_hn
metrics: {"points": 3, "comments": 3, "engagement_velocity": 3}
comments_count: 3
comments_total: 3
discovered_via: "hn:show_hn:3d"
---

# Show HN: I inadvertently built an English to Bash transpiler

> [!info] 一句话导读
> npcs/termy/README.md

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49778185>
> 指标：点赞=3 · 评论=3 · engagement_velocity=3
> 作者：gioscarab　|　发布：2026-09-20T17:54:30Z
> 项目链接：<https://github.com/gioblu/NPC-Forge/blob/main/npcs/termy/README.md>
> 采集：2026-09-21T09:44:03+08:00　|　id：`65a8c78929b41086`

## 正文

# npcs/termy/README.md

- Branch: main
- Repository: gioblu/NPC-Forge

---

## TERMy
TERMy is an experimental, deterministic terminal assistant implemented using FlintParser and FlintNPC that translates your plain English requests in shell scripts in milliseconds. It is incredibly lightweight and can run on very small targets such as RPI or ESP32, just type `termy` followed by your prompt:

Terminal demonstration

### How to install TERMy
Open the terminal inside the npc-forge repository main directory and digit:
```bash
npc-forge install npcs/termy
```
If you plan to work with the dataset install both `npc-forge` and TERMY in development mode:
```bash
# Clone the forge from the cloud
git clone https://github.com/gioblu/NPC-Forge.git

# Step into the temple of clean code
cd NPC-Forge

# Run the installation script in development mode
chmod +x setup.sh && ./setup.sh --dev

# Install TERMy
npc-forge install npcs/termy
```

### How to use it

Just digit `termy` followed by your request:
```
termy hello
```

You can also write a script in plain english and pass it to termy, create a file `test.termy` with the following content:
```
search on wiki the programma 101
append it to p101.txt
open it in the browser 
```
Then digit:
```
termy -y < test.termy
```
Then digit `termy -y < test.termy` and watch TERMy transpile it to a Shell script and execute it.

### How to add entries to the dataset

Be sure to read carefully the NDF 0.0 (NPC-Forge Dataset Format). In the `npcs/termy/dataset` directory there are `dataset_*.json` and `templates_*.json` files which contain dataset entries organized in categories, such as `dataset_files.json` or `templates_directories.json`.

Once you added an entry remember to restart the server:
```bash
npc-forge reboot
```

### Intent lookup

If you want to explore the abilities of termy you can just write `termy` followed by a keyword:

```
termy files

TERMy | rejected | Confidence: 0.00%

Response: Your request was not specific enough, please choose between the options below! 

Related intents:

1) list files - Lists the files in the current directory.
2) create a file - Creates a new file.
3) encrypt a file - Encrypts or decrypts a file using GPG.
4) manage archives - Compresses or decompresses directories.
5) print json file - Prints JSON file with proper indentation.

```

As you can see TERMy, when is not confident enough on an answer, will output a list of intents related to your prompt.

# TetherPHP

## 评论（3/3）

> **gioscarab** · 2026-09-20T17:56:05.000Z　
> More info here: https://github.com/gioblu/NPC-ForgeHow I built it: https://github.com/gioblu/NPC-Forge/blob/main/docs/developme...A video of TERMy transpiling plain english: https://www.youtube.com/watch?v=QMohFF55opc

---

> **Founderarcstone** · 2026-09-20T17:57:08.000Z　
> Nice work looks good!

---

> **gioscarab** · 2026-09-20T18:03:56.000Z　
> Thank you! Let me know what you think if you try it out :)

## 关联链接

- https://github.com/gioblu/NPC-Forge.git

## 导航

- 项目页：[[10-项目/github.com_c98d2ba4]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
