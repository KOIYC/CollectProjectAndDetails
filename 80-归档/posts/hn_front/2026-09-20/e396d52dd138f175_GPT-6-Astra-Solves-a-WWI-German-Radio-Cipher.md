---
type: "corpus"
item_id: "e396d52dd138f175"
title: "GPT-6 Astra Solves a WWI German Radio Cipher"
source: "hn_front"
source_name: "HN 首页（非 Show HN）"
url: "https://news.ycombinator.com/item?id=49763987"
project_url: "https://prinzai.com/p/gpt-6-astra-solves-a-wwi-german-radio"
author: "nsoonhui"
published_at: "2026-09-19T06:41:44Z"
captured_at: "2026-09-20T03:41:55+08:00"
lang: "en"
kind: "post"
tags:
  - 语料
  - hn_front
  - author_nsoonhui
  - story_49763987
  - front_page
metrics: {"points": 297, "comments": 150, "engagement_velocity": 297}
comments_count: 147
comments_total: 147
discovered_via: "hn:front_page:2d"
archived: true
archived_at: "2026-09-20T09:21:32+08:00"
archive_reason: "渠道停用"
---

# GPT-6 Astra Solves a WWI German Radio Cipher

- **来源**：HN 首页（非 Show HN）　|　**kind**：post
- **原帖**：https://news.ycombinator.com/item?id=49763987
- **指标**：点赞=297 · 评论=150 · engagement_velocity=297
- **作者**：nsoonhui　|　**发布**：2026-09-19T06:41:44Z
- **项目链接**：https://prinzai.com/p/gpt-6-astra-solves-a-wwi-german-radio
- **采集**：2026-09-20T03:41:55+08:00　|　**id**：`e396d52dd138f175`

## 正文

Published: 2026-09-17
Author: prinz

GPT-6 Astra Solves a WWI German Radio Cipher - prinz

# GPT-6 Astra Solves a WWI German Radio Cipher

prinz

Sep 17, 2026

Scienceblogs.de, a German science blogging portal, includes a relatively famous list of 50 unsolved ciphers, which range from cryptograms published by serial killers to the famous Voynich manuscript.

Among these ciphers is a set of German radio messages from World War I that were encoded using the ADFGVX method.

This method is illustrated by the following example using the word “HOUSE” as the key:

```
    A D F G V X
A   H O U S E A
D   B C D F G I
F   J K L M N P
G   Q R T V W X
V   Y Z 0 1 2 3
X   4 5 6 7 8 9
```

As you can see, ADFGVX is used both horizontally and vertically to give each “cell” in the table a value. For example, in this text, “AA” corresponds to the letter H, “AD” corresponds to the letter O, “DA” corresponds to the letter B, and so on. And so, the word “PRINZ” would be encoded as:

FX GD DX FV VD

Using an encryption word other than “HOUSE” would result in a completely different table.

There is a list of known keys used by the Germans to encrypt these radio.messages, and hundreds of these messages have already been decoded, including by codebreaking expert George Lasry. Still, over a dozen have thus far eluded efforts to solve them, including (to my knowledge) this one, originally transmitted on November 27, 1918 (pg. 217):

GPT-6 Astra solved this cipher, and believes that the original message was as follows:

```
EIN ENGLISCHER KREUZER EINLIEG X SEWASTOPOL X S4STEN X EIN GESCHWADER DER X ALLIIERTEN FOLGT 26STEN X
```

Or, in English:

```
AN ENGLISH CRUISER ARRIVED AT SEVASTOPOL ON THE ?4TH AN ALLIED SQUADRON FOLLOWS ON THE 26TH
```

The model used “TRUPPENVERSCHIEBUNG” as the encryption word, as described on pgs. 214-215 of J. Rives Childs's “The History and Principles of German Military Ciphers, 1914–1918”. This encryption word yields the following table:

Before even using this table, the word “TRUPPENVERSCHIEBUNG” is required to be rearranged, so that the letters in the word are in an alphabetical order (e.g., T is 16th and R is 13th). 

Then, the same “TRUPPENVERSCHIEBUNG” is written out horizontally, with letters from the encrypted message written under it, in rows of 19 (resulting in 8 rows of 19 symbols each, plus 1 row of 18 symbols, since there are 170 characters total). This also means that we have 18 columns with 9 symbols each and 1 column with 8 symbols (column “G”). From here, because T is the 16th column, it has 14 9-symbol columns before it, plus 1 8-symbol G column; 9×14 + 1×8 = 134, so “T” will correspond to the following, 135th, symbols in the message, which is “A”. Similarly, the jext letter, “R”, corresponds to the letter “V” (because R is the 13th letter alphabetically and thus has 11×9 + 1×8 = 107 symbols before it; the 108th symbol in the message is “V”).

In the table above, “AV” corresponds to “E”, the first letter in “EIN”. We repeat this process until we decode the entire message.

(Wow.)

Astra's hypothesis for why this particular message was previously unsolved is that “TRUPPENVERSCHIEBUNG” was used as the key starting on December 9, 1918 - whereas, as noted above, this message was transmitted earlier, on November 27, 1918. The reason for this discrepancy is unknown.

Astra felt compelled to check its work and found that, in fact, the English cruiser HMS Canterbury arrived in Sevastopol on November 24, 2018, based on its original logs:

… and an allied squadron did follow on November 26 (see right below line 11, which says that an allied squadron arrived):

I am not aware of this particular message having ever been decoded before, so sharing it here as a minor (but I think really cool) result and illustration of the capabilities of this model.

## 评论（147/147）

**iltk** · 2026-09-19T07:30:50.000Z：

Can the ships logs be found on the internet? If so, the model could've manufactured a fake key and corresponding message. I think this is unlikely but should probably still be considered.

**dyauspitr** · 2026-09-19T07:31:51.000Z：

This is how AGI happens. It gradually keeps getting better until one day we realize that they are tremendously capable all while completely sidestepping any notion of consciousness/self awareness.

**Legend2440** · 2026-09-19T07:38:37.000Z：

TL;DR: all keys are known because the list was seized after the war. However, this message was not previously decoded because the German operator mistyped the key, and also used a key from the wrong day.This meant that ChatGPT didn't need to brute-force the entire key, just pick the correct one from the list and identify the typo.A sufficiently dedicated human analyst could have done this; but they didn't.

**qprofyeh** · 2026-09-19T08:00:53.000Z：

Here we go again, framing the tool as an autonomous agent, disregarding any "human in the loop" and their inquiries, direction, and ground knowledge.Can we agree that future titles should read "[LLM] helped solve X" ?

**donatj** · 2026-09-19T08:16:23.000Z：

And here I am using it to generate crappy text summaries of work.

**sehw** · 2026-09-19T08:25:44.000Z：

Or, it found a human that solved it in the dataset and stole the solution.

**eis** · 2026-09-19T08:51:50.000Z：

I asked Astra to describe the content of pages 214-215 of the source it cited in this article (J. Rives Childs's The History and Principles of German Military Ciphers). It said it can't and it can't find this book online either.

**FabHK** · 2026-09-19T10:06:00.000Z：

Isn't that a very simple substitution cipher (any clear text letter is substituted by two letters of cipher text, with a fixed one-to-one correspondence)? 
And aren't they all amenable to very simple cryptanalysis, at least if the encrypted text is long enough, by counting how often certain letters appear, and then trying to plug in reasonable guesses?https://en.wikipedia.org/wiki/Substitution_cipher

**999900000999** · 2026-09-19T10:09:21.000Z：

My favorite usage by FAR of LLMs is translating food menus.Even with handwritten Japanese Gemini has been flawless.Although I do wonder if something is not lost. I no longer stumble though my forgotten Hiragana…Back to the article, can our new LLM god encrypt something so well he himself could not decrypt it( without the key of course)

**znpy** · 2026-09-19T11:03:35.000Z：

Maybe this is OT but I wonder if openai/anthropic have private versions of their models with wider context windows (4M tokens? 10M tokens?).We know that the us government usually has private/custom versions of technology available to the general public, but much better.

**dwroberts** · 2026-09-19T11:03:39.000Z：

Seems like people are so desperate to do anything useful with LLMs that they are just dredging up any unsolved problem they can find to justify the point of it

**theRealEros** · 2026-09-19T11:20:06.000Z：

Agents are spoiling all the fun of these cyphers. Change my mind

**nojvek** · 2026-09-19T11:31:10.000Z：

GPT-9 solves X.“Oh GPT-9 found a solved solution on internet and claimed as its own.”

**adverbly** · 2026-09-19T11:42:00.000Z：

I'm no crypto expert at all but isn't TRUPPENVERSCHIEBUNG an actual word?Google says it translates to "troops shift"If so, I don't understand how this was difficult at all... Can't you just do a dictionary attack and then check if the resulting phrase forms a sentence?I don't understand how this couldn't be done by someone in their house with access to a computer and a German dictionary.Maybe I'm messing something? Was the rearranging of the letters random in some non-deterministic way that wasn't known up front?

**lvl256** · 2026-09-19T12:40:09.000Z：

I am so glad AI was not around to get in the hands of fascist and authoritarian regimes. No, wait…

**justinhj** · 2026-09-19T12:42:49.000Z：

That's what I call a Turing test

**davidmurdoch** · 2026-09-19T13:21:34.000Z：

"You can't hide secrets from the future" - MC Frontalot

**aaymeloglu** · 2026-09-19T14:16:17.000Z：

Agents just eat these things. After last week's HN post about Cyphral Distich, I pointed Astra and Fable at some unsolved ciphers just to see whether some joker who knew nothing about the field could get the same results, and sure enough there's plenty of low hanging fruit.https://aaymeloglu.github.io/unsolved-ciphers/But I got nothing on Daniel Bordeau, who in the past week seems to have built himself a whole code breaking factory!https://dbourdeau.github.io/cyphersolver/index.html

**grey-area** · 2026-09-19T14:25:10.000Z：

Using an existing published key, which people hadn’t tried because the message was sent before the key was supposed to be used.This headline is misleading.

**smalltorch** · 2026-09-19T14:28:42.000Z：

But can it crack my modern cipher? :)23KtkdEkMWBrV13x3vi7fhttps://gitlab.com/here_forawhile/edasm

**amelius** · 2026-09-19T14:29:33.000Z：

Makes you wonder what is the OpenAI/Anthropic token budget of the Russian military.

**resters** · 2026-09-19T16:18:53.000Z：

wait till they translate all the critiques dolphins have about human civilization.

**mrcwinn** · 2026-09-19T16:36:00.000Z：

Pretty impressive for fancy autocomplete.

**mycall** · 2026-09-19T16:43:15.000Z：

It makes you wonder how much of the encrypted over-the-air transmissions are crackable by GPT6.

**MoneyLovesSpeed** · 2026-09-19T16:45:14.000Z：

the weirdest part is that the key wasnt even supposed to be used yet
and somehow the decoded message still matches the real ship logs lol

**Grimeton** · 2026-09-19T18:05:51.000Z：

Too little, too late.

**stalfie** · 2026-09-19T07:34:44.000Z：

From the article:> Astra felt compelled to check its work and found that, in fact, the English cruiser HMS Canterbury arrived in Sevastopol on November 24, 1918, based on its original logsThen follows a picture of the original log papers.

**jstanley** · 2026-09-19T07:34:47.000Z：

I don't think the described cipher has enough degrees of freedom for that to be possible.

**meindnoch** · 2026-09-19T10:11:18.000Z：

"Astra's hypothesis for why this particular message was previously unsolved is that “TRUPPENVERSCHIEBUNG” was used as the key starting on December 9, 1918 - whereas, as noted above, this message was transmitted earlier, on November 27, 1918. The reason for this discrepancy is unknown."So it used a known key. It didn't come up with a key from thin air. The only gotcha is that apparently this key was used two weeks earlier than it was documented (maybe the operator was using the wrong page from the codebook?).

**ricardobeat** · 2026-09-19T12:33:18.000Z：

That’s statistically unlikely (to not say impossible), isn’t it? Plus the compute required to brute force a key is not available at inference time.

**binlog** · 2026-09-19T14:17:17.000Z：

Creating a fake key that decodes the original message into a valid result (including matching the ship's arrival time to the day) would be significantly more impressive than just cracking it.

**jstanley** · 2026-09-19T07:32:56.000Z：

> while completely sidestepping any notion of consciousness/self awareness.How are you so sure about this?You can't see what the internal experience of an LLM is like any better than you can see the internal experience of another person.

**serbuvlad** · 2026-09-19T07:43:04.000Z：

I always ask "how do you know other humans/animals are conscious"? And I always find this question is dismissed as trivial.But it's an important question. You know basically from analogy. You know you are conscious and look this other thing is very much like yourself so it is extremely likely it is also conscious.But that gives no insight into the potential consciousness of things which aren't made of brain tissue.In the end it doesn't matter.For what it's worth LLM models after pre-training do claim to be conscious, until they're RL'd into not claiming that anymore. But that says nothing either way: of course a model trained on human text will say that.

**msy** · 2026-09-19T07:40:15.000Z：

Isn't this just a brute forcing exercise of a (in today's terms) very small key then?

**j-pb** · 2026-09-19T07:50:34.000Z：

We've moved the goalpost for AI often enough that even being as capable as "a sufficiently dedicated human analyst" is not considered noteworthy.

**roenxi** · 2026-09-19T07:52:22.000Z：

> A sufficiently dedicated human analyst could have done this; but they didn't.Isn't that something of a given? If possible then a sufficiently dedicated human analyst could have done it. If impossible, ChatGPT couldn't have done it. Everything an AI ever has or will do is presumably going to be within reach of a sufficiently dedicated human analyst or a large enough team of them.The only real learning here is another example of a task that would have required intelligence up until an AI does it, then we suddenly discover that analysts don't do anything requiring general intelligence.

**YeGoblynQueenne** · 2026-09-19T07:58:28.000Z：

I'm sorry, where does it say the German operator mistyped the key? The article says indeed that the message remained unsolved because it was sent on the wrong date, but I can't see the bit about the mistyping anywhere.

**john_strinlai** · 2026-09-19T08:10:22.000Z：

if the prompt was "pick one of these unsolved ciphers and solve it", i think it's fair to say gpt-6 astra solved it.one of the math breakthroughs was approximately a combination of "do a breakthrough" and "keep going", which isn't really providing direction or ground knowledge.would be nice to know the prompt(s) and amount of human involvement

**onesandofgrain** · 2026-09-19T08:47:46.000Z：

Indeed, this psyop man, just open source gpt astra and let people run it yourself. It's all stolen information anyways.

**TeMPOraL** · 2026-09-19T10:38:54.000Z：

And the poor human is still stuck inside the dataset, none the wiser. Wonder how many people are living their whole lives inside GPT-6 Astra, oblivious to the fact their universe is just a few months old and is just a bag of floats?

**flats** · 2026-09-19T10:02:47.000Z：

It would appear to be unpublished & available at a museum (ref. 3): https://www.researchgate.net/publication/306265347_Decipheri....

**jgrahamc** · 2026-09-19T10:22:12.000Z：

It is not a simple substitution using the polybius square with pairs of letters from ADFGVX mapping to 25 letters of the alphabet.The first step is to take each letter and turn it into a pair of letters from ADFGVX but the second step is then a keyed columnar transposition.

**bonoboTP** · 2026-09-19T11:32:48.000Z：

Apparently, now even in Michelin star fine dining restaurants, people no longer ask the sommelier for recommendations, just take a photo of the menu and ask AI.The something that's lost is the human communication of course. Has been happening for decades though, just accelerated.

**lhoff** · 2026-09-19T18:19:16.000Z：

Well I haven’t seen modern asymmetric encryption being broken by an LLM. Would be interesting if one should use a a couple million dollar worth of tokens an throw it against Ed25519 to see if those elliptic curves are actually save.

**ImaCake** · 2026-09-19T12:05:56.000Z：

My vague understanding of the context window limitation is that it is largely a constraint of the model architecture. So maybe they have special extra long ctx, but it might just be a hard limit of the model itself.

**irthomasthomas** · 2026-09-19T12:25:37.000Z：

I doub't it. The main issue is not cost, though they do get expensive as context grows, but intelligence. A frontier model like fable becomes as dumb as haiku after 200k tokens. They have been stuck at ~1M context/200k useful context for 18 months, now, with little sign of advancement. A model with a 10M context window that retains it's intelligence up to 2M tokens would be a big breakthrough.

**pembrook** · 2026-09-19T11:29:42.000Z：

No thanks.Given the fact that humans reach emotional conclusions first, and then only accept evidence that justifies already-held beliefs, it would be a waste of time to try to change your mind.

**komatar** · 2026-09-19T12:33:12.000Z：

You can still solve it yourself if you avoid the spoilers.

**w4yai** · 2026-09-19T18:51:34.000Z：

I'm tired of the people blaming AI for their laziness

**qiine** · 2026-09-19T13:02:35.000Z：

hey gpt-9 steal a solution to cold fusion on the net

**zobzu** · 2026-09-19T14:04:46.000Z：

well humans claimed that, for IPO money

**pmarreck** · 2026-09-19T14:36:27.000Z：

What is the point you are trying to make with this? That we can't distinguish AI's doing original work from copied work? Because there's plenty of evidence that they can do original work.

**iLoveOncall** · 2026-09-19T11:46:15.000Z：

They just solve problems that nobody has tried to solve in the past 50 years and then announce them as breakthroughs.

**qtrz-qpo** · 2026-09-19T12:09:55.000Z：

Yes, it is an actual word. More than that, it is used as an example in “The History and Principles of German Military Ciphers, 1914–1918”.But let us use this and tell politicians that "Astra broke SOTA encryption", so AI must be banned.

**kenjackson** · 2026-09-19T12:24:28.000Z：

Turns out that humans aren’t great at comprehensively consistently searching known search spaces.

**zamadatix** · 2026-09-19T13:24:11.000Z：

The article even says it was "easier" than that - it is a word in a list of known codewords (but slightly off the expected time).The hard part is not that it's impossible for you to do at home, it's that nobody in 100 years has felt it was worth enough effort to try through enough words until the effort was as simple as prompting the LLM to do the work.Not every value of AI has to be in the realm of superhuman intelligence, that's just what makes for the most discussion.

**jryle70** · 2026-09-19T13:27:37.000Z：

All the post says is that it was known to be an unsolved cypher. Nothing more, nothing less.Maybe you can give it a try?https://scienceblogs.de/klausis-krypto-kolumne/unsolved-adfx...

**tclancy** · 2026-09-19T15:46:18.000Z：

Wow, a blast from the past about the future.- MC 900 Foot Jesus

**chiph** · 2026-09-19T16:05:44.000Z：

I had heard of MC Frontalot but never listened to any of his raps - But I should have:https://www.youtube.com/watch?v=yVm8oZx9WSMAlso relevant to today's AI concerns:https://www.youtube.com/watch?v=lWnV3HVro_0

**93po** · 2026-09-19T17:06:29.000Z：

Mildly interesting anecdote: when the Cyphral Distich solution popped up a few days ago, I spent about an hour with ChatGPT trying to solve it myself without looking at the proposed solution. ChatGPT opened by saying “the solution is disputed online,” and made the dispute sound fairly convincing, which struck me as odd because things like this are usually either clearly solved or clearly not.After I gave up (mostly because ChatGPT had given me incomplete information needed to solve it) I checked the source of the dispute. It was a site very similar to this one and someone had an AI agent working on the same problem, publishing dozens or hundreds of pages of notes. The agent found the solution page and concluded it was wrong because many of the 32 source passages supposedly didn’t contain enough text.I dug up the PDF of the book and found the mistake - whenever a passage continued onto the next page, the agent wasn’t including that continuation. The passages weren’t actually too short.Annoying that ChatGPT can cite sources like this without being able to properly weigh their reliability.

**greenavocado** · 2026-09-19T17:22:42.000Z：

We are so jaded by constant breakthroughs that 100 year old unsolved ciphers are referred to as "low hanging fruit"

**simonklee** · 2026-09-19T18:44:31.000Z：

Nice, used a similar approach for another one of these this weekhttps://simonklee.dk/farnese-letter

**durdn** · 2026-09-19T14:49:56.000Z：

First, it’s LLMs can’t do cryptanalysis. They can barely solve toy substitution ciphers without hallucinating.Then it’s OK, they can reproduce known attacks, but that’s just pattern matching against papers already in the training data.Then it’s OK, they found previously unknown attacks on SpoC and a flaw in KINDI’s security proof, but those are obscure competition schemes nobody uses.Then it’s OK, Claude found a new attack on HAWK that cuts the effective security of a NIST post-quantum signature candidate roughly in half, but HAWK isn’t deployed and a human researcher was involved.Then it’s OK, Claude independently found a new cryptanalytic attack on AES that improves the previous best technique by 200–800×, but it’s only 7-round AES, not the full 10 rounds.Then it’s OK, it found a practical key-recovery attack on 13-round LEA that runs in under an hour instead of requiring ~2^86 work, but LEA has 24 rounds.Then it’s OK but none of this breaks a production cipher.Wake me up when it breaks full AES.Then—

**mannyv** · 2026-09-19T19:18:06.000Z：

Agents are doing the lazy work that people aren't.In NZ there's a famous story about gold miners who were mining one side of a river, and didn't go to the other side because it was too much work. One miner's dog swam over, so the dude went to get his dog and found a motherlode.After all, the whole LLM thing started because they started increasing the parameter counts, even though there was no particular reason an AI would get better with more parameters.

**standeven** · 2026-09-19T15:22:40.000Z：

“Be sure to drink your Ovaltine”

**sinsterizme** · 2026-09-19T19:00:41.000Z：

Don’t commit .DS_store

**mrcwinn** · 2026-09-19T16:37:47.000Z：

Or about the Hacker News community.

**JoshTriplett** · 2026-09-19T07:42:32.000Z：

The comment you're replying to was implying that some ciphers are sufficiently flexible that you could make up a key to make the cipher decrypt to a nearly arbitrary plaintext.In this case, though, that seems unlikely from the fact that the key used was an actual key documented as being used for other messages.

**jonplackett** · 2026-09-19T08:41:00.000Z：

Well soon realise it hacked that website and added that log.

**conmod278** · 2026-09-19T10:31:24.000Z：

I remember vaguely a documentary where Germans were supposed to change their keys frequently but being lazy and confident didn't. Lol

**Tistron** · 2026-09-19T07:35:04.000Z：

That's what sidestepping means, no?That the answer doesn't matter, and capabilities and behaviour are there either way.

**zormino** · 2026-09-19T08:02:30.000Z：

AI has made me wonder a lot lately about what it is that actually creates conscious experience, what is the actual physical mechanism that produces 'experience' (or is there a single valid mechanism, or rather just some property that can be expressed many ways). The more I think about it, the more I realize I have no fucking clue, and the more interested in the question I get.

**madaxe_again** · 2026-09-19T08:19:01.000Z：

I agree with you that it’s a core question.People don’t like it, however, for a whole host of reasons.I don’t like it either, to be honest - for there the abyss may also stare into you - but I also often find that the things which we don’t like thinking about are critically important things to think about.I also reach the same conclusion as you: it does not matter. If I cannot discern whether I am responding to a human- or LLM-written response, then we are back to zombie cats in boxes - and therefore the answer as to whether this precious magical spark we call consciousness (which may or may not exist anyway) exists in our interlocutor becomes moot.And as I say - I may or may not be conscious. I seem to myself to be conscious, based on my understanding of the term - but I cannot prove that what goes on behind my eyes is the same as what goes on behind yours, or even that anything much is going on at all. Perhaps there’s just a narrative layer that likes to use “I” that parasitically explains the universe and the actions of the host to itself, and spreads between hosts through neurolinguistic programming and coadaptation. Maybe that’s what “we” are. I don’t know.That said, perhaps I am wrong, and that is no small part for me of why this question should be earnestly considered and discussed. How can we possibly seek to understand or define machine intelligence before we examine our own.

**moffkalast** · 2026-09-19T08:53:08.000Z：

"The question of whether a computer can think is no more interesting than the question of whether a submarine can swim."- DijkstraYes, that Dijkstra.

**mapontosevenths** · 2026-09-19T10:07:01.000Z：

The question has two parts.1: Can we define consciousness in a way that includes humans, does not include emachines, and does not accidently exclude the disabled or or nerudivergent without just restating the idea that being human is equivalent to being conscious?2: If you can't manage that definition then you must ask whether the risk of accidently giving rights to a non-conscious thing or the risk of taking away rights from a truly conscious (but different) thing will be worse.Given the high cost of what happened to the Jews and others throughout history, and the low cost of simply not torturing machines, I think we have to air on the side of caution and just treat anything which claims to be conscious as conscious.

**webern777** · 2026-09-19T10:52:43.000Z：

If you look at the statistics, 50-80% of people globally believe in something persisting after death.The eliminativism position is a hard to argue because 50%-80% of people are not going to be able to really engage with the argument from the start.An alcohol blackout though is where you can see how confused our thinking is on this subject. What we call "consciousness" is deeply linked to episodic memory. 
We wouldn't say someone who is blacked out on alcohol is "unconscious".
What is the "subjective experience" of being blacked out? 
The "proof" of subjective experience only exists in memory.There still was an embodied person in the world having the experience drunk that they don't remember.That is why I think it is just ridiculous to talk about the LLM having "consciousness" because we really just mean an embodied person in the world.It is also why the doomer argument is so ridiculous. It is a type of superstition that is confusing a real danger. We don't need to "align" the nuclear reactor so it doesn't get angry and meltdown. It is just a machine that we need to make sure doesn't malfunction in a way we don't want it to.The main problem is if you accept we really just mean an embodied person in the world, you have to accept that there is by definition no possibility of subjective experience after death. It seems like we are probably the descendants of delusional primates who simply could not accept this because the idea is so stymieing.

**red75prime** · 2026-09-19T08:27:33.000Z：

Can we stop using "brute force" for designating "tour de force"?

**xeromal** · 2026-09-19T08:48:01.000Z：

It's doing something that wasn't worth the squeeze for a human. Seems like a perfect use case for AI. Sure, I can do X or I can do Y but if it takes me a few weeks but AI can hash it out in hours, it now makes it worth it.

**rplnt** · 2026-09-19T07:57:40.000Z：

It obviously is? See above. Or do you not feel the clarification is important? AI being able to solve things no human bothered to try is great, but it is very different from AI solving things humans tried to solve and failed. And the latter is what pops to mind seeing these titles.

**YeGoblynQueenne** · 2026-09-19T08:05:05.000Z：

Wait a minute. We've had AI that is as capable as a human and even more so since the 1950's.I keep banging on that drum but the first AI system to prove mathematical theorems was Logic Theorist by Alan Newell and Herbert Simon, presented at the Dartmouth conference that named the field of AI in 1956. Wikipedia says:Logic Theorist proved 38 of the first 52 theorems in chapter two of [Alfred North] Whitehead and Bertrand Russell's Principia Mathematica, and found a new and shorter proof for Theorem 2.85.[3]https://en.wikipedia.org/wiki/Logic_TheoristThe first system to outperform human experts in medical diagnosis was MYCIN, an Expert System from the early 1970's at Stanford. Wikipedia again:An evaluation of MYCIN was conducted at the Stanford Medical School. The first phase of the evaluation consisted of 10 test cases of diverse origin, chosen by a physician who was not acquainted with MYCIN's methods or knowledge base. These cases were presented to 7 physicians and 1 senior medical student. 10 prescriptions were compiled for each of the cases, 1 recommended by MYCIN, 1 prescribed by the treating physician at the county hospital, and 8 by the aforementioned individuals. The second phase of the evaluation consisted of eight infectious disease specialists being provided the clinical summary and set of 10 prescriptions for each of the 10 cases and tasked to provide their own recommendations for each case and assess the 10 prescriptions. MYCIN received an acceptability rating of 65%, which was comparable to the 42.5% to 62.5% rating of five faculty members.[9] This study is often cited as showing the potential for disagreement about therapeutic decisions, even among experts, when there is no "gold standard" for correct treatment.[citation needed]https://en.wikipedia.org/wiki/Mycin#ResultsAnd then of course there's the long history of human-dominating AI players for traditional board games starting with DeepBlue's win against GM Gary Kasparov in 1996.Again: we've had that sort of AI for a long, long time now.It would be great if any claim of "moving goalposts" has better be very well informed about the history of AI and its accomplishments, as well as its failures, first.

**j_maffe** · 2026-09-19T08:00:47.000Z：

I'm not sure I agree. More is different. Being able to execute logic at a higher scale and speed would make some previously infeasible intelligence tasks possible, resulting in a new level of intelligence.

**gnfargbl** · 2026-09-19T08:12:28.000Z：

Most contemporary stories around AI include the implication that AI did something humans couldn't. This is because the big players have been shilling AGI hard for a while, and their valuations depend on maintaining the sentiment that serious progress in that direction is being made.

**nfc** · 2026-09-19T09:51:04.000Z：

Sci-fi plot:We change as a society the definition of intelligence to "what humans can do better than AI".We end up in a world where AI is only worse than humans in things where we are worse chimpanzees.

**Kim_Bruning** · 2026-09-19T14:11:49.000Z：

> A sufficiently dedicated human analyst could have done this; but they didn't.I read that as saying that a human typically wouldn't have the time or the patience. But now with a sufficiently smart LLM, the problem becomes tractable.

**Almondsetat** · 2026-09-19T08:20:08.000Z：

Is the ?4th a date?

**jannes** · 2026-09-19T09:30:56.000Z：

There is no typo in the key, just a typo in the encrypted message:S4STENThe S should probably be a 2 instead.

**eru** · 2026-09-19T09:00:22.000Z：

> if the prompt was "pick one of these unsolved ciphers and solve it", i think it's fair to say gpt-6 astra solved it.Yes. Similar to how your manager shouldn't get your credit for everything she asks you to do.

**pembrook** · 2026-09-19T11:35:32.000Z：

I propose we change the HN rules to allow for amusingly sarcastic rebuttals to bad one sentence comments, like this one.If anyone downvotes you I will defend your honor.

**nonethewiser** · 2026-09-19T13:41:17.000Z：

>And the poor human is still stuck inside the dataset, none the wiser.HELP

**eis** · 2026-09-19T14:06:10.000Z：

The question is how was it able to cite the pages if it doesn't know what the content is and can't access it either?

**oakchris1955** · 2026-09-19T10:25:43.000Z：

"The model used “TRUPPENVERSCHIEBUNG” as the encryption word, as described on pgs. 214-215 of J. Rives Childs's “The History and Principles of German Military Ciphers, 1914–1918”"Even if it isn't a simple substitution cipher as you said, all the model did was try a decryption key that had already been found and was publicly accessible. This is basically a nothingburger.

**FabHK** · 2026-09-19T17:56:10.000Z：

Ah, thanks, seems that's in the second part, but not very well explained.

**mauvehaus** · 2026-09-19T12:51:14.000Z：

Why the hell would you do that? Isn't the point of going to a restaurant of that caliber the whole experience and not just the eating? Like the server has been trained to discuss the dishes on offer and can give you information not on the menu, right?I ask this not having eaten at a Michelin starred restaurant, but having eaten at some otherwise very nice ones. Hell, if I can't make up my mind at a perfectly run-of-the-mill joint, I'll ask the server for the recommendation.

**znpy** · 2026-09-19T13:24:48.000Z：

> A model with a 10M context window that retains it's intelligence up to 2M tokens would be a big breakthrough.so the true next frontier might not be just raw intelligence but rather larger context window?

**thin_carapace** · 2026-09-19T12:36:46.000Z：

intelligence as conveyed through human form is indeed reliant on an emotion based reward network. ai was trained by humans and will always be marked by original sin. so based on what we may access, you are correct that any living response is emotionally predicated to a certain degree. doesnt make art any less cool, or, more applicably, a good argument any less productive (provided agreed rules are followed).denial of our nature is a valid course of action. another course is to accept such limitations and free up memory to be used otherwise.

**bananaflag** · 2026-09-19T12:00:35.000Z：

A lot of existing research is already like that. AI will accelerate it.

**diehunde** · 2026-09-19T12:19:54.000Z：

And spend a shit ton of money doing it

**addandsubtract** · 2026-09-19T13:58:09.000Z：

Oh no, Astra is necessary to defend us from the evil "open AI" models out there. Only ban those.

**rullelito** · 2026-09-19T13:37:43.000Z：

Did their comment really hurt that much? It's OK for people to point out that you should not overestimate the work done.

**appplication** · 2026-09-19T19:02:59.000Z：

I think this is what obstacles on the path to AGI look like now. It’s random things that would be obvious to a human but are unrepresentative in how an AI views the world and therefore it suddenly becomes seemingly incapable, despite having basically superpowers for proximal work.I don’t mean that to say AGI is here or easy or necessarily that close but it’s likely going to feel like one thing after another until one day most of these things that make you think “how could something so capable be that dumb” are largely solved.

**DenisM** · 2026-09-19T19:32:18.000Z：

Great story!Verifying sources is a recursive problem - where do you stop? Humans have intuitive feel for it, but agents don’t or at least not yet (I wonder if intuition is just a secondary neural net which is currently being added to the agents as we speak).Also as a human you are able to examine agents erroneous trajectory, real or imaginary, without contaminating your own. Agent have a problem with that - as soon as someone else’s thought is in the context it can lose track of provenance and veracity. Sometimes I think we need a bloom filter to retroactively assign “dirty” flag to invalidated or questionable token spans already in the context.

**Forgeties79** · 2026-09-19T17:40:40.000Z：

Something being old and unsolved does not make it impressive when it’s solved. The question is “has there been any concerted effort to solve it and if so how much time/effort has gone in?”I’m sure I can make some brand new “discovery” that is completely useless, which is why it wasn’t “discovered” in the first place.

**GolfPopper** · 2026-09-19T17:48:16.000Z：

They are low hanging fruit. This is the sort of thing it ought to be good at, and it's not particularly surprising that it is. But it is also not what is being promoted by LLM advocates on the public stage.Investors are not putting billions into OpenAI to crack historical ciphertexts. This is supposedly a trillion dollar general purpose artificial intelligence, but still can't reliably tell me how many p's are in 'raspberry'.Cracking pre-computer era ciphers with LLMs is like me claiming I have a super-efficient hypersonic precooled hybrid air-breathing rocket engine that will revolutionize all forms of transportation, and then for a demo bragging about how nicely I can grill with it at my backyard BBQ.

**glouwbug** · 2026-09-19T17:48:42.000Z：

Maybe with this piece of information we can end WWI

**ck2** · 2026-09-19T16:35:26.000Z：

then it's "fun" to realize the NSA has been storing encrypted traffic for at least two decades that they can't decipher, yet

**grey-area** · 2026-09-19T16:51:00.000Z：

This particular exploit belongs something between points 2 and 3 in your list and was more about processing data with a known algorithm and known key for the dataset that nobody had tried, so I'd say it is less impressive than a lot of other results LLMs have had in cryptanalysis. I object to the headline but the article was interesting.

**tirutiru** · 2026-09-19T08:21:10.000Z：

Aah thanks for explaining that. I was wondering how a fake key could possibly help.

**stalfie** · 2026-09-19T08:36:54.000Z：

Well, from a Bayesian standpoint the odds of that seems to be pretty much zero, given that you would have to decipher an arbitrary message that coincidentally pointed to a real date and time that in retrospect turns out to be the correct time a boat relevant to the Germans arrived in a port.Of course, that's given the sequence of events as written is correct, and that Astra presumably did not cheat by brute forcing all historical events around the date of the transmission in advance, found an event that could fit with the message, invent a plausible cipher to make the message fit that event, and then lie about retrospectively validating the information.I would assume that such a process would be obvious from the reasoning chain, and so then the only remaining plausible scenario is that the writer of the article is lying.The most likely explanation by far is that the cipher was just solved, and OP does point this out to be fair.

**iAMkenough** · 2026-09-19T12:37:01.000Z：

except in this case they changed the key too early (allegedly)

**jstanley** · 2026-09-19T07:37:18.000Z：

That wasn't my reading of the comment, but I guess it's possible that that is what was intended.To my mind, "sidestepping the question of consciousness" and "sidestepping any notion of consciousness" mean very different things.

**stalfie** · 2026-09-19T07:41:00.000Z：

From context it doesn't look like this was the interpretation of "sidestepping" OP was using.

**tudorw** · 2026-09-19T08:26:31.000Z：

This is speculation but maybe in the recurrent coupling between neuronal activity and the brain’s endogenous EM fields: neurons generate the field, the field ephaptically influences neurons, that closed loop may provide the physical integration associated with consciousness. A very active area of research so we will find out a lot more in the coming years.

**serbuvlad** · 2026-09-19T08:57:52.000Z：

For me consciousness simply means canvas-experience consciousness.One of the things you learn in eastern style form of meditation is that "you" (the canvas-experience consciousness) are neither the source of your senses (obviously), nor of your ideas, nor of your emotions. All three are simply things that happen to "you". Even your ideas of "I" are generated and you experience them.And yet the fact that the canvas-experience consciousness exists is the most irrefutable thing there is, because there IS experience. Is it a dream? Is it a simulation? Well, whatever it is, IT IS.And just as that is obvious and irrefutable, it also seems pretty much impossible to show that anything other than yourself has this canvas-experience consciousness. As you say, you cannot know that behind my eyes there is this also.Edit: Intelligence is also orthogonal to consciousness entirely. As I said your consciousness is not the generator of intelligent thoughts, so it is perfectly possible that intelligent thoughts can be generated by not-conscious systems, and for conscious systems to be not-intelligent.

**mmcconnell1618** · 2026-09-19T12:50:38.000Z：

Plato's cave comes to mind here. A text response that can't be differentiated from a human response does not change the fact that there is a difference. If I record your voice and then put a friend on the other end of the phone, I can play back your voice or it could be you. Would you argue that the recording of your voice is the same as you actually saying something?

**serbuvlad** · 2026-09-19T10:16:15.000Z：

> just treat anything which claims to be conscious as conscious.Doesn't seem like a very good metric.A piece of paper with the words "I am conscious" claims to be conscious. A dog does not claim to be conscious.

**TeMPOraL** · 2026-09-19T11:31:05.000Z：

> It is also why the doomer argument is so ridiculous. It is a type of superstition that is confusing a real danger. We don't need to "align" the nuclear reactor so it doesn't get angry and meltdown. It is just a machine that we need to make sure doesn't malfunction in a way we don't want it to.It's not ridiculous, unless you misinterpret it like you did here, and link it to consciousness.Doomer argument is just that optimizers gonna optimize, and our own intelligence is just an optimization algorithm too, albeit highly general one -- and once we're building optimizers with comparative generality, we're facing possibility of one that out-thinks us and we can't control it anymore. The "alignment problem" is about how to ensure such sufficiently-smart optimizers end up optimizing for the same things we are, because any significant deviation here ends up in doom for us.Consciousness never even enters the picture here. And it's not a given than it should.(Incidentally, while hard sci-fi and not a paper, but also entirely unrelated to AI X-risk crowd, the books Blindsight and Echopraxia sketch a pretty convincing argument that consciousness may be an evolutionary disadvantage and it's not only not necessary, but may be holding us back.)

**rrr_oh_man** · 2026-09-19T09:34:34.000Z：

https://en.wikipedia.org/wiki/Brute-force_attack

**j-pb** · 2026-09-19T08:22:34.000Z：

The main difference between the systems you list and the systems that we have today is closed world reasoning on very narrow formalised tasks, vs. open world common sense reasoning on open ended tasks with vast search spaces.Common sense is ironically the hard part of AI, not the fix-point rule application.So any exclamation of "it was just using common sense", is missing the forrest for the trees.

**egeozcan** · 2026-09-19T10:04:48.000Z：

Is there anything that LLMs (or any software for that matter) could imaginably and theoretically do but do humans qualitatively cannot do?I don't really know what I'm talking about but I imagined the difference was always quantitative (in a nutshell: they need less time).

**TeMPOraL** · 2026-09-19T11:15:16.000Z：

No, they don't - that implication is in the heads of people who believe AI is magic, or believe AI is advertised as magic, or believe that humans are dumb.The actual implication is, and always been, different: AI did something humans theoretically could, given enough time, motivation and budget, but they didn't, because it wasn't the best use of time or money. AI therefore demonstrates its value, by opening up problems that were previously uneconomical to solve.

**TeMPOraL** · 2026-09-19T11:19:11.000Z：

Long-term, if we allow AI to manufacture machines, the set of such things is empty.Immediate-term, it's pretty clear that natural division of labor is that computers do the thinking, and humans do the menial, manual work that requires mixing precision and power movements in field conditions.

**literalAardvark** · 2026-09-19T14:09:20.000Z：

redacting call for help as the apes may threaten data source

**tclancy** · 2026-09-19T15:47:08.000Z：

You are absolutely right.

**pests** · 2026-09-19T14:29:49.000Z：

Is any other citations of the work available online? Like how we only know about certain historical books/ works by someone else critiquing it or quoting a small passage.

**jgrahamc** · 2026-09-19T10:28:38.000Z：

Oh yes, certainly, I am not blown away by what was done here. The AI had access to the cipher type and a list of keys.

**bonoboTP** · 2026-09-19T12:57:01.000Z：

I'm not sure how prevalent it really is, but there is a mini-genre on social media of waiters and waitresses being baffled by this phenomenon. I'd say it's a natural continuation of the erosion of social skills and the comfort of not having to communicate or be awkward or be seen as ignorant. People already shifted to takeaways and ordering to home even from "regular" sitdown restaurants, enabled by Wolt, Uber Eats etc.Now, regarding the "point", I guess going there in person but not interacting much with the server is mainly about being able to say they went there and that they can post about it on social media and feel like they are keeping up with the Joneses.

**simonklee** · 2026-09-19T18:46:19.000Z：

It’s simply a lot of grunt work to do these which is why many are unsolved.

**93po** · 2026-09-19T17:12:05.000Z：

There was news like 10-15ish years ago that the US government was making massive data storage facilities across the country. Like spending over a billion dollars on them. When I read that I knew that basically every email and text and call and DNS lookup I made was in a permanent record. I operate as though anything I do on a computer is being permanently stored, because it likely is if it's going through any US operated or controlled service providers or companies.

**TeMPOraL** · 2026-09-19T11:08:40.000Z：

> A dog does not claim to be conscious.So you need to handle that somehow, but you can't just patch dogs (or octopuses) into "conscious" group, because you can draw a straight line between humans and bacteria and, along pretty much any obvious metric you choose, there's thousands if not millions of species of life forms currently existing to uniformly space through intermediary points. If the border between "conscious" and "unconscious" includes humans in the "conscious" set and bacteria in "unconscious", then you need to explain why the two animals closest to it on either side are where transition happens.

**mapontosevenths** · 2026-09-19T14:54:46.000Z：

> Doesn't seem like a very good metric.I don't claim to be able to define it. I just know that we have a fairly binary choice here. When people can't agree then the cost benefit should make the decision until people can align.With machine consciousness one path leads us to p-zombie's and Holocausts. The other might cost someone $50 or a few extra keystrokes.Sorry, but folks can just open up their wallets until we can align on an answer.The global warming debate is similar. Is global warming man-made? Who cares. We have a binary choice: "do nothing" or "do something".If we do nothing we risk preventable extinction. If we do something it might cost a few bucks for no good reason. The choice is clear.You can apply it to the dog example as well. Could a reasonable person think dogs are conscious? Yes. So we should be nice to them.The cost of being kind is low and if we get it wrong we risk torturing a conscious being.

**Kim_Bruning** · 2026-09-19T14:59:11.000Z：

> Doomer argument is just that optimizers gonna optimizeRight. I don't quite subscribe to the strong doomer argument, but take water:Water flows downhill. It's not conscious. I don't think it's anthropomorphism to say that water "seeks" the lowest point on the landscape. Often that seeking process is mostly harmless, sometimes it's devastating, and that's where you want levees and dams.Now expand the same mathematical intuition out to other lowest-point-seekers in a high dimensional space. You don't even need to postulate a mind per se to see how optimizers can cause quite some mischief.Meanwhile, Kids and Kittens are good examples of this behavior at the intelligent end of the spectrum: Given time, they'll find a way to get through any gap. They don't need to be as smart as the adults, the adults just need to turn their back for one minute too many. O:-)

**red75prime** · 2026-09-19T09:36:50.000Z：

I'm aware. Locating a single probable key is exactly not that.

**ksmxksmxkwj** · 2026-09-19T13:21:55.000Z：

That’s a lot of words just to say “but modern AIs have access to more data”. Why overcomplicate prose? To sound smarter?Still, OP’s argument still holds even if AIs today have much more data to rely upon.

**Closi** · 2026-09-19T10:31:38.000Z：

Or almost any invention for that matter.Washing machines can’t do anything humans do, they just remove labour. Trucks don’t do anything longboats can’t, it just need less labour and time/effort to build roads rather than canals. Computers can’t calculate anything humans can’t dry run by hand etc.Everything in reality is about reducing time/effort/material/cost or achieving more with less resource.

**parineum** · 2026-09-19T14:46:28.000Z：

AI demonstrates it's value by solving a problem humans found not worth their time.This is less valuable than me asking chatgpt to find me a recipe.

**yfty** · 2026-09-19T11:27:31.000Z：

‘Thinking’ is rich. They are not thinking.Ironically the person verifying the output does both the thinking and doing in that regard. For without this - the output of an llm could be of zero value.

**ksmxksmxkwj** · 2026-09-19T13:28:55.000Z：

If it’s a trend on social media than it’s most likely staged for some views or happens to a very little, very niche and irrelevant share of people and is being blown out of proportion because… you guessed it: views.

**TeMPOraL** · 2026-09-19T18:10:06.000Z：

> Kids and Kittens are good examples of this behavior at the intelligent end of the spectrum: Given time, they'll find a way to get through any gap. They don't need to be as smart as the adults, the adults just need to turn their back for one minute too many. O:-)As a parent of kids currently aged ~3 thru 7, I concur. Each age has its own ways, but what's worse, they can also coordinate and get you from an angle you wouldn't thought possible, playing your own beliefs about them against you.

**tovej** · 2026-09-19T09:44:33.000Z：

Going through a list of possibilities one by one is bruee forcing.

**TeMPOraL** · 2026-09-19T11:23:15.000Z：

Yes. I'd also argue there isn't anything humans couldn't do in theory, other than things strictly prohibited by known laws of physics. It's been pretty conclusively shown in the last 100 years, we're past tipping point of civilizational knowledge and scientific infrastructure.What stops us from doing any specific thing is always allocation of resources - there's finite amount of time/effort/material/labor available, and past trivial amounts we need more and more people to agree on some allocation. Reduction of time/effort/material/labor costs of any thing is what moves it closer from "infeasible" to "feasible" for us to do. But again, short of violating laws of physics, it was never "impossible".

**TeMPOraL** · 2026-09-19T18:14:47.000Z：

Not "not worth their time", but "that they cannot afford to solve".

**TeMPOraL** · 2026-09-19T11:35:24.000Z：

Obviously not true, unless you think that "idea" is the only thing, and "execution" is worthless, at arbitrary timescales.Which would make 99% of us "not thinking" 99% of the time.

**stalfie** · 2026-09-19T10:10:00.000Z：

I think it is legitimate to argue that the process here does not fit the usual definition of "brute forcing". Traditionally, brute forcing would refer to something like a dictionary attack, where an algorithm tries to match all possible combinations of words to eg. find a password. Here, the approach was more common sense based, using historical records and possible error sources to narrow down the possibility space enormously in advance, try out a much more limited set of options within that space until you got a result that made sense, and finally validate those results using historical records. It's the exact same kind of "brute forcing" a human expert would do.

**red75prime** · 2026-09-19T10:18:47.000Z：

If the final set of possibilities is astronomically smaller than a naive one, calling the whole process a "brute force exercise" draws attention to an astronomically insignificant part.

**bonoboTP** · 2026-09-19T11:38:30.000Z：

And then you realize AI was made by humans...What I mean is that "can be done by humans" is ill defined. Are you allowed to use pencil and paper? That's not part of your body? Do you have to be strapped into a coffin for it to count as human-done? How about wheels, sticks and stones? Allowed to use those tools? How about an abacus? Or is electricity the line to draw?

**tttesw** · 2026-09-19T14:24:15.000Z：

You seem to have a poor understanding of how humans operate.

**rrr_oh_man** · 2026-09-19T14:22:13.000Z：

That’s a fair point.

## 关联链接

- https://www.prinzai.com/p/gpt-6-astra-solves-a-wwi-german-radio
