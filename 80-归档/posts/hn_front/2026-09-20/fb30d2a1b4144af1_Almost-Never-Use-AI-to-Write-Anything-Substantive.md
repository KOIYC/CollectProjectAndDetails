---
type: "corpus"
item_id: "fb30d2a1b4144af1"
title: "Almost Never Use AI to Write Anything Substantive"
source: "hn_front"
source_name: "HN 首页（非 Show HN）"
url: "https://news.ycombinator.com/item?id=49767937"
project_url: "https://erichgrunewald.substack.com/p/why-you-should-almost-never-use-ai"
author: "erwald"
published_at: "2026-09-19T16:35:24Z"
captured_at: "2026-09-20T03:41:55+08:00"
lang: "en"
kind: "post"
tags:
  - 语料
  - hn_front
  - author_erwald
  - story_49767937
  - front_page
metrics: {"points": 93, "comments": 50, "engagement_velocity": 93}
comments_count: 50
comments_total: 50
discovered_via: "hn:front_page:2d"
archived: true
archived_at: "2026-09-20T09:21:31+08:00"
archive_reason: "渠道停用"
---

# Almost Never Use AI to Write Anything Substantive

- **来源**：HN 首页（非 Show HN）　|　**kind**：post
- **原帖**：https://news.ycombinator.com/item?id=49767937
- **指标**：点赞=93 · 评论=50 · engagement_velocity=93
- **作者**：erwald　|　**发布**：2026-09-19T16:35:24Z
- **项目链接**：https://erichgrunewald.substack.com/p/why-you-should-almost-never-use-ai
- **采集**：2026-09-20T03:41:55+08:00　|　**id**：`fb30d2a1b4144af1`

## 正文

Published: 2026-08-06
Author: Erich Grunewald

Why I Think You Should Almost Never Use AI to Write Anything Substantive

### A plea.

Erich Grunewald

Aug 06, 2026

I think you should almost never use AI to write -- that is, to do the thing you’re doing when you type words on a page -- whether for a blog post, a research report, a memo, a thoughtful email, a novel, or any other text aimed at conveying an idea, an argument, an analysis, or other substantive 1 thoughts. I think this is the case even when you give the AI very detailed bullet points, dictated thoughts, or other context, and even when you edit the AI-written text. 2

I think so because (1) the writing process is an essential part of the thinking process, (2) AI writing is vague and wrong in hard-to-notice ways, and (3) writing with AI (and not labeling it as such) is rude and misleading. I’ll explain these points in more detail below, but first, a few throat clearings.

As you may know, I’m not anti-AI. I think it makes a lot of sense to use AI for many other parts of the research and writing processes, such as transcribing audio, analyzing data, searching for information, brainstorming, and giving feedback on drafts. I also think using AI for line and copy editing, or for rewriting a passage to make it clearer or tighter, is fine, as long as all the edits are deliberately accepted or rejected by a human. It’s just using AI to write text that I’m against. 3

And yes, there are various advantages to using AI for writing. For example, it’s less effortful and much faster than writing yourself. So the disadvantages of using AI for writing need to be substantial for it to be bad overall. As you may have guessed by now, I think they are.

And finally, I’m just making a claim about the AI models that exist now and that I expect to exist in the near future. There will likely exist models at some point that are good enough that it makes sense to delegate the writing to them (although at that point it might make more sense to delegate the entire research or writing process end-to-end, since in addition to the writing they will also need to be doing all or most of the thinking).

The Writing Process Is the Thinking Process

The point of doing any kind of research is to form accurate beliefs about important questions, which you can then communicate to an audience. One of the best ways of doing that is in my opinion by writing.

Paul Graham has written 4 that

> Writing about something, even something you know well, usually shows you that you didn’t know it as well as you thought. Putting ideas into words is a severe test. [...] Half the ideas that end up in an essay will be ones you thought of while you were writing it. Indeed, that’s why I write them.

On an episode of Patrick McKenzie’s podcast, Clara Collier says that

> When I am writing something, something substantive, there’s no part of that writing process in which I am not thinking and changing my mind. Everything from the outline to turning it into text to just the sentence. Often I’ll have an experience where I’m trying to turn an outline into a finished product, and I’m playing with a transition, and it’s not working, and I realize, oh, the reason this transition isn’t working is because actually these two points should not be juxtaposed. The thing that I’m trying to do here is wrong. And if I feed the outline into an LLM, it is not going to stop and consider maybe the outline is bad. [...]

Patrick replies:

> I absolutely agree that the writing process is the thinking process, and I think we now have empirical demonstration of this, because you make a machine that does writing and thinking just pops out as a side effect.
> 
> But when writing a multi-page piece, even if you have a strong thesis, the act of forcing yourself to write that down into sentences and paragraphs to structure the argument will show you where the holes are in the argument. It will show you where your research process has been inadequate. It will surface things like: oh, actually, there is something that is contradictory to the thing that I want to say. And, being a reasonably ethical person, I think I will acknowledge that there are counterarguments, or have to add that the full claimable conclusion is less than the one that I would, quote-unquote, “like to write”.

I basically agree with these takes. When I write something, I must first know what I want to say, i.e., I must think about evidence and arguments and arrive at some beliefs. So writing forces me to do those things, which are necessary for any writing or research project. For any such project, someone has to have the entire thing in their head -- all the bits of evidence, considerations, arguments, and how these fit together. Writing with AI makes it easier to avoid the necessary thinking.

AI Writing Is Vague and Wrong in Hard-to-Notice Ways

When I write something, I make a lot of small decisions about specific wording and phrasing. Together, these small decisions contribute to the overall clarity and correctness of the text.

For example, if I ask Claude Fable 5 to “write a short paragraph introducing the problem of AI chip smuggling”, a topic that’s been written about and reported on extensively, it outputs:

> Since October 2022, the United States has restricted exports of advanced AI chips to China, aiming to slow Chinese progress at the frontier of AI. But export controls are only as strong as their enforcement, and AI chips are compact, extraordinarily valuable, and sold through sprawling global supply chains — properties that make them attractive and feasible to smuggle. Diversion networks route controlled GPUs through intermediaries in places like Singapore, Malaysia, and the UAE, using shell companies and falsified paperwork to move them into China. Estimates of the scale vary widely, from tens of thousands to perhaps more than a hundred thousand high-end chips per year, and even the lower end represents enough compute to matter for training and deploying capable AI systems. Meanwhile, the Bureau of Industry and Security, tasked with policing a multi-hundred-billion-dollar trade, operates with a budget and headcount better suited to a far smaller problem. Chip smuggling thus threatens to quietly hollow out one of the central pillars of US AI policy.

That’s not terrible, and perhaps even quite reasonable, but is that how I would write it? No, in fact, Claude made a lot of choices that I find subtly wrong or bad:

- Claude writes that “export controls are only as strong as enforcement”, but what does this mean? It either says something obvious (of course policies that are not enforced or poorly enforced are less effective) or nothing at all. 5
- Claude writes that AI chips are “compact”, which is true, but what is usually smuggled are AI servers, which are not compact. Anyway, more importantly, this doesn’t matter, because AI chip smuggling rarely involves hiding products to get through customs; usually the products are just relabeled as some other kind of good and shipped in plain sight, so to speak.
- Claude writes that being “sold through sprawling global supply chains” makes AI chips “attractive and feasible to smuggle”. What does this mean? Is it that smugglers can more easily buy chips from companies outside the US? (Until recently, smugglers seem to have been able to procure AI chips from US-headquartered companies with relatively little difficulty.) Is it that it makes smugglers buying a lot of AI chips in countries such as Malaysia less conspicuous? (This is closer to being true, I think.) Or is it something else?
- Claude writes that estimates of the scale of smuggling “vary widely, from tens of thousands to perhaps more than a hundred thousand high-end chips per year”. This is literally true, but the low estimates are almost certainly wrong, and the true number is probably much closer to the higher end mentioned by Claude, i.e., hundreds of thousands. 6 So this is misleading. Also, Claude doesn’t specify a year, but smuggling

# mindbox77/zxdesk

## 评论（50/50）

**atdt** · 2026-09-19T17:22:55.000Z：

This advice is too coarse. I believe LLMs have made me a better writer of technical reports. I have a keen ear for language, and I can usually tell when a sentence or a paragraph is orbiting around a point rather than landing on it firmly. Some writers insist that unclear prose is dispositive proof of unclear ideas -- a sign the writer has not thought things through. My experience is different: I often have a clear idea in mind that I cannot quite find the right idiom to express. Sometimes I can find it if I keep revising, but staring at a sentence too long can entangle you in a particular linguistic frame that can be hard to escape.LLMs are helpful because their idiom-list is vast and they are indefatigable and infinitely patient. You can keep iterating on a sentence and it will keep giving you fresh takes. Eventually, whether through careful steering or brute-force iteration, it will come up with something that has the right resonance. Like a word on the tip of your tongue, you recognize it when you hear it.For me, the end result of this writing-process is often a document where much of the language first came from the agent, but the voice is recognizably mine, and I feel a clear sense of authorship. It is still my work because of the microscopic attention I paid to every word. The marble is the agent's, but the chisel and mallet are in my hands.

**alas44** · 2026-09-19T17:23:22.000Z：

"AI writing is vague and wrong in hard-to-notice ways"
This one felt to me, at work I lost a lot of time re-reading and correcting AI prose that was launched to "summarize" a collective white paper, and where subtlety and nuance disappeared in ways that harmed the initial ideas/arguments I was writing about, but in sneaky ways.

**polotics** · 2026-09-19T17:26:04.000Z：

If I may propose a broader rule, that I think this post presents a special case of;Only ever use AI to make yourself think harder, and more.

**sklargh** · 2026-09-19T17:29:27.000Z：

I don't find AI helpful for truly constructive or creative prose, it devolves to the median output very quickly and it's almost painful to hear in my inner voice when I read out an AI-ified idea. The "not this but that" formulation is especially bad or cloying attempt at pretending to refine an idea or lightly correct something to start from a position of authority, very annoying.That said, I have a lot of situations at work where I am asked to simplify something I am an expert in or convey something for a different audience, particularly as I prepare for presentations and I do find it helpful in helping me step down my writing or work. YMMV.I also skip words a lot and can miss that even after 2-3 editorial passes and it's very helpful at that vs. say normal spellcheck.

**patrickmay** · 2026-09-19T17:36:18.000Z：

From TFA: "Eric Schwitzgebel writes that . . . There’s a huge cognitive difference between nodding along while reading something and actually productively generating a text. Two reasons: First, once the text is on the page, it’s easy to passively let the approximate word suffice, rather than thinking about word choice in the same effortful, active way we do when generating prose de novo. Second, as I suggested above, I doubt that human beings, even experts, have a good sense of all the factors that shape word choice -- everything they’re being sensitive to. You would have phrased it slightly differently, and even if you don’t know that, or why, a different signal is sent and received."This is the best articulation I've seen of why simply reviewing and copy-editing does not provide remotely the same value as writing from scratch. I spent a considerable amount of time over the past two weeks reviewing and improving a work document that was the output of an LLM. Given the number of people involved and the final level of effort, I'm firmly convinced that writing it manually would have been faster and resulted in a higher quality product. Getting the wording right matters.

**rectang** · 2026-09-19T17:38:40.000Z：

Instead of asking AI to write something substansive for you, ask it to critique your writing. Then use your own judgement as to which bits of advice to follow and which to ignore.The LLM will always give you a full rewrite — don't use it. It always does too much, and persuading it to tone it down is a constant battle.

**AlienRobot** · 2026-09-19T17:45:24.000Z：

I find it so weird that people use AI to write things. Writing is one of the easiest things you can do. Just put one word after the other.

**jameshart** · 2026-09-19T17:47:44.000Z：

Use AI to write things for you to read that you wish someone else had written. ‘Give me a summary of the research on this topic’; ‘Write a report on this data to help me make a decision’. ‘Take this transcript of a meeting and write me the email it could have been’.Don’t use AI to write things that you are producing for someone else to consume.

**calebkaiser** · 2026-09-19T17:52:55.000Z：

I think about this a lot. I started my teenage-to-young-adult life in the literary world as a poet who loved programming, and made a living as a ghostwriter. At some point, I fell in love with mathematics and wound up in ML in research/engineering for the last 8 years or so. So, I've thought a lot about writing and ML and their intersection.I think one of the underappreciated things about writing "substantive" work is that the work you see at the end isn't the first attempt. And I don't mean the first draft of the piece. I mean that almost always, writers iterate on the same topic many times, either with complete published pieces or abandoned drafts or even just conversations and sessions of unproductive daydreaming. It's a cliche that your best work typically also comes out fastest, but it's not because of divine inspiration, it's because you've whittled the big idea you actually care about down so much in your mind that you instinctively know exactly how to write it.My experience has been that for people who don't work this way or don't write a lot, LLMs can give them this incredible feeling of leaping straight from inkling to "substantive" writing. And because they haven't built up those muscles or "taste", they don't immediately recognize that it's imprecise and hard to follow.That's not to say they're not brilliant in their own right, just that they haven't spent a lot of time on this particular thing. Sort of like a very gifted programmer who doesn't have a ton of experience yet (speaking as someone who is gifted at nothing and frequently has to do things they're inexperienced at).So I don't think the problem is that LLMs just write bad. It's that LLMs are so wonderfully powerful that they allow you to confidently leap forward to create something that is a little beyond your experience.And that's why I have different reactions to heavily AI generated writing. When it feels like marketing at scale, it grosses me out. But when I feel like it's just someone who is excited to write an idea and maybe doesn't have a lot of experience doing it, I'm not judgemental. My hope is that it makes them more excited about writing, and that trying to make their next piece better will lead them inevitably to start thinking about where the last piece fell short. And if there's some slop along the way, eh, I'm not compelled to read it.

**bko** · 2026-09-19T17:55:21.000Z：

> I think so because (1) the writing process is an essential part of the thinking process, (2) AI writing is vague and wrong in hard-to-notice ways, and (3) writing with AI (and not labeling it as such) is rude and misleading. I’ll explain these points in more detail below, but first, a few throat clearings.1. Agree writing process is essential, but just getting your thoughts down is the start.2. Human writing is very often vague and wrong in hard to notice ways, but I would say it's more likely to be wrong in easy to notice ways, which is ... better?3. I think it's rude to not use the best tools to convey the message most clearly and most respectfully of my time. I often use AI to help me write emails and nearly every time it provides more concise well structured versions of what I have to say. 99% of the time I'm just trying to convey a message clearly, that's all. When I write my draft there is often words I can delete or phrases that I can shorten. It's hard to spot but when you have AI point them out it's obvious. This is the role of an editor (check out Stephen King book On Writing which makes this point). Unfortunately I don't have an editor, but I have AI that helps trim the fat, get to the point and save my readers time.If these tools are available to you and you don't use them, then I think that would be disrespectful. I don't take any solace thinking how much time and effort went into what someone wrote me. If I could save them time and have AI write or edit, and save me time reading it since it would be more concise and better structured, it's a win-win.

**Sharlin** · 2026-09-19T17:55:35.000Z：

Communication between two people is hard enough. Involving another actor as an intermediary rarely helps. It quickly becomes a game of telephone. Doubly so if the intermediary is an LLM.

**vanschelven** · 2026-09-19T18:07:11.000Z：

I can't help but think that some of the arguments here apply equally well to writing _code_ as they to to other substantive writings.Writing code is thinking, AI code is often vague and wrong in hard-to-notice ways, and the (human) reader of code is the one that pays the cost for this later.The cost/benefit analysis may still work out differently for code though...

**pigpop** · 2026-09-19T18:53:09.000Z：

I don't know what everyone else is doing but I've certainly been writing a lot more often because of my interactions with AI. Maybe some people used to write more but have been leaning on AI so they can write less but I don't think that's universally the case.I agree that being lazy about writing and simply using a short prompt or list is detrimental if you are replacing your own output but you don't have to do that and you don't have to accept any of the output either. The best chats I've had usually start with a large amount of my own writing up front, thinking through the idea, listing several alternative ideas, asking a lot of questions, jotting down related topics, etc. and then reading the resulting output and critiquing it, asking for clarification, doing my own research on it, even just discussing it with the AI and doing this for a number of turns until I feel like I've exhausted the topic in the chat. I then often take what I've shaped in my own mind from that process and write something myself, either that or take the best parts of the output and edit, rearrange, reinterpret, and add to it in order to produce something.I guess it all comes down to whether you are actively engaging with the material, regardless if that material is the result of a Google search, pulled from a book or generated by AI. If you just read it or copy paste it and don't engage with it and think about it then it doesn't do much good.

**tptacek** · 2026-09-19T19:20:12.000Z：

So, I think I agree with all of this, but want to use this post to host my take on AI writing, a take I don't think I can get across on the big thread here on my post about AI writing:https://news.ycombinator.com/item?id=49747070I think people are stuck in the idea that the way you "use AI to write" is to let it generate alternative words for your thoughts. That's a terrible way to write. I advocate for a rule: "any word an LLM suggests to you is disqualified, even if it's better than the word you've chosen". Nobody is vigilant enough to keep LLM word selection from bleaching out their personal style.But LLMs can do things for language (natch) that deterministic programs can't. Those things are helpful and you should consider taking advantage of them. Here's a short list of ways an LLM can potentially improve your writing:* It can instantly spot overused words and turns of phrase, or, better still, worthless filler and throat-clearing like "just" and "very" and "it's important to note".* It can rescue active verbs trapped inside nouns, where sentences are wrapped in zombie verbs like "make" or "reach" or "start" or "have", carbonite-frozen verbs like "decision" or "agreement" or "distortion".* It can match the subjects of your sentences with actual characters in the action of your story or argument, flagging all the times you accidentally nail the subject of a sentence down to some random part of the scenery. It can check to see whether the new detail each sentence adds (if it adds any at all --- something else it can check) is in the stress position of the sentence.* It can check your transitions and flag places where the openings of sentences and paragraphs are abrupt. For that matter: it can check the topic sentences of paragraphs and the flow from graf to graf.* It can check for passive voice, but also note the (many) instances where passive is the right call for what you're trying to say.The model never gets tired. It generally never forgets the rules. It can instantaneously diagram out a sentence and work out an accurate model of the semantics of your writing. It's doing things you cannot do with a grammar checker.You're not going to want to act on everything an LLM flags. LLMs have an idiosyncratic sense of style (I keep saying they write every sentence like it's the headline of a magazine article). Some of these quirks of writing will be part of your voice, and you'll need to keep them.You're not going to want the LLM to give you alternate words and sentences. That way lies Velveeta. And many times, the LLM will flag a usage issue and your response won't be to act on the suggestion, but just to rewrite the sentence or paragraph entirely --- or, better yet: just delete it, which is an awesome feeling.This is using an LLM as a copyeditor. I've worked with professional copyeditors, and the feeling of working with an LLM copyeditor is comparable, except that the LLM is much more thorough, and I don't feel bad about ignoring it when we disagree. This style of working doesn't allow the model to infect your writing; it's just making you better informed about the words you're choosing. I think more people should try it.

**Ampersander** · 2026-09-19T19:27:11.000Z：

Who cares? AI gives me lots of text and it's not like it's ever going to go away. Any time in my life in the future when I need text, I can just have AI generate it. Thinking is solved.

**breezybottom** · 2026-09-19T18:25:22.000Z：

You say the voice is clearly yours, but that's an illusion. I can recognize your comment as AI written.

**AnimalMuppet** · 2026-09-19T18:37:55.000Z：

> Sometimes I can find it if I keep revising, but staring at a sentence too long can entangle you in a particular linguistic frame that can be hard to escape.This expresses quite well an experience that I have sometimes had. Your first words can trap you in a box that you know isn't right, but you can't figure out how to escape.

**D-Machine** · 2026-09-19T17:34:19.000Z：

AI is very bad at properly handling statements that make heavy use of vague quantifiers (e.g. "some", "most") and also commits a lot of pretty serious logical fallacies. It is also bad at handling subtle logical negation, generally.One of the most egregious negation issues I run into a lot is when I (or someone) makes a statement of the form: "not X" or "X is thus not true", and the AI then proceeds to interpret or summarize this as 'whatever is the opposite of X is the case'". This will cause it to go down a useless path investigating or disputing the opposite of X, which generally has no relevance or bearing on anything.It also often very harmfully will replace your carefully chosen words with weirdly specific academic operationalizations or formalisms, then again waste huge amounts of text refuting / showing "problems" that result from that formalism, all of which again have no bearing or relevance on the original statement. An example would be you saying something like "intelligence, generally, must surely explain some of the differences in X", and then it will go "actually IQ does not correlate with X", unless you specifically tell it not to conflate psychometric IQ with intelligence generally.Sometimes this is helpful, but the more specific / technical the domain, the more often you specifically have to prevent it from going down stupid paths that should be obvious given the expert context and wording, because it can seem almost hungry to try to catch you in some kind of insipid 'gotcha'. Much of these issues often clearly arise immediately from the first-pass "reword what the user said" part, given the reasoning traces.

**michaelchisari** · 2026-09-19T19:20:34.000Z：

Most of us have worked our whole lives to be writers in some domain: Code, documentation, specifications, product requirements, corporate communication, etc.If we don't want to be writers, then we have to be editors. And editing is an entirely different job and it's not an easy one. In many ways it's harder.Especially when LLMs love writing novels when all we need is a short story or less.

**D-Machine** · 2026-09-19T17:29:43.000Z：

And also to think in different directions than you would have gone in isolation. Regardless, this is a great heuristic / rule that I will be sharing and keeping in mind.

**onraglanroad** · 2026-09-19T18:17:24.000Z：

While I mostly agree with you, what is the real difference between an editor saying, 'when generating prose de novo' sounds pretentious to an American audience so let's use 'when writing from scratch' instead, versus an LLM giving the same advice?Not that it's necessarily better but it's the kind of thing an editor might pick up and so why would you reject the advice if it's a machine giving it rather than a human?

**lokar** · 2026-09-19T18:39:23.000Z：

Writing is thinking. In many situations where we are called on to write, what is actually needed is thought.

**gyulai** · 2026-09-19T18:39:33.000Z：

A workflow I've recently discovered for myself that provides a kind of middle ground: I'll ask the LLM to write a first draft in a language that isn't the one the piece should ultimately be in. Then I'll use the LLM's first draft as a blueprint, to write a first draft myself in the intended target language. This fights my brain's temptation to just shut off, and forces every word choice to actually be mine. Then I'll hand that over to the LLM for editorial suggestions and iterate from there.

**kelnos** · 2026-09-19T18:44:07.000Z：

I really did like the author's framing there, but I think there is a different, simpler way to put it:Why would you think that asking someone else (that is, another human) to write something (and then reviewing it) is the same thing as writing it yourself?You may trust the other writer's opinions and knowledge, but it will not have the same tone, structure, word choice, understanding, or narrative flow as it would if you were to write it yourself.And when it's an LLM, you should not trust it's "opinions" and "knowledge", because it does not have either of those things. The appearance of those things is just that, an appearance.

**devindotcom** · 2026-09-19T19:38:54.000Z：

AI can't critique because it has no critical faculty. It can only offer critique-shaped language. That may be useful for some, though.

**D-Machine** · 2026-09-19T17:47:27.000Z：

Writing is pretty hard for a lot of people, maybe especially so if they are more non-verbal thinkers, and then doubly so again if one must write not in one's native language.

**nephihaha** · 2026-09-19T18:43:33.000Z：

It depends on what you are trying to convey and how.

**sublinear** · 2026-09-19T18:48:50.000Z：

I don't think I have to speculate why comments like yours get downvoted so much.Anyway, I completely agree. Writing isn't something to be delegated.The problem is not new with LLMs. Businesses have been delegating writing to idiots who don't really care for the entire history of business. Authors and musicians have traded their souls for inauthentic crowd-pleasing results for about as long.No, the problem with LLMs is that people are all using the same generic models. This only further shows that the future of LLMs is locally trained and locally run. Personal LLMs on a personal computer. Business LLMs on-prem. We will continue see them flourish in ways that generate absolutely no money whatsoever on their own, but do add marginal value when combined with a heavy dose of human creativity.All the clueless old farts that are still alive by this point will continue to lecture the rest of us with more condescending gee whiz "whaddyaknow" and "whodathunkit" nonsense. As if they've even had their finger on the pulse since the early 2000s.

**bdangubic** · 2026-09-19T18:07:49.000Z：

I am someone else, if AI can write something that I want to and can consume then it can do the same for other’s consumption. Perhaps a disclaimer would be nice, “co-written with ____” but I see no difference between the two though of course I understand what you are trying to convey conceptually

**kelnos** · 2026-09-19T18:48:10.000Z：

I think that's somewhat reasonable, but not always: the effort of researching and of writing yourself will teach you better then reading something someone else wrote, especially an LLM that will get things wrong in surprising ways that a human would not.I'm not saying you should never do this: our time is valuable, and we shouldn't spend it on things that are not genuinely worthwhile to us if we can help it. But we're still losing something by having an LLM write for us, even if the intended audience is just ourselves.

**mathgeek** · 2026-09-19T17:57:15.000Z：

I think your point on “cutting down on words”, so to speak, is relative to personal writing style. I find that AI tends to write far more words than I personally do, which is sometimes useful, but in the opposite direction that it works for you.

**elmomle** · 2026-09-19T18:01:31.000Z：

Just a couple of days ago, a customer rep at a company we partner with dropped a long doc that had basic reasoning errors once you got into the individual sections.I would have much preferred if the rep had written a shorter document and reached out about things they were uncertain about. Instead thet wasted my and my team's time as we first tried to make sense of the document on good faith before realizing the problem.I don't care if people use LLMs per se, but if this is functionally the result, then in this aspect of my work things would go much better if people did not use them. They are a great interface for talking to a machine, but due to the laziness they breed, they are a terrible interface for talking to other humans unless approached with a great deal of discipline.

**perrygeo** · 2026-09-19T18:16:56.000Z：

I never use AI for writing but do so regularly for code. They are quite different to me.My reason: code can be checked objectively. I can run it and confirm it works. I don't get attached to it. I don't feel pride in it (even when I write it by hand). Code just is. It's lifeless, inert, and entirely replaceable.How do I do the equivalent for prose? How can I tell if my words "work"? Do they clearly convey my ideas to the intended audience? There's an element of subjectivity here forces me to identify personally with the prose.Code has no such personality. I don't tie my identity or ego to code the same way I would an essay.

**layer8** · 2026-09-19T18:41:57.000Z：

TFA is about having AI do the writing, not about having AI suggest editorial improvements. The parent comment argues against having the AI write the text and having the human merely review it, not against having the AI review human-written text (and the human deciding which of the AI’s suggestions they might apply).See also this existing comment: https://news.ycombinator.com/item?id=49768564, which I completely agree with and which is complementary to the above root comment.

**telesilla** · 2026-09-19T18:41:51.000Z：

Excellent idea, I'll try this. And for those who don't speak a second language other than English, you could use leet.

**dkga** · 2026-09-19T19:36:00.000Z：

Wow, love this! Could even match with a language I am actively learning so it helps that as well!

**card_zero** · 2026-09-19T19:28:58.000Z：

There's knowledge in books, and it's ingested all the books, so it does hold knowledge. But I guess that's not how you mean it.

**bigstrat2003** · 2026-09-19T18:29:31.000Z：

Depends on the writing. Writing a blog post or something is challenging because you want to have an engaging style. But I see people at work using LLMs to fill out tickets, which is the easiest thing in the world. It's just a plain description of things, it requires no skill at writing at all. It baffles me that people are using LLMs for something like that, which should take less than a minute of your time to fill out and will be more pleasant for the recipient than the slop the model produces.

**boredatoms** · 2026-09-19T18:21:54.000Z：

There is a higher tolerance for LLM-isms if you asked an LLM to write something for youElsewhere it’s painful and irksome when you didn’t ask for it

**AnimalMuppet** · 2026-09-19T18:23:54.000Z：

There's a difference between me getting AI to write something I want to read, and getting it to write something you want to read. The difference is that I know me, but I don't know you.The other difference is that, if I get AI to write something for me, I expect something AI-written. If I am writing something for you, you expect something that I wrote, not something that AI wrote.

**bigstrat2003** · 2026-09-19T18:26:00.000Z：

The words of a machine are not of interest to me. I want to hear what you, the human, have to say, imperfections and all. Reading something written by an LLM is actively annoying, and it's not very respectful to inflict that upon others.

**ssl-3** · 2026-09-19T19:34:31.000Z：

When I seek input (whether passively or actively; it doesn't matter) from another person, then I generally want that person's input. I want their words.They can be broken and jumbled, or terse AF, or combine to be Pulitzer-quality prose. Either way: I want to consume their own unique human expression of a concept.There's value in raw human expression, including in the missteps.If I instead want the regurgitated waggyings of a bot, then: I know how to get that on my own.We've all got web browsers and pocket supercomputers. We've all (well, most of us) been alive and aware of LLMs since their recent rise from infancy.It's a no-brainer for us to paste some paragraphs into our favorite chatbot and get a summary or an artificial expansion or whatever else we wish to have. If that's what our goal is, then we can do that on a whim -- and we can still retain the original expression.But doing it on our behalf is deleterious, unsettling, and unhelpful. It has negative value to the beholder.

**bko** · 2026-09-19T18:08:47.000Z：

PROMPT: make this more concise while conveying the same messageI think “cutting down on words” depends on personal writing style. AI tends to write more than I would, so I usually have the opposite problem.

**bko** · 2026-09-19T18:07:34.000Z：

Yes, you hit on the main problem with LLMs for writing. It doesn't cost you anything. It can do the reasoning for you and creating long messaging with dodgy reasoning.I think you should write down your thoughts, tell it to make the points you spelled out and be concise and respectful of the reader's time and attention. When I do this, it works very well. But I agree if you just have it respond and reason it tends to often produces bad responses.

**vanschelven** · 2026-09-19T18:47:25.000Z：

Programs must be written for people to read, and only incidentally for machines to execute. -- Hal Abelson

**layer8** · 2026-09-19T18:56:49.000Z：

> My reason: code can be checked objectively. I can run it and confirm it works.Running code only confirms that it works with the precise input, in the precise environment, under the precise circumstances you run it under. It doesn’t ensure that the code is correct. Thinking through the code, on the other hand, lets you consider all possible cases. It’s the difference between experiment and (mathematical) proof.For an objective correctness proof, the code is indispensable.

**onraglanroad** · 2026-09-19T18:43:05.000Z：

True, but I was responding to the comment rather than the article.

**D-Machine** · 2026-09-19T18:53:33.000Z：

Here I would maybe argue that the simplicity makes these kinds of tasks tedious (like doing taxes), so it also makes a lot of sense for people to want to just throw AI at it. Tedious, easy rote tasks can be much more unpleasant than engaging ones.I think people massively over-rely on AI and I really worry about the consequences of this. But there is nothing baffling at all about the basic appeal, IMO.

**cubefox** · 2026-09-19T18:35:42.000Z：

Moreover, when you wrote it yourself, you are intellectually responsible, you can defend it, while if the LLM wrote it for you, nobody is really responsible: The LLM didn't write it "out of its own motivation", it was merely extrapolating your prompt; and you only provided the prompt, not the extrapolation.So the intellectual responsibility is diluted to a substantial degree: The text is not the opinion of anyone who can be expected to honestly defend it. It's bullshit in the technical sense.

**layer8** · 2026-09-19T18:47:04.000Z：

I expanded my comment since.
