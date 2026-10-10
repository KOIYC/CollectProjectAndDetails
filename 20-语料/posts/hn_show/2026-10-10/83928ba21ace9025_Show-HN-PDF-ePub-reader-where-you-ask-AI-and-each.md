---
type: "corpus"
item_id: "83928ba21ace9025"
title: "Show HN: PDF/ePub reader where you ask AI and each answer links to the passage"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50024097"
project_url: "https://marginal-ia.app/en"
author: "folio_j"
published_at: "2026-10-09T17:42:49Z"
captured_at: "2026-10-10T09:53:50+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-10"
pub_day: "2026-10-09"
tags:
  - 语料
  - hn_show
  - author_folio_j
  - story_50024097
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: PDF/ePub reader where you ask AI and each answer links to the passage

> [!info] 一句话导读
> Loading… — marginalia

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50024097>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：folio_j　|　发布：2026-10-09T17:42:49Z
> 项目链接：<https://marginal-ia.app/en>
> 采集：2026-10-10T09:53:50+08:00　|　id：`83928ba21ace9025`

## 正文

Loading… — marginalia
 For medicine For law For programmers For mathematics Library Send us feedback Español
marginalia How it works Text view For your field Questions Library Español Sign in Try it free
AI reader for PDF and EPUB
 Ask your book. The answer takes you to the page.
 Open a PDF or an EPUB in your browser, read it without zooming, even on your phone, and ask what you do not understand. Every answer cites the exact passage and one tap takes you there. The file never uploads anywhere.
 Ask a book
One physics chapter, 6 MB, a few seconds. The first three questions need no account. Got your own book? Open your own PDF or EPUB no account, nothing to install
 PDF and EPUB Phone and desktop English and Spanish Free
University Physics · 13.7 Einstein's Theory of Gravity Original Text view replay
 Book Answer
 Chapter 13 · Gravitation
 13.7 Einstein's Theory of Gravity
 The prediction is that if an object is sufficiently dense, it will collapse in upon itself and be surrounded by an event horizon from which nothing can escape. Karl Schwarzschild was the first person to note this phenomenon in 1916, but at that time, it was considered mostly to be a mathematical curiosity.
The event horizon
 The Schwarzschild radius is also called the event horizon of a black hole. We noted that both space and time are stretched near massive objects, such as black holes.
However, if a neutron star gains additional mass, it would eventually collapse, shrinking beyond the Schwarzschild radius. Once that happens, the entire mass would be pulled, inevitably, to a singularity.
In the diagram, space is stretched to infinity. Time is also stretched to infinity. As objects fall toward the event horizon, we see them approaching ever more slowly, but never reaching the event horizon. As outside observers, we never see objects pass through the event horizon: effectively, time is stretched to a stop.
Ask the book 3 free questions
Pick a question, or type your own Why do we never see anything cross the horizon from outside? What is the Schwarzschild radius?
University Physics, OpenStax · CC BY-NC-SA Answers the app gave on this chapter.
How it works From the book to the answer, and back to the book.
 It is not a chat next to a PDF. It is a reader with the AI in the margin: you read, you ask, you check , all without leaving the page.
Step 1 Open the file
 Open a PDF or an EPUB from your device. It is saved in your browser and never uploaded anywhere. Nothing to install.
 Why does time stretch?
 Step 2 Ask what you do not understand
 About any part of the book or the paragraph you select, in your language. The AI answers with the book's passages in front of it and tells you when something is not in it.
 1 As objects fall toward the event horizon, we see them approaching ever more slowly, but never reaching the horizon . As outside observers, we never see objects pass through it.
 Step 3 Tap the number and check
 Every answer carries its citations. Tap a number and the book jumps to the passage, highlighted. If the AI gets it wrong, you see it right there.
swipe
Text view A PDF that finally reads well on your phone.
 No zooming, no dragging from side to side, no words cut in half. Text view reflows the PDF so the text fits your screen and the font size you choose. The original page is one tap away.
 Two columns, tables and figures where they belong
 Formulas and code blocks preserved
 Light, sepia or dark theme, and the typeface you prefer
 A table of contents even when the PDF has none
Try it: tap “Text view” and watch how the very same page adapts to your screen.
 Original Text view
Size − 16 + Theme a a a
Chapter 4 · Processes
 4.2 Process scheduling
 The scheduler decides which process gets the CPU at every instant. The simplest policy serves in order of arrival, and its flaw is well known: a long process holds the CPU while short ones wait behind it, and the average response time explodes.
Fig. 4.3. Circular queue: the process returns to the back after its quantum. The classic alternative splits time into quanta. Each process gets a slice and goes back to the queue. The cost is the context switch, which is not free: save registers, invalidate the cache, restore the memory map. Measuring that cost precisely requires hardware counters, because the system clock is far too coarse for slices of a few microseconds. A real sched -
 uler combines both ideas with priority queues that age, so no process is left without a turn indefinitely. The core loop fits in a few lines:
 while (!queue_empty(&rq)) {
 task_t *t = dequeue(&rq);
 run_for(t, QUANTUM_US);
 if (t->state == RUNNABLE)
 enqueue(&rq, age(t));
} With aging, a process's effective priority grows with the time it has been waiting, which bounds the maximum latency to a multiple of the quantum.
118
Ask
 Pro Git · 2.2 Recording Changes to the Repository
 Remember that each file in your working directory can be in one of two states: tracked or untracked. Tracked files are files that were in the last snapshot; they can be unmodified, modified, or staged. Untracked files are everything else.
 is "staged" the same as the staging area? Margin note · saves itself
 When you first clone a repository, all of your files will be tracked and unmodified because Git just checked them out and you haven't edited anything.
Highlight and annotate Marginalia: notes in the margin, in the book itself.
 Highlight in four colors, write a note next to it and ask from the highlight : the conversation stays linked to the passage. With an account, progress, highlights, notes and conversations wait for you on your phone.
 Change the font size or the theme and every highlight stays on its sentence.
Privacy Your file never uploads. Ever.
 The file and the index for searching inside it stay in your browser. When you ask, only your question and the passages needed to answer it travel, and the answer comes back with its citations. With an account, the book's text also passes through the server to build the search index, and it is not stored.
 The trade-off: with an account, on another device you will see the book in your library with your notes inside, but you need to open the file there once to keep reading.
Your browser anatomy.pdf stays
 Search index stays
 Highlights and notes stays
question + passages answer + citations the file, never
 Server The AI reads the passages only those
 Answers with citations without storing the book
For your field Made for what you read.
 A two-column paper, a statute, a programming manual or a textbook. Pick your field and try it with a real document like the ones you will open.
Medicine
 A textbook or a two-column paper, readable on your phone. Ask about a clinical picture and the answer takes you to the passage that explains it.
 Tested with PAPPS 2020 and The Lancet See it with a real paper Law and bar exams
 Open the statute or the syllabus and ask about an article: the answer cites the text and takes you to it so you can check.
 Tested with the GDPR and the BOE See it with a real statute Programming
 Specifications, RFCs and technical books with syntax colors. Select a block of code and ask what it does.
 Tested with Pro Git and RFC 9110 See it with Pro Git Math and physics
 Formulas are preserved in text view and, with an account, you can tap one to ask about it.
 Tested with OpenStax and Gutenberg See it with a textbook
 swipe
Questions Before you open your first book.
Do I need to make an account? No. You open the file and read. You can ask three questions without an account; to go on, create a free one with just your email.
 Is it free? Yes, for now. Each account has a daily and monthly question limit, generous for normal use. Any change will be announced here before it takes effect.
 What kinds of files can I open? EPUB and PDF. If the PDF is a scan (a photo of each page), you can view it as it is, but you can't switch it to text view or ask it questions.
 Is my book uploaded to a server? No. The file stays on your device. When you ask, your question and the passages of the book needed to answer it are sent. With an account, the book's text also passes through the server to build the search index, without being stored, and your account keeps your highlights with their quotes and your conversations, never the book itself.
 Do you record what I do on screen? The shape of the session is recorded, without your name: where you tap, which panels you open, how long things take to load. Not the text: the book shows up as a grey block, and your questions, the answers, your notes and the titles are covered. It shows where people get stuck. Turn it off with “Don't record my session” at the foot of the page or in the reader settings, and nothing is recorded if your browser asks not to be tracked.
 Can I keep on reading from my phone? Yes. With an account, your highlights, notes, conversations and the page you were on are waiting on your phone. Open the file there once and pick up where you left off.
 Can the AI get it wrong? Yes, it can make mistakes even with the book in front of it. That is why every answer comes with its citations: tap a number to check the original passage.
 Why does Marginalia exist? It started with a technical book and a phone beside it: a photo of the page, the photo sent to an AI and, from there, a conversation that truly helped. But the book and the conversation lived in separate places, the AI couldn't quote, and coming back meant hunting for the paragraph by hand. In Marginalia they share one screen and every answer takes you back to the page. For now it is free, with no ads and no catalog: you bring the books.
 What happens if I clear my browser data? Only the copy saved in the browser is deleted; your original files are never touched. With an account, you reopen the file and get your highlights, notes and conversations back.
Get started Open a book and ask it what you do not understand.
 Start now, no sign-up. If Marginalia becomes part of your routine, install it as an app and your books wait for you in the library.
 Try the sample chapter
Open my own book
 Three free questions, no account. The file never leaves your browser.
Try it with a chapter Three free questions, no account Try it

## 导航

- 项目页：[[10-项目/marginal-ia.app_3ee0c439]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
