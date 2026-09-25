---
type: "corpus"
item_id: "86c5374589006a7e"
title: "Show HN: Clueless: how I made a scalable freeform crossword generator"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49830649"
project_url: "https://clueless.crossword.is/blog/development-history"
author: "informades"
published_at: "2026-09-24T13:55:44Z"
captured_at: "2026-09-24T23:57:22+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-24"
pub_day: "2026-09-24"
tags:
  - 语料
  - hn_show
  - author_informades
  - story_49830649
  - show_hn
metrics: {"points": 2, "comments": 1, "engagement_velocity": 2}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Clueless: how I made a scalable freeform crossword generator

> [!info] 一句话导读
> Clueless Crosswords™ Freeform Crossword Generator

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49830649>
> 指标：点赞=2 · 评论=1 · engagement_velocity=2
> 作者：informades　|　发布：2026-09-24T13:55:44Z
> 项目链接：<https://clueless.crossword.is/blog/development-history>
> 采集：2026-09-24T23:57:22+08:00　|　id：`86c5374589006a7e`

## 正文

Clueless Crosswords™ Freeform Crossword Generator
Free to use ✌️ no registration required!
 But you can support me! Buy me a coffee
 or say hi by mail! 👋 [email protected]
☰ Menu Generator 🛠️
 Solve Puzzles 🧩
 Artwork 🖼️
 About 👋
 Blog 🆕
Clueless: how I built a deterministic scalable freeform crossword generator
 September 24, 2026 · Frido Emans
 tl;dr : I spent 9 months working on a scalable deterministic freeform crossword algorithm able to create dense layouts containing thousands of words. I turned it into an online tool at clueless.crossword.is and made $9 revenue with it.
 Pt. 1 - the problem
 the cause
 2 years ago I wanted to make a crossword puzzle based on around 60 silly question/answer jokes in the style of “What’s green and slides down the slope?” [1] and found that all the online crossword making tools were doing a pretty mediocre job at putting the words together.
 The ones I tried mainly produced a bunch of disconnected word ‘tails’ (chains of words connected each by one intersection with a dangling word at the end) with very little coherence. Also they seemed to rely a lot on luck/randomness.
 Crossword Labs output for a list of 64 composers , single run, default parameters. I believe the runs are randomized so results may vary. every beginning is hard
 Thinking: “it can’t possibly be that hard to do it better” , I started hacking on the problem and came up with several algorithmic strategies, state representations and heuristics, always with the premise that it should be deterministic, to be able to tune the algorithm for best results. But despite promising approaches, I found out - the problem is in fact extremely hard!
 After a few months racking my brain it did not scale well even to modest numbers, so I gave up, clueless whether this was even possible.
 Placing a few dozen words correctly and densely in a grid in crossword style is a Constraint Satisfaction Problem (CSP); each added word needs to intersect other words in matching letters, preferably more than one.
 A word placement chosen in step 5 restricts many options in step 20, so you have to evaluate astronomical amounts of options to find a few decent ones. Moreover, there is massive redundancy among different paths, which is very wasteful because it causes the algorithm to find the same layout many times. Pt. 2 - the solution
 the challenge
 This January someone presented me with a challenge: “here is a list of 18 words, recreate the original crossword layout”. I presented it to ChatGPT which told me: this is impossible. I remembered my project, so I dusted off my code and fed it the words. And it sort of worked; it created something that didn’t look quite like what it should but got close.
 I started thinking again about why I could never get past ~20 words and couldn’t produce good connectivity between the words, when suddenly I had an epiphany which let me tackle both these issues with a single modification.
 killing three birds with one line of code
 The insight was an embarrassingly simple rule: If the last word added had only one intersection, the next word to place must intersect that word. In other words, whenever there is a dangling word, continue daisy-chaining it until it latches on somewhere.
 This was literally one line of code which killed three birds with one stone: first, there could never be more than one tail at a time (with one exception: the first word remains dangling until something circles back to it). Secondly the branching factor collapsed in most steps. And third, many permutations of the ordering of steps leading to the same state are not even considered [2] .
 While this effectively prohibited many valid states, most of these states are heuristically not interesting at all. There are some caveats, details I will discuss in a later publication, but overall this worked extremely well. With this, the algorithm scaled quickly to the 60 words I originally intended and even well beyond, while maintaining a relatively adequate density.
 An interesting side effect was that the quality of the output seemed to improve with the input size; intuitively logical because more words implies more options to connect words, but algorithmically unusual.
 The same 64 composers as in the CrosswordLabs run of Pt. 1, fed to the first version of the Clueless Crossword Algorithm. I had solved the problem of which I hadn’t even been sure if it was solvable; it could actually reproduce some (unclustered, see below) crossword layouts from their word list.
 Pt. 3 - the improved solution
 But I still wasn’t satisfied. The algorithm couldn’t (re)create clustered crosswords yet, the type where intersections appear in clusters, such as found most prominently in American style crosswords, where every letter on the grid is an intersection (see image below). This is due to the fact that to create such a cluster you have to place two or more words simultaneously, or accept that you sometimes break the constraints and find a way to reconcile that again. (N.b., these crosswords are created in a different way, typically by deciding the layout upfront and selecting fitting words from large dictionaries; see Ginsberg et al., 1990 ).
 I spent another month and a half developing another algorithm on top of the first to solve that too, by combining some variations of traditional beam search approaches [2] , which was very challenging and rather complex — I will dedicate another publication to that. But sure enough, large clusters of intersections were created and it could even recreate several traditional/NYT-style crossword layouts from their word list [3] .
New York Times crossword of March 24th, 2019 by Trenton Charlson, edited by Will Shortz and the reproduction of it by the Clueless Crossword Algorithm; source: https://nyxcrossword.com/2019/03/0324-19-ny-times-crossword-24-mar-19-sunday.html off to the deep end
 By then I was neck-deep in generative search theory and computational complexity. Often I stayed up deep into the night, studying, documenting, hacking and pushing its limits. For months, I couldn’t think about anything but crosswords and algorithms.
 Of course I kept pushing the envelope. One night I ran it against a word list of 5000 randomly selected unique words from the ENABLE word list with an average length of about nine letters. It placed 4821 of them in a grid of 205x297 (see header image or here: https://clueless.crossword.is/artwork/treasure_map ), which it filled for 54%, producing 10,301 intersections and featuring enormous clusters – an average of 4.27 intersections per word (because every intersection belongs to two words).
 Ordinary runs of a few hundred words take a few seconds at most, but this had to run all night multithreaded over 8 cores and required over 50GB of memory. I tried with even more, but my laptop said: “Stop, please, I can’t take any more, this is enough!” Many nights I had run it near boiling point for hours on end, and I decided “Ok, you are right, the algorithm works really really well, I am done.”
 Pt. 4 - putting it to good use
 sharing the results
 I still had plenty of ideas for improvements. 3D-puzzles and hexagonal puzzles for starters, but also combining backtracking with the beam search approach to overcome dead ends — right now the algorithm can terminate early if it runs out of options — but I never got around to developing proper recovery from that. Moreover, the algorithm still explodes in time and memory when going into thousands of words, and this continues to haunt me.
 But throughout the process I had experienced many moments of bliss, watching things I didn’t expect to be possible suddenly working so beautifully it made me want to cry - and felt it was enough. I needed to take a break from this and to consolidate what I had achieved.
 I had written hundreds of pages - technical details, (failed) experiments, hypotheses, plans, reports, complexity analyses. I had started condensing this into a technical writeup with the plan to publish this together with the source code. Turns out writing this is a mental challenge of its own. I had hoped to be done with that four months ago but am still working on it and will publish them when I am ready.
 Maybe I or someone else can continue later on this to make the algorithm even more efficient, such that it could consume the entire ENABLE word list and beyond. For now I can safely say I solved the original problem and much more.
 the tool
 Since it worked so well, I decided to make it useful for others and built a free-to-use web app around it.
 As one of the many tests I ran, I generated a crossword with the countries of the world (see https://clueless.crossword.is/artwork/the_world ). This suggested a different type of puzzle, where the title defines the complete set and clues were no longer necessary. (Some people indeed solved it, see https://www.reddit.com/r/crossword/comments/1unldnk/comment/owo4d38/ ).
 This inspired the name “Clueless crosswords”. It also felt fitting because I still felt clueless why I actually had done all of this stuff (N.b. I am not particularly big on crossword solving, occasionally I like to play Scrabble). And the platform didn’t support adding clues to the crosswords (yet). The clues were never the interesting part to me, just the constraint problem.
 Over the summer holidays I expanded functionality of the platform, including a way to add clues and an online puzzle solver, a public listing of puzzles, and I will keep working on it when I feel inspired.
 buy me a coffee ftw
 Finally I added a “buy me a coffee” button on the site and after a reddit post, someone actually bought me three coffees, so after 9 months - not counting the work of 2 years ago - the total revenue of this project was $9. Not bad!
 Please try it out, use it for pleasure or stress-test my claims on clueless.crossword.is [4] . I would love to hear feedback, about what works well but just as much what doesn’t. And if you like it, don’t hesitate to buy me a coffee !
 N.b. I noticed I use the terms "consistency", "connectivity" and "density" rather loosely and synonymously in this article and I might as well say "aesthetically pleasing", but in the technical publication that will follow I will make sure to give proper mathematical definitions for everything.
 Answer: a skiwi ↩
 I will elaborate in the technical writeup all the relevant details. ↩ ↩
 I have not found any examples where this didn’t work, but if you find any counter-examples, I’d be happy to know; I can try it out with more compute/mem to see if that works. The online platform is fairly limited in resources. ↩
 N.b. it runs on modest hardware and there is a single queue. There are no cookies, but there is an anonymous random tenant ID which associates jobs with a browser. The puzzle data is stored unencrypted so don’t upload sensitive information. ↩

## 评论（1/1）

> **informades** · 2026-09-24T13:56:05.000Z　
> Hi HN; Author here of the article;
> I spent 9 months working on a problem I wasn’t sure could be solved at the start; creating a scalable deterministic freeform crossword generating algorithm with sufficient connectivity/density.In January I had a breakthrough that made this possible and also made the algorithm scalable. The insight was a single-line pruning rule that collapses branching factor, tail formation and path redundancy, further described in the article.I wasn’t happy yet, because I couldn’t create clustered crosswords. I spent a long time hacking on that issue and came up with a solution for that, making it possible to exactly recreate NYT-style crossword layouts just from their word list.Pushing this to the limits on my laptop, I managed to squeeze out a nearly 5000-word crossword with over 10k intersections and a grid filling of 54% letters against 46% whitespace, which ran overnight using up all my laptops’ resources.Finally I built a web app around it for anyone to use for free, and I’d love for you to try it out and hear your feedback or answer questions. Remember that the app runs against modest hardware and there is a single queue. You can find it here: https://clueless.crossword.isA formal technical writeup will follow together with the release of the source code, but this takes longer than planned. In the meantime I’d be happy to discuss about the project and the algorithm.Hope you find it interesting!

## 关联链接

- https://clueless.crossword.is/artwork/the_world
- https://clueless.crossword.is/artwork/treasure_map
- https://nyxcrossword.com/2019/03/0324-19-ny-times-crossword-24-mar-19-sunday.html
- https://www.reddit.com/r/crossword/comments/1unldnk/comment/owo4d38/

## 导航

- 项目页：[[10-项目/clueless.crossword.is_410836b2]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
