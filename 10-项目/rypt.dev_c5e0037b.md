---
type: "project"
title: "Show HN: Encryption as a Service"
project_url: "https://rypt.dev/"
first_seen: "2026-09-26T09:41:08+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_levidurfee
  - story_49846752
  - show_hn
lang: "en"
---

# Show HN: Encryption as a Service

> [!info] 一句话导读
> Encrypt a field in five minutes.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://rypt.dev/>
> 首次收录：2026-09-26T09:41:08+08:00
> 来源渠道：HN Show HN
> 标签：author_levidurfee, story_49846752, show_hn
> 最新指标：点赞=3 · 评论=2 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-26T09:41:08+08:00 | HN Show HN | 点赞=3 · 评论=2 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-26/a41d3a26001d6406_Show-HN-Encryption-as-a-Service]] |

## 摘要正文

Skip to content rypt .dev How it works Pricing Security Sign in Encrypt a field in five minutes. Symmetric encryption over HTTPS. One bearer token, one call per operation, and no key rings or IAM policies to set up. Start with one free key and 10,000 operations a month. Get an API key  Sign in at dashboard.rypt.dev . Your first sign-in creates your account. visitor@rypt.dev:~/demo  idle $ cat visitor.txt user-agent Mozilla/5.0 language en-US timezone UTC viewport 1280 x 800 received - $ This is an illustration. With JavaScript on, the page encrypts your browser's details locally, with a throwaway key, to show what ciphertext looks like. It makes no network request. Run for real, the same command sends the file to the rypt API over HTTPS and writes the ciphertext it gets back, and the key stays with rypt. The command is real: rypt.sh , the command line for the API, installs with one line. Run it again The call Send plaintext, get ciphertext back Every operation is one POST to api.rypt.dev with your API key as a bearer token. Bodies are JSON, and binary fields are standard base64 with padding. This is the whole encrypt call. Request $ curl -sS -X POST https://api.rypt.dev/v1/keys/0f1…
