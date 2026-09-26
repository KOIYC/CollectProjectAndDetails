---
type: "corpus"
item_id: "a0a6055cc981434a"
title: "Show HN: Claude-account – switch Claude Code accounts without logging in again"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49111019"
project_url: "https://github.com/hamzarehmandeveloper/claude-account"
author: "hamza_rehman"
published_at: "2026-07-30T14:58:59Z"
captured_at: "2026-09-26T10:00:49+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-21"
pub_day: "2026-07-30"
tags:
  - 语料
  - hn_show
  - author_hamza_rehman
  - story_49111019
  - show_hn
metrics: {"points": 54, "comments": 31, "engagement_velocity": 54}
comments_count: 29
comments_total: 31
discovered_via: "hn:show_hn:83d"
---

# Show HN: Claude-account – switch Claude Code accounts without logging in again

> [!info] 一句话导读
> I use separate Claude Code accounts for work and personal projects. Having to log out and go through the login flow every time I switched accounts became annoyi…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49111019>
> 指标：点赞=54 · 评论=31 · engagement_velocity=54
> 作者：hamza_rehman　|　发布：2026-07-30T14:58:59Z
> 项目链接：<https://github.com/hamzarehmandeveloper/claude-account>
> 采集：2026-09-26T10:00:49+08:00　|　id：`a0a6055cc981434a`

## 正文

I use separate Claude Code accounts for work and personal projects. Having to log out and go through the login flow every time I switched accounts became annoying, so I built a small CLI to solve it.The commands are intentionally simple:claude account add myworkaccount
claude account add mypersonalaccount
claude account use myworkaccount
claude account currentAfter switching, Claude Code works normally:claude
claude "fix this bug in main.py"
Repository: https://github.com/hamzarehmandeveloper/claude-accountGive it a try

## 评论（29/31）

> **pandoro** · 2026-07-30T16:12:18.000Z　
> I use this: https://gist.github.com/KMJ-007/0979814968722051620461ab2aa0...Simple and works great but requires one alias per account

---

> **bdemirkir** · 2026-07-30T16:35:47.000Z　
> Or use https://omp.sh and add multiple accounts. omp tracks usage and when limit is reached it uses the next account.

---

> **dotancohen** · 2026-07-30T16:42:57.000Z　
> Does it share the global ~/.claude/CLAUDE.md file? For some use case I'd like that, for others it could be problematic.

---

> **brentmitchell25** · 2026-07-30T16:53:25.000Z　
> Another way for those who use mise. You can auto-switch accounts by directory:~/development/account1/mise.toml:[env]CLAUDE_CONFIG_DIR = "{{ env.HOME }}/.claude-account1"

---

> **acuteaura** · 2026-07-30T17:04:21.000Z　
> revolutionary. you can do this with 2 lines of shell code.i do this: https://github.com/acuteaura/universe/blob/main/overlays/cla...

---

> **carloslfu** · 2026-07-30T17:10:11.000Z　
> appreciate you building this! I have two Claude max accounts. The way I do it is that I have two app launchers (claude desktop). I use the desktop app and a different data directory for each launcher like `open -n -a /Applications/Claude.app --args --user-data-dir="<its profile directory>"`. I got my first Claude to make me two different launchers for the two apps, and it's been working perfectly. wdyt?The only problem I've noticed is with Claude in Chrome. It seems to not work well in the second account. And this makes sense because it was designed just for one app. Do you find yourself having the same problem with this setup? have you tried the second one with the Claude in Chrome ext?

---

> **baron3dl** · 2026-07-30T17:26:12.000Z　
> don't people get banned for doing this kind of thing?

---

> **pwython** · 2026-07-30T17:36:43.000Z　
> I use the Claude Code desktop app for work, and the CLI for personal, so I'm always logged into both accounts!

---

> **swyx** · 2026-07-30T18:24:41.000Z　
> does this also extend to codex?

---

> **hmokiguess** · 2026-07-30T18:44:08.000Z　
> I built the same thing for myself, but I like your implementation so much better.

---

> **hassanmehdi98** · 2026-07-30T21:19:34.000Z　
> Is it even safe to switch accounts frequently? worried about them imposing a ban

---

> **pdimitar** · 2026-07-31T02:47:29.000Z　
> Cool but I would like to reuse my entire account directory and just switch accounts and nothing else. Now I just do `/logout` and then go through the login flow again because I don't want to lose access to all memories and transcripts.Is that supported?

---

> **lukasco** · 2026-07-31T12:01:04.000Z　
> Can you be logged into two accounts at once? It's not the switching, but the different sessions on different accounts that I find myself doing.As some have said, easy enough to build yourself, but I think it' nice not to have to test it and make sure it works.

---

> **kingzabbu** · 2026-08-01T01:52:45.000Z　
> Is this safe to use? as some print from other accounts may leak and will it not harm the accounts?

---

> **mlitwiniuk** · 2026-08-01T11:22:05.000Z　
> And knowing Anthropic being developer friendly we can expect them to ban this in 3... 2...

---

> **orliesaurus** · 2026-07-30T16:17:00.000Z　
> simple and easy - thank you

---

> **cowlby** · 2026-07-30T16:25:42.000Z　
> This is great. My enhancement was to create a .claude-profile file which specifies the account alias. "claude" can be aliased to read the file, set the correct env var, and launch claude.Another benefit was if no .claude-profile file exists, claude refuses to launch.

---

> **AlexErrant** · 2026-07-30T16:45:11.000Z　
> Sadly incompatible with Claude subs.

---

> **kn9** · 2026-08-01T16:36:31.000Z　
> Try https://www.onorca.dev/ too very good

---

> **dpoloncsak** · 2026-07-30T17:30:16.000Z　
> If it's honestly 'One account is paid for by my employer and used as a tool for my job' and 'One account is for personal use, where I work on passion-projects and the likes' I think it's fine....? Not a lawyer but I'd assume as long as you're not using it to bypass usage limits Anthropic wouldn't even really notice or care.

---

> **rew0rk** · 2026-07-30T18:00:29.000Z　
> The threat of account bans and a less than friendly appeal system does make me wary of trying it, even though this would be incredibly useful.

---

> **ttoinou** · 2026-07-30T19:06:08.000Z　
> A lot of them also don’t get banned, right ? There are vibecoders youtubers switching accounts all the timeSo what’s the differenve ?

---

> **hamza_rehman** · 2026-07-31T09:46:11.000Z　
> Not currently
> It is specific to Claude Code right now

---

> **hamza_rehman** · 2026-07-31T09:19:14.000Z　
> No, I kept the whole CLAUDE_CONFIG_DIR isolated because I didn’t want it to directly copying or replacing Claude’s credential files.
> It felt too easy to get wrong

---

> **spk_** · 2026-07-31T13:25:08.000Z　
> Yes, you can, just need to set a separate config dir. I have the below in my zshrc.alias claude-personal='CLAUDE_CONFIG_DIR=~/.claude-personal claude'

---

> **hamza_rehman** · 2026-07-31T15:01:05.000Z　
> Yep, that’s supported. Switching only affects newly started Claude processes, so you can keep work open in one terminal and personal in another using claude account

---

> **bdemirkir** · 2026-07-30T17:37:36.000Z　
> Subs are supported

---

> **baron3dl** · 2026-07-30T17:56:32.000Z　
> not sure law matters, anthropic is draconian about bans/appeals.

---

> **AlexErrant** · 2026-07-30T19:28:14.000Z　
> Doesn't this require pi, which CC famously bans you for using?

## 关联链接

- https://github.com/hamzarehmandeveloper/claude-accountGive

## 导航

- 项目页：[[10-项目/github.com_64a1dcce]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
