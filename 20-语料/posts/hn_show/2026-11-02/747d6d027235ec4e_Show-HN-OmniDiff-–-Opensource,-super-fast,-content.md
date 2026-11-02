---
type: "corpus"
item_id: "747d6d027235ec4e"
title: "Show HN: OmniDiff – Opensource, super fast, content aware Git difftool, in Rust"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50325253"
project_url: "https://github.com/ivankovic/omnidiff"
author: "FabCH"
published_at: "2026-11-01T13:02:30Z"
captured_at: "2026-11-02T09:51:51+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-02"
pub_day: "2026-11-01"
tags:
  - 语料
  - hn_show
  - author_FabCH
  - story_50325253
  - show_hn
  - front_page
metrics: {"points": 157, "comments": 41, "engagement_velocity": 157}
comments_count: 38
comments_total: 41
discovered_via: "hn:show_hn:3d"
---

# Show HN: OmniDiff – Opensource, super fast, content aware Git difftool, in Rust

> [!info] 一句话导读
> I have been researching what the ultimate diff tool would look like, based on actual diffs in open source repositories.OmniDiff can diff: code (25 languages), c…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50325253>
> 指标：点赞=157 · 评论=41 · engagement_velocity=157
> 作者：FabCH　|　发布：2026-11-01T13:02:30Z
> 项目链接：<https://github.com/ivankovic/omnidiff>
> 采集：2026-11-02T09:51:51+08:00　|　id：`747d6d027235ec4e`

## 正文

I have been researching what the ultimate diff tool would look like, based on actual diffs in open source repositories.OmniDiff can diff: code (25 languages), config, images, PDFs, archives, cursors, fonts...It's fast. It can diff C++ files of tens of thousands of lines in under 100ms, on a 2023 ThinkPad T14s.It's open source. AGPLv3.It's based on real diffs. I looked at the 7400 repositories that are listed in Gentoo packages, sampled 2000 diffs and solved them manually to get a good understanding of what is needed, before putting together the diff pipelines for each content type. Incidentally, this also forms the basis of the CI pipeline, so the robustness of the codebase is quite high.I'm still developing it. It's v0.3.0 at this time. But I have been using it daily as my git difftool for months now, and it works well.AI Disclosure: Yes, I do use AI. No, I do not vibecode.

## 评论（38/41）

> **paaloeye** · 2026-11-01T13:39:32.000Z　
> How is it better or worse compared to https://github.com/dandavison/delta ?

---

> **paaloeye** · 2026-11-01T14:07:19.000Z　
> Older submission: https://news.ycombinator.com/item?id=49891989

---

> **anilgulecha** · 2026-11-01T15:21:16.000Z　
> You have a good core idea here. You're pretty much killing your project in infancy with the AGPL+donation license model. Meanwhile, some other projects will take the core idea of "language aware differ" and release BSD, and one of those will win, including perhaps making it into git/future version controls.IMO, you should seek to make this a standard that wins, and hopefully other opportunities that come will be where you make commercial hay. My unsolicited 2c.

---

> **cocoto** · 2026-11-01T16:02:42.000Z　
> How does it compare with diffstatic?

---

> **arkenflame** · 2026-11-01T17:55:04.000Z　
> Really well done, I like this a lot. It produces much more minimal diffs than other tools I've tried.One feature I miss from difftastic is showing diffs side-by-side on wide terminals, and unified when narrow.

---

> **nickjj** · 2026-11-01T18:08:58.000Z　
> Delta has a really nice way to show diffs with its diff-so-fancy mode, it's more similar to GitHub's UI where not only the line is colored up differently but there's a different shade of color to highlight the characters.There's a screenshot and video of it here that I wrote a while back: https://nickjanetakis.com/blog/awesome-git-diffs-with-delta-...In OmniDiff's readme and web version I didn't see a way to do that.In a different comment you mentioned OmniDiff is much better than Delta and you mentioned "About a third of diffs are significantly better.". Can you provide some examples of these? I've never seen Delta fail a diff.Also Delta has a package for Arch in its official repos. For folks who just want a "it works" experience, that's a pretty big win. With Delta the same package can be installed in the same way on Debian, Arch and macOS with Brew using standard package managers. With OmniDiff, there's 3 different ways to install it (manual deb package on Debian, manual package compile on Arch and brew install on a Mac). Just something to think about, as someone who has public dotfiles that work in those 3 environments, I'd skip OmniDiff based on this alone.

---

> **bita_nidir** · 2026-11-01T18:50:23.000Z　
> Wow, I've often wished I had a tool like this. Thanks!Since most people do click-and-run most of the time (based on decades long research, n=1), I'll just add paste the link for more examples: https://ivankovic.github.io/omnidiff/showcase/content.html

---

> **davvid** · 2026-11-01T19:55:12.000Z　
> Nicely done OP. Does it do 3-way diffs for merges as well? The instructions only mention the two-way `git difftool` configuration so maybe that'll be a future feature?Any interest in getting the setup upstreamed[1] so that users only need to `git config --global diff.tool omnidiff` to enable it by default? Disclosure: I created `git difftool` a long time ago, and am always happy when builtin support for useful tools are added to it. Feel free to reach out if you'd like help making that happen.[1] https://github.com/git/git/tree/master/mergetools

---

> **smallnix** · 2026-11-01T20:27:54.000Z　
> Very cool! I'd love to see support for figma or Photoshop, perhaps it's already possible via export to an image format, but native would be cool.

---

> **burner-account** · 2026-11-01T20:41:43.000Z　
> I am sorry, I looked through the examples and I am not sure I prefer the output of omnidiff... Seeing how everyone else over here is instead overly enthusiastic makes me feel extremely dumb :D

---

> **andunie** · 2026-11-01T21:12:31.000Z　
> This looks really good. It does look like you put a ton of effort into it, I'll give it a try.I feel like the moved code cases would look great in https://github.com/andunieee/twain, I was looking into how I could slurp your code and make it work there (although for some reason I have the impression that I had already seen this repository in the past, I can't remember where).

---

> **enriquto** · 2026-11-01T22:32:23.000Z　
> cool to see fresh Rust software with copyleft license !I feel safer, as a user, enjoying the freedoms that the AGPL provides me. (No evil middleman will be able to give me non-free versions of this program.)

---

> **gslepak** · 2026-11-01T23:17:09.000Z　
> Is there a way to use it with git without having to change your global git config? I.e. `git diff | omnidiff` or something?You can do this with delta: `git diff | delta --side-by-side`

---

> **FabCH** · 2026-11-01T13:53:03.000Z　
> It’s much much better with moved code.Delta adds color to the standard git diff algorithm.Omnidiff uses a completely different algorithm.About a third of diffs are significantly better.

---

> **FabCH** · 2026-11-01T14:12:28.000Z　
> Not quite.In the meantime, I added support for all other non-code file formats. Hence the name change.It’s quite a big chunk of functionality.

---

> **FabCH** · 2026-11-01T15:39:55.000Z　
> I really do care about copyleft and AGPL. It’s a political choice. I specifically chose it because I know from direct experience that big tech is allergic to it.I actually don’t care about the commercial license. It’s more of an experiment for my own amusement than an actual attempt at building a commercial project.If it inspires someone to build another one and we still end up with a better differ, I’m ok with that world. As long as the open source community has a better differ.Note that there already are at least 3 that I am aware of. But they do perform worse on speed and accuracy.

---

> **IshKebab** · 2026-11-01T17:12:56.000Z　
> > Meanwhile, some other projects will take the core idea of "language aware differ" and release BSD, and one of those will win, including perhaps making it into git/future version controls.Diffsitter and Difftastic have been around for a while, both MIT, so I doubt it.

---

> **FabCH** · 2026-11-01T16:11:36.000Z　
> Comparing is slightly complicated but roughly speaking:Difftastic only diffs code, which is only 2/3 of all diffs.When only measured on stuff difftastic supports:Difftastic is perfect on 64% of diffs and near-perfect on 17% more.Omnidiff is perfect on 90% of diffs and near-perfect on 5% more.Speed isp50 - 35ms difftastic vs 4ms OmniDiff
> p99 - 637ms vs 420msDifftastic wins on license. MIT vs AGPL.

---

> **FabCH** · 2026-11-01T18:03:35.000Z　
> It should… it considers wide to be 200+ columns.You can force it with “v”.I am not super set on that value, if the community has a better default for “wide”, happy to modify it.

---

> **FabCH** · 2026-11-01T18:19:02.000Z　
> OmniDiff is character based by default. It will only highlight the changed characters. I suppose I could add an option to additionally highlight the line as well. Thanks for the feedback!As for packaging. Unfortunately AUR is closed at the moment due to spam. I can add brew commands for Linux, happily.In terms of “better”. It’s actually somewhat complex, but a simple way to think about it is that if you move a function up or down in the same class, text-based diffs paint that as “Deleted here, Inserted there” where ideally you would want it to say “Moved”.

---

> **FabCH** · 2026-11-01T18:58:14.000Z　
> And this: https://ivankovic.github.io/omnidiff/showcase/index.html?cas...

---

> **FabCH** · 2026-11-01T20:14:13.000Z　
> At the moment the algorithm for code diffing is a particularly efficient implementation of APTED which is a tree diffing algorithm that doesn’t natively construct anything useful for a three way diff. I have a notebook with a bunch of failed attempts at a good algorithm for a three way merge, but so far nothing particularly impressive.It’s a long term goal to solve, but it’s the hardest one.I’ll definitely reach out to you to upstream. Thank you for the kind offer!

---

> **FabCH** · 2026-11-01T20:29:54.000Z　
> Depending on how proprietary their formats are, it could be done.

---

> **andunie** · 2026-11-01T23:40:38.000Z　
> I don't know what I did wrong, but using this as a git difftool (following the config) I didn't get any of the cool things from the demos, I got a weird single-column diff output that only showed the new side of the changes, not a diff.

---

> **nh2** · 2026-11-02T01:11:28.000Z　
> Piping the output of `git diff` might withhold information from the tool that it needs for its feature set, while `delta` is just a different way to display any diff output.

---

> **forgotpwd16** · 2026-11-02T01:27:03.000Z　
> https://github.com/ivankovic/omnidiff#usage OmniDiff also works directly with git diff and git log -p, through GIT_EXTERNAL_DIFF. This path needs no difftool config:
>
>  GIT_EXTERNAL_DIFF=omnidiff git diff

---

> **paaloeye** · 2026-11-01T14:04:38.000Z　
> Okay, I'll give it a try then.

---

> **ipsi** · 2026-11-01T15:46:55.000Z　
> FWIW, there's probably no point in using a copyleft licence if AI is involved[1][2], unless you've got pretty solid proof AI only "assisted" rather than doing the bulk of the work. Otherwise, you don't have copyright on the generated code, and without copyright the licence is meaningless, AFAIK.This is not to say you can't or shouldn't use AI, but it's important to understand the tradeoffs you're making.[1] https://www.scotusblog.com/cases/thaler-v-perlmutter/
> [2] https://www.jenner.com/en/news-insights/client-alerts/us-cop...

---

> **shock** · 2026-11-01T19:05:28.000Z　
> I support the choice of AGPL. I wish more software used it.
> Whenever I use AI to write code, in my experience it invariably chooses the MIT license. For example, for all the ansible roles that I've written using AI it put the MIT license in the meta file, unless otherwise prompted. It makes me wonder if it comes from RLHF.

---

> **LVB** · 2026-11-01T17:52:46.000Z　
> > Difftastic wins on license. MIT vs AGPL.I'm a little confused on that, since in other comments you've mentioned that AGPL was a deliberate choice for . So, what's the definitions of "winning" here?

---

> **catlifeonmars** · 2026-11-02T01:14:41.000Z　
> How do you handle degenerate trees? I’m curious what heuristics are used in practice to eg backtrack or whatever. I’m not very well versed in TED but superficially the problem seems to resemble wave function collapse.

---

> **FabCH** · 2026-11-01T15:53:34.000Z　
> I’m not based in the US so SCOTUS doesn’t set meaningful precedent for my IP.That said, even under those rules, I would be comfortable arguing before the court that this code has significant human involvement and easily passes the copyright standard.It’s also why I don’t think someone can just easily create another one and license it under BSD. My code is AI assisted, but all truly important pieces were human made.

---

> **noir_lord** · 2026-11-01T21:28:14.000Z　
> You are assuming OP is in the US.Though AI code copyright is an unknown pretty widely either way, it's too new for the legal system to have caught up with it yet.

---

> **FabCH** · 2026-11-01T18:05:01.000Z　
> It was a tongue-in-cheek joke :)But it was worth pointing out the difference in license, it is one of the ways in which the projects differ.

---

> **folmar** · 2026-11-01T23:37:55.000Z　
> The more permissive MIT is often an advantage if you want to build it into something bigger, which is reasonable for diff tool.Discrete users would arguably win more with integrity of AGPL, but developers have reasons to prefer MIT.

---

> **dspillett** · 2026-11-01T17:26:59.000Z　
> > It’s also why I don’t think someone can just easily create another one and license it under BSD. My code is AI assisted, but all truly important pieces were human made.Get one AI to describe what the code does, and another to implement based on that description. You might even get away with a human doing one of the steps. A variation of the classic “clean room reverse engineering” method that was used by Compaq to reimplement IBM's BIOS and start the clone PC market.Some argue that “it doesn't work like that” but it certainly seems to be what some people are doing and as yet no one has been confident enough that their copyright extends through this mechanism that they've tested the theory in court.Note: I'm not saying it is right, but that it might well be perfectly legal. It is definitely possible, practical even. I'd still release stuff under AGPL/similar for the same reasons stated above, but I'd not operate under any illusion that I'd be safe from someone using that method to copy everything they wanted to.

---

> **FabCH** · 2026-11-01T17:36:19.000Z　
> If an individual went through all this effort just to release it under MIT, I’d honestly be mostly just surprised someone cared so much. I’d probably just send them my own project relicensed under MIT out of pure curiosity.But I am counting on the fact that _companies_ would be too worried about legal uncertainty to try this.

---

> **dspillett** · 2026-11-01T21:11:10.000Z　
> > I am counting on the fact that _companies_ would be too worried about legal uncertainty to try thisOh, my sweet summery child :-)Companies have been doing far more dodgy things, things that look objectively illegal where-as the clean-room reverse engineering thing looks to me (caveat: not a legal expert at all) to be legally defensible, for a long time, definitely pre-AI.Even if a company operating in your jurisdiction, where you as an individual might have a cat in hell's chance of even trying to sort the situation to your preference, might not, you can bet your last  that a company elsewhere will feel more free to do so if they wanted what you have without agreeing to your terms.

## 导航

- 项目页：[[10-项目/github.com_89307f73]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
