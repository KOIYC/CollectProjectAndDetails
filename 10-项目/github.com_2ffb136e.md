---
type: "project"
title: "Show HN: Shell utility for encrypting and decrypting files using scrypt"
project_url: "https://github.com/nodesocket/cryptr"
first_seen: "2026-09-21T03:11:27+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_nodesocket
  - story_49504769
  - show_hn
lang: "en"
---

# Show HN: Shell utility for encrypting and decrypting files using scrypt

> [!info] 一句话导读
> A simple shell utility for encrypting and decrypting files using OpenSSL.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/nodesocket/cryptr>
> 首次收录：2026-09-21T03:11:27+08:00
> 来源渠道：HN Show HN
> 标签：author_nodesocket, story_49504769, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:33:52+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/bccdc1b144b97519_Show-HN-Shell-utility-for-encrypting-and-decryptin]] |
| 2026-09-21T03:11:27+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/bccdc1b144b97519_Show-HN-Shell-utility-for-encrypting-and-decryptin]] |

## 摘要正文

# nodesocket/cryptr  A simple shell utility for encrypting and decrypting files using OpenSSL.  - Stars: 149 - Forks: 36 - Watchers: 149 - Open issues: 1 - License: Apache License 2.0 - Default branch: master - Created: 2017-10-02T05:59:36Z  ## Languages  - Shell  ## Topics  - aes-256 - aes-256-cbc - aes-encryption - bash - bash-script - bash-scripting - cryptography - decryption - encryption - openssl - shell-script  ## Top Contributors  - nodesocket (28 contributions) - Gu1llaum-3 (4 contributions) - adam12 (2 contributions) - nioupola (2 contributions)  ---  ## README  # cryptr  #### A simple shell utility for encrypting and decrypting files using OpenSSL.  ## Installation  ``` git clone https://github.com/nodesocket/cryptr.git ln -s "$PWD"/cryptr/cryptr.bash /usr/local/bin/cryptr ```  ## Requirements  - shred if optionally deleting original file.  ### Bash tab completion  Add `tools/cryptr-bash-completion.bash` to your tab completion file directory.  ## Commands  ### encrypt  > encrypt \ - Encryptes file with OpenSSL AES-256 cipher block chaining. Writes an encrypted file out *(ciphertext)* appending `.aes` extension.  ``` ➜ cryptr encrypt ./secret-file enter aes-256-cbc encryp…
