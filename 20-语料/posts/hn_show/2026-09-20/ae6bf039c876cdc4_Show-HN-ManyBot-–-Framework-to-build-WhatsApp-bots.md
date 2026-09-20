---
type: "corpus"
item_id: "ae6bf039c876cdc4"
title: "Show HN: ManyBot – Framework to build WhatsApp bots, without the boring part"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49727647"
project_url: "https://manybot.org/"
author: "synt-xerror"
published_at: "2026-09-16T14:31:40Z"
captured_at: "2026-09-20T09:37:02+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-20"
pub_day: "2026-09-16"
tags:
  - 语料
  - hn_show
  - author_synt-xerror
  - story_49727647
  - show_hn
metrics: {"points": 9, "comments": 0, "engagement_velocity": 9}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: ManyBot – Framework to build WhatsApp bots, without the boring part

> [!info] 一句话导读
> ManyBot - Construa seu bot para WhatsApp, sem a parte chata

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49727647>
> 指标：点赞=9 · 评论=0 · engagement_velocity=9
> 作者：synt-xerror　|　发布：2026-09-16T14:31:40Z
> 项目链接：<https://manybot.org/>
> 采集：2026-09-20T09:37:02+08:00　|　id：`ae6bf039c876cdc4`

## 正文

ManyBot - Construa seu bot para WhatsApp, sem a parte chata

# Construa seu bot para WhatsApp, sem a parte chata.

Framework modular para desenvolver bots para WhatsApp. Simples, extensível e feito pela comunidade.

O ManyBot não é um serviço, mas sim um framework. A ideia central é que o bot seja apenas um núcleo estável, enquanto toda a lógica de negócio e funcionalidades residam em plugins independentes.

Isso permite que você adicione, remova ou atualize recursos sem a necessidade de reiniciar o sistema inteiro ou lidar com a complexidade de um código monolítico.

## Baileys puro vs ManyBot

O ManyBot é um framework TypeScript/JavaScript baseado em plugins, construído como uma camada de abstração sobre o Baileys — ele cuida da conexão, reconexão e do roteamento de mensagens, pra você focar só na lógica do comando.

Baileys puro~50 linhas

```
const {
  default: makeWASocket,
  useMultiFileAuthState,
  DisconnectReason
} = require("@whiskeysockets/baileys");

async function start() {
  const { state, saveCreds } = await useMultiFileAuthState("./auth");

  const sock = makeWASocket({
    auth: state,
    printQRInTerminal: true
  });

  sock.ev.on("creds.update", saveCreds);

  sock.ev.on("connection.update", ({ connection, lastDisconnect }) => {
    if (connection === "open") {
      console.log("Connected to WhatsApp");
    }

    if (connection === "close") {
      const shouldReconnect =
        lastDisconnect?.error?.output?.statusCode !==
        DisconnectReason.loggedOut;

      if (shouldReconnect) start();
    }
  });

  sock.ev.on("messages.upsert", async ({ messages, type }) => {
    if (type !== "notify") return;

    const message = messages[0];
    if (!message.message || message.key.fromMe) return;

    const jid = message.key.remoteJid;

    const text =
      message.message.conversation ||
      message.message.extendedTextMessage?.text ||
      "";

    if (text === "!ping") {
      await sock.sendMessage(jid, {
        text: "Pong!"
      });
    }
  });
}

start();
```

Com ManyBot 4 linhas

```
export default async function (ctx) {
  const { msg } = ctx;
  if (!msg.is("ping")) return;
  msg.reply.text("Pong!");
}
```

## O que você ganha:

Modularidade

Tudo é um plugin. Desde comandos simples até integrações complexas de IA, cada funcionalidade vive em seu próprio espaço.

Resiliência

O framework isola falhas. Se um plugin apresentar um erro crítico, o núcleo captura a exceção e mantém o restante do bot operando.

Ferramentas

O ManyPlug CLI automatiza o ciclo de vida dos plugins: da criação do scaffold à validação estática de dependências.

Suporte nativo a módulos ESM e tipagem rigorosa, garantindo desenvolvimento fluido e menos propenso a erros.

# Fortitude-Group/OmnisBench

## 导航

- 项目页：[[10-项目/manybot.org_bc38a935]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
