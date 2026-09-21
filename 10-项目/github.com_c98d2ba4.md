---
type: "project"
title: "Show HN: I inadvertently built an English to Bash transpiler"
project_url: "https://github.com/gioblu/NPC-Forge/blob/main/npcs/termy/README.md"
first_seen: "2026-09-21T09:44:03+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_gioscarab
  - story_49778185
  - show_hn
lang: "en"
---

# Show HN: I inadvertently built an English to Bash transpiler

> [!info] 一句话导读
> npcs/termy/README.md

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/gioblu/NPC-Forge/blob/main/npcs/termy/README.md>
> 首次收录：2026-09-21T09:44:03+08:00
> 来源渠道：HN Show HN
> 标签：author_gioscarab, story_49778185, show_hn
> 最新指标：点赞=3 · 评论=3 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T09:44:03+08:00 | HN Show HN | 点赞=3 · 评论=3 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-21/65a8c78929b41086_Show-HN-I-inadvertently-built-an-English-to-Bash-t]] |

## 摘要正文

# npcs/termy/README.md  - Branch: main - Repository: gioblu/NPC-Forge  ---  ## TERMy TERMy is an experimental, deterministic terminal assistant implemented using FlintParser and FlintNPC that translates your plain English requests in shell scripts in milliseconds. It is incredibly lightweight and can run on very small targets such as RPI or ESP32, just type `termy` followed by your prompt:  Terminal demonstration  ### How to install TERMy Open the terminal inside the npc-forge repository main directory and digit: ```bash npc-forge install npcs/termy ``` If you plan to work with the dataset install both `npc-forge` and TERMY in development mode: ```bash # Clone the forge from the cloud git clone https://github.com/gioblu/NPC-Forge.git  # Step into the temple of clean code cd NPC-Forge  # Run the installation script in development mode chmod +x setup.sh && ./setup.sh --dev  # Install TERMy npc-forge install npcs/termy ```  ### How to use it  Just digit `termy` followed by your request: ``` termy hello ```  You can also write a script in plain english and pass it to termy, create a file `test.termy` with the following content: ``` search on wiki the programma 101 append it to p101.txt…
