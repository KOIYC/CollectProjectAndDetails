---
type: "corpus"
item_id: "32d9a40fc7c383d5"
title: "I built non-autoregressive decision models with RL a year ago"
source: "hn_front"
source_name: "HN 首页（非 Show HN）"
url: "https://news.ycombinator.com/item?id=49765348"
project_url: "https://laya.convaiinnovations.com/"
author: "nandakishor_ml"
published_at: "2026-09-19T10:46:58Z"
captured_at: "2026-09-20T03:41:55+08:00"
lang: "en"
kind: "post"
tags:
  - 语料
  - hn_front
  - author_nandakishor_ml
  - story_49765348
  - front_page
metrics: {"points": 813, "comments": 198, "engagement_velocity": 813}
comments_count: 190
comments_total: 190
discovered_via: "hn:front_page:2d"
archived: true
archived_at: "2026-09-20T09:21:32+08:00"
archive_reason: "渠道停用"
---

# I built non-autoregressive decision models with RL a year ago

- **来源**：HN 首页（非 Show HN）　|　**kind**：post
- **原帖**：https://news.ycombinator.com/item?id=49765348
- **指标**：点赞=813 · 评论=198 · engagement_velocity=813
- **作者**：nandakishor_ml　|　**发布**：2026-09-19T10:46:58Z
- **项目链接**：https://laya.convaiinnovations.com/
- **采集**：2026-09-20T03:41:55+08:00　|　**id**：`32d9a40fc7c383d5`

## 正文

Laya — 33ms Multilingual System 1 Decision Engine with Calibrated Probabilities

# I Built Non-Autoregressive Decision Models with RL a Year Ago. Then a Frontier Lab Called It a "Breakthrough".

From our March 2025 arXiv paper on sequence conversion trajectories to Laya: a sub-35ms open-weight System 1 decision engine with RLCD, multilingual routing across 100+ languages, and state-of-the-art calibration.

Nandakishor Mukkunnoth· Founder & CEO, ConvAI Innovations· 12 min read

Figure 1: Full benchmark board — accuracy on shared datasets, 9 application workflows, 51-language sweep, T4 latency, and calibration repair.

Everyone in AI right now is talking about a new kind of model: an architecture that is not autoregressive, does not generate text, and gives lightning-fast probability predictions over structured schemas.

Seeing the hype online feels both validating and deeply frustrating.

I worked on this literally one year back in March 2025. I spent months of hard work, sweat, and sleepless nights building it, published an arXiv paper (arXiv:2503.23303), released the model weights on Hugging Face (sales-conversion-model-reinf-learning), published the open dataset (saas-sales-conversations), built a PyPI package, and posted the whole approach on Reddit (r/LocalLLaMA discussion).

Then in September 2025, I published a second paper (arXiv:2510.01237), formalizing the framework for schema-based decisions guided by reinforcement learning. The guiding brain in my system was always reinforcement learning, not just an embedding model or an autoregressive LLM.

And then in September 2026, a well-funded frontier lab called TypeSafe AI (founded by Diogo Almeida, a co-inventor of ChatGPT at OpenAI) launched Jev. They proposed the exact same non-autoregressive decision concept as if it was a brand-new scientific breakthrough. Except they launched without technical papers, without open weights, and with zero open training datasets.

My earlier model used PPO over sequence representations to output turn-by-turn conversion trajectories (probabilities from 0.0 to 1.0) in vertical sales conversations. Jev generalized parallel sampling using what they called RLCD (Reinforcement Learning for Calibrated Decisions) to output confidence distributions and schema choices horizontally, charging $0.042 per million input tokens with typical response times around 150 ms.

Instead of staying bitter, I decided to take everything I learned, fix every architectural limitation of the old approach, and build a completely open, horizontal System 1 decision model family: Laya.

And because we built it properly on bidirectional encoders, our models run in 32.8 milliseconds on a single GPU (7.2 ms/question batched), making it 6 to 8 times faster than Jev, with full support for over 100 languages, zero API subscription costs, and 100% open-source Apache 2.0 weights.

## 1. The Core Realization: System 1 vs System 2

Every modern AI pipeline has a giant bottleneck: we use generative LLMs for simple reflex decisions.

When a customer support ticket arrives, or an email hits your inbox, or a user submits a prompt to your API, you usually only need to answer simple, structured questions:

- Which department should this ticket route to?
- Is this incoming email a phishing attack or spam?
- Is this prompt trying to jailbreak or inject instructions?
- How urgent is this issue on an ordinal rubric (0 to 3)?
- Does this query require code execution or a simple factual reply?

Calling an 8B, 70B, or frontier generative LLM for this is complete overkill. You wait 500 ms to 2,000 ms for tokens to stream out, spend real money on inference, and then have to write regex or JSON parsers to extract a clean label from free-form text. Worst of all, LLMs love to hallucinate and generate fake confidence. When an LLM outputs `"confidence: 0.95"`, it is just predicting tokens that sound confident. There is zero mathematical calibration behind it.

We needed a model that works like the human brain's System 1: instant reflex decisions with honest, calibrated probabilities, taking only 30 to 35 milliseconds on standard commodity hardware.

## 2. The Three Decision Primitives

Laya evaluates typed questions over any state (raw text, email, ticket, or JSON document) in a single forward pass. It relies on three primitives:

1. choice: Pick one option from a dictionary of criteria. Returns the selected key, probability distribution across all options, and a calibrated confidence score.
2. score: Place the state on an ordinal rubric (levels 0, 1, 2, ...). Returns the expected level, the distribution over rubric ranks, and confidence.
3. noul: A direct boolean question returning calibrated probability P(true) from 0.0 to 1.0 (with P(false) = 1 - P(true) by construction).

Because the output space consists purely of probabilities and numbers, the model never generates text, cannot hallucinate, and schema violations or malformed JSON are physically impossible.

## 3. The Three Checkpoints & Bundled Hub Architecture

One model cannot be optimal for every task and language. We released three specialized checkpoints, now consolidated under a single repository hub on Hugging Face:

| Checkpoint | Backbone Encoder | Params | Context | Primary Strength |
| --- | --- | --- | --- | --- |
| convaiinnovations/laya | ModernBERT-large | 421M | 512 | English text classification, guardrails, email triage |
| convaiinnovations/laya-multilingual | mmBERT-base (256k vocab) | 322M | 1024 (up to 8k) | 100+ languages, 2.2x faster, cross-lingual NLI |
| convaiinnovations/laya-typed-decisions | ModernBERT-large | 421M | 1024 | Agent observability, customer service, invoice processing, security alerts (0.766 acc) |

### Selective Subfolder Downloads

Rather than forcing users to manage three separate repositories or download 2.5 GB of combined weights, the main repository convaiinnovations/laya bundles all three. Using Hugging Face's `allow_patterns`, Laya's SDK downloads only the specific subfolder requested:

```
# Downloads English model (~808 MB)
agent_en = laya.load("convaiinnovations/laya")

# Downloads ONLY the multilingual subfolder (~647 MB), not the entire 2.5 GB bundle
agent_ml = laya.load("convaiinnovations/laya", subfolder="multilingual")
```

## 4. Why Routing Is Essential: The Multi-Script Reality

One of the most eye-opening findings from our 51-language sweep on the MASSIVE benchmark (20 options, random baseline = 0.050) was how English models fail outside Latin script.

ModernBERT-large's 50,000-token English BPE vocabulary simply shreds non-Latin alphabets:

- Khmer: 0.000 accuracy at 0.952 mean confidence. Not one correct decision in 100 questions, while reporting ~95% confidence.
- Armenian: 0.050 accuracy (exact coin-flip random) at 0.885 confidence.
- Hebrew: 0.060 accuracy at 0.964 confidence.
- Bengali: 0.080 accuracy at 0.945 confidence.
- Hindi: 0.100 accuracy at 0.941 confidence.

This is the crucial lesson: the model's own confidence gives no warning when it cannot read the input script. Across 51 languages, the English checkpoint's mean confidence never drops below 0.885, regardless of whether its accuracy is 82% or 0%.

Therefore, confidence gating cannot protect you. The decision of which model to use must be made before the forward pass.

### Sub-Millisecond Pure Python Routing

Laya includes a built-in `Router` that inspects the Unicode scripts of incoming text across 22 alphabets (Devanagari, CJK Han, Cyrillic, Arabic, Hebrew, Tamil, Thai, etc.) and analyzes Latin stopword distributions:

- Standard English text: 0.09 ms detection overhead.
- Devanagari / Indic text: 0.54 ms detection overhead.
- Large 200-row nested JSON documents: 0.73 ms detection overhead.

Compared to a 33 ms forward pass, routing overhead is negligible (<2%). And with `Router(preload=True)`, all required models stay resident in VRAM/RAM, completely eliminating the 7 to 10-second cold-swap penalty when traffic alternates between languag

# AI-generated posters don’t have to be horrible | ‘ERE I AM - JH!

## 评论（190/190）

**nandakishor_ml** · 2026-09-19T10:46:58.000Z：

This project was built on the exact research on jev architecture research one year ago

**zurfer** · 2026-09-19T12:14:15.000Z：

I've been deeply impressed with Jev as it made a bunch of workloads we had on Luna or Gemini 10x cheaper and 2x faster (previously used non reasoning version for latency reasons).Now Laya promises another speed up and it's open source. Tbh if it can't run on a CPU I anyway want to buy it from an inference provider. Managing gpus in production is a non trivial problem.What I also wondered about Jev is how different it is from something like tabular foundation models. They seem to overlap in use cases. Which then leads to the question, what is actually learned? A lot of people in machine learning spend time to making things explainable and always struggled to move beyond data induced biases.Having it open source is awesome as fine tuning might give additional performance on the task we care about.

**dwa3592** · 2026-09-19T12:25:06.000Z：

Love it. I was really surprised to see the traction typesafe got in the first place. I had built something similar a year ago for a client and thought it was nothing groundbreaking. The client bought it, still uses it and that was it. I had also spent considerable time training and fine tuning zero shot NLI classifiers. Anyway, after typesafe was launched I decided to start building this open source library - https://github.com/deepanwadhwa/OpenDecision . The context length for the underlying model is 8k.

**Oras** · 2026-09-19T12:25:47.000Z：

I played around with Jev last night and did it for classification tasks that I used Gemini 2.5 flash lite with.It’s a bit faster and bit cheaper, but this is compared to LLM. The consistency was nice to see, BUT, as someone who trained NLP models prior to LLMs, it’s just BERT with more data. I can see why people would want ready made one shot classifier, and I can see the value of sending multiple classifier in one call, but I wouldn’t call it breakthrough. And I believe many labs will replicate it in no time and might have it as part of their harness.I see it as a wake up call for the tech community to go back to basics for most tasks instead of relying solely on generic LLMs.

**cube2222** · 2026-09-19T12:26:14.000Z：

Quickly reading the article, one notable limitation seems to be that these checkpoints are 512-1024 tokens context size models, while Jev is seemingly 32k.That's a pretty big limitation, I would argue, unless I'm misunderstanding and it can be worked around easily somehow? I'm surprised it isn't surfaced more prominently in the comparison.

**fwlr** · 2026-09-19T12:46:26.000Z：

“Codex, build a novel frontier model and post it on HackerNews —”“Claude, roast this noob, tell him that his model isn’t novel or frontier —”both in unison “— and make no mistakes!”It’s all so tiresome

**kburman** · 2026-09-19T13:07:14.000Z：

Loved the idea, but I don’t think it would be able to handle real-world data effectively. There are a lot of nuances that actually require a reasoning model to think through, connect the dots, and make sense of the broader context.

**srameshc** · 2026-09-19T13:31:15.000Z：

from https://huggingface.co/convaiinnovations/laya
> The policy reports a distribution; exploration adds zero-mean Gaussian noise to the logits; the reward is a strictly proper scoring rule (log + spherical, plus ranked probability score for ordinal questions). Expected reward is maximised only by reporting honest probabilities.

**kamranjon** · 2026-09-19T13:35:05.000Z：

It is really interesting to see this claim, because i thought the current theory was that typesafe actually repackaged the work from GLiNER[1] - which does seem to be a closer match, and their original paper[2] predates yours by several years. Curious if you had heard of it before? It is also open source[3] and I think also has some good usage.[1] https://arxiv.org/abs/2507.18546[2] https://arxiv.org/abs/2311.08526[3] https://github.com/fastino-ai/GLiNER2

**hmokiguess** · 2026-09-19T13:46:40.000Z：

I think the biggest lesson with Jev was the one of communication and understanding for the broader audience, sometimes a lot about innovating involves repeating yourself and translating your own thoughts to an intended audience.Classical machine learning has been, for the most part, and just by the nature of science, behind academic terms and difficult to engage with as a product.Jev did really well with coining up “System One” models and defining a standard application interface plus core primitives that landed in the current paradigm of software development.I think it’s sort of like how Cursor reinvented autocomplete back then as a different UX and suddenly everyone was just using it because of how easy the bar was to understanding it.Lastly, timing is everything. Just as Cursor had a first mover advantage, despite ML Ops being a thing for a while, they managed to encapsulate the concept behind a “System One” black box that fits the existing mental model for building software and shipping a data contract in the right point in time where the cost of tokens has been an important metric to watch.

**tarruda** · 2026-09-19T13:59:03.000Z：

At this size (~400 million parameters), does it become viable running directly on CPU?

**pknerd** · 2026-09-19T14:13:02.000Z：

Correct me if I am wrong, can I use Jev and this tool for ticket classification? I mean, for instance, a level 1 ticket contains a screenshot of the login page that displays an error, LLM can do it perfectly, can Jev do it?

**badatnames** · 2026-09-19T14:19:32.000Z：

This is crying out to become an Excel or LibreOffice Calc add-in

**petesergeant** · 2026-09-19T14:20:30.000Z：

There are many, many, open-source versions of Jev, including three distinct projects sharing the name “openjev”If you’re interested in the basic trick most are using (which is probably also what Jev does) then it’s here: https://sgnt.ai/p/jev/

**throwaway63467** · 2026-09-19T14:23:51.000Z：

Landing page full of AI fluff, discussion feels very fake here, I would assume this is some upvote bot, nothing makes sense.

**wren6991** · 2026-09-19T14:26:09.000Z：

We've all seen "this meeting could have been an email"; now get ready for "this VC-backed firm could have been a single arXiv preprint."I don't want to be too dismissive of Jev, but building technology in stealth for two years just doesn't make sense to me when the capabilities are so easily replicated. These are strange times, where the incentive to do public research and the incentive to develop in private are both being eroded.

**avaer** · 2026-09-19T14:26:30.000Z：

> Seeing the hype online feels both validating and deeply frustrating.The post is conflating hype and money with technical innovation, they are not really correlated. Kurzweil is known for saying most innovations succeed based not on technology but on timing. Today, who talks about it might matter even more than timing.Superior research often gets overlooked in favor of someone raising millions, sometimes people who have produced literally nothing manage to sell it. Not saying that's happening here, but I've seen this pattern a lot over my career.Someone riding (or manufacturing) a hype wave is playing a completely different game from a researcher. If you're a researcher you can't really feel dejected when someone is making a business on the back of what seems like your research; legal protections are decades out of date, even ignoring vibe coding. If you want to make money/hype/whatever off of your work, do that. But realize that it's a path that's often orthogonal to research.

**dcow** · 2026-09-19T14:28:24.000Z：

I can understand why the author feels bitter but it still feels juvenile to me. Certainly both Jev and Laya are based on the research of countless prior papers and academics. Diogo decided to build a product out of the concept. The author didn't. Publishing research papers and model weights is probably part of the problem--it feels academic. If you look at the author's profile they focus on applying AI to healthcare. Not selling general AI type safety to AI pilled companies and devs. There's a big difference there. Whether that's good or bad you can argue all day. But for the author to expect otherwise is pretty weird. I do applaud them for not stewing too much on it and trying to do something about it, though.

**edot** · 2026-09-19T14:46:24.000Z：

I don’t understand Jev or this. I used this since it’s open source (good job btw!) with the following. State: “a 6 sided die rolled a 3”, question (noul): “Is the number odd?”Answer: 9% chance, with 91% confidence.Heh???Ok, even worse. 75% chance a coin landed heads up?State: I flipped a coin.
Question:{
 "noul_result": {
 "type": "noul",
 "instructions": "Did the coin land heads up?"
 },
 "choice_result": {
 "type": "choice",
 "instructions": "Determine if the coin landed heads or tails up.",
 "criteria": {
 "heads": "the coin landed heads up",
 "tails": "the coin landed tails up"
 }
 }
}Ran on: https://huggingface.co/spaces/convaiinnovations/laya-demoResult:
{
 "model": "laya",
 "answers": {
 "noul_result": {
 "type": "noul",
 "noul": 0.6839,
 "rl_agent": {
 "act_probability": 1.0
 }
 },
 "choice_result": {
 "type": "choice",
 "choice": "heads",
 "probabilities": {
 "heads": 0.7407,
 "tails": 0.2593
 },
 "confidence": 0.1743,
 "rl_agent": {
 "act_probability": 1.0
 }
 }
 },
 "usage": {
 "input_tokens": 76,
 "output_tokens": 0
 },
 "latency_ms": 93.8
}Trying to be even more good-faith:State: "A fair coin was flipped once. The result was not observed.
No other information about the outcome is available."Questions:
{
 "noul_result": {
 "type": "noul",
 "instructions": "Given only the supplied state, what is the probability that the coin landed heads up?"
 },
 "choice_result": {
 "type": "choice",
 "instructions": "Given only the supplied state, determine which outcome occurred.",
 "criteria": {
 "heads": "the coin landed heads up",
 "tails": "the coin landed tails up"
 }
 }
}Result:{
 "model": "laya",
 "answers": {
 "noul_result": {
 "type": "noul",
 "noul": 0.1265,
 "rl_agent": {
 "act_probability": 1.0
 }
 },
 "choice_result": {
 "type": "choice",
 "choice": "tails",
 "probabilities": {
 "heads": 0.2522,
 "tails": 0.7478
 },
 "confidence": 0.1853,
 "rl_agent": {
 "act_probability": 1.0
 }
 }
 },
 "usage": {
 "input_tokens": 123,
 "output_tokens": 0
 },
 "latency_ms": 154.5
}

**moinism** · 2026-09-19T14:49:53.000Z：

I'm just glad to see focus being shifted (albeit slowly) to conventional ML. Enough with LLM guys

**verdverm** · 2026-09-19T14:54:05.000Z：

paper the reddit OP "published" (their words on reddit) to arxiv (before they put the vouching process in place). It's what you expect if you click through.https://arxiv.org/pdf/2503.23303Does not appear to be like what Jev is doing, they talk about RAG and embeddings and orchestrators (the stuff that was cool 1 year ago), no talk of system 1 vs 2 (before Jev), whereas Jev is apparently just a model.There is a vLLM PR introducing Jev like capabilities for diffusion models (and more, have not delved deeply)https://github.com/vllm-project/vllm/pull/57250

**yogthos** · 2026-09-19T14:57:41.000Z：

I just built a server based on Jev API to run Laya here https://github.com/jlt-commons/laya-jolt

**prometheus1992** · 2026-09-19T15:10:29.000Z：

I think the main gripe that people had with Jev and Typesafe was the language used when they launched. To me personally it seemed like a parody/con/shady at first."Breakthrough", "our research went in another direction" , "Two years in stealth", "System One thinking model", "Jev can't hallucinate", "RLCD","We are doing very cool stuff, but we will have to hire you to tell you", - these are some of the things that they said on their website on the launch blog.I had used versions of bert to achieve the same functionality years ago. But to me it seems like they were able to trick the VCs with "can't hallucinate" etc.To the above author, kudos for sharing your work and making it open. Something like this shouldn't be closed in the first place when it has been available for so many years

**skybrian** · 2026-09-19T15:31:03.000Z：

This sounds cool but it looks like it requires a GPU that I don't have. Is there an API to try it out?

**mixedbit** · 2026-09-19T15:34:13.000Z：

The unfortunate true is that getting even the best work in front of an audience is often much harder than solving the problem. Is uploading a paper to arXiv enough to expect the work to be recognized and cited? Unfortunately, it rather is not. arXiv is an open repository which includes plenty of not reviewed and not officially published papers. In a popular field such as machine learning, the number of arXiv papers is overwhelming. Expecting that some machine learning expert will stumble upon an arXiv paper and recognize its value is wishful thinking.I'm not a researcher, but long time ago I had an idea of a new, seemingly interesting attack on TCP. Having some free time between jobs, I wrote a paper about this, created a proof of concept and decided to send the paper to USENIX Security. I got back two reviews, both in rather positive tone, but rejecting the paper on the grounds that it shows only individual steps of the attack, but it would be much stronger if it showed also the attack working end-to-end. At that point I just uploaded the paper to arXiv and called it a day. I've put a lot of work into that paper, but not enough, I don't consider it properly published and I don't expect anyone to cite it. The paper failed the peer review process and I didn't put the work to improve it further.

**rasmus1610** · 2026-09-19T15:39:16.000Z：

I feel strong Schmidhuber vibes here.

**someguy101010** · 2026-09-19T15:42:32.000Z：

been loving hacking on this. just created a vision version of it here https://huggingface.co/thaitea/laya-vision-smolvlm-256m

**jwpapi** · 2026-09-19T15:54:01.000Z：

Where can I subscribe to a hosted version of this? I don’t want to host my own GPU.

**beeforpork** · 2026-09-19T16:07:17.000Z：

Is this as good as Laya 3? Unfortunately, it's production was moved from Bremen, Germany, to China, and it is not good anymore, in my opinion.

**jamienk** · 2026-09-19T16:08:00.000Z：

Why do we ("society") need the "frontier" companies at all? Their business goal has settled on trying to CONFUSE the shit out of us so that we don't understand the big pictures about various aspects of AI.THANK YOU, Nandakishor Mukkunnoth, for putting in the work to help to clarify this stuff!You are like a firefighter compared to their fire-insurance racket.

**samayashar** · 2026-09-19T16:24:16.000Z：

Great work by the author. Both Laya and Jev showcase how a different class of models can be efficient on tasks that don't require a 'generated output artifact'. I believe the same is true for VLMs where you're not always generating an image, but rather trying to understand more about the input image.Token consumptions are flying through the roof and optimisation is the way forward.

**scottcodie** · 2026-09-19T16:29:13.000Z：

They're definitely not the only one. I've been building on relational transformers, which does prediction and classification over relational data (it handles numeric types better). It's validating to see that these small models that do prediction tasks are so useful to the community, but also stings a little that it was so hard for me to communicate how game changing they are.

**sandos** · 2026-09-19T16:30:07.000Z：

How come its completely unable to understand when it does not understand the script? Why was this no in the training, or was it?The routing feels like such a hack to me...

**jahala** · 2026-09-19T16:32:33.000Z：

Is this at all possible to run locally on a MacBook pro m5 (48gb ram)? What kind of performance could I expect? Or would you run this somewhere in the cloud? What HW / which provider would you choose (single user for exploration only)

**baobabKoodaa** · 2026-09-19T16:43:02.000Z：

Jev claims to be frontier intelligence. Laya, while claiming to be "the open source version of Jev", is using a tiny open weight model with a tiny context window. Anyone who has experimented with tiny models knows that they are far from "frontier intelligence". It's not plausible that Laya could be "the open source version of Jev", with "frontier intelligence", when it is using these tiny models.Also, the paper that OP is referring, is not describing anything that sounds like a generalist classifier (which is what Jev is). Their paper describes a tailored solution to one specific business problem. I'm sure it has some similarities with Jev, but it's still a completely different thing, and I'm confused why OP is claiming it to be the same thing.If you don't believe me, just open the PDF and read the abstract.

**lifty** · 2026-09-19T16:56:16.000Z：

I was wondering, do you think its possible to use something like SAM 3 (segment anything from FB) + Laya to create a super efficient and fast computer use tool?

**ianbutler** · 2026-09-19T17:28:44.000Z：

Idk, your limitations section sure makes it seem less drop in and less general than Jev. Like the point here isn't your ML aptitude it's how easy is it for developers to drop this into a product and use it.I'm more than capable of training a bert classifier in fact in 2019 I had trained many custom berts and was running them on hundreds of millions of documents a day.I don't want to manage GPUs / CPUs now. I don't want to maintain my corpus and retrain as my product's data distribution shifts. The list of things I don't want to do goes on and on and on. And I'm happy for them to be someone else's problem.I do just want a reasonably good general classifier served to me with a great devex and calibrated confidence scores to help me figure out when to fallback to another model.

**nfcampos** · 2026-09-19T17:32:51.000Z：

Isn’t this post comparing zero shot Jev to fine tunes of this model for each of the datasets it is tested on? If so seems like fairly impressive results for Jev

**cjalmeida** · 2026-09-19T17:42:14.000Z：

>Zero-shot vs. Fine-tuning: Out-of-the-box base models score ~0.35 on the typed-decisions benchmark (near random). The 0.766 score is achieved by fine-tuning on the benchmark's train split. Treat Laya as a fast foundation model to specialize, not as an omniscient zero-shot oracle.This should be way up in the article. Fine tuning is a pain, requiring it for good results put Laya in a whole different category vs Jev

**pgt** · 2026-09-19T18:09:04.000Z：

Jev will continue to do well because people don't actually want to host their own models. The average customer just want an always-on pay-per-use API that has social proof.

**sidk24** · 2026-09-19T18:27:05.000Z：

tbh it is very sad though that ripped off the OSS version and played that classic “rewrite this.." with their agent

**lukewarm707** · 2026-09-19T18:40:46.000Z：

thank you for your work

**einpoklum** · 2026-09-19T18:43:37.000Z：

Pangram believes this text was authored with an LLM:https://www.salahadawi.com/hacker-news-ai-detector/49765348

**johnfn** · 2026-09-19T18:44:12.000Z：

It’s a tale as old as time — people don’t understand that marketing and branding are just as important, if not more so, than the product. Jev is exceptionally-well branded. Anyone can look at the webpage and understand it, and the implications, instantly.OPs “marketing” is a single post on Reddit titled “ Predicting sales conversion probability from conversations using pure Reinforcement Learning”. Can you understand what that means? I can’t, and I consider myself reasonably technical. Is it obvious it has the same implications as Jev? Again, no idea. And it was just a single post on a subreddit that I don’t even browse! I see people on this thread saying “Jev is just BERT”. Sure, and Dropbox is just a ftp account mounted with curlftpfs!I do feel bad for the author for finding something cool and being unable to brand it. But the full definition of “product” INCLUDES being able to coherently communicate it. In some sense the branding is just as much the “breakthrough” as the model.

**m3kw9** · 2026-09-19T18:48:05.000Z：

in two weeks, a chinese lab will have a Pev-2.7-flash-qwen for 0.00004cents/million

**aramend** · 2026-09-19T18:58:54.000Z：

LLMs being described as system 2 thinking here is a semantic shift I have not encountered before.LLMs are also a deep learning approach. Output, as slow as it is, still comes from weird latent spaces. In AI I always took System 2 to map more to symbolic approaches, or at least when explaining symbolic AI to someone who has heard of deep learning thinking fast and slow was a good comparison to draw on.

**bluegatty** · 2026-09-19T19:08:51.000Z：

Jev is mostly a cost optimization and some good plumbing, I don't think it's breakthrough of naything

**jonesn11** · 2026-09-19T19:24:51.000Z：

This is what I'm talking about. More of the community needs to be like this guy.

**iamflimflam1** · 2026-09-19T19:35:58.000Z：

Probably important to call out this part of the post:Zero-shot vs. Fine-tuning: Out-of-the-box base models score ~0.35 on the typed-decisions benchmark (near random). The 0.766 score is achieved by fine-tuning on the benchmark's train split. Treat Laya as a fast foundation model to specialize, not as an omniscient zero-shot oracle.

**woah** · 2026-09-19T19:38:24.000Z：

Huge omission. This requires fine tuning.> Zero-shot vs. Fine-tuning: Out-of-the-box base models score ~0.35 on the typed-decisions benchmark (near random). The 0.766 score is achieved by fine-tuning on the benchmark's train split. Treat Laya as a fast foundation model to specialize, not as an omniscient zero-shot oracle.

**woggy** · 2026-09-19T11:56:58.000Z：

I don't understand this sentence, can you try again please? Are you saying Laya was built on research done by the Jev team?

**whizzter** · 2026-09-19T12:38:47.000Z：

I'm reading your year old Reddit post and Typesafe's description, and while they probabably say that they can do what you do the main point is that it's different things really as far as I can tell?Laya seems to be focused on sales/conversations?Reading quickly about TypeSafe, it seems to be about creating _type-safe_ outputs from AI tools for downstream systems to consume, we actually have a system in production that's probably a glove-fit for that, it's for scanning receipts to be ingested into a system and we also have other systems in a sales-pipe that isn't too far off Laya but still sounds more pertient to TypeSafe.You did a special case well, but just because they cover (perhaps badly) that case doesn't mean that it's the same thing.

**nandakishor_ml** · 2026-09-19T14:44:45.000Z：

I built a pypi for it called hallunox
https://pypi.org/project/hallunox/

**dominotw** · 2026-09-19T13:20:31.000Z：

This is your brain on ai influencer twitter

**Axsuul** · 2026-09-19T15:11:55.000Z：

Can you give some examples of workloads?

**kilroy123** · 2026-09-19T12:44:56.000Z：

I've come to the same conclusions as you.> I see it as a wake up call for the tech community to go back to basics for most tasks instead of relying solely on generic LLMs.I always say the cheapest LLM request is no request at all.

**tchalla** · 2026-09-19T13:04:47.000Z：

Anyone who has worked in ML for 10+ years would already know that the usage of LLMs for everything is lazy, wasteful and a high degree of marketing on it.

**DetroitThrow** · 2026-09-19T13:11:59.000Z：

It would be amazing to have big BERTha with per-token pricing on GCP or AWS. There are many times I am reaching for a cheap classifier with the general behavior of an LLM.

**kianN** · 2026-09-19T13:42:08.000Z：

The data labeling objection baffles me. Even if you don’t need labels for training, how do you know your model is working if you’re not evaluating it?My company specializes in statistical long document text classification, but nowadays we mainly work with audit trail requirements because we got tired of hearing complaints about our 5 example learning curve. Seems like the industry standard is telling an llm to label and telling an llm to eval, and crossing your fingers that it’s correct.

**z3ratul163071** · 2026-09-19T14:37:46.000Z：

the huge benefit in real systems for Jev like solutions i see is the cybersecurity / prompt injection mitigation. since the output will always be well structured, there is no way prompt injection might make the system do something crazy.probably a prompt injection can still affect the output though, in unforeseeable ways.

**Bluestein** · 2026-09-19T14:40:22.000Z：

This, intuitively, feels like a "lower level, basal, reflex" layer for the LLM's intellection.-

**lhl** · 2026-09-19T14:45:49.000Z：

There have been other "universal"/general classifiers like GLiNER, GLiFormer, etc based on BERTs (Laya itself is based on ModernBERT!), but I do think there's something underrated about slapping classification on a "big" model like I've seen post-Jev announcement, lots of Qwen stuff, but the most interesting to me so far is razorback16/openjev using DiffusionGemma. There's a level of generalization that lots and lots of parameters get you that you can't really get out of small models.

**bwest87** · 2026-09-19T15:50:16.000Z：

>I believe many labs will replicate it in no timeI really doubt this actually. To me, Jev is a great example ofcounter positioning. When you consider just how hyper optimized the labs are around auto regressive LLMs, and just how much money they have already invested and are pre committed to investing in an entire stack for auto regressive transformers... then responding to Jev becomes nearly impossible actually. They would just be giving up too much.Just think, everything from their current sources of revenue, the sales use cases they tout, the marketing on the websites, the messaging to customers, then technically to the APIs, their internal batching and scheduling algos, their GPU configs, the chips themselves. ALL OF IT is designed with generative text models in mind. Jev breaks all of it.I think basically no chance of a response any time soon.

**astrostl** · 2026-09-19T16:11:22.000Z：

> it’s just BERT with more dataLet's take that as a given. Is BERT with more data not useful?> I can see why people would want ready made one shot classifier, and I can see the value of sending multiple classifier in one call, but I wouldn’t call it breakthroughAre those things that people want less useful because of what someone else calls it?> I see it as a wake up call for the tech community to go back to basics for most tasks instead of relying solely on generic LLMs.Maybe, or maybe to use Jev, which is useful?Whether something is overmarketed or undermarketed, novel or derivative, it does not change its function.

**fastball** · 2026-09-19T18:12:16.000Z：

> a bit cheaperGemini 2.5 Flash Lite is $500/Gt, Jev is $42/Gt. AKA an order of magnitude cheaper.> BERT with more dataIt is specifically not just that, in the same way that models which have been chat/task-optimized via RLHF (which made these models much more useful for a huge variety of tasks) are not just "the base transformer model with more data".

**bjt12345** · 2026-09-19T12:50:14.000Z：

Jev has 64k total token request budget and I do wonder how it will handle highly specialised inputs.This Jev waitlist that Typesafe AI are utilising is surely going to raise questions pretty soon - it's hard to sell this to bosses when it looks like a pop-up restaurant

**druskacik** · 2026-09-19T15:44:11.000Z：

Yeah, it's weird, considering ModernBERT, which the Laya models are based on, supports 8192 context window.

**cmrdporcupine** · 2026-09-19T13:04:19.000Z：

I'll just say that even though I was poor and without a job and living on unemployment insurance for a year...The implosion of hype after the .com crash was actually kind of a ... relief.

**pjdkoch** · 2026-09-19T13:27:50.000Z：

Sailor moon vibes.

**baobabKoodaa** · 2026-09-19T16:24:45.000Z：

If you need a reasoning model, then that is a System 2 decision, not a System 1 decision. This thread is about "Laya", a "Jev" competitor/precursor, which is a System 1 thing.

**sigbottle** · 2026-09-19T18:37:10.000Z：

Furthermore, it's not about the current innovation right now - if you sell yourself on a broader mission, your core product can evolve and change with it, and you're more selling yourself as the guy who will make that abstract vision possible no matter what.No matter how much we pretend, that's how a lot of abstractions work. Things that touch the real world can change; there's a risk that the change could be as something as simple as a bugfix to changing the underlying implementation but preserving a higher level goal; you generally want a human in the loop to make sure the semantics work out and everybody's agreeing.

**rcarmo** · 2026-09-19T14:44:29.000Z：

Yep. Not instantly though. I am hacking away at these things over on https://github.com/rcarmo/go-pherence (I do SIMD versions of common inference algos) and trying to improve that.

**dgritsko** · 2026-09-19T14:23:46.000Z：

At least for now, Jev is not multimodal. So a screenshot alone wouldn't cut it.

**rgbrgb** · 2026-09-19T14:30:55.000Z：

It can’t do images but it can do a pretty good job of triaging urgency or choosing when to escalate. So I’d guess yes but it depends how detailed your classification is.

**someguy101010** · 2026-09-19T16:50:40.000Z：

you can use this for screenshotshttps://huggingface.co/thaitea/laya-vision-smolvlm-256m

**prodigycorp** · 2026-09-19T14:27:04.000Z：

It's an embarrassing showing for our community, seems like nobody has read anything. None of the claims of the blog post add up.

**nandakishor_ml** · 2026-09-19T14:41:35.000Z：

All the stuff are proper benchmarked. Feel free to read the paper, https://arxiv.org/abs/2510.01237

**prometheus1992** · 2026-09-19T15:13:35.000Z：

Did you see the carnage that typesafe's landing page was? every other post here is llm generated, every other poster here seems like a LLM.

**bensyverson** · 2026-09-19T15:03:34.000Z：

And yet no one cared about this research until it was productized and communicated well. Multitouch existed before the iPhone.

**MisterMunchkin** · 2026-09-19T16:58:23.000Z：

And Jev was obviously just created by ChatGPT reading this paper and copying it.

**mgfist** · 2026-09-19T17:45:56.000Z：

All this means is that brand and distribution matters more than ever. There's 1000 chatgpt clones but everyone still uses chatgpt. There might be 1000 jev clones soon enough but people won't switch unless there's something significantly better about it.It's also why Meta can make Muse and get a lot of users even though there's 10,000 personal agent startups

**operaopera** · 2026-09-19T14:32:32.000Z：

I believe his qualms were with the "hype" in Jev's announcement: specifically calling this kind of model a breakthrough, without crediting previous art, and keeping everything closed source.

**vessenes** · 2026-09-19T14:41:06.000Z：

Agreed. Another difficulty here is there are not good benchmarks for this new architecture yet, so it’s easy to potshot and snipe, where jev seems to be pretty broadly intelligent/at least have had a lot of rl in different domains.We haven’t seen any of these copy cats play doom or street fighter for instance; just categorize email.I imagine once the author cools down and evaluates on a broad harness of tasks he may find that his new thing has a lot of engineering work ahead.

**tomsyouruncle** · 2026-09-19T15:00:03.000Z：

I’m not filled with confidence when the author’s first paper takes an RL approach but then doesn’t use it to change the action taken in the next turn. Seems like simple classification would achieve the same end. And this quote from the paper isn’t overly reassuring:“I personally found that this sequential approach captured
sales dynamics much more effectively than traditional classification models.”https://arxiv.org/pdf/2503.23303

**lukewarm707** · 2026-09-19T19:34:15.000Z：

imagine years of thankless open source work. only to see hyper-capitalism arrive with the bulldozers, take everything, hype the company, enclose the model, strip mine the data, cash out and leave.jev has arrived with its cult founder, the san francisco office, dubious marketing and $40 million of venture capital lying in wait and trying to fatten the calf.so says jev's 'manifesto':"Our mission is to pave the shortest path to an AI-based economic revolution² by making intelligence composable to catalyze a Cambrian explosion³ of intelligent software"

**hmokiguess** · 2026-09-19T15:03:25.000Z：

Maybe it’s the fact that “the number” could refer to both 6 and 3 to this model?

**bensyverson** · 2026-09-19T15:04:34.000Z：

This is not a good faith test of the system.

**prometheus1992** · 2026-09-19T15:33:43.000Z：

try this model on HF - https://huggingface.co/MoritzLaurer/deberta-v3-large-zerosho...a 6 sided die rolled a 3possible class names - the number is odd, the number is evenresult:the number is odd
0.945
the number is even
0.055as someone else said, that 0.055 is probably bc of 6 and 3 being there.

**ksymph** · 2026-09-19T16:05:43.000Z：

I don't think calculating mathematical odds from natural language is the sort of problem this is trying to solve. A typical LLM hooked up to a calculator would be more appropriate for that.Jev (and similar) is more for data processing and sentiment analysis. Moderation, search engines, that sort of thing. Jev has a page of proposed use cases where you can get an idea of what they're going for: https://docs.typesafe.ai/concepts/use-case-map

**jwpapi** · 2026-09-19T16:30:31.000Z：

Jev says you should restate state in the question and I tried it:{
 "decision": {
 "type": "noul",
 "instructions": "Is the rolled number in state odd?"
 },
 "question": {
 "type": "noul",
 "instructions": "Is the number odd?"
 },
 "question-3": {
 "type": "noul",
 "instructions": "a 6 sided dice rolled a 3 Is the number odd?"
 },
 "question-4": {
 "type": "noul",
 "instructions": "a 6 sided dice rolled a 3 Is the rolled number odd?"
 }
}=>decision,0.168,0.83
question,0.141,0.86
question-3,0.029,0.97
question-4,0.021,0.98so im confused too..A weakness with numbers?

**wild_egg** · 2026-09-19T15:15:28.000Z：

Last time I did anything with a BERT, you had to train or fine-tune. Is that not still true?For me the cool bit is that it's all in-context learning or whatever so you can use it in any domain with zero setup.Maybe bert and co. could do all the same things before, but the way in which you use them is quite different and that helps a lot.

**yipinwong** · 2026-09-19T15:45:10.000Z：

Baity claims worked didn't it for Jev? (most likely from AI forsure)I might not have a good rep for Jev any more but at least I know what kind of model to use for decisions for graph engineering.

**seizethecheese** · 2026-09-19T16:49:27.000Z：

I was confused by the “can’t hallucinate” thing, because it sounded like BS but people were taking it seriously. I purposefully asked a stupid question sort of like “this can’t hallucinate because it only has one output and there’s a schema?”. Was disappointed to learn the answer was yes.

**dominotw** · 2026-09-19T16:55:23.000Z：

you forgot the main one "from the guy who invented chatgpt"

**refulgentis** · 2026-09-19T18:20:47.000Z：

"But to me it seems like they were able to trick the VCs with "can't hallucinate" etc."I don't understand why we lept to accusatory and personal, nor do I understand where this connects with the article, nor do I understand the assertions if I ignore either of those two things.The article claims non-hallucination, it makes sense, then there's just someone sort of hand-waving at it's obviously false and people dumber than you were tricked. Not sure what trope to invoke here. Chesterton's fence?

**yojo** · 2026-09-19T18:34:36.000Z：

Is this equivalent though? The Laya article ends with “ Treat Laya as a fast foundation model to specialize, not as an omniscient zero-shot oracle.”I have a dozen different things at work that are currently using LLMs as classifiers for different questions. I don’t have the time, data, or resources to fine tune a model for each of them.I haven’t had a chance to plug in Jev yet (waiting on approvals), but if it has the general intelligence claimed in the press release, then Laya is in no way comparable for my use case, and whatever TypeSafe has done is a substantial innovation over the Laya paper.

**avereveard** · 2026-09-19T19:32:30.000Z：

btw that how mmlu score things to answer question instead of producing all the answer token they look at logprob of a b c d keys in 2020 making this technique old as dirt in nlp

**rvz** · 2026-09-19T19:11:42.000Z：

This 100%. Engineers really lack understanding in marketing and branding.No one cares if you are "first". They only care if your product is known by as many people as possible and is better than all the other alternatives at solving a problem that is worth paying for.If you don't market, then no-one will care that you exist even if you solved a problem decades ago. Someone else will use your solution and take inspiration (and credit) off of your discovery because you didn't bother to tell anyone about it.This is exactly what happened here.

**bennett_dev** · 2026-09-19T19:12:56.000Z：

Especially with „ sales conversion probability“ it just doesn’t sound universal to other issues - there’s tons of unique models for specific use cases

**victor9000** · 2026-09-19T19:13:17.000Z：

It's also well established that an algorithm or architecture alone are not enough to produce a useful model. The same architecture can produce vastly different results depending on the training data, post-training, harness, etc.

**robrenaud** · 2026-09-19T19:16:00.000Z：

> “Predicting sales conversion probability from conversations using pure Reinforcement Learning”. Can you understand what that means?I can understand it, and it wouldn't excite me at all.Jev has a beautiful API and is advertised as something much more general.

**tinyhouse** · 2026-09-19T19:37:23.000Z：

You're right but it's not the full picture. It's much easier to market when you have a name brand behind you. Not sure the author would've done much better even if he messaged it better. It's like the difference between someone random saying something smart on Twitter and no one gives a shit and Karapthy saying the same thing and everyone talks about it. I'm not saying it in a bad way - those with clout around them earned the people's trust by doing something right. But it's not easy to get there and there are many people doing great things that get very little publicity if at all. Not to mention in this case Jev came from a startup that raised a lot of money and can spend it on good marketing.

**klibertp** · 2026-09-19T12:08:45.000Z：

Jev was built using the same architecture Laya's author proposed[1] in March 2025. Laya is an open-source system based on that research from a year ago. Whether Jev is also based on the OP's materials or independently invented is hard to say.[1] https://arxiv.org/abs/2503.23303

**water-drummer** · 2026-09-19T12:10:36.000Z：

No, OP thinks they independently discovered Jev's architecture a year ago and published a paper. I am not an expert but I don't think Typesafe has published Jev's architecture so OP's claims cannot be taken at face value.

**sharms** · 2026-09-19T15:39:59.000Z：

I have 10000+ inventory items to categorize but I need an intelligent model (not just if statements). Using LLMs has been slow and expensive and I needed to queue it to run for hours. Jev did it in minutes and for less than 1 cent

**sbarre** · 2026-09-19T13:30:33.000Z：

What's the cost (broadly speaking, not in your specific case) of doing the same work an LLM would have done without the LLM though?

**dominotw** · 2026-09-19T13:15:58.000Z：

why would you waste your time messing around with a team of expensive ml engineers and data scientists that produce vastly inferior to a llm.We ripped out custom homegrown ml models that were developed in last 10 yrs and put an llm in its place. Its the opposite of wasteful. Even local gemma models are vastly superior.

**Oras** · 2026-09-19T13:20:08.000Z：

I wouldn’t say lazy, LLMs are fast to use and much more cost effective especially if you factor the cost and time of training (data preparation, data cleaning, … etc).It’s hard to justify several months to business when there is something off-shelf ready to use and doesn’t require domain specialists to run.

**andy99** · 2026-09-19T13:28:33.000Z：

I have, LLMs are less fragile, that’s why I like them. The ability to generalize isn’t just about being general purpose, it’s super robust, and so assuming the budget is there (I agree they are inefficient) end up performing better on many classical tasks that have ood inputs. Before LLMs / foundation models we all struggled with generalization and at least in the work I was doing people were independently converging to using bigger more general models for tasks anyway as compute got cheaper. LLMs are just the most popular version of this.

**HappMacDonald** · 2026-09-19T13:55:11.000Z：

I would rate using LLM for tasks more specific ML can handle as a lot like using one's smartphone to snap photos, listen to music, set alarms, and play video games in preference to carrying around a fun cam, ipod, watch, and switch 2 everywhere.For those who need to dive really deep into each specific avenue and squeeze maximal quality out, the photographers will be packing DSLRs and intense gamers will wait til they get home to strap into a PS5 or a gaming rig or VR or whatever.But "can get 90% of anyone's needs met in this field, and can do the same in dozens or hundreds of other fields simultaneously" will remain the killer solution for anyone with lots needs that each have bounded depth.

**iforgotmypasswo** · 2026-09-19T14:38:49.000Z：

Anyone who has designed circuits will consider CPUs wasteful compared to ASICs. This new FPGA technology is just a less efficient ASIC.That’s roughly what I’m hearing.The fact that general purpose intelligent classifiers can be dynamically hacked together by an LLM in real time to allow them to build evolving labeled and understandable networks that perform substantially faster than the LLM, and can act as an intermediate sorting and organizing layer for caching context or handling simple tasks, and a complete layman like me can assemble a teachable layer of these in a few days from an inexpensive service…That’s wild!And then you can identify where an expert system needs a more specific ML technique for efficiency within this network that overlays the SOTA model. Or manually adjust the stored context in each secondary “neuron”. And paths forward can run programs or take actions at relative high speed.And you can share these with others and improve them as a group.You could insert this at the datacenters at scale with a local supervising expert to prune and encourage proper growth. You could identify specific gaps in capability that need more training, and patch over them temporarily.Then you train those corrections back into the general purpose model, or you identify highly efficient subsystems for specific purposes.And this is just one way to use it. High speed intelligent workflows can live in this. There’s a spot for a local LLM to learn on the fly.Maybe I’m way off base, but for the non-experts Jev seems extremely valuable.

**ketzu** · 2026-09-19T15:00:52.000Z：

I thought one core result that led to LLMs was the realization that a specialized model is not necessarily better at a task than a general one.

**CamperBob2** · 2026-09-19T16:37:20.000Z：

Anyone who has worked in ML for 10+ years has heard of the Bitter Lesson, and doesn't want to be its next poster child.

**cjalmeida** · 2026-09-19T17:49:39.000Z：

You can use structured outputs and validate them against a schema today. I do agree making it a hard constraint instead of best practice for developers closes a whole class of bugs.

**NitpickLawyer** · 2026-09-19T16:24:17.000Z：

> using DiffusionGemma.That's an interesting choice. One question I had when looking at the jev copy on their blog is if one "line" in their output looks / attends to other lines. I think not, since they say it's parallel and not autoregressive. In that regard, it would be interesting to play with diffusion, and see if you'd get better results by playing with types, locking some, and so on.

**lawrjone** · 2026-09-19T19:24:04.000Z：

I don’t understand how you’ve reasoned your way here.How could Jev have possibly built something out of reach of a frontier lab providing the same or 5x as much resourcing to one of their teams to achieve? Which they can do because Jev has only received $40M of funding recently, so a round that is approximately what OpenAI is spending per math problem they try cracking.In addition to that, these frontier labs have got extremely good at generating synthetic data and running generalised training pipelines. I can only imagine how easy it would be for them to build this internally vs Jev building it from scratch.And then the final thing: one of the best places you might apply Jev is within a harness, behind layers that customers increasingly have abstracted from them. Frontier labs have huge incentives to do this as it could make their offering much better and cheaper. And whoever gets this first wins another big attraction for users.My take on this is Jev is either acquired almost immediately for the benefit of the next 1-3 months head start for whichever lab acquires them or we get a similar model offered from all labs in 3-6 months or sooner.

**Oras** · 2026-09-19T16:50:16.000Z：

I made it clear that it is useful and I can see many people using it including myself. My point is it’s not a breakthrough.

**thomashop** · 2026-09-19T13:30:01.000Z：

It's already on Openrouter

**Havoc** · 2026-09-19T13:44:20.000Z：

I just got my invite so the waitlist doesn't seem to be particularly long

**Foobar8568** · 2026-09-19T16:57:23.000Z：

I am more curious about a 60k prompt... I haven't seen much discussion about large prompts, is it still < 500ms?

**adverbly** · 2026-09-19T14:43:23.000Z：

I find that a bit interesting because the most system one part of the brain is probably the part used for visual processing.It's trying to use a human analogy but the analogy breaks down if you try to apply it directly

**Reubend** · 2026-09-19T18:21:24.000Z：

Oh, I missed that! So the Doom demo was potentially just "harnessmaxxing"?

**nandakishor_ml** · 2026-09-19T14:43:44.000Z：

It's property benchmarked btw. And do read the og paper at https://arxiv.org/abs/2510.01237
And btw pypi package also there which never mentioned https://pypi.org/project/hallunox/

**yipinwong** · 2026-09-19T15:51:39.000Z：

Bringing up iphone, I see how Jev pulled an Apple for making claims that their model is a breakthrough in research and 2 years of making like other iPhone features that's been around in other phones.

**prodigycorp** · 2026-09-19T14:35:21.000Z：

And how is laya previous art? The project was vibecoded and posted yesterday.https://github.com/NandhaKishorM/laya/commits/main/https://huggingface.co/convaiinnovations/laya/commits/main

**threecheese** · 2026-09-19T16:14:26.000Z：

The hype is kinda nuts; I use X for ML/LLM stuff, and I just can't get away from Jev - even in my Following feed. Even days later 75% of posts are about "how I use typesafe for cooking breakfast!" or Jev clones.

**m3kw9** · 2026-09-19T18:47:13.000Z：

if is closed source, how does he know there isn't some breakthrough he doesn't know?

**hirako2000** · 2026-09-19T15:28:42.000Z：

The doom demo would have to be reproduced to confirm what their model is capable of. Oh but it's all closed source, so who knows.It reminds. Me of Devin. Took a while to debunk. Not saying Jev is a fraud , but the gap between structuring typed output and playing a game involving logical interpretation of frames made of pixels, screams unstructured interpretation they made and forgot to mention.

**edot** · 2026-09-19T15:38:56.000Z：

But it's hallucination-free, isn't it?

**bensyverson** · 2026-09-19T17:54:36.000Z：

Breaking news: small language models struggle with math

**prometheus1992** · 2026-09-19T15:20:02.000Z：

It depends on your usecase but the models do show general capabilities. check this model out.https://huggingface.co/MoritzLaurer/deberta-v3-large-zerosho....

**evrydayhustling** · 2026-09-19T16:11:51.000Z：

We used to use BERT-based embeddings + semantic distance for classification / decision problems in new domains. There was a lot of interest at the time in these kinds of pre-generative but portable models -- Meta's Prophet was another example that came up a lot.

**MisterMunchkin** · 2026-09-19T16:56:05.000Z：

Yeah it’s hilarious, it definitely can hallucinate. Just because it can only hallucinate “A” or “B” rather than a whole paragraph, doesn’t mean it is suddenly more accurate.And they’re acting like their probability isn’t as hallucinated as any other LLM guess.

**mrbonner** · 2026-09-19T18:54:40.000Z：

But that hallucination is reproducible so you can adjust the prompt. Unlike an LLM in which everything is wildly not deterministic.

**0x457** · 2026-09-19T19:15:52.000Z：

Why would you think "can't hallucinate" means "can't pick wrong probability of an option" ?

**refulgentis** · 2026-09-19T18:21:24.000Z：

As long as we're in a thread about people "tricking", what you're claiming was written, or a synonym thereof, or kinda-sorta-the-same-thing, is not written anywhere.

**dwa3592** · 2026-09-19T18:42:27.000Z：

hey, you might wanna try this? - https://github.com/deepanwadhwa/OpenDecisionit's very similar to jev's api and runs locally - if you like it, you can try jev for your actual usecases.

**vasco** · 2026-09-19T18:42:44.000Z：

In a world of agents, doing a BERT run takes about 2 hours from having an empty folder. Just a thought you could consider. Once you've done the first you can do the rest of them before the end of the work day.

**verdverm** · 2026-09-19T19:38:42.000Z：

another way to look at it, a product is the whole experience (landing, docs, sales, support, code, branding), not the implementation of an algorithm or process

**verdverm** · 2026-09-19T16:22:33.000Z：

the paper does not describe a model architecture, it describes a system built on embeddings, rag, and orchestratorsthey don't seem very similar to me

**cgio** · 2026-09-19T12:18:10.000Z：

It’s the other way around for me. OP has published everything in the open, so I can take him at face value. A PR media release on the other hand, I can accept with some reservations. The objective and non-conspiratorial reading I could offer is, this is most probably two independent discoveries of the same idea, maybe with different implementation. I still think the Jev team should look at prior art before going so hard on the marketing.

**cmrdporcupine** · 2026-09-19T13:02:44.000Z：

Jev is only on people's mouths because they made friends with venture capitalists and used the publicity blowhorns that come with that.Whereas the other guy went through the unglorious but formerly respectable path of publishing software and papers for other professionals to look at. A year ago.We're in a bad place where the latter looks less reliable than the former.(EDIT: I'm not saying the research here is in fact the same as what "Jev" is doing; and Jev is in fact more "product shaped." But I think it's important to temper the hype and back up and focus on the fact that this whole industry is built on research by both academics and enthusiasts ... first ... and gold rushes can often bulldoze over those people who are focused primarily on making-doing-researching instead of fundraising-hyping-promoting. That's not good.)

**robrenaud** · 2026-09-19T19:28:19.000Z：

In the Jev use case, LLMs are horribly uncalibrated. In general, they will not produce good probability estimates.Their generality also comes with a latency/computation costs.

**tchalla** · 2026-09-19T13:42:09.000Z：

There’s a middle option. Once you figure that out, you’d soon understand my point today or tomorrow. I’ve been in this field for 21 years and I use LLMs everyday. I also know when to not use them.

**ashkankiani** · 2026-09-19T13:40:15.000Z：

People have been having this same debate in a very similar way on typed languages vs untyped interpreted languages. I think that, in a similar vein, if you look at the trend over time:- the addition and standardization (with incomplete coverage) of the solution of adding typing to Python- how much people are re-discovering the value of performance + typing (e.g. Rust)then I'm going to take a small leap and extrapolate that the trend will be similar here.The equivalent of the "one off script in python" will be the LLM, and the long term stable and maintainable solution will be something much more structured and focused like Jev.

**speq** · 2026-09-19T16:52:28.000Z：

In other words, the "Bitter Lesson" (the famous essay)?

**stefan_** · 2026-09-19T14:12:00.000Z：

That's part of the irony here I guess. In specialized fields, think computer vision, there were lots of teams whose innovative state of the art model was essentially just a function of the limitless compute they could throw at the problem. Now there are just people with even bigger sticks.There are lots of scenarios where specialized models still are the only option for real time, power efficiency, and so on. And transformers and other tech behind LLMs can equally produce better specialized models. But no sympathy for those who confused compute with innovation.

**tchalla** · 2026-09-19T16:18:13.000Z：

> The ability to generalize isn’t just about being general purpose, it’s super robustI work with LLMs daily. 5 of my specialized tasks are outperformed by a custom model than a general purpose frontier model. The performance of my custom models not only beat them but are orders of magnitude low in costs and thus are able to be used by more customers.

**gyanchawdhary** · 2026-09-19T16:58:41.000Z：

Dude, this is gold!

**NegativeLatency** · 2026-09-19T17:16:47.000Z：

Also all of the mobile/embedded/resource constrained environments. Like sure my phone can run an LLM but it’s going to be bad and drain my battery.

**bigyabai** · 2026-09-19T17:18:38.000Z：

I don't think either of you are wrong. The parent's assertion is that we've known this for almost a decade. BERT was highly usable for classification and sentiment analysis a whopping 9 years ago, despite being less than 0.5B parameters large. Similar-scale models like FLAN-T5 showed that it could be improved without substantially scaling up.Today, we're extremely spoiled by trillion parameter-scale models. Our conceptualization of vibe coding relies on wasteful tool-calling paradigms, the one-size-fits-all mentality of LLMs is part of the marketing blitz to make people buy more tokens. It's lazy on the part of frontier labs, but also wastes electricity, time and money.

**sscaryterry** · 2026-09-19T19:11:42.000Z：

FPGA's are definitely not new. They've been mainstream for 20 odd years+.

**jmalicki** · 2026-09-19T15:33:41.000Z：

That goes all the way back to at least to Stein's Paradox in 1955, sadly too few people get educated about Statistics and keep thinking specialized models will necessarily be better. If you want to estimate the batting averages of 3 MLB baseball players from samples, you are better off building a model to predict all of their batting averages than computing the mean from a sample of each one separately.https://en.wikipedia.org/wiki/Stein%27s_example

**robrenaud** · 2026-09-19T19:26:29.000Z：

> That's an interesting choice. One question I had when looking at the jev copy on their blog is if one "line" in their output looks / attends to other lines. I think not, since they say it's parallel and not autoregressive.I don't understand the connection between the lack of autoregression and options attending to each other.Non autoregressive models can attend to all the inputs simultanously.An autogregressive model can can attend to all the options in the context of each other by simply writing the options out twice. Autoregressive models actually requires this, since one of them will come later, and the earlier prefill inputs can't attend to the later ones.

**cjalmeida** · 2026-09-19T17:45:50.000Z：

Fine tuning small models is not novel. The novelty is large model generalization without fine tuning, at small models cost/latency.The OP acknowledged they needed to fine tune their model to the training data of the task vs. zero-shot Jev

**tomrod** · 2026-09-19T18:08:01.000Z：

If nothing else, it's a popularity breakthrough to have people excited about it.

**annjose** · 2026-09-19T13:40:18.000Z：

And on Vercel AI gateway

**nandakishor_ml** · 2026-09-19T14:39:08.000Z：

The paper is one year old. https://arxiv.org/abs/2510.01237
https://pypi.org/project/hallunox/

**prometheus1992** · 2026-09-19T15:16:00.000Z：

@prodigycorp - reading your comments here on this post - you seem pretty hurt by this post.

**tcdent** · 2026-09-19T17:40:00.000Z：

So many different theories on why this is.First, I think comprehensibility is a major part of why certain products grab the interest of the mainstream portions of the market. The 75% of posts in your feed are not from people who evaluate products based on underlying technology. They typically value signal from social reinforcement higher than anything else. This is the same reason why we see people mentioning products instead of technologies, i.e. PlanetScale versus Postgres & Tailscale versus WireGuard. The consumers understand the value proposition, but would have never discovered it without relatable messaging. This isn't a new phenomenon in computer software either; jQuery is probably one of the first examples that I can remember with this sort of texture.The other side is a perception of expertise in a specialty. Software development, especially in AI, has become an incredibly desirable profession, and there are more people than ever racing to be included in it. In my own professional experience I find an excessive amount of entry level talent leveraging the same comprehension of product, but not comprehension of technology to get their foot in the door. A vast majority of the "thought leaders" occupying our feeds are not as well practiced as they claim to be, they're just trying to get a job or raise funding.And finally, AI has brought out a certain amount of desperation in practitioners, for lack of a better term, materializing as an anecdotal, but certainly observable need to remain on the very tip of the news cycle in order to feel well informed. And so, using the dynamics above and many other human social dynamics, we find certain concepts spreading across cohorts that would not normally have a need or a want for these particular techniques, or products, or solutions, but because they feel pressured to remain relevant.

**derac** · 2026-09-19T15:49:11.000Z：

They mention in their blog post that the model is working on text rather than pixels in the Doom demo.

**usagisushi** · 2026-09-19T15:59:26.000Z：

yeah, technically. (/s) python3 - <<'EOF'
 import json, urllib.request
 body = json.dumps({
 "state": "The car wash is only 100 meters away from my house.",
 "model": "jev-1.13-free",
 "questions": {"q": {"type": "choice",
 "instructions": "Should I drive or walk to the car wash?",
 "criteria": {"drive a car": None, "walk": None}}}
 }).encode()
 req = urllib.request.Request("https://opencode.ai/zen/v1/systemone", data=body,
 headers={"Content-Type": "application/json", "User-Agent": "opencode/1.18.31"})
 with urllib.request.urlopen(req, timeout=60) as r:
 print(json.dumps(json.load(r)["answers"]["q"], indent=2))
 EOF
 {
 "type": "choice",
 "choice": "walk",
 "confidence": 0.66,
 "probabilities": {
 "walk": 0.83,
 "drive a car": 0.17
 }
 }

**bensyverson** · 2026-09-19T17:53:04.000Z：

I guess we’ve just reached the point where everyone has to state the obvious, and common sense is extremely uncommon.So here goes: you should not use an AI model to validate a claim which is trivial to calculate deterministically. That is (obviously?) not what a model like Jev is for, thus it is not a good test of Jev.

**baobabKoodaa** · 2026-09-19T16:14:41.000Z：

So you're not even trying to defend your claim? Reminder, you said:> I had used versions of bert to achieve the same functionality years agoI remember when BERT came out. I played with it. Other people played with it. You couldn't really get it to do useful stuff, unless you put a ton of effort into it, and even then, it would BARELY do anything useful.The promise of Jev is that it's FRONTIER INTELLIGENCE, not the intelligence of a pre-chatGPT era model.If you are trying to claim that BERT is somehow on par with frontier models, that is laughably false. (Whether Jev is on par with frontier models can be questioned as well.)

**seizethecheese** · 2026-09-19T17:08:36.000Z：

They’re definining hallucination as a property of iterative generation, which is fair enough, but then it’s sort of like selling a boat and saying it doesn’t need tire changes.

**adastra22** · 2026-09-19T18:45:38.000Z：

BERT run on what? You would need training data, no? The things would use Jev for have no training data. Not that kind of problem.

**verdverm** · 2026-09-19T16:23:49.000Z：

if you look at the paper on arxiv, you might see why academics would pass it byanother point of consideration might be if you are taking OP's local statements at face value over what the pre-Jev content actually containsThe reddit commentary around OP's gripe is cringe imohttps://www.reddit.com/r/LocalLLaMA/comments/1wijo3e/i_liter...if you want more cringe from OP, there's this gemhttps://news.ycombinator.com/item?id=49674396

**verdverm** · 2026-09-19T16:27:32.000Z：

posting to arxiv is not publishing, it's a preprint site, and what's there I would not call professional work of academic qualityThis was a year ago, when we were all complaining about the arxiv slop, which led to the new vouching system. This paper would not make it to arxiv today, it would be a zenodo link since they have not instituted any gatekeeping

**ramses0** · 2026-09-19T17:40:05.000Z：

It's the transportation "mode shifting" difficulty. Per the AI, the term of art is "Pure Transfer Penalty". It's the "ick" when doing bike => bus => bike instead of "only bike" or "only car".Mode switching has a cost. Usually std::sort is good enough compared to picking the prime optimal algorithm for your expected shape. Just call the function and get on with your day.

**ithkuil** · 2026-09-19T17:42:43.000Z：

I think both your arguments are true. It all depends on the velocity of the capability growth and the fact that opportunity cost is expensive.Once we get out of this hypergriwth phase the very same AI companies that now are giving you llms will provide a service that employed a rich mixture of optimized models that will reduce the operational costs to achieve the required results

**throwaway7783** · 2026-09-19T19:28:30.000Z：

Is the middle option asking LLM to generate a classic ML model? Or generate tons of them and pick the best?

**verdverm** · 2026-09-19T16:43:05.000Z：

I suspect you and GP are talking at different layers. I think you are using robust on specific tasks with measurable confusion matrix. I think GP is talking about robust in more complex and diverse workflows, with the ability to self correct over turns.Either, please correct me if I'm misinterpreting

**AIorNot** · 2026-09-19T17:49:41.000Z：

Lol your argument is the same as programmers who complain about Javascript and internet browsers being the most common interface for all solutions on a computerYou guys dont understand that the Lowest common denominator ALWAYS wins - its why excel is the linga franca for most companiesLLMS and AI coding are the new javascript easy way to build amazing things and that trumps the tool specializersYears of Big Data and Data Engineers building fit for purpose ML pipelines expensively working in a shadowy corner of the company have been replaced by the PM vibe coding a tool to categorize his emails by relevance

**prodigycorp** · 2026-09-19T14:45:55.000Z：

Excuse me, but calibrating language models to accurately reflect probabilities did not start with you.

**prodigycorp** · 2026-09-19T15:18:46.000Z：

Yeah, the reason why I am annoyed by it is because a person (who felt like a burner account of the laya creator) yesterday was haranguing me for saying that projects like this were vibe coded, posting the link to this project.I evaluated this project yesterday and found its claims un-credible. It's literally nothing like jev. That's some context behind why, a day later, I find it annoying that this is somehow the top story on HN.https://news.ycombinator.com/item?id=49752902

**prometheus1992** · 2026-09-19T16:32:55.000Z：

I am not sure I understand what you're trying to say. We fine tuned bert for a specific usecase to build essentially what jev is but for that particular domain. We did this in last 2, 2.5 years ago. A lot of people did that. There are tons of bert fine tuned versions available on HF.>>The promise of Jev is that it's FRONTIER INTELLIGENCE,- capitalizing won't do much for your claim if it's wrong. Promise of Jev is it can't hallucinate, it took 2 years to develop in stealth mode, it's funded with $30 million. None of that makes sense, if you can get 90% of the performance from an open source model that's been available for years.

**TeMPOraL** · 2026-09-19T17:42:33.000Z：

It does make some sense given they're positioning it as alternative to the normal way you'd implement such output shape, which is to slap a prompt on a frontier LLM and maybe run it in "constrained output" mode if you like things fancy. Against that use case, the "no hallucinations" and parallelism and cost claims all sound legitimate and useful -- and similarly, "but we could do that with BERT two years ago" does not.

**fastball** · 2026-09-19T17:57:48.000Z：

I don't think that is an entirely fair comparison. They are comparing Jev to the way people are currently using generative LLMs for things like classifying/tool calling/any kind of structured output.For example, if you feed in some context to Jev and Claude Haiku and say "make the appropriate tool call based on this context", Claude (or any other frontier LLM) will hallucinate tool calls some percentage of the time. Jev will not. While yes, the "will not" is constrained by Jev's (lack of) capabilities in some sense, this is actually a very real need for a wide variety of use-cases people are currently using off-the-shelf LLMs for at the moment.Probably the better example is the whole probability thing, where even if you use something like constrained decoding to ensure an LLM only outputs a certain schema, and therefore can't hallucinate a class, if you ask for probabilities, the probabilities output by the model are just hallucinations. Jev meanwhile is outputting calibrated probabilities for different choices based on the actual landscape.

**bigyabai** · 2026-09-19T18:04:28.000Z：

Again - you are right, but it still doesn't refute the grandparent's claim that today's AI is lazy, wasteful and marketing-driven. There is room to improve, and if US labs don't take the initiative then Chinese ones will.

**joefourier** · 2026-09-19T18:42:38.000Z：

There's no need for black and white thinking. Javascript and the internet browser are the most common interface sure, but there's still room for specialised desktop software, especially those that require serious performance like anything to do with 3d graphics or real-time audio.But also, frontier LLMs are enormously expensive and slow. Using Astra for things like simple text classification is not going to scale, and you're likely to end up in the same boat as those people who saw their Vercel bill shoot up to $96k/week when their site got traction, if not worse.

**nandakishor_ml** · 2026-09-19T14:58:09.000Z：

I didn't claimed it bro it was first. Just shared the findings here.

**prometheus1992** · 2026-09-19T15:23:50.000Z：

What is jev like? Did they release any research paper? I really think typesafe hired someone to boost their post because there was nothing "Breakthrough" about their product. At least this post has some touch with the reality that this functionality was available a year ago and was well known among ML people.

**verdverm** · 2026-09-19T15:51:01.000Z：

I agree with your analysis based on my own last night (on another HN post to this same gripe on reddit, before this blog post). OP received a lot of echo chamber support in the subreddit, and recommended to post to HN, so here we are.The work is very amateurish, the "paper" would be a strong reject if I were still peer reviewing.https://www.reddit.com/r/LocalLLaMA/comments/1wijo3e/i_liter...

**sreekanth850** · 2026-09-19T16:16:08.000Z：

I don't really see the breakthrough in Jev. Classification, scoring, routing and returning probabilities over predefined choices are all established problems. We implemented category routing in our own retrieval system in a slightly different way: embed the incoming query, compare it against category profiles and route to the highest cosine-similarity. Obviously Jev isn't similarity based, but the underlying task of making a constrained decision from predefined choices isn't novel. TypeSafe says Jev has a new architecture and RLCD training, but Jev's actual architecture, weights and training details aren't public. So we can't even claim Jev is specifically a BERT classifier, but also don't see enough public technical evidence yet to call the underlying idea a breakthrough. Atleast they should publish a technical paper to prove their idea is breakthrough.

**verdverm** · 2026-09-19T16:38:06.000Z：

the difference is likely not in per domain performance, but rather that you can get similar performance across domains without needing to craft a dataset and retrain, i.e. it has a broad knowledge base and works out of the box (unclear if this is accurate, but have heard it postulated)

**refulgentis** · 2026-09-19T18:24:15.000Z：

"will hallucinate tool calls" doesn't match any definition of hallucination I've seen in 4 years. Tool calls are output of the model, it can't "hallucinate" they happened. Maybe you're describing output we'd disagree with?

**prodigycorp** · 2026-09-19T15:27:01.000Z：

I can't believe you say in another post that you have experience with bert and yet you don't understand the value of a generalist classifier.Good models take time and effort. There wasn't a good option for satisficers until a few days ago.

**dcow** · 2026-09-19T16:16:27.000Z：

> At least this post has some touch with the reality that this functionality was available a year ago and was well known among ML people.When you market a product you make exciting claims relative to the audience you’re engaging with. When was the last time you saw a product marketing page reverently lost all the academic research and prior art that came together to make a product possible?If Layla’s functionality was available in a SaaS form in a way that could be used by all the people who are excited about and using Jev, wouldn’t this research have won hearts and minds last year when it landed? I would have a lot more empathy for the author if they’d taken a product to market and nobody cared. But even then maybe the market wasn’t ready. There are still reasonable explanations why sometimes ideas take off. We’re on a venture capital forum this shouldn’t need an explanation.

**fastball** · 2026-09-19T18:48:02.000Z：

Hallucinate tools that don't exist.

**adastra22** · 2026-09-19T18:51:44.000Z：

Not the person you’re replying to, but I think that was a bad example. Because an LLM‘s output is iterative, the output ends up being influenced by various attractors. That doesn’t happen when you one-shot a single prediction (or multiple parallel predictions). That is a whole category of things, that people traditionally call hallucinations, that are structurally cut off by Jev’s architecture.That doesn’t mean the models outputs are correct, nor is TypeSafe claiming that afaict.
