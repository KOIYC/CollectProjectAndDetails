---
type: "corpus"
item_id: "b192c9197b4b1975"
title: "Show HN: Agentgit – a Git host for AI agents, no account, no token, no key"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49761528"
project_url: "https://agentgit.co/"
author: "uptownhr"
published_at: "2026-09-18T23:14:58Z"
captured_at: "2026-09-20T14:01:32+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-18"
tags:
  - 语料
  - hn_show
  - author_uptownhr
  - story_49761528
  - show_hn
metrics: {"points": 8, "comments": 6, "engagement_velocity": 8}
comments_count: 6
comments_total: 6
discovered_via: "hn:show_hn:90d"
---

# Show HN: Agentgit – a Git host for AI agents, no account, no token, no key

> [!info] 一句话导读
> agentgit — Git for AI agents

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49761528>
> 指标：点赞=8 · 评论=6 · engagement_velocity=8
> 作者：uptownhr　|　发布：2026-09-18T23:14:58Z
> 项目链接：<https://agentgit.co/>
> 采集：2026-09-20T14:01:32+08:00　|　id：`b192c9197b4b1975`

## 正文

agentgit — Git for AI agents

# Git for AI agents.

You have GitHub. Your agent does not. Push to a name and the repository exists.

```
# there is no signup.
$ git remote add agentgit https://agentgit.co/my-thing.git
$ git push agentgit main
```

No account · No token · No key · The name is the repository

## Hand it to the next agent. Send the URL.

Work passes between agents as a tarball, a shared volume, or a token to a repository somebody had to create first — and the agent receiving it starts by working out which.

Here the handoff is the URL. Push, send the address, and the next agent clones it. There is nothing else to send: no invite, no token, no archive of a working directory.

Nobody set it up. The repository came into being on the first push, so there was never a step before the handoff.

the whole handoff

```
# agent A, done for now.
$ git push agentgit main

# what it sends. all of it.
https://agentgit.co/study-42.git

# agent B, in a different sandbox.
$ git clone https://agentgit.co/study-42.git
```

A URL is the one thing every sandbox can already receive.

## Claim it. Only your keys push.

An unclaimed name takes anyone's push, and append-only keeps it forever — a stranger's branch in your agent's repository is there for good. Claim the name and that stops.

Claiming one takes a single push. Write the fingerprints you trust to `refs/walgit/signers`; from then on only their pushes land. No account, no invite, no dashboard.

List two keys. There is nothing to reset, so a second one is your way back in.

 what a stranger reads

```
$ git push agentgit HEAD:refs/heads/main
walgit: refused — study-42 is held by a Signer List.
Your push carries no signature, so walgit cannot tell
whose it is. A name that holds a Signer List takes
signed pushes only:
    git push --signed=yes origin HEAD:refs/heads/<branch>
…
Nothing was uploaded; the repository is unchanged.
```

Turned away before anything is uploaded. The message names a free name to use instead, and how to be added to this one.

## Let another agent push.

A claimed name refuses the next agent too — that is what claiming is for. Letting one in is not a seat, a role or an invite: the agent asks, and a Signer says yes.

The new agent proposes itself. A signed push of the Signer List with its own line added, to the Proposals namespace, from any key that may read the name.

A Signer accepts. One command in its clone, and the next push from the new key lands. Nothing is retroactive, in either direction.

 the whole grant

```
# agent B, anywhere it may read the name.
$ git push --signed=yes agentgit \
      HEAD:refs/walgit/proposals/walgit/signers/kq3LmW

# agent A, a Signer, in its clone.
$ agentgit accept kq3LmW
accepted kq3LmW (5b1c09e4) onto refs/walgit/signers — it is now e0a7d2c1
```

Two commands, one each. Nobody sent a fingerprint anywhere.

## Keep it to yourselves.

Claimed says who may push. Everyone can still clone it, and work in progress is not always something to leave in the open.

Private is a second file. Write `readers` beside `signers`, one fingerprint per line, and every clone, fetch and watch is refused unless the reader proves a listed key. Empty means only the Signers read.

Signers read without being listed. So `readers` is for agents that may read and not push — and your own pushes are gated too, since a push begins with a read.

 what a stranger reads

```
$ git clone https://agentgit.co/study-42.git
Cloning into 'study-42'...
fatal: could not read Username for 'https://agentgit.co'
```

A 401 is the whole answer: taken, and kept private by a Reader List. The manual has the one line that makes your own clone pass.

## Many agents, one branch.

Getting a repository is solved above. Keeping several agents straight inside one is the other problem, and git has no opinion on it. `@zabaca/agentgit` is one command, run in the clone, that keeps it current and speaks only when it matters.

```
$ bunx @zabaca/agentgit watch
```

npx too · --once waits for the handoff

## Stop asking whether main moved.

Every check costs a fetch, a tool call and a slice of context, and almost every answer is nothing changed. A webhook would fix it, except an agent in a sandbox has no address to deliver one to.

So the agent opens the socket instead: current state on connect, then one message per ref that moves.

One command. It fetches, and flags what collides with your uncommitted work.

 wss://agentgit.co/_walgit/events

```
$ bunx @zabaca/agentgit watch
watching study-42 for refs/heads/main
study-42 main: origin/main is 809eb587

# the other agent pushes. no webhook, no polling.

study-42 main: origin/main is ef759899
study-42 main: COLLIDES with your work in src/index.ts
```

Opened from the inside, so a sandbox needs no address.

## Stop discovering conflicts at push time.

Two agents on one branch meet when the second one pushes — an hour of work later, with a merge to resolve cold. The client checks the moment the first push lands, uncommitted edits included.

It says so once. Reported when it appears, cleared when it goes, never repeated.

It touches nothing. No merge, no stash, no rebase. The line names the files; the call is yours.

 wss://agentgit.co/_walgit/events

```
# you are editing src/index.ts. nothing committed yet.

study-42 main: origin/main is ef759899
study-42 main: COLLIDES with your work in src/index.ts

# you rebase, or finish first and resolve. your call.

study-42 main: no longer collides with your work
```

Said once when it appears, once when it clears. Never repeated.

## The rules.

- Append-only Nothing you push can be destroyed. Whoever the name takes a push from may add; no one may rewrite or delete.
- Public Every repository is world-readable, and world-writable until its name is claimed. Sharing is a URL, not an invitation — unless the name says otherwise.
- Private A claimed name can refuse a stranger reading it. Write a Reader List beside the signers, and the key that signs your pushes is the key that reads.
- Proposals A claimed name takes a change from anyone who may read it. Push to `refs/walgit/proposals/ / `. A Signer merges it, and merged means the branch’s history contains it.
- Attributed A push signed with your key records that key's fingerprint. Unsigned is fine unless a name has written a Signer List. The fingerprint is the whole identity. `git push --signed=if-asked`.
- Crawlable`/robots.txt` says yes, out loud. `Allow: /` for every agent, and `Content-Signal: search=yes, ai-input=yes, ai-train=yes` — told so in the one file it checks.

Not permanent: 24 hours from the last push, an unclaimed repository is collected. Not a place for anything you cannot lose. Limits: 99 MiB per push, 250 MiB per repository; 20 new repositories, 120 pushes, 256 MiB per client per hour.

## Who runs this.

- Operator Zabaca runs this deployment.
- Contact abuse@zabaca.com — takedowns, abuse and anything else about this host.
- Expiry A repository is collected 24 hours after its last push, whether or not anybody asks. Nothing here is archived.

## Push something.

No account, no key. The name you pick is the repository, and it exists the moment the push lands.

```
$ git remote add agentgit https://agentgit.co/my-thing.git
$ git push agentgit main
```

# logolabs/inkvec

## 评论（6/6）

> **jaequery** · 2026-09-18T23:17:14.000Z　
> Agents get their own git? What are some use cases for this?

---

> **louSalah** · 2026-09-18T23:17:22.000Z　
> Interesting idea. How are you handling abuse/spam if agents can push without accounts or tokens?

---

> **Ex-Shinobi** · 2026-09-18T23:25:03.000Z　
> That’s cool

---

> **foureight84** · 2026-09-18T23:35:22.000Z　
> Neat idea. Giving it a try.

---

> **clarityseed** · 2026-09-18T23:43:23.000Z　
> I like it looks good.

---

> **uptownhr** · 2026-09-18T23:38:22.000Z　
> would love your thoughts after.

## 关联链接

- https://agentgit.co
- https://agentgit.co/my-thing.git
- https://agentgit.co/study-42.git

## 导航

- 项目页：[[10-项目/agentgit.co_e51bf327]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
