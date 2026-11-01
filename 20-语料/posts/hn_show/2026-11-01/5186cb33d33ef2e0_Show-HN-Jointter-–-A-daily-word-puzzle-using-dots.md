---
type: "corpus"
item_id: "5186cb33d33ef2e0"
title: "Show HN: Jointter – A daily word puzzle using dots and lines"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50317548"
project_url: "https://jointter.com/"
author: "proy87"
published_at: "2026-10-31T16:24:24Z"
captured_at: "2026-11-01T09:38:09+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-01"
pub_day: "2026-10-31"
tags:
  - 语料
  - hn_show
  - author_proy87
  - story_50317548
  - show_hn
metrics: {"points": 12, "comments": 19, "engagement_velocity": 12}
comments_count: 19
comments_total: 19
discovered_via: "hn:show_hn:3d"
---

# Show HN: Jointter – A daily word puzzle using dots and lines

> [!info] 一句话导读
> Hello everyone. I’m a mathematician by training, and I love mathematical and logical puzzles and brain-teasers. Inspired by popular games like Sudoku and Wordle…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50317548>
> 指标：点赞=12 · 评论=19 · engagement_velocity=12
> 作者：proy87　|　发布：2026-10-31T16:24:24Z
> 项目链接：<https://jointter.com/>
> 采集：2026-11-01T09:38:09+08:00　|　id：`5186cb33d33ef2e0`

## 正文

Hello everyone. I’m a mathematician by training, and I love mathematical and logical puzzles and brain-teasers. Inspired by popular games like Sudoku and Wordle, I decided to come up with an engaging game of my own.As it turns out, that’s not so easy! I had a few ideas, but beyond the core mechanics, a game also needs to be interesting and easy to explain — after all, nobody (including me) wants to spend a long time reading through rules.Let’s start with the concept, which came to me quite spontaneously: what if we represented letters like the digits on a digital clock — using lines, with dots at the points where those lines intersect? For instance, the letter "E" would consist of four lines and six dots — three at the intersections and three at the ends of the lines.It turns out that every letter of the Latin alphabet can be represented this way (with a minor caveat) using three rows of dots connected by some lines. This immediately presented a challenge: how do you represent O-shaped parts, like those found in "B", "O", or "R"? I decided not to use O-shapes, an use onl rectangles/squares. This "alphabet" is always displayed below the game board, so the player can see the letters.The goal of the game is simple: you are presented with three rows of dots and a set of lines, and you have to figure out the word. A great feature of the game is that it’s possible to deduce the word in a single turn — all the necessary information is right there on the board, allowing you to arrive at the answer with certainty.
And what if you can’t figure it out on the first try? You can enter a guess, much like in Wordle: if the lines from the entered word are part of the target word, they turn green; if not, they turn red. The same applies to the dots.
As you play, more and more lines gradually appear...Why provide some lines at the start? To uniquely identify a specific word — or a small set of words — from the dictionary. For example, you could select a configuration of lines that corresponds to only one word, like "RADIO", or perhaps to just two possible words, such as "WEIGH" and "WRONG".The rules seem clear, but the mechanics — not so much.
There are dots on the board; when I enter a word, I realize there aren't enough dots. What should I do? Initially, if the target word had 5 letters, I allowed users to enter 4- or 5-letter guesses, but that just confused players. So, I came up with a different solution: adding red dots for dots that aren't part of the target word.Another drawback is that the game is somewhat skewed. Since letters are processed from left to right, the first letters are revealed more frequently than the last ones.Then there’s the game design itself: should the target words be 5 letters long, or 6? Should a single board allow for multiple possible answers (like "WEIGH" and "WRONG"), or should it be limited to one — or perhaps more than two? Should the difficulty increase from Monday to Sunday? Currently, it’s set up this way: Monday is the easiest (a few 3-letter words), while Sunday is the hardest (more than two 7-letter words).The tech stack is simple: I use Flask for the backend and Python for the algorithms; I wrote the algorithms myself. While the JS, HTML, and CSS were created with the help of AI.I’d love for you to test the game and share what you like, what you don’t, and what could be improved.Specifically, I’d like to know:1. Is the game and its goal clear?2. Is it fun to play, and what could be improved?3. Would you share it with your friends?I welcome any constructive criticism.You can find the game at https://www.jointter.com/It’s free and requires no registration.Thank you very much.

## 评论（19/19）

> **yboris** · 2026-10-31T17:31:43.000Z　
> I would love a reset button so as to return to the state I found the puzzle in when I just loaded the page.

---

> **dofm** · 2026-10-31T17:49:35.000Z　
> Top tip: make your instructions actually readable.Your LLM has used text with too low contrast, the absolutely pointless and annoying webkit-smoothing: anti-aliased, with text that is too small, cramped and squeezed into place.People with eyes that are getting over forty years old will start to find this difficult to read.You might want to consider making important instructions stand out, left-align the text, etc.And then consider writing them with clarity and simplicity yourself rather than letting the LLM write them. The instructions are crucial. You should own that.

---

> **pmx** · 2026-10-31T18:15:13.000Z　
> Tooltips keep spamming me covering up the actual game area. Spend more timing dismissing those than figuring it out

---

> **grandfunction** · 2026-10-31T18:25:16.000Z　
> I want to filter by dots on the sides. My brain and I are struggling!

---

> **unsnap_biceps** · 2026-10-31T18:26:54.000Z　
> I found it really hard to understand how this worked at first. I feel that having a tutorial would be extremely useful, show a board, describe the problem, show picking a letter, undoing it, picking the right letter, etc.

---

> **smitty1e** · 2026-10-31T19:55:15.000Z　
> I backed down to a three letter one and found some joy.

---

> **proy87** · 2026-10-31T20:01:02.000Z　
> The most simple games are on Monday, for example, https://www.jointter.com/2026-10-26/

---

> **proy87** · 2026-10-31T17:54:52.000Z　
> Hello.The button is added.

---

> **proy87** · 2026-10-31T17:55:35.000Z　
> Thank you very much.I appreciate your feedback.

---

> **proy87** · 2026-10-31T18:08:42.000Z　
> Updated.
> Waiting for feedback.

---

> **proy87** · 2026-10-31T18:51:59.000Z　
> Thank you. They are removed.

---

> **proy87** · 2026-10-31T18:44:14.000Z　
> Sorry, I didn't understand.Do you need another filter?

---

> **tetraodonpuffer** · 2026-10-31T19:08:44.000Z　
> +1 on this one, there should be a tutorial with maybe a shorter word to explain how it works, this said I don't think I am smart enough for this one :D if the dots were fixed and you just had to reason on the connections, maybe, but being able to move dots left/right makes it a bit too hard at least for me. This could also be a "expert mode" thing too, have the basic mode with the dots where they are supposed to be, then expert mode making them movable

---

> **proy87** · 2026-10-31T19:15:38.000Z　
> I've made a video tutorial.
> Check it out.

---

> **proy87** · 2026-10-31T19:58:42.000Z　
> Do you find 4+ letter words hard to find?

---

> **grandfunction** · 2026-10-31T23:38:03.000Z　
> Yes. Left side of letters.A=2
> B=3
> C=2
> P=3Right side too I guess.I am finding it quite difficult and this might help.Also a button that automatically gives the answer would make it easier.

---

> **proy87** · 2026-10-31T19:15:57.000Z　
> Possibly, a video tutorial would be better?
> Check it out.

---

> **proy87** · 2026-10-31T19:38:26.000Z　
> I think that if the dots are on their places, you can "read" the word immediately.

---

> **smitty1e** · 2026-10-31T22:39:06.000Z　
> I would need to spend some more time on this to get my mind around it.My Wordle pimp hand is strong, but this seems an order of magnitude harder.

## 关联链接

- https://www.jointter.com/It’s

## 导航

- 项目页：[[10-项目/jointter.com_bb836090]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
