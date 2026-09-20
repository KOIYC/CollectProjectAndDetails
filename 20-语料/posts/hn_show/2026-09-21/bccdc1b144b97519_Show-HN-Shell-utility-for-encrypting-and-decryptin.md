---
type: "corpus"
item_id: "bccdc1b144b97519"
title: "Show HN: Shell utility for encrypting and decrypting files using scrypt"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49504769"
project_url: "https://github.com/nodesocket/cryptr"
author: "nodesocket"
published_at: "2026-08-31T01:55:41Z"
captured_at: "2026-09-21T03:11:27+08:00"
lang: "en"
kind: "post"
topic: 内容/媒体
shard: "2026-09-21"
pub_day: "2026-08-31"
tags:
  - 语料
  - hn_show
  - author_nodesocket
  - story_49504769
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:52d"
---

# Show HN: Shell utility for encrypting and decrypting files using scrypt

> [!info] 一句话导读
> A simple shell utility for encrypting and decrypting files using OpenSSL.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49504769>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：nodesocket　|　发布：2026-08-31T01:55:41Z
> 项目链接：<https://github.com/nodesocket/cryptr>
> 采集：2026-09-21T03:11:27+08:00　|　id：`bccdc1b144b97519`

## 正文

# nodesocket/cryptr

A simple shell utility for encrypting and decrypting files using OpenSSL.

- Stars: 149
- Forks: 36
- Watchers: 149
- Open issues: 1
- License: Apache License 2.0
- Default branch: master
- Created: 2017-10-02T05:59:36Z

## Languages

- Shell

## Topics

- aes-256
- aes-256-cbc
- aes-encryption
- bash
- bash-script
- bash-scripting
- cryptography
- decryption
- encryption
- openssl
- shell-script

## Top Contributors

- nodesocket (28 contributions)
- Gu1llaum-3 (4 contributions)
- adam12 (2 contributions)
- nioupola (2 contributions)

---

## README

# cryptr

#### A simple shell utility for encrypting and decrypting files using OpenSSL.

## Installation

```
git clone https://github.com/nodesocket/cryptr.git
ln -s "$PWD"/cryptr/cryptr.bash /usr/local/bin/cryptr
```

## Requirements

- shred if optionally deleting original file.

### Bash tab completion

Add `tools/cryptr-bash-completion.bash` to your tab completion file directory.

## Commands

### encrypt

> encrypt \ - Encryptes file with OpenSSL AES-256 cipher block chaining. Writes an encrypted file out *(ciphertext)* appending `.aes` extension.

```
➜ cryptr encrypt ./secret-file
enter aes-256-cbc encryption password:
Verifying - enter aes-256-cbc encryption password:
do you want to shred the original file? (y/N): N
```

```
➜ ls -alh
-rw-r--r--  1 user  group   1.0G Oct  1 13:33 secret-file
-rw-r--r--  1 user  group   1.0G Oct  1 13:34 secret-file.aes
```

You may optionally define the password to use when encrypting using the `CRYPTR_PASSWORD` environment variable _(be aware of shell history storing passwords)_. This enables non-interactive/batch operations.

```
➜ CRYPTR_PASSWORD=A1EO7S9SsQYcPChOr47n cryptr encrypt ./secret-file
```

### decrypt

> decrypt \ - Decrypt encrypted file using OpenSSL AES-256 cipher block chaining. Writes a decrypted file out *(plaintext)* removing `.aes` extension.

```
➜ ls -alh
-rw-r--r--  1 user  group   1.0G Oct  1 13:34 secret-file.aes
```

```
➜ cryptr decrypt ./secret-file.aes
enter aes-256-cbc decryption password:
```

```
➜ ls -alh
-rw-r--r--  1 user  group   1.0G Oct  1 13:35 secret-file
-rw-r--r--  1 user  group   1.0G Oct  1 13:34 secret-file.aes
```

You may optionally define the password to use when decrypting using the `CRYPTR_PASSWORD` environment variable _(be aware of shell history storing passwords)_. This enables non-interactive/batch operations.

```
➜ CRYPTR_PASSWORD=A1EO7S9SsQYcPChOr47n cryptr decrypt ./secret-file.aes
```

To print the plaintext to `stdout` instead of writing the file to disk pass the `--stdout` flag as the **final** argument to the decrypt command:

```
➜ cryptr decrypt ./secret-file.aes --stdout
```

### help

> help - Displays help

```
➜ cryptr help
Usage: cryptr command <command-specific-options>

  encrypt <file>                  Encrypt file
  decrypt <file.aes> [--stdout]   Decrypt encrypted file
  help                            Displays help
  version                         Displays the current version

```

### version

> version - Displays the current version

```
➜ cryptr version
cryptr 3.0.0
```

### default

> default - Displays the current version and help

```
➜ cryptr
cryptr 3.0.0

Usage: cryptr command <command-specific-options>

  encrypt <file>                  Encrypt file
  decrypt <file.aes> [--stdout]   Decrypt encrypted file
  help                            Displays help
  version                         Displays the current version

```

## Changelog

https://github.com/nodesocket/cryptr/blob/master/CHANGELOG.md

## Support, Bugs, And Feature Requests

Create issues here in GitHub (https://github.com/nodesocket/cryptr/issues).

## Versioning

For transparency and insight into the release cycle, and for striving to maintain backward compatibility, cryptr will be maintained under the semantic versioning guidelines.

Releases will be numbered with the follow format:

`.. `

And constructed with the following guidelines:

+ Breaking backward compatibility bumps the major (and resets the minor and patch)
+ New additions without breaking backward compatibility bumps the minor (and resets the patch)
+ Bug fixes and misc changes bumps the patch

For more information on semantic versioning, visit http://semver.org/.

## License & Legal

Copyright 2026 Justin Keller

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

## 关联链接

- http://semver.org/.
- http://www.apache.org/licenses/LICENSE-2.0
- https://github.com/nodesocket/cryptr.git
- https://github.com/nodesocket/cryptr/blob/master/CHANGELOG.md
- https://github.com/nodesocket/cryptr/issues

## 导航

- 项目页：[[10-项目/github.com_2ffb136e]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`内容/媒体`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
