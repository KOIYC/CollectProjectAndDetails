---
type: "project"
title: "Show HN: ManyBot – Framework to build WhatsApp bots, without the boring part"
project_url: "https://manybot.org/"
first_seen: "2026-09-20T09:37:02+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_synt-xerror
  - story_49727647
  - show_hn
lang: "en"
---

# Show HN: ManyBot – Framework to build WhatsApp bots, without the boring part

> [!info] 一句话导读
> ManyBot - Construa seu bot para WhatsApp, sem a parte chata

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://manybot.org/>
> 首次收录：2026-09-20T09:37:02+08:00
> 来源渠道：HN Show HN
> 标签：author_synt-xerror, story_49727647, show_hn
> 最新指标：点赞=9 · 评论=0 · engagement_velocity=9

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=9 · 评论=0 · engagement_velocity=9 | [[20-语料/posts/hn_show/2026-09-20/ae6bf039c876cdc4_Show-HN-ManyBot-–-Framework-to-build-WhatsApp-bots]] |
| 2026-09-20T09:37:02+08:00 | HN Show HN | 点赞=9 · 评论=0 · engagement_velocity=9 | [[20-语料/posts/hn_show/2026-09-20/ae6bf039c876cdc4_Show-HN-ManyBot-–-Framework-to-build-WhatsApp-bots]] |

## 摘要正文

ManyBot - Construa seu bot para WhatsApp, sem a parte chata  # Construa seu bot para WhatsApp, sem a parte chata.  Framework modular para desenvolver bots para WhatsApp. Simples, extensível e feito pela comunidade.  O ManyBot não é um serviço, mas sim um framework. A ideia central é que o bot seja apenas um núcleo estável, enquanto toda a lógica de negócio e funcionalidades residam em plugins independentes.  Isso permite que você adicione, remova ou atualize recursos sem a necessidade de reiniciar o sistema inteiro ou lidar com a complexidade de um código monolítico.  ## Baileys puro vs ManyBot  O ManyBot é um framework TypeScript/JavaScript baseado em plugins, construído como uma camada de abstração sobre o Baileys — ele cuida da conexão, reconexão e do roteamento de mensagens, pra você focar só na lógica do comando.  Baileys puro~50 linhas  ``` const {   default: makeWASocket,   useMultiFileAuthState,   DisconnectReason } = require("@whiskeysockets/baileys");  async function start() {   const { state, saveCreds } = await useMultiFileAuthState("./auth");    const sock = makeWASocket({     auth: state,     printQRInTerminal: true   });    sock.ev.on("creds.update", saveCreds);    s…
