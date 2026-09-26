---
type: "corpus"
item_id: "a41d3a26001d6406"
title: "Show HN: Encryption as a Service"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49846752"
project_url: "https://rypt.dev/"
author: "levidurfee"
published_at: "2026-09-25T16:36:14Z"
captured_at: "2026-09-26T09:41:08+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-26"
pub_day: "2026-09-25"
tags:
  - 语料
  - hn_show
  - author_levidurfee
  - story_49846752
  - show_hn
metrics: {"points": 3, "comments": 2, "engagement_velocity": 3}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:3d"
---

# Show HN: Encryption as a Service

> [!info] 一句话导读
> Encrypt a field in five minutes.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49846752>
> 指标：点赞=3 · 评论=2 · engagement_velocity=3
> 作者：levidurfee　|　发布：2026-09-25T16:36:14Z
> 项目链接：<https://rypt.dev/>
> 采集：2026-09-26T09:41:08+08:00　|　id：`a41d3a26001d6406`

## 正文

Skip to content
rypt .dev
How it works
Pricing
Security
Sign in
Encrypt a field in five minutes.
Symmetric encryption over HTTPS. One bearer token, one call per operation, and no key rings or IAM policies to set up. Start with one free key and 10,000 operations a month.
Get an API key
 Sign in at dashboard.rypt.dev . Your first sign-in creates your account.
visitor@rypt.dev:~/demo
 idle
$ cat visitor.txt user-agent Mozilla/5.0 language en-US timezone UTC viewport 1280 x 800 received - $
This is an illustration. With JavaScript on, the page encrypts your browser's details locally, with a throwaway key, to show what ciphertext looks like. It makes no network request. Run for real, the same command sends the file to the rypt API over HTTPS and writes the ciphertext it gets back, and the key stays with rypt.
The command is real: rypt.sh , the command line for the API, installs with one line.
Run it again
The call
Send plaintext, get ciphertext back
Every operation is one POST to api.rypt.dev with your API key as a bearer token. Bodies are JSON, and binary fields are standard base64 with padding. This is the whole encrypt call.
Request
$ curl -sS -X POST https://api.rypt.dev/v1/keys/0f1e2d3c-4b5a-6978-8796-a5b4c3d2e1f0/encrypt \
 -H "Authorization: Bearer ry_K3pQ7xTa_9fL..." \
 -H "content-type: application/json" \
 -d '{"plaintext":"aGVsbG8gd29ybGQ="}'
Response
{"ciphertext":"CiQALS4vMDEyMzQ1Njc4OTo7PD0+P0BB..."}
Decrypt is the same call to /decrypt in place of /encrypt , with {"ciphertext": ...} in the body. It returns {"plaintext": ...} . The ciphertext records which key version made it, so it still decrypts after a rotation for as long as the key keeps that version. The free key keeps only its current version, so rotating it makes everything encrypted before the rotation undecryptable at once.
Plaintext is 1 to 65,536 bytes per call, or 8,192 bytes together with any aad on a Hardware key. The path holds the key's id. The token is redacted here; a real API key is 44 characters and starts ry_ . The response shown is from a Software key. A free or extra wrapped key returns an envelope of rypt's own, which looks different.
From sign-in to the first ciphertext
Sign in at dashboard.rypt.dev . Your first sign-in creates your account and makes you its owner.
Create a key. Give it a name and choose its tier. A key's tier is fixed when you create it.
Issue an API key. It is on screen once and cannot be recovered, so copy it then.
Make the call. The dashboard shows the encrypt and decrypt round-trip in curl, Node and Python.
Operations
Direct for small values, envelope for everything else
Direct mode is encrypt and decrypt: send the value, store what comes back. Envelope mode is for files and large objects. Ask for a data key, encrypt the data with it in your own code, keep only the wrapped key beside the data, and unwrap it when you need to read.
Operation What it does Send Get back
encrypt Encrypts up to 64 KiB under the key's current version, or 8 KiB together with any aad on a Hardware key. plaintext ciphertext
decrypt Decrypts under whichever kept version made the ciphertext. ciphertext plaintext
wrap Generates a 32-byte data key and returns it with its wrapped form. Send your own data key of 16, 24 or 32 bytes and only the wrapped form comes back. dek optional dek , wrapped
unwrap Returns the data key from its wrapped form. wrapped dek
rewrap Moves a ciphertext onto the key's current version in one call. The plaintext never comes back to you. ciphertext ciphertext
Every operation also takes an optional aad . A value encrypted with an aad only decrypts with the same one, which binds it to its row, file or tenant. Each operation counts once toward the key's monthly operations, rewrap included.
Audit
Every operation on a key is written down
Each create, rotate and delete, and each encrypt, decrypt, wrap, unwrap and rewrap on one of your keys, writes an audit row, whether it succeeds or fails. A failed create is recorded without a key, so it appears in no key's log. Requests refused before they reach a key are not recorded, for example a bad API key, the rate limit, a malformed body or an unknown key id.
The log is append-only. A call whose row cannot be written returns an error, never a success, though the operation may already have taken effect. After an error on a create, rotate or delete, check the key before you retry.
GET /v1/keys/{id}/audit
[{"id":42,"ts":"2026-09-16T10:00:00.123456Z","key_id":"0f1e...","api_key_id":"1a2b...","user_id":null,
 "op":"encrypt","kms_version":"3","result":"ok","error_code":null,
 "request_id":"018f8a0e-2a4a-7b8e-9f1c-2f7a6d5c4b3a","src_ip":"10.0.0.7","bytes":11}]
bytes is the length of the operation's input, never its content. No request or response body is ever written to rypt's logs. Read a key's log through the API or on the key's page in the dashboard.
Pricing
Four tiers, priced per key
Every key has a tier and a monthly price. The calls are identical across all four. What changes is where the key material lives, how many operations a month the price includes, and what happens past them.
Tier Key material Price per key Operations included a month Past the included operations
Free A data key held by rypt, wrapped by an HSM root key. One per account. $0 10,000 Refused until 00:00 UTC on the 1st
Extra wrapped Each additional key held the same way as the free key $3 a month 50,000 $0.10 per 10,000
Software A dedicated key, protected in software $10 a month 100,000 $0.20 per 10,000
Hardware A dedicated key in a hardware security module $35 a month 250,000 $0.50 per 10,000
A key's tier is fixed when it is created. Hardware keys accept at most 8,192 bytes of plaintext and aad together per call. Only the five operations above are counted, and only once the cryptography succeeds. The free key keeps only its current version, so rotating it makes anything encrypted under the previous version undecryptable at once.
A free key at its cap
{"error":"ops_cap_reached","message":"monthly operation cap reached",
 "request_id":"018f8a0e-...","cap":10000,"resets_at":"2026-10-01T00:00:00Z"}
Custody
Your keys stay with rypt
The keys themselves never reach you or your servers. You hold an API key that can use them. That API key can also create, rotate and delete every key in your account, so guard it like a root credential. A key rotates only when you call rotate, never on a schedule.
This is not zero-knowledge. Your plaintext reaches rypt so it can be encrypted, and rypt holds the keys that decrypt it. If that rules it out for you, use a key management service in your own cloud account instead. The security page names the one underneath and says where the keys live.
How keys are held
Start with a free key.
One key and 10,000 operations a month, at no cost. Paid keys start at $3 a month.
Get an API key
Copyright 2026 x6c LLC | rypt.dev | This site uses Google Analytics.
Dashboard
Command line
Security
Privacy
Terms
support@rypt.dev

## 评论（2/2）

> **annrap1d** · 2026-09-25T18:53:26.000Z　
> This is really nicely done. One question. Since you state 'this is not zero-knowledge' because plaintext briefly hits your API over HTTPS, what precise architectural isolation protects that plaintext in memory while it is being encrypted?

---

> **levidurfee** · 2026-09-25T20:45:18.000Z　
> That's an excellent question! It's currently running on Google Cloud Run, which to my knowledge, doesn't offer any encrypted memory options. So, as of now, there isn't any architecture in place to protect the plaintext.It's definitely something we've thought about. And something we may pursue.

## 关联链接

- https://api.rypt.dev/v1/keys/0f1e2d3c-4b5a-6978-8796-a5b4c3d2e1f0/encrypt

## 导航

- 项目页：[[10-项目/rypt.dev_c5e0037b]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
