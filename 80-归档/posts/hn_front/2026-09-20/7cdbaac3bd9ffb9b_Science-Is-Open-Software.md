---
type: "corpus"
item_id: "7cdbaac3bd9ffb9b"
title: "Science Is Open Software"
source: "hn_front"
source_name: "HN 首页（非 Show HN）"
url: "https://news.ycombinator.com/item?id=49762687"
project_url: "https://jepedersen.dk/blog/202505_research"
author: "jegp"
published_at: "2026-09-19T02:21:35Z"
captured_at: "2026-09-20T03:32:45+08:00"
lang: "en"
kind: "post"
tags:
  - 语料
  - hn_front
  - author_jegp
  - story_49762687
  - front_page
metrics: {"points": 145, "comments": 64, "engagement_velocity": 145}
comments_count: 64
comments_total: 64
discovered_via: "hn:front_page:2d"
archived: true
archived_at: "2026-09-20T09:21:32+08:00"
archive_reason: "渠道停用"
---

# Science Is Open Software

- **来源**：HN 首页（非 Show HN）　|　**kind**：post
- **原帖**：https://news.ycombinator.com/item?id=49762687
- **指标**：点赞=145 · 评论=64 · engagement_velocity=145
- **作者**：jegp　|　**发布**：2026-09-19T02:21:35Z
- **项目链接**：https://jepedersen.dk/blog/202505_research
- **采集**：2026-09-20T03:32:45+08:00　|　**id**：`7cdbaac3bd9ffb9b`

## 正文

Published: 2025-05-24
Author: Jens Egholm Pedersen

Science is open software · Jens Egholm Pedersen

# Science is open software

24 May 2025 7 min read research practice software

TL;DR I claim that modern science is synonymous with open source software. This post explains why, why it matters, and what you can (and should) do next.

> Why do you care about (open source) software? - Everyone

I spend a lot of my time working on software. I have been asked why software matters more times than I can remember. Software is, people say, not science. It’s a time sink, something to rush past in the pursuit of what really matters: results (and papers if you’re in academia). Publish or perish.

Well. I think software matters. In fact, I think open source software is science. Or, at least computational science. And this post tells you why. Why we as scientists must insist on the scientific method and why that means working on open and reproducible software. This post is not easy to write. It challenges many of the current trends in academia, but it is an important move towards better science that doesn’t turn us all insane.

## What is science?

If you look up science on Wikipedia, here’s what hits you:

> Science is a systematic discipline that builds and organises knowledge in the form of testable hypotheses and predictions about the universe. - Wikipedia

Now, go and grab a random arXiv paper. It clearly contains “knowledge” of some sort. But, does the paper contribute predictions that are testable and can by systematically organized? Can you test it? Can you systematize it?

The answer is never a flat no, but it’s hard. You rarely have direct access to that knowledge.

### The good explanation - inner models

> If the organism carries a 'small-scale model' of external reality and of its own possible actions within its head, it is able to try out various alternatives, ... and in every way to react in a much fuller, safer, and more competent manner to the emergencies which face it.

In his excellent book The Nature of Explanation, Kenneth James Williams Craik posits that we use small simulations of reality to explain and predict the world outside.

This point seems obvious today, but it highlights the goal of pursuing science in the first place: you, as an acting entity, improves your inner model to the point that you can make better predictions than before. The inner model here is critical: if the arXiv paper does not help their readers predict the world, it is not science. This is why computational reproducibility matters–software is how we encode and share predictive models.

## What is reproducibility?

Recall that according to Wikipedia, it is not enough to demonstrate results alone. Results have to be (1) systematic and they have to be (2) testable.

It is entirely possible that the given paper is too hard to understand or unaccessible to the audience for other reasons. That does not mean that there are no scientific insights to find—readers may find ways to systematize them on their second or third reading. No, it means that you specifically cannot take the idea as your own, test it, and use it to improve your world model.

Reproducibility, in this context, is not only the duplication of results. It is the ability to take the scientific idea, embed it into your own inner model, adapt it, and build upon it—or discard it because it reduces predictabilitly.

If an idea is not reproducible, the findings cannot be expanded. And are, therefore, useless.

This becomes clear if we do a quick thought-experiment where we replace “software model” with “mathematical model”. Just as we wouldn’t accept a physics paper that said our equations predict X but we won’t show the math, we shouldn’t accept (computational) science that hides its methods.

## Why is software science?

> How many fields have been held back, and how many people have had their careers disrupted, because of a buggy program? - Greg Wilson

Software is ubiquitous in modern science. Anything from CoVid models to search algorithms to lab protocols are build on software built by other people. Researchers are busy people. They don’t bother to look through all software dependencies to verify correctness, understand implementation details, or check for potential errors that could invalidate results.

From that follows that the scientific results depend on the software. If the software is wrong, the science is wrong. (Software bugs already cause numerous retractions, such as here, here, here, and several places here).

And that is well and good, because at some point we have to trust and rely on other’s work. For that to happen, it (software) needs to be reliable.

## Why open source?

We found that software needs to be

1. Reproducible, meaning executable, as well as modifiable, and
2. Reliable, meaning that the results are consistently trustworthy

Modifiability is important for science for the same reason that equations are important for scientific predictions. Reliability is crucial because we want systematic improvement of our knowledge, not flaky and partial results that only work occasionally.

This is what open source software gives us. We can change code and retrofit it to suit our needs (just think about Hugging Face models) and we can iterate upon it to continue to improve it. It already generates trillions in value and there is room for much, much more.

Of course, open source software is not a perfect cure. There are IP and security concerns, bugs can still occur, and stability can be a problem. But at least the imperfections are on public record. They can be amended and improved, just like our scientific understanding. From that perspective, one can claim that open source software is the scientific method—just in simulation.

## A vision for future science

If we accept these premises we can ask: what would truly open (computational) science look like?

Every result is instantly reproducible. When you read a paper claiming that a new drug reduces symptoms by 30%, you click a link and watch the exact analysis run in your browser. The data processing, statistical tests, and visualizations execute in seconds using the same environment the authors used—preserved perfectly through reproducible containers.

Scientific software evolves like Wikipedia. Climate models aren’t developed in isolation by single labs, but maintained by global communities. When a researcher in Kenya discovers a bug in atmospheric turbulence calculations, the fix propagates instantly to climate simulations worldwide. Models improve continuously rather than languishing in academic silos.

The pace of discovery accelerates. Instead of each researcher building from scratch, we stand on shoulders of giants whose work is not just readable, but runnable and modifiable. Scientific progress compounds at an unprecedented rate.

Trust in science strengthens. When climate models, economic forecasts, and medical recommendations are built on transparent, auditable code, public confidence grows. Science communication improves because the models themselves become part of the conversation—not just their conclusions.

This isn’t utopian fantasy. Every piece already exists—open source communities, reproducible environments, collaborative development platforms. We just need to shape them into a coherent vision for how science should work in the digital age.

The question isn’t whether this future is possible. The question is: how quickly can we build it?

## What now?

I posit that open source software is a necessary condition if we are to science in a computerized world. Software is executable mathematical models that we should prioritize much higher.

We still have work to do and this is how you can help:

- Share and document your code

- Papers without code is less scientific because it is harder to build on the insights. In the ideal world any claim should be backed up by reproducible code. Always use code from day 1 and always share it.
- Write stable code, use NixOS

- Code should be 

# Jalapeño Shows Power of LLMs for Chip Design - IEEE Spectrum

## 评论（64/64）

**jegp** · 2026-09-19T02:21:35.000Z：

TL;DR I claim that modern science is synonymous with open source software. This post explains why, why it matters, and what you can (and should) do next.

**random3** · 2026-09-19T02:47:25.000Z：

Science is open, but science is not software and software definitely not science.

**willtemperley** · 2026-09-19T03:31:16.000Z：

> modern science is synonymous with open source software.Another problem with reproducibility is the openness of the underlying data. Many academics are terrified of giving away the golden goose and the software is often useless without the data.However many scientists do work openly, e.g. The Journal of Open Source Software:https://joss.theoj.org/

**samayashar** · 2026-09-19T03:51:13.000Z：

Nice read. I believe that traditional software is a great way to showcase the proofs when it comes to physics and mathematics. You can easily code up a theorem in a language of your choice and justify that 'Okay, the output matches the expected value'.I am particularly fascinated by labs like DeepMind [https://deepmind.google/science/]. The recent advances in their frontier models that are able to predict diseases before they're diagnosed is incredible. This is what AI should be built for and actually do!

**flopsamjetsam** · 2026-09-19T03:56:58.000Z：

> Every result is instantly reproducible. When you read a paper claiming that a new drug reduces symptoms by 30%, you click a link and watch the exact analysis run in your browser. The data processing, statistical tests, and visualizations execute in seconds using the same environment the authors used—preserved perfectly through reproducible containers.At least some journals have this as a stipulation e.g. https://www.nature.com/nature-portfolio/editorial-policies/r...Particularly the "data availability" and "Availability and peer review of computer code and algorithm".However, in my limited experience, of trying to reproduce certain scRNA-seq processing pipelines, in practice it's never available as just a Github link. I can understand that some/many researcher's code is not in good shape, so I think it'll be quite a stretch to have this available.I do think it's laudable though, to try and make it available. It would certainly have been very useful for me in the past.

**throwaway27448** · 2026-09-19T04:05:43.000Z：

We really need to ban tech people from using the word "open".

**D-Machine** · 2026-09-19T05:58:13.000Z：

Science should be more like this, in current times, yes.But until much of academia is burned to the ground, or until science can be properly separated from modern academia, this will never be so. The current academic incentives are all wrong: low-quality research is rewarded and results in publications, whereas high-quality research (that takes time, and usually reveals that most exciting publications depend on p-hacking or other highly data-dependent analyses and selective presentations) is not published or actively blocked during peer review.So instead you get BS arguments about how data can't be released for various privacy concerns (when in reality the vast majority of most datasets are trivial to scrub of identifying factors, and even in more complex datasets where you need to consider k-anonymity, it is still trivial to release data that allows replication of core analyses), and academic science is increasingly irrelevant unless it is tied to tech and industry, where producing junk actually has real negative economic and personal consequences.I don't know what world this article / post lives in, but it isn't the messy world of actual reality.

**txrx0000** · 2026-09-19T08:34:20.000Z：

I agree with the general sentiment, but there's one major caveat. We should implement reproducible programs on top of a virtual machine spec like JVM or WebAssembly rather than replicate the entire environment. It's more practical to do and doesn't push software towards further centralization. Let people use whatever OS and VM implementation they want, or even write their own.

**Muhammad523** · 2026-09-19T08:54:16.000Z：

Replace "Open" with free as in "freedom"
gnu.org

**enbugger** · 2026-09-19T09:35:51.000Z：

> NixOS is quickly becomming the biggest and best tool there is. It will guarantee that your code will run exactly the same way, even 100 years in the future. Docker, Conda, and similar tools are better, but NixOS gives more comprehensive guarantees.I like how this is dropped as a fact. Dare to explain why though? Especially vs Docker. NixOS is not even standardized. No guarantees it will not be superseded by some descedant or eg. Guix in a near decade.

**flimflamm** · 2026-09-19T11:02:34.000Z：

One can decide to dedicate their own time to creating open SW. Typically someone (like tax payers or private companies) pay for the creation of scientific discoveries.Thus there is indeed a difference in the monetary intensives.

**shevy-java** · 2026-09-19T11:08:00.000Z：

> modern science is synonymous with open source softwareBut why does the public have to pay for e. g. Elsevier? We pay for research of scientists already via taxpayers money (at the least in a civilized country), then we have to pay again for a private entity. If science is really open then it also needs to require public publishing. Gangsters such as Elsevier and others should not be able to drain the public here. Taxpayers financing something should also require public access to findings, at all times. Instead, Elsevier, Springer etc... get more public money while keeping things private. That's the antithesis to science.

**btrettel** · 2026-09-19T13:27:39.000Z：

The title reminds me of this, which is arguing the opposite direction: https://softpanorama.org/Articles/oss_as_academic_research.s...

**runningmike** · 2026-09-19T13:28:19.000Z：

100% disagree! Do not mix and cherry pick terms and definitions to make your point. That's not scientific -) Take e.g. a look in https://opensciencemooc.eu/ and check a nice accepted handbook like "The Turing Way" [1][1] https://book.the-turing-way.org/

**analog31** · 2026-09-19T14:14:00.000Z：

When all you have is a hammer, everything looks like a nail.I refer to what I think the author is asking for, as "push button reproducibility," i.e., the idea that the results will reproduce themselves at the push of a button, anywhere, at any time in the future. I have a couple of misgivings about this.First, the whole idea of "open" research predates computer technology. Forcing science to keep up with the latest ideas in software distribution is too much of a burden, when science is already too risky and slow. I had the odd privilege of learning the scientific method from my mom, before there was widespread access to computers. Her version was that a study should be reproducible by a reasonably skilled person. This is a greatly relaxed standard, but is realistic for a discipline that spans decades if not centuries.I supplied all of the data and code for my thesis research (and a sufficient number of mechanical and electrical drawings). But nobody has Turbo Pascal today, and some of the commercial instruments such as specialized lasers were already obsolete by the time I finished. Also, the experiment was dangerous, and might not pass safety review today. It required about $500k of equipment and a dedicated lab.Today I have the luxury of saying that if my code fails upon loading a new version of a dependency, the person who discovers that failure is probably skilled enough to fix it, and my work rarely hinges on the idiosyncracies of dependency versions. If it goes into a product, they'll totally rewrite it anyway.Second, science is still at its core an experimental discipline. Even in physics, there are more experimentalists than theoreticians. Reproducibility means roll up your shirt sleeves and head for the lab. To this day, some processes have not been mechanized, and you still need to spend years developing "lab hands" which not all people succeed at.I think there's a clue in the fact that the social and medical sciences seem to be the most deeply embroiled in the reproducibility crisis. It's because the quality of results depends on the the quality of measurements, and it's just harder when dealing with living subjects or one-of-a-kind specimens (such as the earth's climate). In fact, not much more than a century ago, it was believed that studying those things was beyond the reach of scientific methodology.Third, we're not going to stop doing science in areas where it's hard, particularly in medicine, but we're also not going to staff up in areas such as software development, to make science work better. People are suffering from disease right now so there's always an urgency to finding cures, plus an obvious profit motive.Disclosure: Experimental physicist, developing better measurement equipment.

**5555watch** · 2026-09-19T15:15:35.000Z：

GPTZero says: "We are highly confident this text was AI generated (100%)"Am I the only one that's tired of "my random shower thought turned into full article with AI" articles?

**crustyoldhuman** · 2026-09-19T16:54:29.000Z：

This article is correct but it bummed me out. It made me think of how much of science has been perverted into other goals, like medical science for example. The advancement of human health largely depends on corporate interests, and that is so insane to my brain it hurts to think about. very few independent scientists can research anything because everything costs money so you need a corporate interest to even do research. And the corporation gets the "rights" to those findings? It's absolutely insane to discover something natural and claim it as your own, and science is natural nobody is inventing it or being creative and writing it themselves, they're essentially walking up to a mountain and saying "Ok it's mine now I'll charge you 100$ to walk on the mountain". It genuinely makes my brain do somersaults in my skull that we've somehow backed SCIENCE of all things into this weird gatekept scenario its in now. It wouldn't bum me out so much but it clearly does nothing but hinder progressThe point at the end "The scientific revolution succeeded because it insisted on transparency, reproducibility, and constant scrutiny." is a good one. But the real kicker that makes the situation so bleak is it's not the scientists who get to decide whether or not these things get applied to science or not, it's government policies and corporate interests.

**gradus_ad** · 2026-09-19T02:32:43.000Z：

What's the equivalent of closed source?

**jibal** · 2026-09-19T03:31:43.000Z：

You argue that open software is science, which is not at all the same as claiming that science is software. ("is" in this context is not equivalence -- "a poodle is a dog" != "a dog is a poodle".)

**jegp** · 2026-09-19T02:49:36.000Z：

Did you read the post...?

**setopt** · 2026-09-19T07:42:58.000Z：

JOSS is great, I’ve both published with and reviewed for them, and enjoyed it more than traditional journals. The process felt more constructive than destructive, in a sense.I believe they’re always looking for new volunteers to review papers, so please do volunteer if you are able.

**jegp** · 2026-09-19T19:13:26.000Z：

I've seen quite a few academics wrangling with patents. What should come first? Proliferation of the sciences or (potential) profit? Your point about the golden goose is pretty interesting and others in this thread has pointed to the misaligned incentive structure in academia. I'm curious, do you think things like JOSS could help open up data and "the golden goose"? I'm not sure the funding bodies I'm interacting with would respect this kind of initiative, but maybe it's just a matter of time.

**jegp** · 2026-09-19T06:09:07.000Z：

Thanks! I appreciate that. Your point about DeepMind and frontier models is spot on. When they "embody"/build on the science done before them we get absolutely mindblowing synergies. But I wonder what happens when the LLMs become way smarter that us: why even loop us in? I guess that's related to the recent field medalist letter https://mathandai.org/

**cge** · 2026-09-19T09:19:54.000Z：

I try to do something like this with my publications, and encourage others to. My goal is to have the pipeline from raw data to complete figures and manuscript in a repository, with cached data for computationally expensive analysis and for stochastic simulation results, and the option for the user to just use those or run the full pipeline, with or without the same random seeds. I just make clear that the code was run-once code and is going to be messy compared to code refined over time and diverse uses. I generally use Zenodo to a GitHub repo, however, in case GitHub decides to do something bad in the future. Making sure things run far in the future can also be a challenge. Sure, you can use a container: will the base of that container be available in 30 years?And with that said, for experimental work, this approach does not make things fully reproducible; it only makes the analysis reproducible. There are always factors that influence experiments: research is by definition at the edge of our understanding, and reality has countless variables, including ones no one has thought of, known about or thought important.

**jegp** · 2026-09-19T06:17:55.000Z：

Erm. Why?

**stalfie** · 2026-09-19T07:24:58.000Z：

Hear hear! There are so many obvious improvements to how almost everything is done. For instance, in medicine review articles as a class of articles largely represent a giant waste of time. RCTs flatten all their gathered data during publishing, summarizing complex trial data, which is gathered but never published, into a few numbers. Then review articles take a bunch of flattened data, discard the articles that don't fit the exact question they are reviewing, and then publish a doubly flattened conclusion. If any of the included articles turn out to have flaws, if treatments change in retrospect, if you are looking for the answer to a slightly different question or you are looking at a different subgroup, then the review is useless and has to be repeated.All of these tens of thousands of man-hours could be replaced by a few GitHub repos, if only RCTs would just publish their damn data. Then you could just run and rerun the statistics on whatever subgroup you're looking for, instead of combing through decades of review articles answering slightly different questions, looking for the answer between the lines. With LLMs making mining of large scale datasets almost trivial (with the process most likely becoming trustworthy within a few years), the current status quo is looking more and more antiquated.If you want to be even more radical, hospitals could just publish their data continuously. Of course, it is easy to point to the risks of doing so, but what's often ignored is the benefits. It is hard to overstate just how many medical mysteries a hospital encounters on a daily basis, how much unknown we are navigating in practice. The current norm is that 99.99% of these cases are never published, and are only ever thought about by a small group of people who happened to be at work. Particularly, when someone dies of something no one figured out, it is never published anywhere, because even if you tried it is not interesting reading material for a journal to publish. And no one ever tries because they're scared of being called out for a mistake. A hospital is essentially a continuously running and extremely interesting experiment, where 99.99999% of all results are thrown in the garbage, and the only published data is subject to extreme selection bias.All of this could be different, and the risks involved are actually quite small in practice. It is easy to automatically anonymize data quite well, but extremely difficult to absolutely guarantee that it is anonymous. And since current ethical norms are extremely averse to any degree of risk, and usually entirely ignore potential benefits, we all suffer for it. It is not entirely unlikely that someone reading this post will one day die because of something that could have been prevented, had things been different.

**epihelix** · 2026-09-19T07:41:00.000Z：

It's changing, though, and articles like this are important. TFA is arguing for change in the future, not presenting this as a fait accompli.In the 27 years I've been in academia, I've seen a lot of progress in data openness (NCBI GEO was a game-changer) and FOSS analysis software (it's now widely expected that a high impact pub will make all data and code available for review, and then publicly available upon manuscript publication; most major journals will not allow submission without this). It is becoming common for big journals to specifically ask reviewers to review the analysis code. It is starting to become more and more common for papers to release all the code used to generate all the figures (including supplementary figures)There is still a long way to go, I agree. But it's always better to light candles than curse darkness, etc.> academic science is increasingly irrelevant unless it is tied to tech and industryWhile I have some sympathy with a lot of your bitterness, this statement is insulting silliness that a quick look at the list of Nobel Prizes in physiology and medicine would prove wrong. Almost all major breakthroughs in the applied sphere stem from decades of basic research that happened just because it interested someone.

**fasterik** · 2026-09-19T18:16:37.000Z：

"Burning academia to the ground" is a terrible idea. We need to fix funding and incentives. If funding and research all happen in industry, where are the incentives to do basic research?Your analysis completely ignores the physical and biological sciences, engineering, and the humanities. It mostly applies to a small subset of academic fields in the social sciences and medicine. You're also ignoring the changes that have happened since the replication crisis. Preregistration, publishing all code and data, reporting null findings, replicating results, etc. are becoming the norm.

**jegp** · 2026-09-19T18:37:03.000Z：

I agree that a lot of the practices in academia are misaligned with the original goal. But can't you say that for other systems/institutions as well?
Point being, what about keeping the scientific method as the north star - as a good heuristic to avoid BS arguments and awarding low-quality research. And, crucially, to stay sane. My post is pretty naive, but I stand by the ideal of pushing knowledge as reproducible models.

**jegp** · 2026-09-19T19:04:40.000Z：

In principle I would agree. But, on a more philosophical level, couldn't you make that same argument about C? Or even assembly? Or even digital computers? Less facetious, it seems to me that the particular abstraction is less important. As long as it's unambiguous and widespread.

**btrettel** · 2026-09-19T13:38:02.000Z：

In my work (scientific or otherwise), I try to avoid dependencies if possible. That's not always possible, so a solution like Docker or NixOS is needed, but the problem can be improved a lot without a technical solution. Either feels like fighting an uphill battle though as most researchers think short term and just pick whatever is convenient in the moment.

**jegp** · 2026-09-19T19:02:24.000Z：

Regarding the biggest: nixpkgs sits at around 140k packages, way more than others.Best: I still argue that Docker and Conda are more accessible, but my point was to go for reproducible, declarative science. Nix environments are exactly that. They're not perfect and are, as you point out, not standardized. But they cover much more ground that Docker. If you trust the upstream nix repo, you can get bit-level equality at every single build you (or anyone else) does. Docker relies on huge binary blobs that you can't inspect and that can be pretty much arbitrarily swapped around.I'm totally fine if Guix takes over. Or the next big thing. As long as it's declarative and reproducible.

**jegp** · 2026-09-19T16:28:42.000Z：

100%. I'm not saying the vision we're talking about is there yet, I just think it's an enticing thought. The existence of (predatory) publishers is a sad and miserable joke in its own right.

**jegp** · 2026-09-19T18:50:02.000Z：

I'd love to hear you expand on how I cherry pick terms and definitions.The Turing Way seems great and I'm all for education. One of the most interesting conversation topics in this thread is, to me, how to create the necessary incentive structures. Know how is only part of the way. We need to secure the credit assignment for "openness" both in academia and industry.

**jegp** · 2026-09-19T19:24:46.000Z：

You make some great points that I largely agree with. I'm wondering whether I'm misrepresenting you though, because I'm not arriving at the same "everything looks like a nail" conclusion.One thing I'd like to surface is the distinction you're making between software and physics. You point out that social and medical sciences are only now becoming approachable with scientific methodology. We can now, to a higher degree than before at least, model and predict what'll happen in social and medical scenarios. Isn't that an excellent example of how subject matters can be virtualized? I can't find good arguments for why this would stop there; why wouldn't our scientific models improve to such a degree that we can predict and "interfacte" with more and more of reality. Put plainly: why can't experiments be done in code one day? Particularly if we imagine having better robotics.Do you see my point about closing the gap between the theorizing and experimenting? Or are they fundamentally different things? The "reasonably skilled person" seems like an excellent heuristic > 2 years ago that's rapidly being replaced by automated thinking machines.

**jegp** · 2026-09-19T16:25:44.000Z：

:-) I can comfort you with the fact that the text is not AI generated. I did use AI to proof read it and I liked some of its suggestions to improve the flow of the text. English isn't my first language, so this is a great help for me.

**jegp** · 2026-09-19T02:42:18.000Z：

Equivalent? In the analogy of the math or physics results it would be a mental model in someone's brain that you can't access or verify. You just hope it's true

**random3** · 2026-09-19T02:44:07.000Z：

It’s research happening privately without publishing, usually going into products

**Matumio** · 2026-09-19T05:26:49.000Z：

Like if CERN published the discovery of the Higgs boson with 99.9997% certainty, but refusing to tell you how they calculated that number, or what equipment they used and how they calibrated it, in order to prevent other labs from copying their methods.Or like a machine learning lab claiming SOTA on a benchmark, beating a well-known method that they re-implemented, possibly with bugs, on their private dataset, for millions of compute. But you don't get the source to check, and they don't release any intermediate results or ablation experiments. Aka, from the outside you can't distinguish it from corporate marketing.

**jegp** · 2026-09-19T03:42:07.000Z：

I agree the post is muddy about whether the relationship is bijective (equivalent, poodle=dog) or injective (onto, poodle is a dog).
I make it slightly more precise in the statement "I posit that open source software is a necessary condition if we are to science in a computerized world". That's where the "is" comes from in the title. Throughout history, this definitely has not been the case. I'm arguing that's changing.

**jibal** · 2026-09-19T03:33:42.000Z：

https://news.ycombinator.com/newsguidelines.html> Please don't comment on whether someone read an article. "Did you even read the article? It mentions that" can be shortened to "The article mentions that".

**random3** · 2026-09-19T05:19:48.000Z：

Yes. It conflates a bunch of things> TL;DR I claim that modern science is synonymous with open source softwareThat's a strong statement that's not supported by the arguments and IMO misguided.I don't have a problem with "open", but rather with "software".Both science and software deal with models, however the focus is quite different. I suspect you conflate theory with models.The goal of science is to produce and test theories — that's an inductive/abductive process. A model, regardless of whether it's reified into mathematical formulas or software, is a means of making a theory operational enough that its consequences can be derived and confronted with observations.Software often starts downstream of this: it's a reification of theories, models, algorithms, or findings that are the result of research. Of course software can also be used as part of the research process itself. The distinction is roughly the familiar one between research and development.

**amarcheschi** · 2026-09-19T12:40:44.000Z：

You're goat, I'm trying to reproduce code from a paper and by following their instructions I can't even get packages to install because they conflict

**D-Machine** · 2026-09-19T07:50:23.000Z：

Yup, strongly agree with all of this, especially the RCT stuff.This has all been profoundly obvious for at least well over a decade or even two now. A consequence has been that too many serious people are driven away from academia and research, to the detriment of science generally.I've no idea what to do about all this, because people have voiced obvious and easy solutions for decades, but they are all routinely ignored.

**jegp** · 2026-09-19T18:46:11.000Z：

This seems to be strongly US-centric. In other (welfare) countries, publicly funded registries are anonymized and made available to research. For every single case. Of course, there are tons of data we don't see, but that shouldn't be an argument for not trying. The 99.99% unpublished cases is because our models/explanations/knowledge can't efficiently condense the medical mystery into a diagnosis code.Everything can be prevented given sufficient knowledge. That's not the point. The point is how to prevent as much as possible.

**D-Machine** · 2026-09-19T08:02:19.000Z：

> it's now widely expected that a high impact pub will make all data and code available for review, and then publicly available upon manuscript publicationI am also in academia and regardless, factually this is not true at all for data, not even remotely (less than like 10% of journals even have data availability policies which are recommendations, and in practice only a small percentage of papers actually make anything available), unless by "publicly available" you mean "available to some academics or academic labs after an often tedious and slow approval process requiring an academic email and various signed agreements". Maybe what you are saying is true in some very specific domains (e.g. machine learning research), but in general what you are saying here is IMO wildly out of touch with present realities in the vast majority of fields, but especially those involving human subjects.> While I have some sympathy with a lot of your bitterness, this statement is insulting silliness that a quick look at the list of Nobel Prizes in physiology and medicine would prove wrong. Almost all major breakthroughs in the applied sphere stem from decades of basic research that happened just because it interested someone.Nobel Prizes are so rare they don't speak at all to the generalizations I am making here. Also, much medical academic research is arguably successful because it is in fact ultimately industry-funded or tied to industry. It is of course though highly dependent on the academic subfield, for sure, and I was painting with a broad brush.If I had to narrow things, STEM academic research isn't so bad, so long as we exclude social science from STEM. Much social science research needs to be defunded ASAP. And I'm not claiming industry research doesn't also have warped incentives. But, on balance, I'd wager outside of pure math/physics and certain more algorithmic/pure domains in comp sci, the smartest people today are going to choose (and be found in) industry, not academia.

**jegp** · 2026-09-19T18:40:18.000Z：

Well said! And thank you for recognizing the effort.The important part here is, as you say, to light candles and insist on rigor. Coincidentally, history tells us that that also gets us further. So by pure memetic selection, this strategy should win

**D-Machine** · 2026-09-19T18:39:57.000Z：

Of course "burning it to the ground" is rhetoric and not meant literally. It is meant to convey though that "nice" and "gentle" solutions might not really be enough here.Yes, for the most part the fixes have to be in terms of funding and incentives. Funding needs to be more careful, and more careful funding can be a carrot rather than a stick here.Re: incentives, IMO we clearly need a stick: there need to be harsh negative consequences for engaging in degenerate research programs and methods that have clearly been shown to result in pathological or cargo-cult science. Null-hypothesis significance testing is one clear practice that needs to go, but building entire fields on phony / meaningless uncalibrated metrics (think: a lot of self-report instruments that are never properly calibrated to objective outcomes or real-world behaviours and/or consequences, with results being reported only as standardized effect sizes) are another more pernicious practice permeating far too many fields. Ideological bias also needs to have funding consequences. Replication issues are still only surface problems in many fields, where the research would still all be worthless even if it replicated 100% perfectly.> Your analysis completely ignores the physical and biological sciences and the humanitiesI admitted later to painting with a broad brush, and yes, it is always hard to generalize and cover everything fairly. But IMO humanities has serious ideological and methodological rigor problems as well, and is overdue for disciplining. I would tend to have stronger positive feelings toward the biological sciences generally, yes. Yes, the social sciences are the major source of the problem (in part because they are so bad they tarnish the reputation of all academia).> These fields have gotten a lot better over the past decade in the wake of the replication crisis. Preregistration, publishing all code and data, reporting null findings, replicating results, etc. are becoming the norm.IMO "a lot better" is subjective, and I don't see those things as being the norm yet (beyond as lip-service), and the rate is far too slow. I agree we'll get there eventually, but I am worried about the loss of public trust and thus the production of real knowledge if we don't try a bit harder at this. Plus, globally, countries like China do seem to be more willing to actively crack down on research misconduct, at least in the past years, and it might not be unrelated to them increasingly pulling ahead technologically in many areas.

**D-Machine** · 2026-09-19T18:43:09.000Z：

Of course, every area has similar issues. The main unique problem with (contemporary) academia is the one I mentioned:> tech and industry, where producing junk actually has real negative economic and personal consequencesIn academia, you can just endlessly produce low-quality garbage, and basically make a career out of this. In industry, things more often eventually at least have to work and survive contact with reality. Academia mostly lacks this basic check.The scientific method should be the north star, sure. Much of what is happening in academia is cargo-cult / degenerate / pathological science though.

**IanCal** · 2026-09-19T04:08:39.000Z：

Open source is much more than source available though. Its about licensing.

**altmanaltman** · 2026-09-19T05:44:26.000Z：

But that doesn't map to software at all right?

**jibal** · 2026-09-19T03:54:02.000Z：

It's not just "muddy", it's thoroughly inconsistent and impenetrable (which probably has a lot to do with why there is so little engagement here). You say "TL;DR I claim that modern science is synonymous with open source software" which is radically different from your "slightly more precise" statement.I won't put any more time into this ... good luck in figuring out what it is you really want to claim and presenting a coherent and cogent argument for it.

**jegp** · 2026-09-19T05:46:08.000Z：

Arguments are fine. Vacuous statements need grounding. The follow-up is way more detailed

**jegp** · 2026-09-19T06:03:02.000Z：

Thank you for engaging. This is a much more insightful take.If I'm reading yiur argument right, you're saying that deployed models are downstream versions (reified) of aa theory. Theory, being the actual object of science.I think this misrepresents science. Science is the ability to build testable knowledge. From that,how would you separate the test from the science? In fact, in an ideal world, why wouldn't you want your theory to be put in a format that's executable? I'm not saying that those things are always the same, my (provocative) title is based on a dream where we can imagine theory and model coexist because software is now a thing.

**D-Machine** · 2026-09-19T06:18:09.000Z：

I think it is worse than that. Science is a process for resolving disagreements, ambiguity, and uncertainty, and also for discovering abstractions (patterns) among phenomena. It is social and can not be reduced to a binary / digital file, as it is dynamic and ongoing, and, fundamentally, exploratory.Software is a static program and basically none of these things.Software development is kind of like science, in some ways, in that you discover abstractions and patterns, and this requires resolving disagreements and ambiguity between you and your users, but in the end, the user demands are usually fairly concrete and specific (though no one may know how to express those demands precisely, initially), and the process is not really exploratory in the way science is.It just really isn't a very good comparison IMO.

**ErikBjare** · 2026-09-19T08:25:37.000Z：

Which are the obvious and easy solutions?

**stalfie** · 2026-09-19T09:49:47.000Z：

I think political lobbying for legal changes might be the only realistic pathway, in that current legislation (eg. GDPR in the EU) is extremely punitive even for minor violations.I personally am trying to float using local LLMs to create anonymized case files and auto-suggest publishing cases in my hospital, which knowing how things work will probably never amount to anything.Or if you want to float truly insane ideas I guess you can shop around with blackhat groups and see if anyone has stolen some juicy records/data during all the ransomware attacks and databreaches over the years, and do some rogue scientific publishing. Obviously that's crazy, but I have to admit that the notion of pirate scientists plundering and publishing data is hilarious to me.

**jegp** · 2026-09-19T16:27:01.000Z：

I think the idea does: the point is that closed-source software isn't useful for anyone else than the (copyright)owner. In scientific standards, that is. Similar to esoteric and cryptic theories that resist accessible explanations.

**jegp** · 2026-09-19T05:47:06.000Z：

Thanks for the well wishes

**dist-epoch** · 2026-09-19T07:34:34.000Z：

> Science is a process for resolving disagreements, ambiguity, and uncertainty ... It is socialMore dramatically stated as: Science progresses one funeral at a time.> An important scientific innovation rarely makes its way by gradually winning over and converting its opponents. What does happen is that its opponents gradually die out, and that the growing generation is familiarized with the ideas from the beginning.https://en.wikipedia.org/wiki/Planck%27s_principle

**jegp** · 2026-09-19T19:09:26.000Z：

I actually disagree that software is a static program. If a program always have the same behaviour, it's a pretty bad program. You need inputs and, as demonstrated by the recent LLM inputs, parameters you can tune to correctly address a specific context.I would also contest the point about science being social. To me, science is the interplay between social constructions and physical reality. Which is why tests and experiments are so fundamental. Your point about software development as kind of like science is spot on: why not be exploratory/empirical in software development? Couldn't we imagine an LLM, say, that would go out and try to solve a question we frame? This seems strikingly close to autoresearch [1][1]: https://github.com/karpathy/autoresearch

**D-Machine** · 2026-09-19T09:08:25.000Z：

Make analysis code available. Make anonymized data available for download without people having to jump through hoops to get it. If you have highly sensitive data, release only the variables or other statistics needed to reproduce core analyses. Don't only do garbage null-hypothesis significance testing or statistical analyses on the full data, also do ML approaches were you have to actually show your analyses replicate on held-out subsets, and report this. Make reviews open (anonymizing as needed) so we can see when biased or incompetent reviewers are blocking good publications. Allow public review (or at least broader academic open review, in some form), since it is no longer defensible to delegate review and decisions to one or two random people that just happen to be emailed and have the time / are on some editorial / review board. Also allow public post-publication review. Publish null findings / results, if only in minimal forms so we don't waste time and money trying to reproduce garbage. Make articles available and don't charge insane article processing fees or open access fees of thousands of USD (especially since hosting fees are not that crazy, and also because journals don't do any of the formatting work half the time anyway, and make academics or RAs or students do all the typesetting and formatting, even though now this could all be automated with template files, mostly).Most of these things are easy to do for the majority of papers, especially in the past 20 years with the internet and modern tech and software. Plenty of frameworks exist already that have done most and/or at least some of these things, but, collectively, academia is decades behind overall.

**analog31** · 2026-09-19T13:43:25.000Z：

Ironically, Max Planck's funeral was in 1947.Disclosure: Old scientist.

**D-Machine** · 2026-09-19T19:27:01.000Z：

> If a program always have the same behaviour, it's a pretty bad programThis is false in far more cases than the cases where it is true, and even in the cases where you are right, you still usually want similar behaviour.> You need inputs and, as demonstrated by the recent LLM inputs, parameters you can tune to correctly address a specific contextYou seem very confused about what "static" means here.> I would also contest the point about science being social. To me, science is the interplay between social constructions and physical reality.Well, almost all philosophers of science would disagree with you, and IMO this sentence immediately contradicts itself.Frankly, you should really work on learning to write more coherently and carefully. You maybe have some good ideas, but they are being communicated extremely poorly and inconsistently.

## 关联链接

- https://jepedersen.dk/blog/202505_research/
