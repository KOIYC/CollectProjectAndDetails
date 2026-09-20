---
type: "corpus"
item_id: "6067e51f15aeacd2"
title: "How to Write with an LLM"
source: "hn_front"
source_name: "HN 首页（非 Show HN）"
url: "https://news.ycombinator.com/item?id=49747070"
project_url: "https://sockpuppet.org/blog/2026/09/17/how-to-write-with-an-llm"
author: "joeriddles"
published_at: "2026-09-17T21:48:38Z"
captured_at: "2026-09-20T03:32:45+08:00"
lang: "en"
kind: "post"
tags:
  - 语料
  - hn_front
  - author_joeriddles
  - story_49747070
  - front_page
metrics: {"points": 587, "comments": 367, "engagement_velocity": 587}
comments_count: 364
comments_total: 364
discovered_via: "hn:front_page:2d"
archived: true
archived_at: "2026-09-20T09:21:32+08:00"
archive_reason: "渠道停用"
---

# How to Write with an LLM

- **来源**：HN 首页（非 Show HN）　|　**kind**：post
- **原帖**：https://news.ycombinator.com/item?id=49747070
- **指标**：点赞=587 · 评论=367 · engagement_velocity=587
- **作者**：joeriddles　|　**发布**：2026-09-17T21:48:38Z
- **项目链接**：https://sockpuppet.org/blog/2026/09/17/how-to-write-with-an-llm
- **采集**：2026-09-20T03:32:45+08:00　|　**id**：`6067e51f15aeacd2`

## 正文

Published: 2026-09-17
Author: A Final Ward

How To Write With An LLM — A Final Ward

# How To Write With An LLM

17 September 2026

Two simple rules that let LLMs streamline and improve your writing without pasteurizing and jacking it with corn syrup.

It’s tricky to write about writing. It comes across as a brag; you’re implying that you write well. Maybe you do, and maybe you don’t, but there’s for damned sure a quorum of critics on the Internet somewhere that think you suck at it. I’m vain and insecure like everybody else and find writing this piece weirdly unpleasant. But I’m getting over myself and getting this down because this advice is important, hard to argue with, and straightforward.

Readers can detect LLM words in the parts per trillion. However much work you put into scuffing up and humanizing it, an LLM paragraph will register to much of your audience not as writing but as output. So, first the bad news: you have to write for yourself.

But LLMs are still extraordinarily useful. It’s just you need to use them like a copyeditor rather than a ghostwriter. So, step one of my method: write your piece. Then, step two: feed it to a good model to find flaws.

But before we talk about how that works, there are two rules you need to understand. They’ll ward off LLM-creep that will knock you into the uncanny valley between expression and output and knock you out of your reader’s attention.

Rule Number One: You may not use a single word an LLM suggests to you.

Breaking this rule is what’s going to get you into trouble. Reason being: frontier models are supernaturally good at selecting pleasing turns of phrase. It’s sort of their whole thing. The problems with what models suggest are subtle. Think of it this way: frontier models are wedged in a mode where everything they write is a magazine headline. Headlines are good, but you’d wonder about someone who wrote an article with dozens of them.

So I think that as a form of intellectual personal protective equipment you should adopt the rule that any specific turn of phrase an LLM suggests is off limits. Be strict about the rule! The whole premise here is that you’re not going to reliably spot all the ways frontier models will try to turn your writing into Velveeta. Even if you like the words, even if you’re sure they’re better than what you already have, LLM-generated phrases are DQ’d.

Rule Number Two: Avoid encouragement

LLMs also infect your writing through influence campaigns. This is a much subtler problem, and the damage is less obvious, but it’s still a way in which LLMs will make your writing worse, and if that’s going to be the outcome, you might as well not enlist LLMs at all.

The issue: hand any piece of writing off to an LLM, and it replies “ that’s gold, Jerry!” But that’s not what you need to hear!

In your first draft, most of your paragraphs are bad, your topic flow is incoherent, and you’ve got at least 750 words you don’t need. The model encourages you about your overall structure. Then, later, about paragraphs and transitions. Then word choices and metaphors. Pop culture references. They’re bad! All bad! Don’t listen!

Here’s how this is going to fuck you. You’re going to double down on all your first-draft impulses. But that’s not normally what you’d do. You’d edit, rethink, and replace paragraphs. Those rethinks are load-bearing parts of your voice. Readers won’t put their fingers on what’s wrong, but they’ll sense that you’ve become artificially-flavored.

For a couple years I opened every copyediting prompt with the lie that I am not the author, but instead the editor of an online publication, screening pieces for inclusion. This helps, but the model usually overshoots, overfitting to the “goals” of my “publication”.

So for now, my best practical advice is: forbid the model from encouragement, and then be hypervigilant about praise.

So, What Can These Things Do?

They’re excellent at flagging problems. Boy, do you have a lot of them. You can spot them mechanically, but that’s tedious and exhausting work. The models don’t get tired. So they’re better than you at noticing:

- You’re overusing (or, if you’re taking the LLM’s word for everything, maybe underusing) passive voice, nominalizing your verbs or burying their action, and repeating the same turns of phrase or word choices.
- You’ve got “very” and “unfortunately” and “really” and “actually” sprinkled all over the draft like sawdust stuck to the work bench.
- There are almost certainly 2-3 paragraphs that you can quickly move somewhere else in the piece that instantly improve clarity (these are really, actually, very satisfying edits).

If you’re a programmer like me, you wish there was a book that provided a schematic for these kinds of edits, a sort of “ C Interfaces And Implementations” that does for prose what Hanson does for the greatest terrible programming language. And: there is that book. It’s called “ Style: Lessons In Clarity And Grace”, and I swear to Christ it turns copyediting into Java coding. Exactly the same tedium, exactly the same effectiveness. I found out about this book from Richard Gabriel and I’m surprised every programmer I know doesn’t have a copy on their desk.

So read “Style”, or something like it, and take notes as you go. Come up with a list of prompts for a model, and then run them in passes over your work.

You can get pretty far with this approach:

1. Ask the model to spot problems in your writing.
2. For each problem, rewrite the paragraph (or sentence, or section).
3. Present the original and new writing to the model and ask it which is better.

Annoyingly, here you run into a variant of Rule Two, because unless you’re careful, the model knows you just rewrote something, and knows you want to hear that the new version is better. So give the options to a model that doesn’t have the context of your editing process.

I conjured a bit of software to manage this for me, after I finally lost patience juggling tabs and trying to persuade the models that I’m not an author but rather a helpful but stern writing coach trying to help a student who might be good but might be terrible. Here’s an opening prompt that worked well:

“We’re going to build a writing workshopping tool. First get the bones up. Python, HTMX for interactions, SQLite backend, Tailwind frontend, use a local build not the CDN. Really excellent prose editor, Notion-style. Support highlighting (we’re going to do editing passes). Do Genius-style sidebar commentary to match highlighted things. Make sure we can tick forward and back through suggestions. Multiple documents, track revisions, allow user to flag major revisions. Get me this far and then I’ll tell you what I really want.”

Then, give the thing the list of editing prompts you came up with, and have it run each through the Codex, Claude, or Antigravity CLIs. Whatever you come up with here, it’ll be better than mine, because whatever anybody comes up with on their own is better, for themselves, than someone else’s.

So: don’t let an LLM pick your words. Be careful not to let it trick you into thinking your first draft is better than it is. Then outsource all the most tedious work to the model. Your voice stays intact, but your work is faster, better, and less painful.

One last thing. Don’t take all of the model’s copyediting advice. This is a corrolary of Rule Two. I fed this piece to GPT5 a minute ago (“I didn’t write this”), and it said the whole thing was 20% too long. It’s probably right. But I’m not fixing it. I’m just gonna be me.

## 评论（364/364）

**jamiejquinn** · 2026-09-17T22:41:09.000Z：

"Those rethinks are load-bearing parts of your voice."Loved the (possibly not deliberately ironic) use of the LLM'S favourite analogy, load-bearing.Nice wee article though. I particularly agree with "Don’t take all of the model’s copyediting advice." I've been using LLMs to review teaching material and often it just doesn't get the point of teaching. It's good for prompting reflection on your writing but it's still an idiot savant.

**abc3354** · 2026-09-17T22:46:24.000Z：

This article was so much better than what I though it would beDoes anyone know about "Style: Lessons in Clarity and Grace" ? Seems like an interesting book

**S-E-P** · 2026-09-17T22:50:25.000Z：

I fear in the future people will read even less because of how often people cheap out and use AI to write.
I know the author of this article tells you never to use a single word it suggests, however I still, while reading, am checking for any amount of AI used.
This makes reading less enjoyable, and even a bit stressful.If you can't spend the time to write it, why should anyone read it?Everything I post is from my own finger tips, only to get a reply from someone using a bot. I'm tired.

**awithrow** · 2026-09-17T23:01:08.000Z：

I've seen this in action as well. The biggest value by far is seeing the overused phrases and tics in your writing style. The prompt I like is to tell it to highlight and flag passive voice and run ons since those are my major pain points. I can also tell when its getting out of "real" advice since it'll offer the same "trim 10-15%". Also important to tell it to highlight specifics otherwise it'll give vague editorial advice that isn't anchored. Another fun exercise is to submit other authors writing as well. Say a short story from a magazine. Some of the edits are legit, but do it enough times and you'll start to see the same generic writing advice gets applies to just about any input.another iteresting thing models can do is to highlight and notice themes and motifs in a piece. I find that helpful when thinking about a piece of work. Might be obvious ones, sometimes it can be subtle themes. Good for stirring your own brain.

**sixtyj** · 2026-09-17T23:03:05.000Z：

> use them like a copyeditor rather than a ghostwriterThis is what you need to know. Seriously, after 25 years in news (writing), you realize that you need “second eyes”, not the first hands.

**trane_project** · 2026-09-17T23:10:12.000Z：

This is similar to how I've come to use them but it's focused too much on the mechanics or writing. I've found them more valuable at role-playing as a specific profile of reader and asking it how they would receive the arguments advanced by the writing and what counterarguments they could present. After some rounds of this process, you either close all the gaps in the argument or realize it's not a strong one.

**SupremumLimit** · 2026-09-17T23:12:56.000Z：

It's darkly amusing that while the author advises us not to let LLMs pick our words, their post includes this chunk of AI slop:"Those rethinks are load-bearing parts of your voice. Readers won’t put their fingers on what’s wrong, but they’ll sense that you’ve become artificially-flavored."The metaphor at the start is AI-like weirdness too: "without pasteurizing and jacking it with corn syrup." Pasteurising is good, corn syrup is bad - what the heck am I supposed to make of it? It's nonsense.It may even have been handwritten by the author, but it's slop nonetheless.You may be telling yourself that you're disciplined and you're just using the LLMs for review. But while you're reading their output, the slop makes its way directly into your brain anyway - and then it drips out into your writing.

**avazhi** · 2026-09-17T23:18:08.000Z：

> How to Write with an LLMTLDR: Don’t.

**thombles** · 2026-09-17T23:30:52.000Z：

Even if you don't want style advice from an LLM (I generally don't, not for blogging), for a technical blogger "please check this post for factual accuracy" is a good way to not look like an idiot. Often it complains about hyperbole, which I tend to ignore since there's no point blogging unless you have some firm opinions, but on at least one occasion it pointed me towards some documentation that undermined my entire post - and led to a much better one a week later once I'd processed and applied that new information. Thanks, LLM.

**felipeerias** · 2026-09-17T23:42:02.000Z：

For commit messages and other technical writing, I use a "narrative coherence" checklist to help ensure that a change is clear and understandable:- Establish a single thesis an external reviewer could recover from the diff.- Unify vocabulary across code, comments, tests, and commit message.- Use the same vocabulary consistently to refer to the same concepts.- Keep every hunk that serves the thesis; consider the removal or deferral of the rest.- Introduce abstractions at the point of need.- Align tests to narrate the same story as the implementation.- Reconcile the commit message and the diff.- Order changes expositorily, not chronologically.- Explain what the change does and why. Do not explain the details of the development process.- Prefer to edit subtractively.- Recompile and run all relevant tests after edits.- Iterate.

**felipeerias** · 2026-09-17T23:49:05.000Z：

If English is your second language and you intent to write in your mother tongue, my advice is to use English to communicate with the LLM.This makes Rule 1 straightforward ("You may not use a single word an LLM suggests to you") and helps avoid the horrible feeling that the machine is taking over your personal voice.

**xianshou** · 2026-09-18T00:04:35.000Z：

Ironically, "load-bearing" appears in the main text of the article that says never to use a single word the LLM suggests. Womp womp.

**le-mark** · 2026-09-18T00:05:18.000Z：

I’ve used llms in two ways while writing fiction. First I’ll have a story idea and use the llm to explore what has come before that may be related; then I’ll go read some stuff. This has worked great for seeing where my ideas fit and flushing them out. Second I’ll describe settings or plot devices and use the llm to brainstorm consequences or further ideas. This fails miserably. The llms suggestions are devoid of creativity. This is all moot though because I’m really not a writer, I’ve just always thought I might like to be one someday.

**Retr0id** · 2026-09-18T00:08:21.000Z：

> Present the original and new writing to the model and ask it which is better.LLMs have absolutely terrible taste when it comes to writing. I don't find their feedback useful at all, beyond trivial spelling/grammar mistakes, which you don't really need an LLM for in the first place.Proofreading is all you need.Edit: I do sometimes ask an LLM for a fact-check, though.

**8bitsrule** · 2026-09-18T01:26:55.000Z：

At one point in my graduate college studies, I tutored qualified (DEI) undergrads 'for free' (for them) as part of a work-study program which paid me a bit for that work.OTOH, an AI could not have qualified as such a student. But even if it did, before we began I would certainly bargain for considerably more than work-study tutoring paid.

**RajT88** · 2026-09-18T05:02:36.000Z：

Indeed. I have been experimenting with using frontier models for creative writing.Using adversarial models to evolve ideas. I have a whole novel of material, and the feedback has indeed been useful. But the actual novel? Not even AI models like their own writing once you give the simple prompt of "account for model sycophancy".The resulting structure and plot beats are good with AI as copy editor. Only the least discerning reader might not care or notice the actual non-human writing. And hey - maybe those are your readers. Probably not.Can we all appreciate for a moment the sci-fi dystopia which snuck up on us all? I just used to phrase: " non-human writing". 50 years ago, that would send a chill up your spine.

**Yashjain413** · 2026-09-18T05:29:17.000Z：

Till today, I was doing the complete opposite of what the article suggests. Definitely going to try this approach out, pretty helpful.I have a specific ChatGPT chat that rewrites my posts really well every time; I usually just give it a rough draft and let it clean things up. But it was pretty interesting to realize how good these LLMs are at actually finding mistakes rather than just rewriting things. The point about not letting the model influence your voice was also very, very relevant.

**fnoef** · 2026-09-18T05:47:37.000Z：

How to write with an LLM?Don’t

**brlewis** · 2026-09-18T06:25:04.000Z：

I agree with the central thesis, but disagree with some details. I wrote a blog response: https://writing.brlewis.com/posts/2026/llm-copyeditor/

**liqiug** · 2026-09-18T06:26:12.000Z：

I mostly use LLMs for coding, so this is an interesting use case. I’m curious how long an article it can handle in practice before the context starts becoming an issue.

**d4rkp4ttern** · 2026-09-18T06:27:31.000Z：

The frontier live voice models (especially GPT Voice/Live or whatever they call it this week) do not have the typical AI-tells. So I wonder about a few things:Why is this?Why couldn’t whatever went into post-training these voice models be applied to the text-gen models to get rid of AI smells?Could we set up a pipeline that leverages the voice models to clean up text that reeks of AI ?

**thunfischtoast** · 2026-09-18T06:42:33.000Z：

I think it's good advice. I find it a bit funny the author said to not use a single word coming out of the LLM, but they probably did just that because I never heard a human being say "load-bearing" before but now it's all over the place, also used here. Or I don't get the irony.

**pmg101** · 2026-09-18T06:58:57.000Z：

It's extremely refreshing reading good human prose isn't it! It's like when I would read a newly-written Paul Graham essay 20 years ago.He also uses rule of three and the phrase "load-bearing", just for fun, which elicited a wry smile from me.Thanks OP for a pleasant start to my day!

**tripvexa** · 2026-09-18T08:03:24.000Z：

But why would you want to write with the help of an llm, you should be moving in the other direction. Don't let the creativity die!

**jjhfarmer** · 2026-09-18T08:22:13.000Z：

Writing is thinking. You are outsourcing the process of thinking through your thoughts so you can communicate and understand them.

**vidarh** · 2026-09-18T08:55:25.000Z：

> Those rethinks are load-bearing parts of your voice.I really hope this was intentional.

**mrieck** · 2026-09-18T09:04:41.000Z：

Thought I'd get an article with tricks how to stop an LLM from sounding like the most obnoxious Linkedin influencer. Instead it says to use it as a copyeditor.Ok - but that's not very useful.

**delis-thumbs-7e** · 2026-09-18T09:53:49.000Z：

I think style is overrated. Yeah if you write commercially, you are a journalist or a copywriter, sure, you need to write in certain style. There’s rules to this shit. I think it was Hemingway who said that. Then again, the good ones break the rules.Today even if you don’t use LLM’s following certain formal style you end up sounding like ad copy or wannabe Atlantic -hack. The. You might read some kid on Tumblr writing beautiful prose with typos and errors and all.First of all you should have something to say. I write a blog just to make tutorials for myself on stuff I need to regularly check out. I don’t really care if anyone reads it. I don’t use LLM to make the posts since, well, pride, but also because I learn better when I need to write the stuff down and check my facts several times. I don’t much care if I make a typo or grammar error here and there. If I want to write it as Jeeves from Wodehouse book, fuck it, I will.If you have a story you have something to write about. It doesn’t have to be fiction, it can be a story on how multicast works. And it needs to be your story. Then the words come by themselves and writing is relatively easy. To have a story you have to live and think. LLM’s don’t help in that.

**nirava** · 2026-09-18T10:23:51.000Z：

I've found the only good way to write with LLMs is to absolutely not use it for the first few drafts, the using it as a tool to list specific kinds of problems in text (word repetition, unnatural hard to read sentences etc) and approaching those points with caution and skepticism. Even copy pasting a single sentence, I've found, is a slippery slope.

**ACV001** · 2026-09-18T10:45:47.000Z：

just don't use it for writing

**arcwhite** · 2026-09-18T10:54:13.000Z：

Simply do not.

**AyanamiKaine** · 2026-09-18T11:13:40.000Z：

If you write with an LLM it will taint you voice. Slowly but surely.

**ramblurr** · 2026-09-18T11:30:48.000Z：

>So give the options to a model that doesn’t have the context of your editing process.> I conjured a bit of software to manage this for me[...]I don't understand how the annotation application shown helps with the stated goal of preventing the model from praising you. What's the actual software assisted workflow?

**pama** · 2026-09-18T11:41:52.000Z：

How I write with an LLM: for each page “suggest up to 10 word changes to increase clarity.”

**Eddy_Viscosity2** · 2026-09-18T12:04:14.000Z：

"LLM paragraph will register to much of your audience not as writing but as output"The best advice for writing for other humans is: don't use LLMs.If you're writing for machines, liking coding, then fine go for it. If you're writing for processes with formal highly structured content like manuals, specifications, form content, procedures, information, that sort of thing, then also ok to use LLMS. But if you're writing for a human mind to ingest and extract meaning from, then LLMs are poison.

**weezing** · 2026-09-18T12:14:34.000Z：

I would have to be an utter moron to use LLM to write anything directed at other people.

**Luucas40** · 2026-09-18T12:18:46.000Z：

Not letting your llm write is good advice and letting him spot problems also is if you want good writing.For anything beyond "good", we're still on our own and I love that for us.

**semiquaver** · 2026-09-18T12:48:58.000Z：

This would sound insane to me from two years ago but I have recently started insisting on writing all my own commit messages and pull request descriptions. I do usually have an agent review them for factual accuracy, but not rephrase them.It slows things down a bit, but in the best possible way. It has helped immensely to improve the depth of my understanding of the agent-generated code. When agents are doing everything its way too easy to “skim” diffs and not really absorb them.I always prided myself on my technical writing, and commit messages and PRs were a great place to hone that skill. I found that I missed it and my work is better now I’ve reclaimed that part of my old job back.

**mjmvisser** · 2026-09-18T12:58:48.000Z：

“Rule Number One: You may not use a single word an LLM suggests to you.”So far so good…“Those rethinks are load-bearing parts of your voice.”Oops.

**VCFundedGenYer** · 2026-09-18T13:39:27.000Z：

This article should just be one word:Don't.

**virgilp** · 2026-09-18T13:40:04.000Z：

> Readers can detect LLM words in the parts per trillion. However much work you put into scuffing up and humanizing it, an LLM paragraph will register to much of your audience not as writing but as output. So, first the bad news: you have to write for yourself.---and then> Those rethinks are load-bearing parts of your voice. Readers won’t put their fingers on what’s wrong, but they’ll sense that you’ve become artificially-flavored.---Are they wrong in the first paragraph? Or are they simply not following the advice they dispense to others?

**globular-toast** · 2026-09-18T14:16:28.000Z：

Why are people not learning to write at school? In most developed countries don't we spend like a whole decade or more learning to do stuff like writing? Yet people still feel like they can't write?Writing is something we really, really need to learn from other people, because it's with people we are trying to communicate. There should be no need for "writing with an LLM". None at all. If what you are writing is important, ask a friend to proof read it. If you can't write, learn.

**4lx87** · 2026-09-18T15:16:02.000Z：

It's more effective in my experience to have an LLM emulate your own writing examples than to apply lists of rules in the hope it sounds human.

**ashton314** · 2026-09-18T16:06:41.000Z：

Step one: open up the LLMStep two: close the LLMStep three: pick up a pen and writeWriting with LLMs is a great way to make yourself stupid: https://lambdaland.org/posts/2026-08-07-ai-writing-stupid/I'm glad the OP acknowledges that you have to have to do the writing yourself—though they say this more as a means to avoid getting pegged as having used an LLM, whereas I see the problem as being cognitive surrender.

**Semiapies** · 2026-09-18T16:50:26.000Z：

LLMs seem overpowered for the use the author suggests, finding and marking problems in prose. Actual human-written programs exist for that purpose, things you don't have to bludgeon into not praising you or semantically ablating your work. Start with langtool or the like and start adding others. Even art-bollocks mode for Emacs can be useful.

**in_absentia** · 2026-09-18T16:54:58.000Z：

I sort of agree, but I also think the advice here is circular. To look at the style suggestions produced by an LLM and decide that you agree with some of them in spirit, but want to put it in your own words, you already need how to know how to write well.In other words, you need to read a style manual or two, and you need to read and have opinions about other people's work. You must have taste. Otherwise, you can't really distinguish between good and bad advice. You'll anchor to the suggestions made by the LLM and it will turn your writing into LLMese. I guess that works - it sure gets clicks on HN - but it won't be your voice anymore.There's still value in getting a second pair of eyes on what you write. But here's another cool trick that gives you a similar benefit: just let it stew. Go for a walk, grab a lunch. Re-read what you wrote. You'll be surprised.

**mcv** · 2026-09-18T17:06:44.000Z：

Sounds like solid advice. Those typical Claude turns of phrase are really grating on me. And I now see them everywhere. Many YouTube channels that are presented by a real human, still sound fake because their script is blatantly written by AI. I hate it.And yet, I'm stuck having to write an important message to someone that has real stakes riding on it, so I use Claude to refine it, and I see myself succumbing to Claude's pressure to use its words instead of my own. I hate it, but my words aren't very good.And finally Claude proclaims the message perfect and I let my wife take a look at it, and she rejects the entire thing, restoring some semblance of sanity again.

**seanmcdirmid** · 2026-09-18T17:14:55.000Z：

I use LLMs for nailing down the narrative in bullet point form. It proposes a lot of inappropriate points that I tell it to remove, but makes some useful proposals as well. It’s actually fairly efficient for narrative exploration, I then keep it away from prose for as long as possible since whatever it writes is pretty bad but once I start editing, it will usually clobber my edits if I make any narrative changes. Humans are still better at actual prose writing, especially when it comes to word rhythm.

**r0ze-at-hn** · 2026-09-18T17:59:27.000Z：

The advice of "use your voice" only works if you have a good writing voice and comes off like Henry Cavill's dating advice or famous writers who said that you shouldn't use a thesaurus.Paying close attention to posts written by folks who are not using LLM's the comments here regularly complain (sometimes extensively) about the writing quality. Doesn't matter what people are saying or suggesting about avoiding LLM writing, the real lesson I am seeing is either to naturally be gifted at writing or somehow figure out how to have LLM's help with your writing. "Rule Number One: You may not use a single word an LLM suggests to you." isn't helpful for probably the majority.

**bzmrgonz** · 2026-09-18T18:10:09.000Z：

This is very good advice. I hate when llms turn into yes-men. I am surprise that the author doesn't use ai to construct the skeleton of the written piece. In my opinion, they excel at this, with all the books they've guillotined and digested, our biological brain cannot match their content retention. I would do the old trick of "asking for a friend". In this case, a friend of mine has mental block and he needs to write a paper on (insert topic here). I want to help him by designing the skeleton, and give the conditions/parameters of your piece.

**apparent** · 2026-09-18T18:56:49.000Z：

I worry that reading too much LLM output will make me tend to write more like an LLM. Seems like it would be inevitable, to some extent. (Here's why it works)

**threetonesun** · 2026-09-18T19:40:38.000Z：

iA Writer's "Style check" feature can do 90% of this in real time.

**dyauspitr** · 2026-09-18T21:02:13.000Z：

Just like you do everything else with an LLM. You ask it for something, if that doesn’t work you just ask it in natural language to change it until it outputs exactly what you want.

**blinkbat** · 2026-09-18T21:44:58.000Z：

Don't. There, easier

**devin** · 2026-09-18T22:18:06.000Z：

Read Ong's "Writing is a Technology that Restructures Human Thought".Emitting words is not really what "writing" is.https://twinada.wordpress.com/wp-content/uploads/2012/09/708...

**brunoarine** · 2026-09-18T23:39:07.000Z：

> Readers can detect LLM words in the parts per trillion.Oh, we do. We can also detect hackeneyed, LLM-made sentences where just one word had been replaced. "That's where it's going to f*** you".

**nicebyte** · 2026-09-18T23:44:51.000Z：

> How To Write With An LLMSimply don't.

**mcapodici** · 2026-09-19T00:28:43.000Z：

For blogging I just don't use an LLM at all. I just use a spelling/grammar checker. I get to sound like me even if that is imperfect.For docs I have used an LLM for the convenience of having them kept up to date.

**asveikau** · 2026-09-19T00:31:05.000Z：

> Your voice stays intact, but your work is faster, better, and less painful.This sentence specifically seems like an LLM. It's hard to quantify that. They just take that sort of tone when they're needlessly summarizing what they already told you. "This thing contrastive thing remains important, but we got XYZ benefit."

**striker44** · 2026-09-19T02:06:28.000Z：

“Here’s how this is going to fuck you“ - this article was either written by a human, or the most aggressively tuned llm.

**politician** · 2026-09-19T02:40:30.000Z：

I was seriously reading this article right up until the word "load-bearing", and then despite my best efforts, my brain just sort of disconnected from the piece. I just skimmed to the end quickly before realizing what happened.

**crossroadsguy** · 2026-09-19T03:07:56.000Z：

> frontier models are supernaturally good at selecting pleasing turns of phraseIt's not even the suggestions in isolation, but it tries to convince you that your writing is stellar and then slips in a word or two, and you accept it because otherwise you'd be skipping greatness. I guess in some way one has to have a bit of hubris about one's writing to tell the model to f off.And OP, assuming this, from your prompt, is your language:> "… First get the bones up…"Congratulations, you are now doing LLM-speak :-)

**drdaeman** · 2026-09-19T04:41:35.000Z：

> Rule Number One: You may not use a single word an LLM suggests to you.I think there's a use case where this rule can be ignored. Sometimes I ask LLM to help me pick a single word or short phrase in some language, that has specific meaning, and connotations. Or doesn't carry some connotations or associations. Especially when I have an idiom from some language in mind, but I'm writing in some other language and my brain struggles to find a good replacement.LLMs are super handy as fancy vibe-based dictionary search engines. They're all about words that go with other words, so when I'm struggling for a good term, I see no harm in asking and picking an option that I feel closest to what I want to express. My choice, my voice, just a very fancy thesaurus machine.

**gyulai** · 2026-09-19T07:18:49.000Z：

A workflow I've recently discovered for myself, that may be useful to anyone who speaks at least two languages: Ask the LLM to write a first draft in a language that isn't the one the piece should ultimately be in. Then use the LLM's first draft as a blueprint, to write a first draft yourself in the intended target language. That way, you won't be tempted to shut off your brain and just meatproxy anything from the LLM's first draft. Then hand your actual first draft back to the LLM for editorial suggestions. At that point, feel free to ignore suggestions, push back on bad ones while adding a rationale about why you don't like them, etc. Work in the best suggestions, then iterate. If you're in “writer block” mode, force yourself to keep going by asking the LLM for five suggestions on how to phrase something, form an opinion about what you like and don't like about them, draft it yourself by frankensteining from among the suggestions, without using any one suggested phrasing literally. Optionally, provide feedback to the LLM explaining your thinking about why you did or did not like certain suggested phrasings.For objective/factual writing, asking for a fact check is a widely-used practice. And there's a useful counterpart for writing subjective things and opinionated hot takes, namely to ask the LLM: “Anticipate how this might be misunderstood in ways that might cause offence or trigger people.” Sometimes, you might want to say something that will cause offence, and there might be no way around it. In this case, making a conscious choice to let that be might be the right thing to do. But I find it surprising, how often an LLM will see an angle that I myself did not see, where something might cause offence in a way that I genuinely missed and genuinely want to fix. And then that gives me a chance to re-write before posting something.

**foobarbecue** · 2026-09-19T09:09:55.000Z：

"Streamline and improve" is redundant. Pasteurization is great. "jacking it with corn syrup" is nonsense.I'll get my writing tips somewhere else.

**vish045** · 2026-09-19T09:25:49.000Z：

I guess more often than not we are thinking about what to write rather than how to write :-D

**brap** · 2026-09-19T13:17:51.000Z：

One thing that you should absolutely never do: have an LLM review and “improve” the text repeatedly in some closed loop.This might work well for some tasks (coding), but for writing it will absolutely take reasonable text and turn it into a pile of incoherent garbage no human would ever write.Maybe I’m the only one keeps trying this (more often than I’m willing to admit), but I suspect it’s a common cope engineers reach for when having to deal with the not-so-fun task of writing prose.

**maurelius2** · 2026-09-19T14:06:06.000Z：

Great article. Thanks for sharing.

**tolerance** · 2026-09-19T14:52:24.000Z：

What this quite reasonable article has to endorse may be useless. I've read some decent articles both obviously and possibly authored with LLM-assistance and while they were well-structured and carried at least the gravitas of objectivity I couldn't help but feel like their technical fastidiousness belabored their messages.

**ameliaquining** · 2026-09-17T22:59:53.000Z：

There's no way in hell that wasn't a deliberate joke.

**stackghost** · 2026-09-17T22:49:48.000Z：

Can't vouch for that but I can vouch for `Dreyer's English` as both hilarious (if you're the sort of person who relishes finding le mot juste, like me) and excellent as a style guide.

**bobmarleybiceps** · 2026-09-17T23:03:49.000Z：

Yeah it's very short, but I can't remember if I read all of it, or just flipped through pieces. It has good advice and I think fairly "famous." (edit: this reminded me I still have my copy :-D)I know someone in a profession that does a lot of writing, and it blew my mind how clearly feedback was communicated by a superior. Made me wish tech people had better written communication skills. ;-;

**cbfrench** · 2026-09-18T00:10:32.000Z：

It’s good—better than the much-revered Elements of Style, imho, which is overly prescriptive and frankly unhelpful at turns, even if it’s well written.But my all-time favorite is Virginia Tufte’s Artful Sentences: Syntax as Style. It illustrates the variety of English sentence structures in an ordered way with a plethora of examples. The approach is not prescriptive; rather, it allows you inductively to develop a feel for the syntactical rhythms of the language.Also, I love Stanley Fish’s How to Write a Sentence: And How to Read One. It’s a lovely, entertaining little book, filled with Fish’s insights as an eminent literary critic. What I appreciate most about the book is that Fish walks you through a number of examples and explains how and why they work, so you can walk away as both a better writer and a better reader.

**ramblurr** · 2026-09-18T11:15:37.000Z：

Paperback copies in EU seem to be very expensive (90+€ on amazone.de) unfortunately.

**K0nserv** · 2026-09-18T16:09:19.000Z：

I've been reading Steven Pinker's "The Sense of Style". Unlike "The Elements of Style", which is fine, it does a good job anchoring its suggestion in first principals. I do think I need to read a book on grammar to truly appreciate it though."On Writing" is another book like "The Elements of Style", both are too prescriptive, albeit not useless.

**pjm331** · 2026-09-19T00:28:12.000Z：

Clear and simple as the truth - another good one

**boplicity** · 2026-09-17T22:57:43.000Z：

> If you can't spend the time to write it, why should anyone read it?That's actually a legitimate question, and one I've been thinking about, as I've been using LLM tools to compile factual information based on various search tools it uses. The workflow gets sources, fact checks them, filters them according to my needs, and gives me clean urls for source information to hand off to an editor for writing a short listing. It's very hard for the editor to do a much better job at this type of writing; the real benefit of the work was in the research, which was handled by the LLM. The rest is basically just putting the facts in the right order, with some guidance on style, preferred word choices, etc. I'm not comfortable with this at all, as giving work to an LLM that a human could do strikes me as wrong. But using LLM tools gives me a big competitive advantage (for now), in the space I'm doing this in.

**jakeinspace** · 2026-09-17T22:57:49.000Z：

Excessive generative AI output devalues all communication media unfortunately. As a greater and greater portion of text, imagery, audio, and video come to be synthetic, I don't see why anybody would be motivated to do deep reading, or listening, or analysis of said media. It's frightening to think what that might do to our civilization, almost like putting us back into a weird version of the ancient past when nobody was literate, save the priest.Maybe humans can adapt to care about generated content and treat it with the same emotional weight that human communication has. I don't know if that's good or not.

**beebmam** · 2026-09-17T23:26:44.000Z：

I don't ever watch TV or streaming shows anymore. It's been a huge improvement in my life. It's the same with reading. Reading is mostly a waste of my time, with some notable exceptions. I'm glad I spend way less time doing each of these!

**NuclearPM** · 2026-09-17T23:36:00.000Z：

Agreed completely. (This reply took me 0.4 seconds to generate.)

**shimman** · 2026-09-17T23:52:28.000Z：

Just read people you can trust. Why are you giving yourself all this busy work?Just make your own tree of material to read. You should have a couple dozen writers/journalists you admire, look at who these people read then start reading those people, then you repeat the cycle.Don't waste your time reading anything new, most new things are bad. Most ideas we struggle with, are ideas we have been discussing since the written record was invented out of necessity.Anything new worth reading will assuredly make your way to you if you are at all connected.

**iqp** · 2026-09-18T04:57:49.000Z：

> If you can't spend the time to write it, why should anyone read it?100%. We're producing more content, faster, than ever before but ... most of it is just click-producing garbage that won't stand the test of time.

**matheusmoreira** · 2026-09-18T05:18:30.000Z：

> If you can't spend the time to write it, why should anyone read it?Because the information in the post could be valuable regardless of human or LLM involvement.

**ferngodfather** · 2026-09-18T06:04:15.000Z：

People on my FOSS project couldn't see the issue with their AI slopped documentation contributions.On one hand I'm like, yeah fair enough it needed writing and something is better than nothing.On the other I know nobody wants to read it now because it's just word vomit rather than how a human would write something they'd like another human to read.I hate it so much.

**siscia** · 2026-09-18T07:36:54.000Z：

> If you can't spend the time to write it, why should anyone read it?Because the value of writing are not the words on a piece of paper but the idea they convey.Politicians speech are not worth listening too because they have a copywriter polish them?Teacher assistant homeworks are not worth to do, because they are made by a TA and not by the course professor?Of course there are writing as: "Hey ChatGPT write me a piece around coding with LLMs" and yeah, those are not worth reading.But most of the writing is usually, these are the ideas, this is how the idea are structured together, now let's review them and then let's get a nice prose out of it.

**JimDabell** · 2026-09-18T09:10:03.000Z：

> If you can't spend the time to write it, why should anyone read it?This isn’t your thought; you are merely regurgitating a sentence we have all heard many times before, practically word for word.Presumably you think there is value in posting yet another copy of that other person’s thoughts in this discussion, despite having spent no time or effort in thinking it up yourself.Why is that? Is it because you think there is inherent value in the sentence you transcribed, in spite of the near zero effort you spent creating it? If you think anybody here should read it, then you have undermined your own point. If you don’t think anybody should read it, then you shouldn’t post it.

**wkjagt** · 2026-09-18T10:21:56.000Z：

The way I see it is that a clearly AI generated article is the result of some prompts. So the "author" wrote tens of words, which then got inflated to hundreds and maybe thousands by a computer program. This is a very inefficient way to convey an idea, especially if the reader has access to the same program. I'd rather the author shared their prompts, because maybe there's some originality in it, and I can then decide if I want to explore the idea further, maybe even with an LLM.

**globular-toast** · 2026-09-18T10:54:27.000Z：

Yeah, I'm sticking to pre-2020 works from here on out. Not sure how I'll be able to read about current events, though.

**iamkitchjay** · 2026-09-18T11:04:14.000Z：

Strongly agree. Whenever I see an "AI-written" disclaimer, I skip it entirely. And if it's not disclosed, the exact moment I realize it's AI output, I immediately close the tab. 
It feels like a waste of the reader's time.

**plasticchris** · 2026-09-18T16:49:05.000Z：

To focus your point: we fear that with ideas having easier replication that the noise in the signal will increase.But this is what people said about the printing press. And the internet. Less effort to spread the memes. Has it been a net negative? Maybe in some respects. Can you stop it? Probably not.

**627467** · 2026-09-18T23:41:09.000Z：

> I still, while reading, am checking for any amount of AI usedIm sorry for you. It must be hard to detach yourself with a fixation. I also cant help but spend my attention spotting where the magician is hiding the coin instead of trying to enjoy the show> If you can't spend the time to write it, why should anyone read it?Most people in these threads repeat this question. As if pre-ai all writing was from deep thinkers full of genuine intention.

**Gigachad** · 2026-09-19T03:01:13.000Z：

At work the jira tickets have become massive walls of AI slop. What’s worse is they contain huge amounts if useless “thinking” where the LLM explains what it did and checked rather than just giving the final result.As a result, when I see an AI wall of text I just don’t bother reading it and DM the submitter asking what it’s about.

**visarga** · 2026-09-19T05:02:48.000Z：

> If you can't spend the time to write it, why should anyone read it?I don't think writing it is the whole process, research could be 10 or 100x longer.

**chenzhekl** · 2026-09-19T07:03:13.000Z：

Language is meant for sharing information. I don't think there's anything wrong with using AI to write - the real issue is that AI-generated writing can be hard to understand. Once AI solves the readability problem, its writing will actually be better suited for communicating with humans.

**Shocka1** · 2026-09-19T16:11:23.000Z：

Agreed. Recently I've made the effort in disclosing on my website posts that 100% of the words are written by me. I do make graphs and share data here and there, and the same applies - I'm transparent if an agent happened to be used in the process. I don't mind if someone used an LLM to write something, but disclosing such is a good rule to go by IMO.

**Retr0id** · 2026-09-18T00:13:15.000Z：

> overused phrases and tics in your writing styleIn the extreme these can be annoying, but more often I find them kinda charming, as an expression of the author's personality.

**WaltPurvis** · 2026-09-18T17:32:00.000Z：

On a somewhat off-topic note, it seems like even the richest publications no longer employ copy editors, or not enough of them anyway. I am constantly spotting obvious and stupid errors in articles (e.g., duplicated words and misspellings) in the New York Times, Washington Post, et al. I'm certain it didn't use to be that way. (Fact-checkers also seem to have gone extinct; at least once or twice a week I'll read a news article with a glaring factual error or an absurd mathematical error.)

**yapfrog** · 2026-09-17T23:29:43.000Z：

The placement of the "Those rethinks are load-bearing parts of your voice" sentence in the article makes me think the author intended the word choice

**simonw** · 2026-09-17T23:36:11.000Z：

I saw "load-bearing" there and instantly assumed Thomas was making a deliberate point that it's OK to use terms that LLMs have poisoned provided you use them effectively and in a way that adds to the piece.I'm personally furious that "load-bearing" has become an LLM tell, it's a really useful metaphor!

**kergonath** · 2026-09-17T23:47:05.000Z：

> Pasteurising is good, corn syrup is badPasteurising something is making it sterile. Safer, but bland and not as interesting. I guess that’s the intended metaphor.

**WaltPurvis** · 2026-09-18T17:19:27.000Z：

I suspect the author was thinking "homogenizing" but his brain picked pasteurizing by accident. Pasteurizing and homogenizing are both things done to milk, but homogenizing has an additional meaning of making something uniform (and more loosely it's often used to imply that you've made something generic, bland, and boring).

**simonw** · 2026-09-17T23:36:42.000Z：

That's what the piece says.

**simonw** · 2026-09-17T23:34:27.000Z：

I do this all the time. It's shocking how well it works. A year or two ago suggesting that someone use LLMs for fact checking would get you laughed out of a room, but today the good ones (Fable, GPT-5.6/6) with a search tool enabled are genuinely excellent at this.They can even retrieve articles you link to and check that you aren't misrepresenting them.

**ralphington** · 2026-09-18T05:06:49.000Z：

Hyperbole = strong opinions? If you're stating your 'strong opinions' as fact, then you deserve the push back. If you're stating your strong opinions as strong opinions, then fair game.

**dormo** · 2026-09-17T23:46:19.000Z：

That checklist sounds like at least as much work as writing a commit message.

**simonw** · 2026-09-18T00:05:17.000Z：

See https://news.ycombinator.com/item?id=49747070#49748296

**thombles** · 2026-09-18T00:05:49.000Z：

I'm somewhere between 100 and 110% sure the author knew what they were doing.

**tptacek** · 2026-09-18T00:12:31.000Z：

That’s what this is: it’s mechanical proofing.

**ttctciyf** · 2026-09-18T07:25:05.000Z：

Yeah, the best advice is: Don't. Write it yourself; make judgements; learn.In general use today, AI primarily functions as a stupidity amplifier: it empowers dumb people to do dumb things more pervasively, with less effort, and at unprecedented scale.We're moving into an era of artificially enhanced stupidity.

**qwerty_clicks** · 2026-09-18T05:47:59.000Z：

I feel like it normalizes writing faux pas; any use of a semicolon could have just been a new sentence.I’m thinking that people that get years semi-colon and colon filled paragraphs are going to believe this is a normal and good way to write on their own.

**riskable** · 2026-09-18T15:08:35.000Z：

All the Big AI APIs handle a million tokens of context. That's enough for 750,000 words or, several entire novels.Context isn't an issue. It's style.The argument the author is making is that if you use an LLM to write for you, you end up with a homogeneous work that's just like everything else.In journalism, that's sort of what you want.In novels/function, that's the opposite of what you want.However, there's degrees to these things. If you're looking at a sentence you wrote, thinking there's something "off" it can be helpful to have the LLM rewrite it just to see how it thinks it could be better worded.I've done this a few times and I do find it helpful. Just like the author, I never just accept what it gives me. I simply use it as an OK-ish copyeditor that's good at spotting issues and suggesting solutions.

**Miraltar** · 2026-09-18T08:09:43.000Z：

I would guess that it's just a matter of context, I haven't used voice mode at all but I imagine you don't get full paragraphs from them but get something more conversational instead

**duckerduck** · 2026-09-18T08:00:45.000Z：

The "load bearing" term has become a bit of a meme, given the author is familiar with these AI-isms, we can assume it's a subtle joke.

**LtWorf** · 2026-09-18T08:08:25.000Z：

In the simpsons there was a load bearing poster in their home, IIRC.

**skydhash** · 2026-09-18T11:10:29.000Z：

> but they probably did just that because I never heard a human being say "load-bearing" before but now it's all over the placeI have but it was a house construction worker explaining its practice on youtube.

**jameshart** · 2026-09-18T12:49:13.000Z：

If you’re familiar with tptacek’s writing you would be confident this is deliberate and recognize it as an ‘I see what he did there’ moment.If not, it does risk planting the seed of doubt - have I been duped once again into reading tokenslop again?Risky move. Surprised the LLM copy editor didn’t flag it.

**lkbm** · 2026-09-18T15:13:10.000Z：

It's been a common phrase for many years.[0][0] https://x.com/search?q=%22load%20bearing%22%20until%3A2020-0...

**inkcapmushroom** · 2026-09-18T17:12:53.000Z：

The irony comes in the last sentence: "Readers won’t put their fingers on what’s wrong, but they’ll sense that you’ve become artificially-flavored." The joke is that he wrote the preceding sentences in the paragraph in a way that intentionally plays up written-by-LLM-isms so that you feel the sense being described in the quoted sentence.

**dilyevsky** · 2026-09-18T21:22:34.000Z：

load-bearing was a meme phrase used sarcastically on twitter long before claude started overusing it.

**CuriouslyC** · 2026-09-18T14:04:43.000Z：

The mechanical act of writing is not thinking any more than talking is. Plenty of people are capable of written word vomit.The act of agonizing over the words you put on the page is thinking. A lot of humans don't do it. The writers who talk about writing being thinking are in a bubble and don't realize that their process is not universal.

**caminante** · 2026-09-18T09:10:57.000Z：

In context, he's just saying this self-scrutiny is what makes your words authentic.

**tptacek** · 2026-09-18T12:26:10.000Z：

It sure was.

**moffkalast** · 2026-09-18T22:18:27.000Z：

How many parts per million did they say again? ;)

**tptacek** · 2026-09-18T12:30:31.000Z：

You can just not copyedit. That's fine. More than fine, lately: rough edges are a signifier of authenticity. If that's the way you want to go, writing raw, I think that can be a good strategy.But if you've generally been doing drafts and want to keep writing like that, if part of your process is going to continue to be refining and sharpening, then I think you should know that we're at a point where automation can accelerate that process for you. You can be getting the same amount of work done with less effort, or allowing yourself to concentrate more on the creative thinking part and less on the tedium.That's the point of the post.

**alansaber** · 2026-09-18T10:53:35.000Z：

Exactly- without constraining the input, you're guaranteed to get slop. First-draft AI copy is usually 95% to-cut, 4% to re-sequence, 1% to keep. Use it to think about iterating, not sweep the solution space blindly.

**bsenftner** · 2026-09-18T11:01:39.000Z：

Just write, write your own words, then create an effective communication persona within your LLM's non-reasoning (non-Chain-of-Thought) capabilities and have it critique your writing after describing your target audience. Then, write your own revision following the critique. Using this, it is not possible to write "AI slop" unless your own writing is already in the style of LLM output. Which I get accused of when I write using my formal voice, but fuck that sorry for being well educated.

**CuriouslyC** · 2026-09-18T13:52:26.000Z：

Try using them to have a long discussion and provide it input data, then have it emit a concise bulleted outline given the points you want to make. Then you can rejigger the outline efficiently as needed and write the text yourself.

**brap** · 2026-09-19T13:23:50.000Z：

One thing that sort of worked for me is to write the skeleton myself, i.e. the general ideas and how they fit together, the overall “flow” of what I want to say, then have an LLM fill in the blanks (I either point it at some context.md or have it ask me questions when details are missing).It’s kind of like designing the high level software architecture yourself and have the LLM write the code for each component.Not bulletproof, requires some iteration, but miles better than what it would produce on its own.

**tptacek** · 2026-09-18T12:43:44.000Z：

Look at the prompt titles in the screenshot. None of them give opportunities for the model to praise --- they're all technical. There's a system prompt applied to all of them: Workshop a piece with me. NO ENCOURAGEMENT. Encouragement is
 useless; the only useful things are suggested corrections.
 DO NOT WRITE COPY FOR ME. Any words you provide will be disqualified,
 so if you come up with good words, I’m fucked because I can’t use
 them. Tell me ABOUT what should change.
 Assume I know my audience extremely well.
 We’re going to do this in a series of passes. Keep your suggestions
 locked in to the current pass we’re on.
 Note typos, but DO NOT generate long structural critiques based on
 those typos; note them and move on, assuming that I meant to write
 properly.

Assume I do 8-12 passes on any piece. Assume I respond to ~60% of suggestions; the other 40% I'm like, "nah, I wanted it to sound that way". And then about half the time I change something, I just rewrite the whole paragraph, mooting the suggestion. (The other half of the time I do roughly what's suggested; ie, removing the word "just" or "very", or switching the subject of the sentence.)

**jackyinger** · 2026-09-18T12:58:12.000Z：

Agreed. If I’m spending my precious time reading something thing, I want the author to have invested their personal effort to write it.

**anonymous_user9** · 2026-09-18T13:05:28.000Z：

Those of us using our human minds to extract meaning from specifications and manuals don't want to look at LLM slop either.

**utopiah** · 2026-09-18T13:40:45.000Z：

Interesting way to put it because it means in most professional software development contexts, it is also NOT appropriate for coding since other human will work on the same codebase, at least review the submitted code. So... according to this (IMHO pragmatic) heuristics it's only acceptable for coding alone, e.g. weekend project that won't be pushed online. Unless code has no meaning beside the output it produces, which does exist but I would wager is rare.

**SamInTheShell** · 2026-09-18T14:13:14.000Z：

> If you're writing for processes with formal highly structured content like manuals, specifications, form content, procedures, information, that sort of thing,Yeah... no. The people doing this lack the communications training, see the output has the necessary information, and regurgitate it with no effort or care. This needs to stop.We spent decades format building to make it easy quick and easy to get through something like a runbook. If your commands are bulleted instead of numbered and code blocked, it's wrong. If you didn't crawl through the playbook, it's immoral to hand that to me, you're wasting my time with untested slop.This is a hill I will die on or absolutely start slaughtering people on. I just refuse to deal with this crap.

**marcelo-earth** · 2026-09-18T14:48:18.000Z：

In fact, post-LLM quality monitoring is a huge time trap.I can't write anything for humans using LLMs, because there is so much to change that it ends up like the Ship of Theseus, I would have been faster writing it myself than delegating the task.

**tptacek** · 2026-09-18T17:01:56.000Z：

The literal first rule of the post is not to have LLMs write for you.

**robwwilliams** · 2026-09-18T19:02:16.000Z：

Too simple, too dogmatic
at the start and at the end (“don’t use LLMs” and “then they are poison”). The middle section is all good.Writing with a LLM is a boon if you are trying to write while mastering a new field. Imagine a neuroscientist entering robotics or an electrical engineer trying to enter the field of neuromorphic systems. In these cases a human will need help from an LLM to think and write more deeply AND broadly. I sure do.You could object that this form of human-LLM collaborative writing is just for one reader; the writer. True at the start but not true toward the end.I do agree that even the frontier models do not touch a really strong human writer. Way too much gimmickry. They do not yet match individuals such as Leslie Lamport, Terry Winograd, John MacArthur, Richard Rorty, Humberto Maturana, William James, Rodney Brooks. They don’t have the depth of understanding to simplify. But give them a few more years and excursions in the real world and a concept if “now” and the situation may improve.I often ask Fable and Opus to explain difficult topics to me as if I were the canonical dog Rover. It works.

**aprilthird2021** · 2026-09-18T21:39:33.000Z：

Absolutely correct. No matter what the detractors say, your writing will get glazed over and you will lose the focus of readers if your AI output sounds like all the AI output your readers have read before.

**delis-thumbs-7e** · 2026-09-18T21:52:57.000Z：

You just should not do things that human beings are good at with automated processes. Things such as: creative writing, painting, dancing that is not pre-programmed, going with the flow, living the moment, having sex, wrestling, cooking, acting, connecting with your loved ones... and so on.Word chains these programs produce are inherently meaningless. They do not feel so, because WE people are amazing at bringing meaning to any old string of symbols: https://www.ubu.com/sound/lin.htmlThey are very useful machines indeed, but they do not help you write well. They mathematically cannot. They just try to guess what is the next tokern you might want to read.

**int0x29** · 2026-09-18T22:31:07.000Z：

I would stay away from it for manuals and documentation as well. AI tends to like inserting meaningless and confusing clarification that is at best a waste of time.Also if you don't understand what you are documenting enough to write the docs that is a problem.

**qarl** · 2026-09-18T22:59:37.000Z：

> don't use LLMsDon't you think they're useful as fact checkers?

**BeetleB** · 2026-09-18T17:00:14.000Z：

At work, I simply don't allow LLMs to make commits. :-)

**hannasanarion** · 2026-09-18T17:01:32.000Z：

This currently is my team's only AI-use policy and I thik it's working out fantastically."No AI PR Descriptions" is a great rule because it does 3 things:1. It's a hard binary that's easy to recognize and enforce2. It establishes personal ownership for the submitter, making it psychologically difficult to submit something you don't understand. If a person has to describe what a change does, how, and why, then they must have looked at it and made a real attempt to understand it, because you can't map a territory you have never seen. This alone prevents "claude-code run amok" scenarios where devs have completely abdicated responsibility that are a real pain to clean up.3. It informs the reviewer of the change's intent. A human PR tells reviewers what a thing is intended to do, as well as the authors belief about what it does, which they can use as a framework to critique the actual substance. It becomes easier to notice missed edge cases, code behavior that subtly differs from intent, or changes that would block off or complicate an intended future project direction or reduce maintainability.And as a bonus, at time of writing, AI pr descriptions basically always suck. They are usually full of irrelevant implementation details, misplaced emphasis, weird presuppositions that seem to come out of nowhere and are really annoying to read, etc. That won't be true forever, they are always getting better, but it is true now, so that's a temporary 4th benefit.

**LeafItAlone** · 2026-09-18T18:17:38.000Z：

A big win of LLMs in my book is the absolute reduction of commit messages with just “fixes” or “updates”. Commit messages have become more meaningful and useful, even if far from perfect.We have one dev who uses LLMs to write the code, but still commits by hand. Most of his messages are of the type above, and none of them are useful.

**initsecret** · 2026-09-18T20:50:54.000Z：

same. also—from the reviewer end—LLM generated PR descriptions are loooooooooooooong.

**dyauspitr** · 2026-09-18T21:03:59.000Z：

Why do you want to understand the agent generated code though? That would make you the bottleneck. Shouldn’t you just concentrate on checking for optimal outcomes, exhaustively trying to find/prompt edge cases and profiling performance?

**cgriswald** · 2026-09-19T04:42:48.000Z：

Using LLMs is like managing people. It’s difficult in some ways and easier in others. You should trust them to a degree but also know what is going on and if you’re “trusting” them out of laziness you’re doing it wrong.

**jdkoeck** · 2026-09-19T06:15:56.000Z：

Two years ago? I don’t get it, coding agents have been compelling for barely a year.

**solarkraft** · 2026-09-19T11:06:47.000Z：

I still manually edit almost every word for utmost precision in anything I expect a human to read since LLM prose is hard to read and often subtly wrong or misleadingly worded (those false contrasts ...).Commit messages are not exactly in this category for me, I view them mostly as a work log to be later inspected by another LLM to gather context. I do usually review them before approving a given plan, so I do care about their structure and content, but find the LLM sufficiently competent at writing them.

**_nivlac_** · 2026-09-18T13:24:24.000Z：

I like to think that was thrown in there as a joke... surely, for a piece like this.edit: it was! https://news.ycombinator.com/item?id=49753395

**simonw** · 2026-09-18T14:07:23.000Z：

I take it you didn't read the article, then.

**zzleeper** · 2026-09-18T14:10:27.000Z：

I thought that was a joke.. Like how I used "delve into" back in 2024 or so lol

**datadrivenangel** · 2026-09-18T21:08:03.000Z：

I actually like this as a method for getting over writers block. The second the AI starts spitting out words I know it will be wrong and dumb and so I might as well do it myself. Enough activation energy to get started

**wannabe44** · 2026-09-18T16:53:40.000Z：

Google docs fixes all grammatical mistakes.

**tptacek** · 2026-09-18T17:03:38.000Z：

What is the actual human-written program that you're thinking of that detects verb nominalization, verifies that the subjects of sentences are actual characters in the action, that new information is placed in the stress position of sentences, and that each paragraph has a clear topic sentence?I'd love to know. I'll buy it!

**tptacek** · 2026-09-18T16:59:30.000Z：

I wrote the article. I am not interested in "style suggestions" from the LLM; I'm interested in things I can verify for myself. Is this word or construction overused in the piece? Is there a pointless throat-clearing like "it's important to note that" crudding up this paragraph? Am I overusing vacuous nouns like "issue" ("the big issue is that") or "factor" ("the next factor to consider is")? Do I have my verbs buried in nouns, like "distortion" where I should just use "distort"?I don't care whether the LLM likes these constructions or not. I don't like them. I usually don't want to keep them in my work. It's my call what to change; I just want issues flagged.Your prompts would be different. Or, they would if you decided that having an LLM merely point things out about your own writing wasn't itself a form of contamination. You do you!I wrote this article in about 45 minutes and didn't workshop it with anybody else, so I'm not surprised it's gone over people's heads; it was just something I was talking about on Twitter that I wanted to get down on a page. But it's pretty obvious that a lot of people here have missed the point.

**andrewflnr** · 2026-09-19T03:13:14.000Z：

That's not "circular" so much as an acceptance that there's no free lunch w.r.t. good writing.And, as a fan of the "let it stew" technique, it's not a full substitute for an actual other perspective.

**zrail** · 2026-09-19T01:35:17.000Z：

"Naturally gifted writer" is not a thing. The way to get better at writing is to write a lot.Developing a voice comes naturally as you go through the pain of being a terrible writer to eventually being mediocre. Accepting the LLM's words is actively harmful to that process because it lets you skip over the part where you read over what you wrote and rewrite until it doesn't suck as much.I mean, you do you. I'm not your dad.

**tptacek** · 2026-09-19T02:32:07.000Z：

Ordinary people were writing before the option existed to accept words from AI models.

**hobom** · 2026-09-19T08:49:58.000Z：

Using your own voice is absolutely important, even if your voice may suck. 
Even a bad writer will manage, if they actually put in effort, to convey some of their own thoughts. This gives the reader a feeling of "there is something there, an actual substance of thought", even if it's hard to find. And that's the Using an LLM risks that the crumbs of actual thought get edited out in favor of meaningless pleasantries.However, I directionally agree though with your message: if you are bad at writing, often you can use LLMs to surgically improve the flow of your sentences for example. One should use a carefully crafted workflow for this though.

**tptacek** · 2026-09-18T23:28:03.000Z：

What is this comment responding to? I don't think anybody in this thread, or the article itself, believes "emitting words" is what writing is?

**tptacek** · 2026-09-19T02:32:41.000Z：

Apparently your detector is out of whack.

**tptacek** · 2026-09-19T02:31:22.000Z：

LLMs do that every sentence. This is the last sentence in the piece. Like the em-dash, and like every transformer model, people overfit.

**claiir** · 2026-09-19T04:39:49.000Z：

“not as writing but as output.”

**tptacek** · 2026-09-19T03:39:51.000Z：

I don't so much worry about whether LLMs taking my prompts enjoy my style.

**mschnell** · 2026-09-19T05:03:37.000Z：

Exactly. I often ask for a list of words that describe a specific concept. The choice is made by me.

**TheFlyingFish** · 2026-09-19T14:43:57.000Z：

The corn-syrup comment made sense to me FWIW. I associated corn syrup with mass-produced food that's optimized to make all your taste receptors go "bling" when it first hits your tongue, but lacks any real substance. Which also describes the text that comes out of an LLM.

**Tomte** · 2026-09-19T07:26:22.000Z：

It‘s been available under different variations of the title, you don‘t need the latest one, and amazon.de should have a used copy for five Euros or so.

**dwhitney** · 2026-09-19T02:51:25.000Z：

Steven Pinker’s “The Language Instinct” is not a bad book for learning grammar. It’s a book about linguistics - not specifically grammar, but it covers diagramming sentences, and grammar falls out from there

**Tomte** · 2026-09-19T15:30:52.000Z：

I found his description of Classical Style very confusing and disorganized. You‘re much better off reading the original, Thomas & Turner.

**derektank** · 2026-09-17T23:15:24.000Z：

>I'm not comfortable with this at all, as giving work to an LLM that a human could do strikes me as wrongWhere does this feeling come from? Is it just because the work is complex? We’re all (excepting maybe the amish) comfortable with using at least some automation, be it mechanical or digital, elsewhere in our lives

**loloquwowndueo** · 2026-09-17T23:27:50.000Z：

> compile factual information based on various search tools it uses. The workflow gets sources, fact checks them, filters them according to my needs, and gives me clean urls for source information to hand off to an editor for writing a short listing.What’s preventing the editor from using one of your prompts/tooling and replacing you entirely?There’s zero value in sharing ai-generated output unless your ai has access to something nobody else’s does on which to base things. If all it’s doing is web research you should share your prompt instead. That way people don’t have to deal with ai-written walls of text.

**sixtyj** · 2026-09-17T23:10:55.000Z：

There is a recent PISA research that students slowly decline in understanding the long reads.E.g. in one country, 21% of high school students do not even achieve “sufficient reading literacy”…So the question should be - what are we going to do with this? LLM can produce texts but we as people will not be able to understand anyway…About PISA research for example here: https://www.edweek.org/leadership/reading-ability-craters-on...

**Insimwytim** · 2026-09-17T23:50:41.000Z：

You can't even watch funny animal compilations anymore!

**TeMPOraL** · 2026-09-18T09:52:32.000Z：

You're skipping any causal connection between the "as greater and greater" and "anybody would be motivated" parts. What is it in "excessive generative AI output" that "devalues all communication media"?Not that I disagree much, but for myself I have an actual cause connecting the two parts, and it's not something inherent to AI.Basically, synthetic content is like those fancy desserts - they look nice and the top layer possibly has an exquisite flavor (probably on purpose), but once you cut deeper, it's some weird fruit or nut or other foodstuff that belongs next to potatoes and meat, not in a cake. So I learned to avoid such desserts and stick to basic stuff I know are good entirely, like IDK a cream pie or cream-filled chocolate stuff or such.Same is with content. My problem isn't that it's AI, but that it's wrong, full of mistakes human authors don't make. Hallucinations mid-text that make half of it convincingly argue bullshit. Or the uncanny or repetitive factor in art that kicks in after few seconds of looking.Like with desert, I'm avoiding disappointment and wasted hopes. When synthetic context gets better, I'll be consuming it just like "vanilla" one, for the same reasons.

**altmanaltman** · 2026-09-19T04:43:37.000Z：

Wait wait wait, why will humand syop wanting to read, listen to music, or watch movies and tv shows just because there are AI generated art? People will still feel the need for all those things, technology alone cannot erase the demand. The problem is generated art is not considered good by audiences because it usually lacks substance and genuine creativity. But that doesn't mean they will not want to watch The Odessy. If an AI can make a movie which is exactly equivalent to a Christopher Nolan movie, then yes people can adapt. But the current situation is that most AI art sucks and people do not like it. Not that people want to stop reading, listening or watching. We are doing that in much larger numbers than we ever did in history.

**incognition** · 2026-09-19T05:55:13.000Z：

A Tower of Bable phenomenon

**UltraSane** · 2026-09-19T06:04:07.000Z：

Drowning in AI output will make people value in person communication far more.

**S-E-P** · 2026-09-17T23:57:27.000Z：

It's sad that reading has become that way for you.I love reading, but I mostly read non-fiction and I'm a bit of an amateur history buff. Last time I read a fiction book I was left feeling like I was preached to by an alien about how life doesn't really matter (sci-fi authors will often do that). The state of literature is pretty dire.

**CuriouslyC** · 2026-09-18T14:00:21.000Z：

If everyone followed this advice it would turn influencer culture to 11, rich get richer, with no "social mobility"

**CuriouslyC** · 2026-09-18T13:55:54.000Z：

The thing is, that was the internet before AI. In fact, generative AI almost certainly raised the AVERAGE quality of stuff on the internet, human slop was/is absolute trash, whereas AI slop is just bland and meandering.The problem here is that the volume of low-mid content is making it harder to find the best content.

**californical** · 2026-09-18T06:18:41.000Z：

But how much slop are you willing to wade through, hoping to find a nugget of insight?

**LtWorf** · 2026-09-18T08:05:12.000Z：

On Debian we recently voted whether to permit or forbid llm usage (spoiler, AI usage at will won).One person was arguing that they need llm because english isn't their first language and then it helps them write better and be understood. I was incapable of reading their (extremely long) email of arguments; I tried but my mind just went elsewhere as my eyes were moving through the lines.At the very end there was a disclaimer that llm had been used to "aid" in writing that very email.Poor guy thinks he's communicating better but all he's doing is making his emails completely unreadable. It's a sad state of affairs.

**graemep** · 2026-09-18T07:54:23.000Z：

"Politicians speech are not worth listening too because they have a copywriter polish them?"It often makes them less informative and a lot less sincere.

**Planktonne** · 2026-09-18T10:57:01.000Z：

> But most of the writing is usually, these are the ideas, this is how the idea are structured together, now let's review them and then let's get a nice prose out of it.I know lots of AI-enabled writers believe this, but I've never actually seen it be true.

**sm-silversight** · 2026-09-18T09:50:41.000Z：

How do you know it's not his/her thought? Just because others have had it does not mean he/she did not put effort into considering it.

**unsungNovelty** · 2026-09-18T09:53:48.000Z：

> despite having spent no time or effort in thinking it up yourself.I mean, how can you say that he didn't think it himself? I thought this same thing and realised apparently I'm not the first. You have no idea how many of my blog posts ideas have come in HN first before I could publish. People can have the same thoughts. And have em all the time as well.Psss.. See how @sm-silversight who commented on your post said the same thing I did? That's realtime example right there.Coming back to the topic at hand. I agree with the OP. If you don't care to write it, why should anyone read it? AI has good usecases. But am not sure writing is one.Writing is not just about the end result. It's also about the thought process. I learn about the topic more as I write. I correct my incorrect understandings as I write. When am pissed, my article has a different tone. Am rude, too direct. When am content/happy, different one. All of this is sterilised into something robotic where the author won't even remember what he/she wrote? What's the to like? For brownie points?

**Applejinx** · 2026-09-18T10:03:34.000Z：

OK, how about 'nothing is real, nobody will ever care again, let's all never listen to anybody else ever again'?That's more or less the same thing expressed more nihilistically. But nihilism is, like, just a word man (to 'The Dude' it up a bit). Perhaps we are either fiddling on the deck of the Titanic, or just staring at the waves?What do you think the results will be of the machines consuming only their own slop and Habsburging themselves intellectually, and then all the humans abandoning any attempt to either talk or listen? As a global civilization of humans? I'm not sure we've explored the likely consequences of 'if you can't spend them time to write it why should anyone read it'.Maybe it's gone too far already.

**phrotoma** · 2026-09-18T10:06:17.000Z：

Agreeing with a person is not the same thing as agreeing with a robot.

**dofm** · 2026-09-18T12:08:40.000Z：

There is critiquing an idea using pointed Socratic critique, and there’s coming across as a bit of a dick, Jim.

**andrewflnr** · 2026-09-19T03:04:31.000Z：

Some things are worth repeating, so the community knows that many people share the belief. Often they're slogans, sometimes they're just plain good arguments.

**63stack** · 2026-09-19T10:29:18.000Z：

I may not be the one that came up with a thought originally, but I can echo it because I agree with it.

**basilikum** · 2026-09-19T13:00:49.000Z：

You are moving the goalpost. OC is not talking about thoughts having to be unique. You can very much read someone else's thoughts, examine them critically and come to the conclusion of agreeing with them. You might then write a comment like OC putting these thoughts into your own words – maybe abridging them, placing different emphasize according to what you find most important or even adding new ideas – and quote or paraphrase something you found very fitting.That is completely different from generating words that are not an expression of your thoughts or at the very best take some concise thoughts from the prompt and stretch them into a lengthy word soup.Of course there are people who just parrot other people's thoughts without understanding them. That's closer to using an LLM. But you can often see how well someone understands something and how much reasoning of their own they put into it through their writing. And for the writer writing is a very good way to reflect on their own thoughts and to get them into order. Proper writing is thinking.

**CuriouslyC** · 2026-09-18T13:58:03.000Z：

What if the prompt for the 1500 word article you're reading is 10k words of research/data collection, thesis testing, etc?

**tripledry** · 2026-09-19T08:03:24.000Z：

Not only hard to understand, but if one uses it without first understanding the topic, it's a disaster.Couple weeks ago I had someone linking to a doc page in my ticket "Made this summary, hope it helps". It was 100% AI generated, the person clearly had no understanding of the problem, it only mentioned UI changes although the thing required changes in many systems. Complete waste of time, I don't think I will humor anyone who makes AI summaries anymore.

**tptacek** · 2026-09-18T00:15:02.000Z：

Simple example from this piece: I scrubbed 7 instances of the word “just” from it. Obviously, Emacs can do that on their own, but you have to know to look for that word, and every other one.

**awithrow** · 2026-09-18T02:52:06.000Z：

Agreed and depends on the writing. It's a very helpful tool though to be able to flag and highlight that sort of thing

**wj** · 2026-09-19T11:40:19.000Z：

I see that as well. Sometimes I can see that they are prioritizing speed to print for breaking news (publishing to the web happens continuously vs the cadence of a daily newspaper) but often it is just being sloppy.When most people are consuming _their_ news (as opposed to _the_ news) in the form of a thumbnail in an algorithmic social media feed, those copy errors matter less.

**tptacek** · 2026-09-17T23:39:07.000Z：

It was a joke.

**throwthrowuknow** · 2026-09-18T11:44:28.000Z：

artificially-flavoured is also a tic unless the author was trying to make fun of load-bearing, but it’s a bit too subtle to make the point

**weezing** · 2026-09-18T12:16:08.000Z：

That's what tl;dr sums up.

**benoau** · 2026-09-18T03:19:07.000Z：

I do something like this with code all the time, “is this idiomatic <foo>?”, I find it very helpful.

**geraneum** · 2026-09-18T09:33:31.000Z：

This is bad advice for anything serious that can be subtly wrong. I’ve had Fable being consequentially wrong about what a certain, rather small, code block does in our codebase. Not even on something very complex which wasted a lot of time and effort from the team until we checked the code ourselves. I think these tools are still useful and one should learn to use them but blind trust for anything of importance is misguided IMO.

**matheusmoreira** · 2026-09-18T05:15:50.000Z：

> If you're stating your 'strong opinions' as factIs there anybody on this site who isn't?

**thombles** · 2026-09-18T05:21:46.000Z：

If I want to say that iOS is useless for developing Bluetooth 5 features then this is true for all practical purposes and doesn’t deserve elaboration in my text, even if Apple’s API technically exposes one or two tiny pieces.

**ferngodfather** · 2026-09-18T06:00:59.000Z：

You say this but fact and opinion are very similar and not at all easy to distinguish.For instance, if I said the grass is green vs if I said the grass looks nice vs if I said the grass is doing well and looks how it should vs if I said in my opinion the grass is healthier than its ever been.

**dan-robertson** · 2026-09-19T18:59:21.000Z：

If a model complains about hyperbole, that doesn’t mean the text is hyperbole, and this can be because of the context of the text or because of the hedging the models are wont to do

**felipeerias** · 2026-09-18T11:03:09.000Z：

But I only had to write it once.

**Retr0id** · 2026-09-18T00:16:37.000Z：

I don't think it's a useful substitute for actual proofreading though, unless you're truly in a time crunch. When I proofread I don't just look for mistakes, I try to put myself into the position of a prospective audience member. LLMs seem to have absolutely no concept of "theory of the reader's mind". If I'm going for extra high effort, I have friends read it, usually asking them to identify anything that was unclear or hard to follow.

**Retr0id** · 2026-09-18T00:22:58.000Z：

As a "proof" of their poor judgement, take a paragraph you like. Ask the LLM to rewrite it to make it better (which I think we both agree will not make it better), and then in a fresh session ask it which it thinks is best. It'll almost always pick its own writing, even when it sucks.

**swah** · 2026-09-18T18:57:22.000Z：

What they took from us....

**vidarh** · 2026-09-18T09:16:01.000Z：

I was referring to the use of the word "load-bearing". It was most likely an intentional joke, but it's one of the most grating current AI-tells to the point it's a word you'll at this point generally want to avoid (unless it's a joke).

**delis-thumbs-7e** · 2026-09-18T21:30:13.000Z：

My point was, however, is that it depends on what -- and how -- you write.Style is kind of a pretense. Communication in general is a sort of a mucks game of guessing how to get your point across across the medum, whether that of air, FM-radio, writing, internet, video... In academia, copywriting and so-on we create these patterns we call writing styles to agree on the rules on the game. But honestly, we should use sá lot more fuckin swear words when disproving the fuckin conjectures.Yes I know automation makes things quicker. Sometimes even close to fast. But htere's things you should do slow.Writing and thinking are amongst them. And hey, LLM's can help you here as well. But they should not speed you up, they should slow you down. Why did you say this? WHat is your premise? What is the source of this? KIM by Moonshot is really easy to take a system prompt that makes the models output a biggest asshole editor in the world. It doesn't help me at all, on the contrary, it creates friction.I don't think more speed is what we need at this point of evolution.

**bovermyer** · 2026-09-18T12:39:41.000Z：

This is close to my approach. I'll use LLMs as a read-only editor for my writing. Sometimes I follow its advice. Sometimes I don't. Other times, it discovers things I want to change, but not in the way it describes.

**thesuitonym** · 2026-09-18T14:36:30.000Z：

Or to put it another way: Why should I be interested in reading something you weren't interested in writing?

**Eddy_Viscosity2** · 2026-09-18T13:22:27.000Z：

Slop is slop of course, but I don't 'read' manuals so much as I look stuff up in them. So I only need the information to be clear and style doesn't matter so much. Provided the LLM knows its writing a manual it can do a fair job of presenting the info in a good enough manner. Granted, if someone had used the tool incorrectly and its spouting out flowery prose in a manual, then that is indeed bad.

**hannasanarion** · 2026-09-18T14:21:33.000Z：

But reviewing isn't the same as reading.When you review code, you're not taking it all in end to end like an email or memo or blog, you're looking for important symbols, recognizing structures and patterns, jumping between different files at different levels of reference and abstraction, and building a model in your head of the principles that make it work and their consequences for the overall procedure.Code is "meant to be read" in the same way as a law, blueprint, policy document, or manual is, ie: jumping between relevant sections to get small pieces of information relevant to some task. The act of "reading" never starts at the beginning, it starts with a ctrl-f or flipping through an index or table of contents for a specific relevant symbol that is the only reason you are looking at the document.Code is invention, not art (and should be covered by patent law, not copyright law, I will die on this hill)

**antonvs** · 2026-09-18T15:47:18.000Z：

That comparison isn’t automatically valid, because the criteria for what makes acceptable code are very different than for natural language prose.It’s perfectly possible to consider e.g. working, LLM generated, human approved code acceptable, while considering LLM writing that hasn’t undergone major human editing unacceptable because of its repetitious, formulaic, marketing-oriented style - a criticism that doesn’t even make sense for LLM generated code.

**antonvs** · 2026-09-18T15:55:02.000Z：

I used an LLM a year or more ago to generate a description of our SDLC for a compliance certification. Perfect application of LLMs IMO. Do you want to die on that hill as well?A lot of documentation generated in corporations has marginal real value.> If your commands are bulleted instead of numbered and code blocked, it's wrong.That’s easy to instruct an agent to do. Put it in a skill.> If you didn't crawl through the playbook, it's immoral to hand that to me, you're wasting my time with untested slop.Using an AI doesn’t absolve the user of their responsibilities. This is an easy problem to solve, just make sure teams know what’s expected of them and encourage everyone to push back (professionally) against offenders.

**keeganpoppen** · 2026-09-18T17:51:06.000Z：

completely agree. i will admit to taking llm phrases when i am really trying to refine every last detail and it just makes a suggestion that is too good to unsee. but in general it doesn’t feel like it helps directly with the “word choosing” part of the writing task at all (if you are someone who cares about word choice), which is… definitely a pretty big part of the job, lol.it is great at analyzing the argument, finding inconsistencies, helping you think through what parts should be cut, helping you refine examples or fix the occasional “how do i get this phrase to work correctly in this transition?” kinds of stuff. but anything where LLMs are the prima materia… that stuff literally only makes sense _to me_. which makes sense, because it is written _for_ me, no matter what instructions i actually give it, bc of memories and a million other things. and i say this as a complete maximalist wrt. trying to use llms for absolutely every last thing they possibly can be used for, just to see what it’s like.i guess i would say that it does very, very little to make the writing process meaningfully faster; it _can_ do _plenty_ to help make your output better though, which is definitely something— just isn’t the thing most people are looking for.

**jerf** · 2026-09-18T18:00:44.000Z：

I've had some success writing certain explicitly technical documents, with a style guide provided to the LLM that it can match, and then going over it by basically iterating on every sentence in the document and asking "can this sentence be removed?".Style guides are a big tools people are missing out on. It isn't enough to say "write concisely and technically". Give them a sample. Yea verily these many 5 or 6 years ago, "style transfer" was a big thing that early LLM tech was doing. It's still very good at it.That said I still tend to cut out at least 25% of the resulting verbiage and adding back another 10% or so more of my own original content even under those circumstances.Where it has been really helpful is that I tend to want to write in a conversational style that doesn't seem to match most people's expectations of a technical document. The LLMs let me write my way and style-shift it into something closer to what people expect. And LLMs, since let's be honest they're the primary audience nowadays. Which I am not even upset about; I'd rather 5 LLMs read the architecture document than the amortized .2 or so humans I could expect in the same circumstance 5 years ago.Which also implies, in many cases, I am feeding the AI as much text as I expect to come out, or in some cases, even more, as I am describing context, reasoning, and other things that may impact the writing but are not necessarily repeated in the final text. I factored out a lot of the context into my user-level CLAUDE.md which has helped cut that down a bit.

**saulpw** · 2026-09-18T21:32:41.000Z：

You have to assume that in many situations a human is asking an LLM about the content you've provided, even if they or another human reads some or all of it themselves too. So it's valuable to proactively ask your own LLM in the same way, so you can see what the other person will get out of it. And tune the verbiage until the LLM tells them what you want it to :)

**TomGarden** · 2026-09-18T21:42:11.000Z：

Agreed. Time trap, and even worse imo: creative flow trap. You enter critique mode too early in the process

**imnotr0b0t** · 2026-09-18T22:01:53.000Z：

True, by the way, editing often takes much longer than writing the same text from scratch yourself, I've noticed that too.

**chaostheory** · 2026-09-18T23:29:52.000Z：

I agree and disagree. Yes, it turns into the Ship of Theseus, but I feel it helps jump start things. This was actually the way some writers work I.e. just write fast expecting garbage. Keep molding it like clay until you get what you want.

**GarnetFloride** · 2026-09-19T01:07:23.000Z：

So much of my time right now is completely rebuilding tutorials that the devs had generated because except for steps like open and save its just wrong and it doesn't work and customers are not going to let that slide.

**lubujackson** · 2026-09-19T01:16:25.000Z：

This has started to be an issue at my work with code. Everyone started using the thermo-nuclear-code-quality-review skill and, while it does a great job finding consolidation opportunities and architecturally-weak code, it also continues to expand PRs well beyond their scope until you end up revamping far more than you intended...

**bradishungry** · 2026-09-18T19:07:38.000Z：

No, you need to learn the new field you’re entering enough to write about it. Having incomplete knowledge and writing for others utilizing an llm that you do not know enough to fact check is about the worst way I can think of to use an llm for writing.

**al_borland** · 2026-09-18T19:43:06.000Z：

A person isn’t becoming a master in the new field if the LLM is doing all that for them.New areas are where it is most dangerous to use an LLM, as a person can’t tell when it doesn’t align with their views (because they don’t have any yet), is misleading, or flat out wrong.If I want to know what an LLM thinks, I’ll ask an LLM. If I’m reading a paper from a human, it’s, because I want to know what that human thinks. If they need the LLM to fill in the gaps in their knowledge, then they don’t know enough to write about the topic yet. Doing that work to write something themselves could help move them learn enough to write something that is hopefully worth reading.

**taco_emoji** · 2026-09-18T19:50:55.000Z：

Maybe don't write about something you don't know?

**jscd** · 2026-09-18T21:51:53.000Z：

This is explicitly the problem people notice with LLMs. The text they produce sounds fine only if you are so ignorant of the subject that you can’t properly read it yourself. That’s not a “boon” it’s a flaw.

**brianpan** · 2026-09-18T21:56:38.000Z：

100% disagree. The more you don't know an area, the more LLMs will lead you astray.Explaining difficult topics or summarizing to you is fine. But that's a world of difference from having an LLM write for you. You THINK the LLM is helping you write above your level, but that's because you are not in a position to tell it's bad.

**max__dev** · 2026-09-19T01:30:11.000Z：

A more facetious way to put "don't use LLMs": share your input prompt. The people who don't want to read LLM output won't have to see it, and those who do can enjoy using an LLM the same way the author would've. This actually saves a loss/noise step as the consumers won't need to deploy an llm to summarize the authors llm expanded output.$ chatgpt make this comment more glib

**combobyte** · 2026-09-18T23:04:45.000Z：

Every time I'm presented with AI-generated text I feel like I'm staring into the Uncanny Valley

**maxerickson** · 2026-09-19T00:03:44.000Z：

It's more or less incoherent to pair the statement about those topics with the sentence that follows.Charitably, they can be thinking that it's fine to have LLMs organize information intended for LLMs.

**tenuousemphasis** · 2026-09-18T23:03:18.000Z：

Sure, if you don't mind your fact checker to be confidently wrong often.

**cheesecakegood** · 2026-09-18T23:59:18.000Z：

Personally I think every single medium to long form piece of writing should go through an LLM grammar check at the minimum (they are great at catching stuff like correcting “reign in” to “rein in”, not to mention their/they’re and so on) although I don’t think they generally have the self control to make the corrections themselves without screwing stuff up.I can see being lazy and skipping it, but refusing to use them even for more minimal advice purposes seems crazy to me.

**vova_hn2** · 2026-09-19T10:31:54.000Z：

Great comment, no idea why it was flagged

**semiquaver** · 2026-09-18T20:14:54.000Z：

Yeah, I know people who have the same zero-explanation `git commit -mfix` style that they did pre-AI and am baffled. If you can’t be arsed to explain yourself, let the agent do it. It literally takes less work to tell the agent to commit for you and they will always do better than -mfix. I don’t understand it either other than obstreperous “become ungovernable” attitude.

**this_user** · 2026-09-18T21:36:09.000Z：

I'm not sure that Claude's "Realigned the shape of the load-bearing ownership gate to reduce the blast radius of the design contract; confirmed, not assumed" is more meaningful than "fix".

**aprilthird2021** · 2026-09-18T21:44:31.000Z：

You've gotta be joking. Every AI commit message, summary, and test plan is full of extraneous garbage I didn't need to read (and a lot of it is not understandable)

**randito** · 2026-09-18T23:19:32.000Z：

Disagree. I've seen so many PR slop grenades -- they are essentially unreadable. I'd prefer a paragraph or two human written explanations. I suspect people are just taking the default AI text -- which is way too wordy.

**Terr_** · 2026-09-19T00:58:55.000Z：

Sometimes minimal information is better than extrapolated information, especially when the extrapolation mentally painful to read and has decent probability of being wrong with inaccuracies that waste people's time.Also:1. It's often a premature extrapolation from diffs and tickets which you could probably generate later, at need, and likely with even better results.2. If those commit messages can ever influence future work, then it's just carcinogenic cargo-cult cruft. Pruning outputs (future inputs) is important to prevent weird unwanted drift.

**FooBarWidget** · 2026-09-19T05:08:44.000Z：

I can relate to that. Most human commit messages aren't good because the author can't be bothered to write a good one, or doesn't know what a good message is supposed to be, or is bad at writing.But AI commit messages are still bad. Way too verbose and focused on the wrong level: that of code mechanics. That's just wrong. Messages should focus on the level of intent and design, with the primary purpose being to aid human review. They should include a high level overview of the change, decisions, caveats, information not obvious from reading the diff.So I wrote a skill that captures these principles and allows the agent to even research past related commits and to ask focused questions in order to uncover the intent rather than guessing and writing a bad one.Now the AI writes better commit messages than it used to, and even writes better than most humans (who can't be bothered to write a good one). Not better than a good manual message, but you can't have everything.But sometimes even the good writers are tired or didn't think things through. Being able to compare with the AI's version is still useful.Here is the skill for anyone interested: https://github.com/FooBarWidget/ai-skills-and-principles/blo...Depends on my "documentation principles" skill: https://github.com/FooBarWidget/ai-skills-and-principles/blo...

**hobo123** · 2026-09-19T06:10:02.000Z：

But that's a code review issue. Nobody should get away with shoddy commit messages like that.

**bob1029** · 2026-09-19T07:42:19.000Z：

I am way more interested in the intentions of the author than anything that can be interpolated from the code or token space.

**atmosx** · 2026-09-19T09:59:34.000Z：

An LLM can read the diff and do the summary on the fly. What it cannot do, is explain the reason behind a change. That was always that valuable part of the commit msg. The rest can deducted, ofc it's much easier to read a short list or a descriptive title.

**vova_hn2** · 2026-09-19T10:26:22.000Z：

I think that the idea of generating a commit message based on the content (diff) of the commit is fundamentally wrong.Even before coding harnesses become mainstream, a lot of tools offered to automatically generate commit messages based on the diff (I think JetBrains IDEs started to offer it very early) and I always cringed when I've seen it.The reason why I don't like diff-base commit messages is because they are redundant. If I want an LLM-generated summary of the diff, I can easily generate it myself, there is absolutely no reason to put it in the commit message.What I would like to see in the commit message is some additional context that is not a part of the diff. I don't need to read what has changed, because I can already can see it in the diff (or get an LLM to summarize it for me). But I often do need to understand why this change was made. What were they trying to achieve? That's the important part that is not contained in the diff itself. And this is the part that diff-base commits rarely contain.I think that even something simple like a link to a Jira (or other bugtracker ticket) is much more helpful than diff summary. Maybe instead of "fix" or "update" you could write just a couple of words about what are you trying to fix and why does it need updated. Still better, than a diff-summary.

**codechicago277** · 2026-09-18T22:17:17.000Z：

It’s difficult if not impossible to know where to look for edge cases or performance problems without understanding the code.

**semiquaver** · 2026-09-19T00:21:15.000Z：

Letting agents run wild with a codebase and no humans understanding it is a recipe for disaster across so many axes.You are not a serious person if you recommend that.Check back in a couple years and I’m sure they’ll be there but today’s frontier models 100% absolutely are not ready to fully own a nontrivial production codebase with no human involvement.

**intended** · 2026-09-19T06:51:12.000Z：

Process vs outcomes.If your work has little liability then you can afford to not care beyond “does it work”.If you have to worry about quality and ensuring you don’t get sued, you make sure the process works.If it has to maintainable, you you need the mental model to be present in someone’s head.

**tiborsaas** · 2026-09-19T12:35:55.000Z：

I do check most of agent code, not because I really care about every tiny detail but to catch if it's going to shoot itself (and my project) in the foot. If I only check the result and it's OK, it still doesn't mean that in two features I won't totally blow up the app.I'm a happy little bottleneck, what's wrong with that? How do you even know how to ask it to build stuff for you if you don't understand what foundations are you building on?Writing commit message (aka. what has changed) gives me a sense of control that I know what's happening and I can confidently build the next thing.

**holoduke** · 2026-09-19T06:22:54.000Z：

I would say from march this year.

**RichardChu** · 2026-09-18T14:35:00.000Z：

It might be a joke, but I'm sure there are lots of people who don't perceive it as such. For me, it pulled me out of the article and diluted its advice.

**politician** · 2026-09-19T02:51:27.000Z：

I think your take has more application than writing. I also suspect that Jev-like use cases for LLMs will begin to overtake the generate-all-the-things paradigm in programming, contracts/legal, music.People are beginning to wisen to how to more skillfully deploy generative models.

**in_absentia** · 2026-09-19T15:32:50.000Z：

Right, but neither is an LLM because most of the time, it conflates "helpful" with "sycophantic" by default (i.e., it loves the thesis of your essay even if it's dumb). If you prompt it to be critical, it often defaults to over-the-top nonsense, so it's hard to strike the right balance.A good approach may be to present an LLM with an article without saying its yours, and then have it write a thoughtful polemic. But it's not a very efficient way of doing things.

**r0ze-at-hn** · 2026-09-19T02:18:56.000Z：

"Naturally gifted writer" is a thing. Yes like any skill there is a learning curve, but some folks can climb that curve incredibly fast while others will struggle even with a lifetime of practice.Clearly I am not a gifted writer as my original comment failed to convey this very well. And now I am pondering, maybe next time I should put my comment in an LLM to review it first. This meta lesson is playing out over and over everywhere by anyone writing anything.I am in no way saying LLM writing in general is good, but ignoring the reality of what is happening is silly. For good or bad the not great writers not only will, but are doing things like voice rambling into an LLM as a starting point and editing it from there.

**hobom** · 2026-09-19T08:33:17.000Z：

And the question is whether that output is better than what an LLM can produce. I am not a good writer, so in my case it's not obvious.

**boplicity** · 2026-09-17T23:49:52.000Z：

Not sure. I don't like LLMs inserting itself into human to human communication, as it can shape our thinking in many ways. Delegating this also makes it much harder for a person to become a subject-matter expert, which is a real loss.

**boplicity** · 2026-09-17T23:38:13.000Z：

> What’s preventing the editor from using one of your prompts/tooling and replacing you entirely?Well, they don't have the many other pieces of the business in place that makes this work meaningful. They certainly could try, though. If they succeeded, this aspect wouldn't be what made the difference, though.

**watwut** · 2026-09-18T07:09:52.000Z：

> LLM can produce texts but we as people will not be able to understand anywayLLM generated text oftentimes just do not have the point to be understood. LLM is training you to NOT read, because trying to do close reading of LLM generated text is usually a mistake. There is no deeper there. Either it was correct on the surface things or it is a gibberish.

**yorwba** · 2026-09-18T11:47:09.000Z：

PISA is a statistical measurement tool designed for sensitivity to differences in student performance. So it uses questions that some students are expected to get right and some are expected to get wrong, and places the result on a bell curve fit to a reference population.It's not clear what you mean by "sufficient reading literacy," but I guess it's one of the PISA proficiency levels. Those are simply equally-spaced intervals on the bell curve. For example, level 1c in reading is 2.4 to 3.1 standard deviations below the reference mean and 21% of participants in Iraqi Kurdistan and Lebanon scored at that level. Relative to the baseline, they are definitely close to the bottom. However, even they must've gotten some questions right, or they would've ended up in the "below level 1c" bucket (like 3% in Iraqi Kurdistan and 5% in Lebanon did). (https://www.oecd.org/en/publications/pisa-2025-results-volum... Table I.B1.2a.11)If you wanted to know how many people achieve "sufficient reading literacy," you would need a test specifically designed for measuring it (i.e. not PISA), where people with sufficient ability can be expected to get all questions right. For example, the literacy rate is typically defined via the ability to "read and write a simple statement about everyday life," a test which 99% of adults in wealthy countries pass, 92% in Lebanon and 84% in Iraq: https://ourworldindata.org/grapher/cross-country-literacy-ra...Of course a test that 99% pass just becomes table stakes and boring, whereas PISA with its large differences between individuals is much more exciting, but you shouldn't let that mislead you into thinking that students scoring relatively low on PISA necessarily must be lacking even those table-stakes skills.

**jakeinspace** · 2026-09-17T23:51:34.000Z：

Probably the worst part

**altmanaltman** · 2026-09-19T04:47:03.000Z：

I think with the desert thing, you are getting at what was once described as "aura" of original art work. Things like photography have already made us question things like synthetic art and how it relates to "real art" and I am pretty sure this is how it will go with AI and art in general. I wrote about this in my full human only blog: https://decodingvibes.com/blog/3-hypothetical-paintings-and-...

**seanmcdirmid** · 2026-09-19T06:00:24.000Z：

People have lessened what they read because they can more easily watch a video or listen to a podcast. It’s not like the 1800s where books were the only game in town. And why read an AI written article when you can listen to the AI generated podcast with banter between two fake personalities (yes, this is what I heard when I wanted info about qwen’s newest model on Apple podcast).

**antonvs** · 2026-09-18T15:57:56.000Z：

It’s hard to find good new literature - it may be out there, but it’s hard to find. But there’s lifetimes worth of good older literature, that’s much easier to find, that you haven’t read yet.

**shimman** · 2026-09-18T14:21:39.000Z：

No it really wouldn't. I like the authors Jeff VanderMeer and Peter Watts. They have had multiple interviews where they talk about their peers, who they respect from the past, and who they like in our current age. I have found maybe subsequent authors + journalists to read from these two.Try to think a little more critically here. If you can't trust the opinion of people you supposedly like, already established in their craft, who can you trust?Have no idea why you think this would increase influencer culture, but thanks for telling us all publicly how you interact with social media: in an sloppy uncritical way.My advice for you is to pull the plug and read books that are older than 125 years.

**xpct** · 2026-09-19T03:37:15.000Z：

I think we could agree that everyone already does this up to a point. This is basically just an exploration-exploitation dilemma, where everyone tries to maximize how much value they gain from the things they read, and a lot of people have strategies to pick what material to read.Reading trusted authors is likely to be valuable, but they may devalue over time. We don't know if our chosen authors maximize our value, nor whether exploratory reading does, etc.https://en.wikipedia.org/wiki/Exploration%E2%80%93exploitati...

**matheusmoreira** · 2026-09-18T07:38:25.000Z：

More than the average person, I suppose. For some reason, AI writing isn't as irritating to me as it seems to be for everyone else.I treat it the same way I treat human writing: by speed reading most of the article so I can find the points the author is trying to make and decide whether I should read the entire thing.

**theasisa** · 2026-09-18T11:01:45.000Z：

I guess the answer to this is feeding the LLM generated content to another LLM and telling it to summarise it

**vlfig** · 2026-09-18T08:19:10.000Z：

There is now increased evolutionary pressure for rules protecting scarcity to become norm. Communication media will likely adopt limits on the size and throughput of messages.

**dist-epoch** · 2026-09-18T10:27:02.000Z：

It kind of makes sense that if English is not their first language, the can't review the LLM English output also.However most likely they just don't understand what good communication looks like, LLMs are perfectly capable of turning anything into clear concise communication, in fact an easy tell that something is LLM written is that it's just too precise and clear, humans are much more rambling.

**andrewflnr** · 2026-09-19T03:07:43.000Z：

Yeah, it's phrased like a reductio ad absurdum but it's close to being literally true. It's not technically "copywriters" but their words are "polished" for pleasantness, often with the explicit guidance of consultants, until most of the truth or novelty is gone.

**Zambyte** · 2026-09-18T12:05:17.000Z：

How about Anthropic? I've seen people say it's surprising that their blog isn't written with AI, but I think it's far more likely that it is written with AI; they are just good at reviewing and getting a nice prose out of their models.

**abc123abc123** · 2026-09-18T11:09:12.000Z：

How do you know it is? Most likely we will never know.

**nearbuy** · 2026-09-18T22:48:01.000Z：

In this comment section alone, 5 people have used some variant of that aphorism, and it's used constantly on hn and other sites. They've heard it.

**dist-epoch** · 2026-09-18T10:18:24.000Z：

Selecting between alternatives is also a very valuable skill. Also known as "taste".You are a senior software architect, you "prompt" 10 junior architects to write a software architecture proposal and then pick one which you send the client.Would you say it's worthless, because the senior architect didn't care to write it?There are plenty of industries where "taste" is a real job.Or you think that for some reason prompting a LLM and forwarding it's output after vetting is different than prompting a human and forwarding the output after vetting.

**JimDabell** · 2026-09-18T12:37:01.000Z：

> how can you say that he didn't think it himself?Because the same sentence has been repeated practically word-for-word ad nauseam all over social media for years. What do you think is plausible - that they repeated something that is damn near omnipresent in the discourse, or that they never saw any of the many, many times it has come up and independently came up with the exact same formulation? They are perfectly able to step in and claim that it was their original thought if they want to.

**wkjagt** · 2026-09-18T16:42:31.000Z：

Yeah ok good point. I think my thinking around this was too simplistic.

**grey-area** · 2026-09-18T06:39:02.000Z：

You are erasing yourself in doing this, not improving your writing.If you want to improve your writing, read more.

**gnabgib** · 2026-09-17T23:45:25.000Z：

Recent comments from the simonw account suggest it isn't operated directly by a human anymore /sigh/

**dist-epoch** · 2026-09-18T10:29:10.000Z：

To paraphrase, "if a junior programmer doesn't understand what your code does, it's bad". If Fable doesn't understand, well...

**simonw** · 2026-09-18T11:54:37.000Z：

You don't blind trust them in the fact checking. You check what they point out.

**black_knight** · 2026-09-19T09:55:11.000Z：

I use Fable to give me feedback on things I write. But I discard about 50%, because it often does not have the context and thus tends to favour hedging stuff. Also, it does not always vibe with my writing style.But the 50% I do take into account, improves the text! And, like TFA, I never ask it for concrete text. It only helps me diagnose the issues, I prescribe the medicine!

**maleldil** · 2026-09-18T12:03:16.000Z：

I like the "strong opinions, loosely held" approach myself.

**tptacek** · 2026-09-18T00:31:19.000Z：

Right, I agree: that’s exactly not what I’m recommending.

**caminante** · 2026-09-18T09:28:03.000Z：

I figured that's what you meant and agree the phrasing is over-speak.To your comment, I wasn't aware of the eye rolling meta for the phrase [0]. I hadn't seen it overused to the extent people are claiming.[0] https://www.reddit.com/r/ClaudeAI/comments/1upxk9r/loadbeari...

**dist-epoch** · 2026-09-18T10:34:59.000Z：

Given that he says "never use a LLM suggested word", and given he's a sophisticated writer, it's clearly a joke.Pangram 4 says it's 100% human written, including the "load-bearing" sentence.

**tptacek** · 2026-09-18T23:19:21.000Z：

People keep writing about "style", as if I'm asking models "hey, how do you like this, and how could we make it more stylish". That's not at all what I'm asking.I have personally decided, in advance, that one goal I have in writing is improved clarity. The model didn't tell me to do that; Joseph Williams did, decades ago.In the service of that goal, I've written down a proofreading checklist. It includes things like "look for overused words", "eliminate throat-clearing filler like 'it's important to remember that'", "make sure every paragraph has a clear topic sentence", "make sure my real verbs aren't buried inside nouns". Stuff like that.Those are stylistic choices, I suppose, but they're mostly the difference between bad style and a whole universe of good styles.More importantly: they're technical. They're not really judgement calls. The subject of a sentence either is or is not a character taking actions in the story you're trying to tell. It is better, almost always, if the subject is a character, and not accidentally some random piece of the scenery of your point.Models are very good at flagging these things. Humans are too, but they're not as thorough.Many people on this thread have suggested that having a model flag these kinds of issues bleaches out personal style. I don't think that's true; what I think is happening is that they missed the point I'm making, and assumed that I was advocating for having a model make broad subjective calls about my writing.

**partyficial** · 2026-09-18T19:46:53.000Z：

the author can ask the same question - why should I write something if you're just going to use a LLM to summarize it ?This is an unnecessary argument both ways. Whether you use a LLM or write it yourself or read it yourself (and then comment on it), you're putting your signature beneath it. I don't care whether you use your natural brain or an artifical brain (LLM)

**utopiah** · 2026-09-18T14:45:30.000Z：

It is not the same yet it requires reading which in turns requires interpretability, trying to make sense of what was read within a very specific, maybe explicit context, e.g. specifications, and that can be optimized for an audience, or not.For example the code I would write for somebody who just started to learn programming will not be the same as the code who is an expert even though both will pass the specifications.Consequently taking into account who (if anyone) will actually review, and thus read, the code changes the code itself.

**SamInTheShell** · 2026-09-18T17:06:06.000Z：

If someone sends me AI slop, they're getting chewed out and told I'm not doing it and I'll even tell my boss "no" and why. If I got fired over something like that, then it tells me everything I need to know about company and the leadership's priorities. I'll die on that hill.To be completely fair though, I'm against the behaviors in information transfer I've been seeing. I've pass along AI generated runbooks, but they look nothing like the default outputs of these models. It's because I took time to apply all the writing knowledge I like to see in my curation. If people are doing this, I can't even tell it's AI writing. My work is done in minutes instead of deciphering so BS pseudo language they developed in their AI workspace (people really need to turn off those memory features).---Edit: Also if I'm the guy receiving a security report and it's AI generated and poorly formatted, I'm failing you short of producing something for a human to parse. Simple as that.

**aprilthird2021** · 2026-09-18T21:40:39.000Z：

Having the style guide and proofreading it and linking it is more effort than the lazy slopulists want to put in, so your writing will reach far better than theirs will

**streetfighter64** · 2026-09-18T23:07:27.000Z：

Sorry if this comes off as critical, but are you seriously doing that? I can't imagine optimizing my writing for people choosing to mangle it through a LLM rather than for the people reading it as-is.Also the word "verbiage" ticks me off as a LLM-ism on the level of "delve" or "smoking gun". Are its users aware that in addition to its usage as somewhat of a synonym of "idiolect", it more commonly means "a profusion of words usually of little or obscure content", i.e. slop?

**strix_varius** · 2026-09-19T19:14:45.000Z：

hey thanks for mentioning that skill, I hadn't heard of it before but I just ran it on a non trivial codebase I've been planning to refactor and it did a great job.I don't use a lot of "skills" so if there are others you've started using frequently I'd be curious to learn about them.

**aprilthird2021** · 2026-09-18T21:42:36.000Z：

But I want everything and want to do no effort for it

**robwwilliams** · 2026-09-19T17:45:25.000Z：

Actually I am in a very good position to tell. And who said “write for you”? How about “write with you as a collaborator?”.Writing is a form of thinking and writing with an LLM makes the argumentation, discussion, and progress toward goals faster and often better in my situation.I am stating an opinion based on 2.5 years of intense interactions and writing with Anthropic models on a difficult topic related to asynchronous computational systems.Background: I am a neuroscientist and behavioral biologist (45 years of experience) who understands the biology of behaviors fairly well but I need to translate this background into hardware architectures that get beyond current asynchronous system (e.g., this recent neuromorphic paper in Nature Communication by Li et al., 2025, A deterministic neuromorphic architecture, doi.org/10.1038.s41467-025-65268-z).Working AND writing with Opus and now Fable has been a blessing of sorts.

**tptacek** · 2026-09-18T23:25:50.000Z：

Which is exactly what the post says, and why I say "do not accept a single word suggested by an LLM".

**qarl** · 2026-09-18T23:16:42.000Z：

You mean hallucinations?Hallucinations don't really work that way. They happen when you ask an LLM to generate new material. Not so much reviewing existing material.But there's always the "ask a second LLM to get two opinions" technique which gets you pretty close to error free.And... now that I think of it... even if it was terrible and missed 50% of the errors... wouldn't that still be better than using no LLM which catches 0% of the errors?

**0x696C6961** · 2026-09-18T23:58:01.000Z：

The long-ass Claude commit messages & PR descriptions suck. But they are 100% better than "fix".

**winrid** · 2026-09-19T02:19:17.000Z：

"fix stupid shit" is all you need :)

**skissane** · 2026-09-19T04:23:27.000Z：

> I'm not sure that Claude's "Realigned the shape of the load-bearing ownership gate to reduce the blast radius of the design contract; confirmed, not assumed" is more meaningful than "fix".For PR/commit descriptions, I mainly use Claude Sonnet 4.5. It isn’t perfect, but it produces significantly less of this weird gibberish than 5.x models or even Opus 4.x doI also use an iterative process in which it writes the description, I read it, and then either manually edit it or ask it to make changes

**ben_w** · 2026-09-19T09:57:53.000Z：

Could go either way, TBH.So long as there are in fact those things, and so long as it didn't sneak something else in there at the same time, it being just on the knife-edge between sense and word-salad is better than "fix".Buuuuuut far to often it says it fixed a bug I reported, when it only touched one superficial failure mode rather than the root cause.Yesterday's issue: Why is zoom/pan randomly failing? It told me it was because it was applying a transformation matrix with every input and sometimes JavaScript gave it a non-invertible matrix (why?) which then propagated NaNs everywhere and you can't update a matrix filled with non-numbers.Why was it doing that in the first place? Seems to be because it's too motivated to perform quick wins and not sufficiently motivated to do good engineering.Good thing this was just a game editor. Spiky intelligence: superhuman on some dimensions, total noob on others.

**TeMPOraL** · 2026-09-19T13:57:23.000Z：

It is, because it includes the key words such as "ownership gate" and perhaps others, which makes it infinitely more informative than just "fix", by pointing at what was in scope, and what wasn't.

**LeafItAlone** · 2026-09-19T11:28:47.000Z：

Fix your harness. Provide rules, format, and good examples.You probably had those for the humans in your team for when new hurts join, right? Just direct your LLMs to them and you’ll have a much better experience.Just like you can’t expect a new junior dev to know what to do without direction, the same applies with LLMs.

**vova_hn2** · 2026-09-19T10:28:02.000Z：

I don't think that many teams review commit messages as a part of code review. At least, I've never seen it "in the wild".

**semiquaver** · 2026-09-19T13:44:32.000Z：

Not all workplaces are high functioning in the way you imagine. Until recently a shocking amount of software development did not use source control.

**vova_hn2** · 2026-09-19T10:29:07.000Z：

Exactly! If I want a summary of the code, I can easily generate it myself.

**LeafItAlone** · 2026-09-19T11:31:46.000Z：

LLMs can provide the intentions of the code they write. To say they can’t is saying that they can’t fix bugs, which they very obviously can do effectively.
So, just tell them to write the intention in the way you want it.
If you are implicitly providing the direction in the prompt, make that explicit - you then it will have the context for the change while working and for the commit message and you’ll likely get a higher quality output.

**miki123211** · 2026-09-19T10:56:00.000Z：

This is why, if you have the agent generate the commit message at all, it has to be the same agent that wrote the code, in the same session.I usually have it lead with a paragraph or two of context on why the change was made (though I often use it as just a tool to turn my rambling on that question into proper English), followed by a couple paragraphs of "abstract" explaining the change (because an LLM-generated summary reviewed by the person who made the commit is better than something which the person reading can get themselves).

**andrewflnr** · 2026-09-19T18:27:21.000Z：

Right, I'm broadly not a fan of LLMs either. But I understand the use case here. If you can't get an actual human to look at your writing, an LLM used carefully could be better than nothing.

**altmanaltman** · 2026-09-19T08:01:04.000Z：

Yes, true, but in the 1800s, literacy rates were extremely low as well. Most people didn't read then either. By the time literacy improved, we already had competing media like radio, television, etc. But books still won because they were a different form of media. And most "popular" books since the invention of the printing press have usually been garbage, like guides on how to burn witches properly, etc. It wasn't like people were reading Dostoevsky in masses then and don't do it now. It was always a small minority of people that cared about actual literature.I think it's also more about active vrs passive consumption these days. People these days consume media mostly passively (watch whatever is on a streaming service, hear a podcast/audiobook while driving, let AI summarize an article instead of reading it), whereas that wasn't really possible previously (go to a theater to watch a movie, actually read stuff with attention, etc.).So yes, people might be reading less, but I don't think it's some massive fall in literacy as people make it out to be. We're much more busy and don't have time to actually sit down and actively focus on media consumption these days as well (assuming you're employed in a somewhat capitalism-based system).

**CuriouslyC** · 2026-09-18T14:36:08.000Z：

For everyone that you consider "good" there are at least a dozen people who are equally "good" but without the social proof. What you describe played out exactly in music and art pre-AI. The record exec and the gallery owner were the people you "trusted" who king-made and gate-kept what we saw based on what they thought was most marketable.> Have no idea why you think this would increase influencer culture, but thanks for telling us all publicly how you interact with social media: in an sloppy uncritical way.This is a personal attack that is unsubstantiated by what I wrote, read the guidelines and follow them or go elsewhere.

**Terr_** · 2026-09-19T02:40:32.000Z：

How does that matter? Parent-poster asked about sincerity of thought, not originality.If the spouses-to-be at a marriage ceremony say "I do", would you leap up from the audience to denounce them as frauds because obviously they heard the vow-formula before a hundred times? Hopefully not, and not only for reasons of decorum.In contrast, most of the LLM slop I deal with from coworkers involve statements that--while less formulaic--are ones they can't even recall saying and are unwilling to defend when questioned.

**unsungNovelty** · 2026-09-18T10:49:04.000Z：

> Would you say it's worthless, because the senior architect didn't care to write it?Lemme ask you a counter question, the senior architect writes the proposal and the junior writes it. Which one do you think client likes better?Moreover, Your focus is on the end-result. Sure, in corporate environment, most people don't care about what they do as long as the end results checks some boxes. That wasn't the discussion here. The discussion is about writing and reading in general. Whether it's worth my time or not if you don't mean (forget mean, don't even remember) what you wrote.Also, in your own example, the client don't care as well. As long the client's checks all the boxes his/her/their manager said should satisfy. Nobody really gives a damn about the quality.Also, are you saying you'll be fine paying for Financial Times, WSJ and NYTimes KNOWING all they do is shove the story through an LLM? Neither will there be a soul, nor will there be any material effect on people who reads it.> Or you think that for some reason prompting a LLM and forwarding it's output after vetting is different than prompting a human and forwarding the output after vetting.There is difference no? I forward the output to get good feedback and correction from someone BETTER. And there is a process involved in it which showcases the "TASTE" you mentioned from the person whom you are forwarding your output to be vetted and that person comes up to you with feedback. And guess what? You learn from the person's feedback. You don't go back again and again forever to learn the same thing. That's exactly what am trying to point out.

**dofm** · 2026-09-18T13:22:17.000Z：

> What do you think is plausible - that they repeated something that is damn near omnipresent in the discourse, or that they never saw any of the many, many times it has come up and independently came up with the exact same formulation?Both are fully possible.We're talking about a simple sentence that sounds a lot like something a primary school teacher or parent of young children would say. "If you won't do/don't/haven't done X, why should I Y?" is very normal moral/ethical phrasing.I suppose I heard someone say it before I spelled it out in that way, but I am pretty confident I would ultimately have used a sufficiently similar expression, because I have been on the receiving end of the problem.And that is putting aside the communicative compression of aphorisms. People don't use shared aphorisms to avoid ever doing the thinking themselves; they use them to shorthand more complex arguments for a listener who has already heard them. They are shared macros for agreed concepts. (Using them correctly requires having done the thinking they package up at least once).

**tptacek** · 2026-09-18T12:27:01.000Z：

No, you're wrong about this. One obvious reason why: I'd have gotten rid of those "justs" myself before models were available; it just would have taken me longer.

**simonw** · 2026-09-17T23:49:08.000Z：

What?

**geraneum** · 2026-09-18T16:18:58.000Z：

Did you just paraphrase yourself in quotation marks?

**Retr0id** · 2026-09-18T00:32:47.000Z：

You are specifically recommending asking the model which of two versions is better (the quote in my top-level comment).We both agree that they are poor "make it better" machines, but I also believe they are bad A/B testers and I'm using the former to demonstrate the latter.

**andrew_lettuce** · 2026-09-18T20:47:08.000Z：

Because it's an asymmetric relationship? If you write something it can be consumed with value at many different levels, and an llm summary is valid. If we could trust llms to get the details right, creation of technical content would also be valid, but for now IME the editing and proof reading required outweighs any gains.

**0c3ca83** · 2026-09-18T21:09:46.000Z：

> the author can ask the same question - why should I write something if you're just going to use a LLM to summarize it ?I wouldn't. LLMs don't summarize things very well. If you don't care if someone wrote it, and you don't plan to read it, why are you even here?

**aprilthird2021** · 2026-09-18T21:43:13.000Z：

I don't care what you use. But if it reads or sounds like slop, I'm tuning out

**hannasanarion** · 2026-09-18T16:42:02.000Z：

Who said interpretability wasn't necessary?Manuals, laws, and dictionaries are not designed to be read, but they are designed to be interpreted. In fact interpretability is what they maximize for. And interpretability isn't an absolute value, it is relative to an audience, this is why household equipment often comes with separate owners, installers, and service manuals, and why Webster publishes Elementary, Collegiate, International, and Mass-Market versions of its Dictionary.Documents that are "meant for human consumption" in the way the top comment intended generally don't optimize for interpretability like code, manuals, and dictionaries do. Novels, letters, emails, internet comments, blogs, articles, nonfiction books, etc often forgo interpretaiblity for practical, expressive, or rhetorical effect. The best moments of these is even when they are confusing on purpose, because imprecise language is a gateway to deeper levels of meaning through fourth-wall breaks, metaphor, analogy, and humor. (all things that LLMs are notoriously bad at and don't seem to be improving on over the years)Those other types of writing are intended to be read in full, every word, end-to-end, in order to educate, entertain, inform, or influence the reader who, and i think this is the critical part, does not drive the experience.When I'm reading a news article, and you realize that you're reading the voice of chatgpt, I'm annoyed because it means that i've been strung along by a stupid machine that somebody else handed me off to to keep me occupied.When I'm reading code, and I notice that it seems AI written for whatever reason, I might then choose to apply more scrutiny, maybe I try to suss out what the prompter intended to happen, so that I can validate whether that actually happened and if it was accomplished in an optimal way. But it's not insulting in the same way, because I'm still in the driver's seat of the experience, deciding on my own which parts to read and which parts to ignore as irrelevant to my investigation, because the only thing I want to get out of it an understanding of a part of the mechanical system that the code creates.

**alchemism** · 2026-09-18T17:55:41.000Z：

If a security report is written for any particular human at all, I’d consider it to be a failure as an enterprise policy document. It should be written for The System, not for the boss; and LLMs are perfect for producing ritual boilerplate.

**antonvs** · 2026-09-18T19:42:27.000Z：

> Also if I'm the guy receiving a security report and it's AI generated and poorly formatted, I'm failing you short of producing something for a human to parse. Simple as that.It’s clear that you’ve never worked for a compliance company and probably have never been involved in a compliance project. As such, you don’t have the context needed to participate usefully in this discussion.

**skydhash** · 2026-09-18T23:11:38.000Z：

I was reading the manual of a car head unit, and it was better quality than 99% of AI flavored content.

**saulpw** · 2026-09-18T23:20:44.000Z：

I wrote a contract proposal a few months ago and I absolutely did a few rounds with an LLM to get the result I wanted. Anyone applying for a job should be doing this with their cover letters. You know that HR has a pipeline set up with a prompt like "here's the job description, here's the candidate's info, rate the candidate on a scale from 1-10" so you can do the same and learn how to boost your own signal. I have zero qualms about doing this.As for "verbiage", I guess that's too bad, I'm going to continue using it anyway. Interesting factoid about the word though. I will say that "utilize" is one of my pet peeves (99% of the time the word you actually want is "use") and I've excised it from my spoken vocabulary, but I like(d) how verbiage rhymes with foliage so I'm more reticent to give that one up.

**kasey_junk** · 2026-09-19T01:46:27.000Z：

This is the real crime of llms on writing. They’ve taken perfectly reasonable verbal ticks (the one I miss being able to use is scaffolding) and caused the audience to rebel against them en masse. Verbiage is a great word. I refuse to give it up. It’s load bearing even.

**ericbarrett** · 2026-09-19T00:42:44.000Z：

Mildly disagree. "Fix" is exasperating but immediately tells me I need to look at the diff. With unconstrained Claude spew, I need to wade through three levels of deep fried LLM-speak before realizing...I need to look at the diff

**burnished** · 2026-09-19T04:35:31.000Z：

How? One looks like someone cared about it and the other can be dismissed at a glance

**my-next-account** · 2026-09-19T04:52:09.000Z：

I use Astra at Very High, and shit is still bad. It doesn't actually understand anything, so it often says things which are clearly not needed to be stated. Recently, I've learned that I have very high standards for these things. For example, "fixes" as a commit msg just is NOT acceptable and would never fly where I work.

**skydhash** · 2026-09-19T12:21:28.000Z：

The issue is with the people sending code for reviews, not people reading the slop commit message.

**hobo123** · 2026-09-19T13:28:53.000Z：

True, is mostly about the code being merged, but when reviewing a PR they might suggest that the dev write better commit messages in the future.

**black_knight** · 2026-09-19T09:06:20.000Z：

> Yes, true, but in the 1800s, literacy rates were extremely low as well. Most people didn't read then either.False, at least from an American or Northern European perspective.In the 1800s reading was an extremely popular activity. Not something restricted to a few. Printing press had been around for ages and the majority of the population read.

**nearbuy** · 2026-09-19T05:41:05.000Z：

JimDabell said they didn't come up with that thought themselves. They never implied the poster didn't mean it. sm-silversight responded, "How do you know it's not his/her thought?" You can reasonably interpret them as asking how we know they didn't come up with that thought independently.If we go with your interpretation instead, then sm-silversight simply misread the comment they replied to and their post doesn't follow. No one doubted OP felt sincere about not wanting to read AI.

**dist-epoch** · 2026-09-18T11:20:41.000Z：

> Neither will there be a soulMaybe I just want the news.> nor will there be any material effect on people who reads it.This is a ridiculous thing to say - "because the Weather app in my phone is 100% automated with no human "soul" in it, I will not take it into account into how should I dress today"> the client don't care as wellThis applies here too. If you didn't pay for author's output, are not a subscriber to their Substack, why should they bother to hand craft you a quality human written post?> If you didn't bother to write it, I won't bother to read itSo the argument is that effort should be somehow matched. Ok, let's go with that. It's well know that writing something takes 10x more effort than reading it. So if we use the market argument, if it takes you 10 min to read a blog post, the author should spend 1 min writing it, because writing is 10x more intense, and this is only possible with a LLM. You might say "but there is one author, and 1000 readers". That gets us back to the paying argument.

**JimDabell** · 2026-09-18T13:27:16.000Z：

I don’t care what’s possible, I asked what was plausible.Do you think that they came up with it independently? If you aren’t willing to say you believe this, you are just asking me to waste my time arguing with a phantom opinion nobody holds.“Just do it” is an incredibly common, generic phrase, but if a new shoe manufacturer chose it as their slogan, it isn’t plausible that they came up with it independently of Nike.

**mtlynch** · 2026-09-19T00:06:24.000Z：

Disappointing. That's exactly what a robot would say.

**tptacek** · 2026-09-18T00:38:01.000Z：

You are writing both paragraphs. You’re specifically not asking a model to make a better paragraph. That would be a load-bearing debacle.

**partyficial** · 2026-09-19T08:02:25.000Z：

> you don't plan to read itNot in full. I plan to read the LLM's summary. Most people could benefit from brevity.author : writes the summary (prompt). LLM expands it to article.reader : LLM summarizes the article. reader reads it.both author and reader are free to use, or not use LLM. I don't see the big deal here.

**skydhash** · 2026-09-18T23:32:47.000Z：

> The best moments of these is even when they are confusing on purpose, because imprecise language is a gateway to deeper levels of meaning through fourth-wall breaks, metaphor, analogy, and humor.I don't agree. Because those metaphors and other word plays reach deep into the human mind (at least for the purported audience), while most technical writing try to be more explicit.Here is the introduction for Laravel Socialite In addition to typical, form based authentication, Laravel also provides a simple, convenient way to authenticate with OAuth providers using Laravel Socialite. Socialite currently supports authentication via Facebook, X, LinkedIn, Google, GitHub, GitLab, Bitbucket, and Slack.

And this is the marketing blug of Shadows of the Gods by John Gwyne A century has passed since the gods fought and drove themselves to extinction. Now only their bones remain, promising great power to those brave enough to seek them out. 
 As whispers of war echo across the land of Vigrid, fate follows in the footsteps of three warriors: a huntress on a dangerous quest, a noblewoman pursuing battle fame, and a thrall seeking vengeance among the mercenaries known as the Bloodsworn. 
 All three will shape the fate of the world as it once more falls under the shadow of the gods.

One is direct, with not a lot of imagery, but rather use specific concepts which has precise meaning. The other is just as clear, but use concepts that ties to bigger ones. They are not imprecise, they just let you be aware there's a bigger canvas than the literal interpretation.

**SamInTheShell** · 2026-09-18T18:21:11.000Z：

We're probably just going to disagree here. These LLMs are built to serve humans. They either need to make the system transparent for the operator or be limited in use to tasks that can be proven in whole (with code that can't be revised without human approval).Should you think it is wise to trust the machine that can't differentiate subject matters in a chat styled context, you have fun with that fluster cluck when it blows up.Like Fable is highly useful, but it's really bad at keeping it's responses straight.In fact, that "it's not X it is Y" pattern always crops up when it reasoned about the idea of X and I never fed it that. It's literally doing that because it can't predict that I'm a different entity despite it being able to say I am a different entity.Edit: Clarification by removal of incomplete sentence fragment. Edit2: Clarification on the "proven in whole" thing.

**SamInTheShell** · 2026-09-18T20:20:04.000Z：

Pure conjecture on your part.

**streetfighter64** · 2026-09-18T23:24:53.000Z：

Fair enough, cover letters and contract proposals are more marketing than actual information, so that's fair game I suppose. Good trick. I wouldn't use it in something meant to transmit actual information though, like a manual or something.

**DrewADesign** · 2026-09-19T01:47:05.000Z：

> Anyone applying for a job should be doing this with their cover lettersSadly people lost the skill to write a standard form concise 3-paragraphs-of-3-sentences cover letter even before keyword-based ATS initiated the beginning of the end. It wasn’t supposed to be a summary of a CV and an essay about your lifelong passion for automated ad-bidding quality checks or some other shit employers delude themselves into believing someone might organically be really into.

**atif089** · 2026-09-19T02:09:41.000Z：

This.

**bitwize** · 2026-09-19T03:05:08.000Z：

"Deep fried" is the perfect analogy. LLMs have been trained on themselves so many times that their output is the linguistic equivalent of many rounds of JPEG compression.

**danielbln** · 2026-09-19T15:11:35.000Z：

I don't get this thread. Just tell the agent to use conventional commit messages and to keep it nice and tight. Are you all just raw dogging agent output with no alignment/conventions?

**manmal** · 2026-09-19T05:11:30.000Z：

Astra is such a mixed bag. It makes some amazing reviews and sometimes architecture suggestions that I like. But it’s also lazy and will just make up things.

**rrr_oh_man** · 2026-09-19T09:37:38.000Z：

Very high does not improve the model, fyi.

**jester997** · 2026-09-19T17:54:30.000Z：

Honestly you probably want a model that has only been trained on language and literature. Nothing from online discourse.And even then… writing is personal expression. Here people are talking about commit messages. That’s fine but AI doing writing for anyone and I WILL NOT READ IT unless it’s literally basic tech manual.We read to hear and engage with people’s thoughts. If someone outsources that to AI then they should be shunned.

**altmanaltman** · 2026-09-19T10:46:00.000Z：

If by majority of the population, you mean no women, no slaves, then yes, sure. And even from an American or NE perspective, you're still overestimating its popularity.Literacy rates in the 1800s across different regions in Western Europe: https://brewminate.com/the-growth-of-literacy-in-western-eur...> According to data compiled by Our World in Data and the World Bank, the literacy rate of the world's population from secondary school age onward was only 12 percent in 1820 - around one person in ten. In 1900, it still barely exceeded 20 percent. From the 1950s on, world literacy began to take off, hitting 42 percent in 1960 and 70 percent in 1983.https://www.weforum.org/stories/education-and-skills/reading...

**dofm** · 2026-09-18T13:32:04.000Z：

> I don’t care what’s possible, I asked what was plausible.OK then. BOTH ARE PLAUSIBLE. Clear enough?It's absolutely not up to me to decide whether they came up with it independently.But then again, it isn't up to you, Jim.> If you aren’t willing to say you believe this, you are just asking me to waste my time arguing with a phantom opinion nobody holds.This is the weirdest thing to put in a comment you could simply not have made. If your time is so valuable why are you here commenting on HN?Again: aphorisms have value regardless of how many times they are used. People can use them without you having the right to demand proof they thought them up for themselves like some prep school debate bully picking on a younger child.

**Retr0id** · 2026-09-18T00:43:07.000Z：

It doesn't matter who writes what, what matters is that LLMs have a preference for LLM-shaped writing. By A/B testing against an LLMs opinion, you are optimizing in the direction of LLM prose even if the LLM never writes any of the prose itself.

**0c3ca83** · 2026-09-19T15:18:04.000Z：

Seems stupid.

**senderista** · 2026-09-19T17:54:12.000Z：

hence adversarial review

**my-next-account** · 2026-09-19T11:56:54.000Z：

Wat, what am I paying for then?

**black_knight** · 2026-09-19T13:48:00.000Z：

As I said. If you look not at the entire world, but say Northern Europe, reading literacy (a different measure from the literacy discussed in many modern sources which includes writing literacy) was almost universal by the late 1800s.For instance, in Sweden, to cherrypick a stat, in 1875 only 1% of military recruits were found unable to read [1].We really must stop thinking that people of yestertimes where so much inferior to people today. Yes, there were differences between men and women, but this was also starting to change.[1]: https://history.state.gov/historicaldocuments/frus1876/d308

**JimDabell** · 2026-09-18T14:06:34.000Z：

> > If you aren’t willing to say you believe this, you are just asking me to waste my time arguing with a phantom opinion nobody holds.> This is the weirdest thing to put in a comment you could simply not have made. If your time is so valuable why are you here commenting on HN?It’s basic intellectual honesty. If nobody believes that they came up with it independently, putting it forward as if it’s a real argument is just a form of trolling. If I don’t believe it, you don’t believe it, and even the person who posted it doesn’t claim it’s original, you’re just baiting me to respond to a position nobody holds.Do you believe that they actually came up with it independently? If you do actually believe this, then a discussion is not a waste of time. But if you aren’t willing to claim that position, it’s pointless me arguing against it because it’s just you deliberately wasting my time on something you don’t believe.> aphorisms have value regardless of how many times they are used.This is a cornerstone of the point I was making. You’re literally supporting the point I was making.

**ameliaquining** · 2026-09-18T01:23:34.000Z：

LLM style is not literally anticorrelated with quality. There are some things that they tend to do poorly, but you're not going to do those because you're writing the text yourself. If you have it judge your writing, and are careful to avoid the failure modes that the post goes into, it can be helpful by serving as a competent editor that doesn't share your blind spots.

**mitxela** · 2026-09-19T13:33:47.000Z：

Dario's yacht and FOMO.

**rrr_oh_man** · 2026-09-19T14:25:50.000Z：

Arguably, your LLM provider might be paying you, in a sense

**dofm** · 2026-09-18T14:17:50.000Z：

Lordy.

**oblio** · 2026-09-19T17:20:45.000Z：

As OpenAI's IPO troubles seem to indicate, that's an OpenAI skill issue.

## 关联链接

- https://sockpuppet.org/blog/2026/09/17/how-to-write-with-an-llm/
